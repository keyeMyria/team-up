import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';
import { throwError } from 'redux-saga-test-plan/providers';

import accountApi from '@/data/Account/api';
import authApi from '../api';
import { actions, actionTypes } from '../actions';
import { getAuthToken, setAuthToken, removeAuthToken } from '../localStorage';
import authSaga, {
  refreshToken,
  tokenExpirationLoop,
  autoSignInSaga,
  signInSaga,
  authorizeSaga,
  signOutSaga,
  signUpSaga
} from '../sagas';
import signIn from '../signIn';
import signUp from '../signUp';
import signOut from '../signOut';

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

const newToken = {
  access_token: 'jF5FU1oOljXTSPcFmiOz1n1iXl9Puu',
  expires_in: 36000,
  refresh_token: 'jlDt3vXPW1BdMOWdtTUdH7COH2YS7C'
};

describe('refreshToken', () => {
  it('gets token, refreshes it and stores a new one back in localStorage', () =>
    expectSaga(refreshToken)
      .provide([
        [matchers.call.fn(getAuthToken), token],
        [matchers.call.fn(authApi.refreshToken), newToken]
      ])
      // token is refreshed
      .call(authApi.refreshToken, token.refresh_token)
      // new token is stored in localStorage
      .call(setAuthToken, newToken)
      // new token is returned
      .returns(newToken)
      .run());

  // it('throws an error when there is no token in localStorage', () => {});
  // it('throws an error when token has expired and authApi call fails', () => {});
  // It's impossible to test it right now with redux-saga-test-plan.
  // The errors being thrown in these cases are important, since they're caught
  // in other sagas that dispatch proper actions (either success or failure)
  // TODO: take a look at refreshToken tests one day
});

// TODO: find out how to test a loop saga with delays
// describe('tokenExpirationLoop', () => {
//   it('works', () =>
//     expectSaga(tokenExpirationLoop, token)
//       .provide([[...]])
//       .put(actions.refreshToken())
//       .put(actions.refreshTokenSuccess(newToken))
//       .run());
// });

describe('autoSignInSaga', () => {
  it('dispatches signInSuccess and returns a refreshed token on success', () =>
    expectSaga(autoSignInSaga)
      .provide([[matchers.call.fn(refreshToken), newToken]])
      .dispatch(actions.autoSignIn())
      .call.fn(refreshToken)
      .put(actions.signInSuccess(newToken))
      .returns(newToken)
      .run());

  it('dispatches signInFailure and returns undefined on error', () => {
    const error = new Error('network error');

    return expectSaga(autoSignInSaga)
      .provide([[matchers.call.fn(refreshToken), throwError(error)]])
      .dispatch(actions.autoSignIn())
      .call.fn(refreshToken)
      .put(actions.signInFailure(error))
      .returns(undefined)
      .run();
  });
});

describe('signInSaga', () => {
  const backend = 'facebook';
  const payload = { email: 'test@example.com', username: 'test', password: 'test123' };

  it('calls signIn and returns a token on success', () =>
    expectSaga(signInSaga)
      .provide([[matchers.call.fn(signIn), token]])
      .dispatch(actions.signIn(backend, payload))
      .call(signIn, backend, payload)
      .returns(token)
      .run());

  it('calls signIn and returns undefined on error', () =>
    expectSaga(signInSaga)
      // signIn returns undefined when it fails
      .provide([[matchers.call.fn(signIn), undefined]])
      .dispatch(actions.signIn(backend, payload))
      .call(signIn, backend, payload)
      // we expect signInSaga to return undefined in this case
      .returns(undefined)
      .run());
});

describe('authorizeSaga', () => {
  it('calls tokenExpirationLoop when signInSaga wins the race and returns a token', () =>
    expectSaga(authorizeSaga)
      .provide([[matchers.call.fn(signInSaga), token], [matchers.call.fn(tokenExpirationLoop)]])
      .call(tokenExpirationLoop, token)
      .run());

  it('calls tokenExpirationLoop when autoSignInSaga wins the race and returns a token', () =>
    expectSaga(authorizeSaga)
      .provide([[matchers.call.fn(autoSignInSaga), token], [matchers.call.fn(tokenExpirationLoop)]])
      .call(tokenExpirationLoop, token)
      .run());

  it("doesn't call tokenExpirationLoop when signInSaga wins the race, but returns undefined", () =>
    expectSaga(authorizeSaga)
      .provide([[matchers.call.fn(signInSaga), undefined], [matchers.call.fn(tokenExpirationLoop)]])
      .not.call.fn(tokenExpirationLoop)
      .run());

  it("doesn't call tokenExpirationLoop when autoSignInSaga wins the race, but returns undefined", () =>
    expectSaga(authorizeSaga)
      .provide([
        [matchers.call.fn(autoSignInSaga), undefined],
        [matchers.call.fn(tokenExpirationLoop)]
      ])
      .not.call.fn(tokenExpirationLoop)
      .run());
});

describe('signUpSaga', () => {
  const userData = {
    email: 'test@example.com',
    username: 'test',
    password: 'test123',
    name: 'Test',
    age: 12
  };

  it('calls signUp with userData from SIGN_UP action', () =>
    expectSaga(signUpSaga)
      .dispatch(actions.signUp(userData))
      .call(signUp, userData)
      .run());
});

describe('signOutSaga', () => {
  it('takes every SIGN_OUT and calls signOut', () =>
    expectSaga(signOutSaga)
      .provide([[matchers.call.fn(signOut)]])
      // on SIGN_OUT dispatch
      .dispatch(actions.signOut())
      // it calls signOut
      .call.fn(signOut)
      // and waits for another SIGN_OUT
      .take(actionTypes.SIGN_OUT)
      .silentRun());
});

describe('authSaga', () => {
  it('forks signOutSaga and keeps starting races after SIGN_OUT dispatch', () => {
    const raceEffects = [matchers.take(actionTypes.SIGN_OUT), matchers.call(authorizeSaga)];

    return expectSaga(authSaga)
      .fork(signUpSaga)
      .fork(signOutSaga)

      .race(raceEffects)
      .dispatch(actions.signOut())
      .race(raceEffects)

      .silentRun();
  });
});

// //////////////////////////////////////////////////////////
// ///////////////// FULL FLOW TESTS ////////////////////////
// //////////////////////////////////////////////////////////

describe('sign in/out flow', () => {
  describe('[facebook]', () => {
    const backend = 'facebook';
    const accessToken = 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea';
    const payloadFb = { accessToken };

    it('logs the user in, stores token in localStorage and enters tokenExpirationLoop', () =>
      expectSaga(authSaga)
        .provide([
          [matchers.call.fn(authApi.convertToken), token],
          [matchers.call.fn(getAuthToken), token],
          [matchers.call.fn(authApi.revokeToken)]
        ])
        .put(actions.signInSuccess(token))
        .put(actions.signOutSuccess())

        .call(authApi.convertToken, backend, accessToken)
        .call(setAuthToken, token)
        .call(tokenExpirationLoop, token)

        .call(authApi.revokeToken, token.access_token)
        .call.fn(removeAuthToken)

        .dispatch(actions.signIn(backend, payloadFb))
        .dispatch(actions.signOut())
        .silentRun());
  });

  describe('[team-up]', () => {
    const backend = 'team-up';
    const email = 'test@example.com';
    const password = 'test123';
    const payloadTu = { email, password };

    it('logs the user in, stores token in localStorage and enters tokenExpirationLoop', () =>
      expectSaga(authSaga)
        .provide([
          [matchers.call.fn(authApi.getToken), token],
          [matchers.call.fn(getAuthToken), token],
          [matchers.call.fn(authApi.revokeToken)]
        ])
        .put(actions.signInSuccess(token))
        .put(actions.signOutSuccess())

        .call(authApi.getToken, email, password)
        .call(setAuthToken, token)
        .call(tokenExpirationLoop, token)

        .call(authApi.revokeToken, token.access_token)
        .call.fn(removeAuthToken)

        .dispatch(actions.signIn(backend, payloadTu))
        .dispatch(actions.signOut())
        .silentRun());
  });
});

describe('register flow', () => {
  const userData = {
    email: 'test@example.com',
    username: 'testname',
    password: 'test123',
    country: 'Poland',
    age: 20
  };

  const { email, username, password } = userData;

  it('creates an account and logs the user in', () =>
    expectSaga(authSaga)
      .provide([
        [matchers.call.fn(accountApi.createAccount)],
        [matchers.call.fn(authApi.getToken), token]
      ])
      .put(actions.signUpSuccess())
      // login flow has its own tests, so just check if signInSuccess was dispatched
      .put(actions.signInSuccess(token))

      .call(accountApi.createAccount, email, username, password)

      .dispatch(actions.signUp(userData))
      .silentRun());
});

describe('auto sign in flow', () => {
  it('refreshes the token, signs the user in and stores the new token in localStorage', () =>
    expectSaga(authSaga)
      .provide([
        [matchers.call.fn(getAuthToken), token],
        [matchers.call.fn(authApi.refreshToken), newToken]
      ])
      .put(actions.signInSuccess(newToken))

      .call(authApi.refreshToken, token.refresh_token)
      .call(setAuthToken, newToken)

      .dispatch(actions.autoSignIn())
      .silentRun());
});
