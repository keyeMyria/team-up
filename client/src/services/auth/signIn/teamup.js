import { call } from 'redux-saga/effects';

import { authApi } from '../api';

function* signInTeamup(credentials) {
  const { email, password } = credentials;
  return yield call(authApi.getToken, email, password);
}

export { signInTeamup };
