import _requests from '@/services/agent';

const prefix = process.env.REACT_APP_ACCOUNTS_ROOT;
const requests = _requests({ prefix });

const accountsApi = {
  changePassword: (oldPassword, newPassword) =>
    requests.put('/change-password', {
      old_password: oldPassword,
      new_password: newPassword
    }),

  createAccount: (email, username, password) =>
    requests.post('/create', { email, username, password }),

  retrieveMyAccount: () => requests.get('/me'),

  updateMyAccount: accountData => requests.put('/me', accountData),

  deleteMyAccount: () => requests.delete('/me'),

  validateFields: values => requests.get('/validate', values)
};

export default accountsApi;
