import { call } from 'redux-saga/effects';

import api from '../api';

function* signInTeamup(credentials) {
  const { email, password } = credentials;
  return yield call(api.getToken, email, password);
}

export default signInTeamup;
