import { call } from 'redux-saga/effects';

import { authApi } from '../api';

function* signInFacebook(payload) {
  // payload contains accessToken, expiresIn, userID
  // and user fields of your choice, currently: email, name, picture
  const { accessToken } = payload;
  return yield call(authApi.convertToken, 'facebook', accessToken);
}

export { signInFacebook };
