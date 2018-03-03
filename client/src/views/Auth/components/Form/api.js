import superagentPromise from 'superagent-promise';
import _superagent from 'superagent';

const superagent = superagentPromise(_superagent, global.Promise);
const responseBody = res => res.body;

const ACCOUNTS_API_ROOT = process.env.REACT_APP_ACCOUNTS_API_ROOT;

const validationApi = {
  validateFields: values =>
    superagent
      .get(`${ACCOUNTS_API_ROOT}/validate`)
      .query(values)
      .then(responseBody)
};

export default validationApi;
