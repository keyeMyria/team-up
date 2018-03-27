import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';
import { routerReducer } from 'react-router-redux';

import { authReducer } from '@/services/auth';

export default combineReducers({
  auth: authReducer,
  form: formReducer,
  router: routerReducer
});
