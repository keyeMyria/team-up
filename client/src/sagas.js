import { all } from 'redux-saga/effects';
import { authSagas } from './services/auth';

export default function* sagas() {
  yield all([...authSagas]);
}
