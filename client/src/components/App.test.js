import React from 'react';
import ReactDOM from 'react-dom';
import { ConnectedRouter } from 'react-router-redux';
import { Provider } from 'react-redux';
import createHistory from 'history/createBrowserHistory';
import configureStore from 'redux-mock-store';

import App from './App';

const mockStore = configureStore([]);
const store = mockStore({});
const history = createHistory();

describe('<App />', () => {
  const ConnectedApp = () => (
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <App />
      </ConnectedRouter>
    </Provider>
  );

  it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<ConnectedApp />, div);
    ReactDOM.unmountComponentAtNode(div);
  });
});
