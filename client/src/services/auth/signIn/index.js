import { call, put } from 'redux-saga/effects';

import { authActions } from '../actions';
import { setAuthToken } from '../localStorage';
import { signInFacebook } from './facebook';

function BackendException(message) {
  this.message = message;
  this.name = 'BackendException';
}

function* signIn(backend, payload) {
  let token;

  try {
    switch (backend) {
      case 'facebook': {
        token = yield call(signInFacebook, payload);
        break;
      }
      default:
        throw new BackendException(`${backend} is not recognized as an authorization backend`);
    }
    yield call(setAuthToken, token); // save to local storage
    yield put(authActions.signInSuccess(token));
  } catch (error) {
    yield put(authActions.signInFailure(error));
  }

  return token;
}

export { signIn };
