import superagentPromise from 'superagent-promise';
import _superagent from 'superagent';

const superagent = superagentPromise(_superagent, global.Promise);

// const agent = request.agent()
//   .use(plugin)
//   .auth(shared);

// await agent.get('/with-plugin-and-auth');
// await agent.get('/also-with-plugin-and-auth');

// add superagent-use? with superagent-prefix and prefix every single auth request

const responseBody = res => res.body;

const appConfig = {
  client_id: process.env.REACT_APP_CLIENT_ID,
  client_secret: process.env.REACT_APP_CLIENT_SECRET
};

const AUTH_API_ROOT = process.env.REACT_APP_AUTH_API_ROOT;

const authApi = {
  getToken: (username, password) =>
    superagent
      .post(`${AUTH_API_ROOT}/token`)
      .send({
        ...appConfig,
        grant_type: 'password',
        username,
        password
      })
      .then(responseBody),

  refreshToken: refreshToken =>
    superagent
      .post(`${AUTH_API_ROOT}/token`)
      .send({
        ...appConfig,
        grant_type: 'refresh_token',
        refresh_token: refreshToken
      })
      .then(responseBody),

  convertToken: (backend, token) =>
    superagent
      .post(`${AUTH_API_ROOT}/convert-token`)
      .send({
        ...appConfig,
        grant_type: 'convert_token',
        backend,
        token
      })
      .then(responseBody),

  revokeToken: token =>
    superagent
      .post(`${AUTH_API_ROOT}/revoke-token`)
      .send({
        ...appConfig,
        token
      })
      .then(responseBody),

  invalidateSessions: token =>
    superagent
      .post(`${AUTH_API_ROOT}/invalidate-sessions`)
      .send({
        client_id: appConfig.client_id
      })
      .set('Authorization', `Bearer ${token}`)
      .then(responseBody)
};

export { authApi };
