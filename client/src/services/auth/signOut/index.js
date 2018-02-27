import { call, put } from 'redux-saga/effects';

import { authActions } from '../actions';
import { authApi } from '../api';
import { getAuthToken, removeAuthToken } from '../localStorage';

function* signOut() {
  try {
    const token = yield call(getAuthToken);
    if (token) {
      yield call(removeAuthToken);
      yield call(authApi.revokeToken, token.access_token);
      // TODO: rethink the order of these calls, since if the error happens in the call api,
      // you can't revoke the token anymore
    }
    yield put(authActions.signOutSuccess());
  } catch (error) {
    yield put(authActions.signOutFailure(error));
  }
}

export { signOut };
