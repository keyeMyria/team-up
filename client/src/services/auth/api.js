import _requests from '@/services/agent';

const prefix = process.env.REACT_APP_AUTH_ROOT;
const requests = _requests({ prefix });

const appConfig = {
  client_id: process.env.REACT_APP_CLIENT_ID,
  client_secret: process.env.REACT_APP_CLIENT_SECRET
};

const authApi = {
  getToken: (username, password) =>
    requests.post('/token', {
      ...appConfig,
      grant_type: 'password',
      username,
      password
    }),

  refreshToken: refreshToken =>
    requests.post('/token', {
      ...appConfig,
      grant_type: 'refresh_token',
      refresh_token: refreshToken
    }),

  convertToken: (backend, token) =>
    requests.post('/convert-token', {
      ...appConfig,
      grant_type: 'convert_token',
      backend,
      token
    }),

  revokeToken: token =>
    requests.post('/revoke-token', {
      ...appConfig,
      token
    }),

  invalidateSessions: token =>
    requests.post('/invalidate-sessions', {
      client_id: appConfig.client_id
    })
};

export default authApi;
