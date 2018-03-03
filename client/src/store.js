import { applyMiddleware, createStore } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension/developmentOnly';
import { createLogger } from 'redux-logger';
import { routerMiddleware } from 'react-router-redux';
import createSagaMiddleware from 'redux-saga';

import history from './history';
import reducers from './reducer';
import rootSaga from './sagas';

// Build the middleware for intercepting and dispatching navigation actions
const myRouterMiddleware = routerMiddleware(history);
const sagaMidlleware = createSagaMiddleware();

const middleware = [sagaMidlleware, myRouterMiddleware];

if (process.env.NODE_ENV === 'development') {
  const logger = createLogger({
    collapsed: true,
    predicate: (getState, action) => !/^@@redux-form/.test(action.type)
  });

  middleware.push(logger);
}

const store = createStore(
  reducers,
  composeWithDevTools(applyMiddleware(...middleware))
);
sagaMidlleware.run(rootSaga);

export default store;
