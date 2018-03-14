import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';

import api from '../../api';
import signInTeamup from '../teamup';

const credentials = {
  email: 'admin@example.com',
  password: 'admin'
};

const { email, password } = credentials;

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signInTeamup', () => {
  it('calls authApi.getToken and returns app token', () =>
    expectSaga(signInTeamup, credentials)
      .provide([[matchers.call(api.getToken, email, password), token]])
      .returns(token)
      .run());
});
