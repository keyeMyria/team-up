import { call, put } from 'redux-saga/effects';

import { actions } from '../actions';
import { setAuthToken } from '../localStorage';
import signInFacebook from './facebook';
import signInTeamup from './teamup';

export class BackendException extends Error {
  constructor(...args) {
    super(...args);
    Error.captureStackTrace(this, BackendException);
  }
}

function* signIn(backend, payload) {
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
        throw new BackendException(`${backend} is not recognized as an authorization backend`);
    }
    yield call(setAuthToken, token); // save to local storage
    yield put(actions.signInSuccess(token));
  } catch (error) {
    yield put(actions.signInFailure(error));
  }

  return token;
}

export default signIn;
