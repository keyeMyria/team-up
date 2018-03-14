import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';
import { throwError } from 'redux-saga-test-plan/providers';

import { getAuthToken, removeAuthToken } from '../../localStorage';
import { actions, actionTypes } from '../../actions';
import api from '../../api';
import signOut from '../index';

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signOut', () => {
  describe('token in localStorage', () => {
    it('revokes token and dispatches signOutSuccess on success', () =>
      expectSaga(signOut)
        .provide([
          [matchers.call.fn(getAuthToken), token],
          [matchers.call.fn(removeAuthToken)],
          [matchers.call.fn(api.revokeToken)]
        ])
        .put(actions.signOutSuccess())

        .call.fn(removeAuthToken)
        .call(api.revokeToken, token.access_token)
        .run());

    it('dispatches signOutFailure on error', () => {
      const error = new Error('network error');

      return (
        expectSaga(signOut)
          .provide([
            [matchers.call.fn(getAuthToken), token],
            [matchers.call.fn(removeAuthToken)],
            [matchers.call.fn(api.revokeToken), throwError(error)]
          ])
          .put(actions.signOutFailure(error))

          .call(api.revokeToken, token.access_token)
          // make sure token wasn't removed from localStorage,
          // so we can signOut and revoke it later
          .not.call.fn(removeAuthToken)
          .run()
      );
    });
  });

  describe('no token in localStorage', () => {
    it('dispatches signOutSuccess', () =>
      expectSaga(signOut)
        .provide([[matchers.call.fn(getAuthToken), null]])
        .put(actions.signOutSuccess())
        .run());
  });
});
