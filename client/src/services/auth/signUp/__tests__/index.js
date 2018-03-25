import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';
import { throwError } from 'redux-saga-test-plan/providers';

import api from '@/data/accounts/api';
import signUp from '../index';
import { actions } from '../../actions';

const userData = {
  email: 'test@example.com',
  username: 'testname',
  password: 'test123',
  country: 'Poland',
  age: 20
};

const { email, username, password } = userData;

const credentials = {
  email,
  username,
  password
};

describe('signUp', () => {
  it('calls api.createAccount, dispatches signUpSuccess and signIn', () =>
    expectSaga(signUp, userData)
      // call api.createAccount with any data
      .provide([[matchers.call.fn(api.createAccount)]])
      .put(actions.signUpSuccess())

      // dispatch signIn with credentials only
      .put(actions.signIn('team-up', credentials))
      .run());

  it('dispatches signUpFailure on error', () => {
    const error = new Error('network error');

    return expectSaga(signUp, userData)
      .provide([[matchers.call.fn(api.createAccount), throwError(error)]])
      .put(actions.signUpFailure(error))
      .run();
  });
});

// describe('watchSignUp', () => {
//   it('takes SIGN_UP action', () =>
//     expectSaga(watchSignUp)
//       // calls signUp with userData
//       .call(signUp, userData)

//       // on SIGN_UP action dispatch
//       .dispatch(actions.signUp(userData))

//       // since it's a infinite generator, run silently to disable timeouit warning
//       .silentRun());
// });
