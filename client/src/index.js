import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'react-router-redux';
import { Switch } from 'react-router-dom';

import store from './store';
import history from './history';

import routes from './routes';
import './styles/index.css';

ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <Switch>{routes}</Switch>
    </ConnectedRouter>
  </Provider>,
  document.getElementById('root')
);
