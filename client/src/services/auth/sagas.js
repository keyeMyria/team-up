import { delay } from 'redux-saga';
import { call, take, fork, race, put } from 'redux-saga/effects';

import { timeoutDelta } from '@/utils';
import { actions, actionTypes } from './actions';
import { getAuthToken, setAuthToken } from './localStorage';
import api from './api';
import signUp from './signUp';
import signIn from './signIn';
import signOut from './signOut';

export function* refreshToken() {
  const _token = yield call(getAuthToken);
  const token = yield call(api.refreshToken, _token.refresh_token);
  yield call(setAuthToken, token);
  return token;
}

export function* tokenExpirationLoop(_token) {
  let token = _token;
  // let's wait until the first token is about to expire
  yield call(delay, timeoutDelta(token.expires_in, -300)); // 5 minutes before

  while (true) {
    yield put(actions.refreshToken());

    try {
      token = yield call(refreshToken);
      yield put(actions.refreshTokenSuccess(token));
      yield call(delay, timeoutDelta(token.expires_in, 0));
    } catch (error) {
      yield put(actions.refreshTokenFailure(error));
      yield call(delay, 5000);
    }
  }
}

export function* signInSaga() {
  const { backend, payload } = yield take(actionTypes.SIGN_IN);
  const token = yield call(signIn, backend, payload);
  return token; // might be null on signIn error
}

export function* autoSignInSaga() {
  yield take(actionTypes.AUTO_SIGN_IN);
  let token;

  try {
    token = yield call(refreshToken);
    yield put(actions.signInSuccess(token));
  } catch (error) {
    yield put(actions.signInFailure(error));
  }
  return token; // might be null on refreshToken error
}

export function* authorizeSaga() {
  const { signInToken, autoSignInToken } = yield race({
    signInToken: call(signInSaga),
    autoSignInToken: call(autoSignInSaga)
  });

  const token = signInToken || autoSignInToken;

  if (token) {
    yield call(tokenExpirationLoop, token);
  }
}

export function* signUpSaga() {
  while (true) {
    const { userData } = yield take(actionTypes.SIGN_UP);
    yield call(signUp, userData);
  }
}

export function* signOutSaga() {
  while (true) {
    yield take(actionTypes.SIGN_OUT);
    yield call(signOut);
  }
}

// This saga starts up authorize and signUp sagas
// and cancels them when the SIGN_OUT action is dispatched
function* authSaga() {
  yield fork(signUpSaga);
  yield fork(signOutSaga);

  while (true) {
    yield race([take(actionTypes.SIGN_OUT), call(authorizeSaga)]);
  }
}

export default authSaga;
