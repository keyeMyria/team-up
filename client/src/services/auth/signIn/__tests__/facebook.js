import { expectSaga } from 'redux-saga-test-plan';
import * as matchers from 'redux-saga-test-plan/matchers';

import api from '../../api';
import signInFacebook from '../facebook';

const accessToken = 'EAAQxTWdZB4g8BAGeBNLSLanHY36ZA';
const payload = { accessToken };

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signInFacebook', () => {
  it('calls api and returns token', () =>
    expectSaga(signInFacebook, payload)
      .provide([[matchers.call(api.convertToken, 'facebook', accessToken), token]])
      .returns(token)
      .run());
});
