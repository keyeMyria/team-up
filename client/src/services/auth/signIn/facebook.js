import { call } from 'redux-saga/effects';

import api from '../api';

function* signInFacebook(payload) {
  // payload contains accessToken, expiresIn, userID
  // and user fields of your choice, currently: email, name, picture
  const { accessToken } = payload;
  return yield call(api.convertToken, 'facebook', accessToken);
}

export default signInFacebook;
