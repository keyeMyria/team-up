import { delay } from 'redux-saga';
import { fork, call, take, race, put } from 'redux-saga/effects';

import { authActions, authActionTypes } from './actions';
import {
  getAuthToken,
  getAuthTokenExpirationDate,
  setAuthToken
} from './localStorage';
import { authApi } from './api';
import { signIn } from './signIn';
import { signOut } from './signOut';
import { timeoutDelta } from '../../utils';

function* refreshTokenOnExpiry(_token) {
  let token = _token;

  while (true) {
    if (!token) break; // something went wrong, got null token

    yield put(authActions.refreshToken());

    try {
      token = yield call(authApi.refreshToken, token.refresh_token);
      yield call(setAuthToken, token); // save to local storage
      yield put(authActions.refreshTokenSuccess(token));
      yield call(delay, timeoutDelta(token.expires_in, -300)); // 5 minutes before
    } catch (error) {
      yield put(authActions.refreshTokenFailure(error));

      yield call(delay, 5000);
      // added some delay on failure, since otherwise it would create an infinite loop
      // if the initial _token is (present) but there is no response from server

      // TODO: check if refreshing old token works (it should not)
    }
  }
}

function* authorizeOnRefresh() {
  yield take(authActionTypes.AUTO_SIGN_IN);
  const token = yield call(getAuthToken);
  const tokenExpirationDate = yield call(getAuthTokenExpirationDate);

  if (token) {
    if (tokenExpirationDate > new Date()) {
      yield put(authActions.signInSuccess(token));
      return token;
    } else {
      yield put(authActions.signInFailure('token expired'));
    }
  } else {
    yield put(authActions.signInFailure('no token in localstorage'));
  }
  return null;
}

function* authorize() {
  const { backend, payload } = yield take(authActionTypes.SIGN_IN);
  const token = yield call(signIn, backend, payload);
  return token;
}

function* authorizeAndRefreshTokenOnExpiry() {
  while (true) {
    const { token, refreshToken } = yield race({
      token: call(authorize),
      refreshToken: call(authorizeOnRefresh)
    });

    if (token) {
      yield call(delay, timeoutDelta(token.expires_in, -300)); // 5 minutes before
    }

    yield call(refreshTokenOnExpiry, token || refreshToken);
  }
}

function* authorizeSaga() {
  while (true) {
    yield race([
      take(authActionTypes.SIGN_OUT),
      call(authorizeAndRefreshTokenOnExpiry)
    ]);

    yield call(signOut);
  }
}

export const authSagas = [fork(authorizeSaga)];
