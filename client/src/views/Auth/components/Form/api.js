import _requests from '@/services/agent';

const prefix = process.env.REACT_APP_ACCOUNTS_ROOT;
const requests = _requests({ prefix });

const validationApi = {
  validateFields: values => requests.get('/validate', values)
};

export default validationApi;
