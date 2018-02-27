import { authActionTypes } from './actions';

const authState = {
  authenticated: false,
  token: null,
  error: null
};

export function authReducer(state = authState, action) {
  switch (action.type) {
    case authActionTypes.SIGN_IN_FULFILLED: {
      const { token } = action;
      return {
        ...state,
        authenticated: true,
        token
      };
    }

    case authActionTypes.SIGN_IN_FAILED: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    case authActionTypes.SIGN_OUT_FULFILLED:
      return {
        ...state,
        authenticated: false,
        token: null
      };

    case authActionTypes.SIGN_OUT_FAILED: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    case authActionTypes.REFRESH_TOKEN_SUCCESS: {
      const { refreshedToken } = action;
      return {
        ...state,
        token: refreshedToken
      };
    }

    case authActionTypes.REFRESH_TOKEN_FAIL: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    default:
      return state;
  }
}
