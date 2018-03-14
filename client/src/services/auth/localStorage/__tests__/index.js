import { LocalStorageMock } from '@/utils/jest';
import { getAuthToken, getAuthTokenExpirationDate, setAuthToken, removeAuthToken } from '../index';

const token = {
  access_token: 'pGJ2mrEVMNgbvbPRgaxbkuBeP3uwNG',
  expires_in: 36000,
  refresh_token: 'exsWfd5mQ7CFtA4TvCE1tmaBq5cUea'
};

describe('localStorage', () => {
  const _localStorage = localStorage;
  const _Date = Date;
  const DATE_TO_USE = new Date();

  beforeAll(() => {
    // freeze time in each test
    global.Date = jest.fn(() => DATE_TO_USE);
    global.Date.UTC = _Date.UTC;
    global.Date.parse = _Date.parse;
    global.Date.now = _Date.now;

    global.localStorage = new LocalStorageMock();
  });

  afterAll(() => {
    // reassign Date and localStorage back to the original objects/functions
    global.Date = _Date;
    global.localStorage = _localStorage;
  });

  afterEach(() => {
    // clear mocked local storage after each test
    localStorage.clear();
  });

  it('gets auth token', () => {
    localStorage.setItem('authToken', JSON.stringify(token));

    expect(getAuthToken()).toEqual(token);
  });

  it('gets token expiration date', () => {
    // time is frozen here
    const dateNow = new Date();
    localStorage.setItem('tokenExpirationDate', dateNow);

    expect(getAuthTokenExpirationDate()).toEqual(dateNow);
  });

  it('sets auth token and token expiration date', () => {
    // time is frozen here
    const expirationTime = new Date(Date.now() + token.expires_in * 1000);
    setAuthToken(token);

    expect(JSON.parse(localStorage.getItem('authToken'))).toEqual(token);
    expect(localStorage.getItem('tokenExpirationDate')).toEqual(expirationTime);
  });

  it('removes auth token and token expiration date', () => {
    localStorage.setItem('authToken', JSON.stringify(token));
    removeAuthToken();

    expect(localStorage.getItem('authToken')).toBeNull();
    expect(localStorage.getItem('tokenExpirationDate')).toBeNull();
  });
});
