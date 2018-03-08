import _superagent from 'superagent';
import superagentPromise from 'superagent-promise';
import prefixer from 'superagent-prefix';

import { getAuthToken } from '@/services/auth/localStorage';

const superagent = superagentPromise(_superagent, global.Promise);

const DRF_ROOT = process.env.REACT_APP_DRF_ROOT;

// const encode = encodeURIComponent;
const responseBody = res => res.body;

const tokenPlugin = (req) => {
  const token = getAuthToken();
  if (token) {
    req.set('Authorization', `Bearer ${token.access_token}`);
  }
};

const requests = ({ prefix, agent }) => {
  const _prefix = prefixer(prefix || DRF_ROOT);
  const _agent = agent || superagent;

  return {
    get: (url, query) =>
      _agent
        .get(url)
        .query(query) // optional
        .use(_prefix)
        .use(tokenPlugin)
        .then(responseBody),

    post: (url, body) =>
      _agent
        .post(url, body)
        .use(_prefix)
        .use(tokenPlugin)
        .then(responseBody),

    put: (url, body) =>
      _agent
        .put(url, body)
        .use(_prefix)
        .use(tokenPlugin)
        .then(responseBody),

    del: url =>
      _agent
        .del(url)
        .use(_prefix)
        .use(tokenPlugin)
        .then(responseBody)
  };
};

export default requests;
