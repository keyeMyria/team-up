import { call, put } from 'redux-saga/effects';

import { getAuthToken, removeAuthToken } from '../localStorage';
import { actions } from '../actions';
import api from '../api';

function* signOut() {
  try {
    const token = yield call(getAuthToken);
    if (token) {
      yield call(api.revokeToken, token.access_token);
      yield call(removeAuthToken);
    }
    // for now, if token is already gone, dispatch success,
    // since it changes auth.authenticated flag
    yield put(actions.signOutSuccess());
  } catch (error) {
    yield put(actions.signOutFailure(error));
  }
}

export default signOut;
