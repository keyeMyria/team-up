import { call, put } from 'redux-saga/effects';

import { authActions } from '../actions';
import { setAuthToken } from '../localStorage';
import { signInFacebook } from './facebook';
import { signInTeamup } from './teamup';

export function BackendException(message) {
  this.message = message;
  this.name = 'BackendException';
}

export function* signIn(backend, payload) {
  let token;

  try {
    switch (backend) {
      case 'facebook': {
        token = yield call(signInFacebook, payload);
        break;
      }
      case 'team-up': {
        token = yield call(signInTeamup, payload);
        break;
      }
      default:
        throw new BackendException(
          `${backend} is not recognized as an authorization backend`
        );
    }
    yield call(setAuthToken, token); // save to local storage
    yield put(authActions.signInSuccess(token));
  } catch (error) {
    yield put(authActions.signInFailure(error));
  }

  return token;
}
