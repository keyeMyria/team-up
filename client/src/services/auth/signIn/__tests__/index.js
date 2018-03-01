import { call, put } from 'redux-saga/effects';

import { setAuthToken } from '../../localStorage';
import { authActions, authActionTypes } from '../../actions';
import { signIn } from '../index';
import { signInFacebook } from '../facebook';

const accessToken = 'EAAQxTWdZB4g8BAGeBNLSLanHY36ZA';
const payload = { accessToken };

describe('signIn', () => {
  describe('facebook backend', () => {
    const backend = 'facebook';
    const gen = signIn(backend, payload);

    it('calls signInFacebook', () => {
      expect(gen.next().value).toEqual(call(signInFacebook, payload));
    });

    it('calls setAuthToken', () => {
      expect(gen.next(accessToken).value).toEqual(
        call(setAuthToken, accessToken)
      );
    });

    it('dispatches signInSuccess action', () => {
      expect(gen.next().value).toEqual(
        put(authActions.signInSuccess(accessToken))
      );
    });
  });

  describe('invalid backend', () => {
    const backend = 'xyz';
    const gen = signIn(backend, payload);

    it('dispatches signInFailure action', () => {
      expect(gen.next().value.PUT.action.type).toBe(
        authActionTypes.SIGN_IN_FAILURE
      );
    });
  });
});
