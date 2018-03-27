import { call, put } from 'redux-saga/effects';

import api from '@/data/accounts/api';
import { actions } from '../actions';

function* signUp(userData) {
  const { email, username, password } = userData;

  try {
    yield call(api.createAccount, email, username, password);
    yield put(actions.signUpSuccess());

    const credentials = {
      email,
      username,
      password
    };

    yield put(actions.signIn('team-up', credentials));
  } catch (error) {
    yield put(actions.signUpFailure(error));
  }
}

export default signUp;
