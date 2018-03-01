import { call } from 'redux-saga/effects';
import { authApi } from '../../api';
import { signInTeamup } from '../teamup';

const credentials = {
  email: 'admin@example.com',
  password: 'admin'
};

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  token_type: 'Bearer',
  scope: 'read write',
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('signInTeamup', () => {
  const gen = signInTeamup(credentials);

  it('calls authApi.getToken', () => {
    const { email, password } = credentials;

    expect(gen.next().value).toEqual(call(authApi.getToken, email, password));
  });

  it('returns app token', () => {
    expect(gen.next(token).value).toEqual(token);
  });
});
