import { call } from 'redux-saga/effects';
import { authApi } from '../../api';
import { signInFacebook } from '../facebook';

const accessToken = 'EAAQxTWdZB4g8BAGeBNLSLanHY36ZA';
const payload = { accessToken };

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  token_type: 'Bearer',
  scope: 'read write',
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signInFacebook', () => {
  const gen = signInFacebook(payload);

  it('calls authApi.convertToken', () => {
    expect(gen.next().value).toEqual(
      call(authApi.convertToken, 'facebook', accessToken)
    );
  });

  it('returns app token', () => {
    expect(gen.next(token).value).toEqual(token);
  });
});
