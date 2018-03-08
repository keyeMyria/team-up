import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';
import { throwError } from 'redux-saga-test-plan/providers';

import { setAuthToken } from '../../localStorage';
import { actions, actionTypes } from '../../actions';
import signIn, { BackendException } from '../index';
import signInFacebook from '../facebook';

const accessToken = 'EAAQxTWdZB4g8BAGeBNLSLanHY36ZA';
const payload = { accessToken };

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signIn', () => {
  describe('valid backend [facebook]', () => {
    const backend = 'facebook';

    it('dispatches signInSuccess on success and returns a token', () =>
      expectSaga(signIn, backend, payload)
        .provide([[matchers.call(signInFacebook, payload), token]])
        .call(setAuthToken, token)
        .put(actions.signInSuccess(token))
        .returns(token)
        .run());

    it('dispatches signInFailure on error', () => {
      const error = new Error('error');

      return (
        expectSaga(signIn, backend, payload)
          .provide([[matchers.call(signInFacebook, payload), throwError(error)]])
          .put(actions.signInFailure(error))
          // token wasn't assigned, so undefined is returned
          .returns(undefined)
          .run()
      );
    });
  });

  describe('invalid backend', () => {
    const backend = 'invalid';

    it('throws BackendException and dispatches signInFailure on error', async () => {
      const { effects } = await expectSaga(signIn, backend, payload)
        // .not.call.fn(signInFacebook) // check if neither of backend signIn were called
        .returns(undefined)
        .run();

      const { type, error } = effects.put[0].PUT.action;
      expect(type).toBe(actionTypes.SIGN_IN_FAILURE);
      expect(error).toBeInstanceOf(BackendException);
    });
  });
});
