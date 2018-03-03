import { authActionTypes } from './actions';

const authState = {
  authenticated: false,
  token: null,
  error: null
};

export function authReducer(state = authState, action) {
  switch (action.type) {
    case authActionTypes.SIGN_IN_SUCCESS: {
      const { token } = action;
      return {
        ...state,
        authenticated: true,
        token
      };
    }

    case authActionTypes.SIGN_IN_FAILURE: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    case authActionTypes.SIGN_OUT_SUCCESS:
      return {
        ...state,
        authenticated: false,
        token: null
      };

    case authActionTypes.SIGN_OUT_FAILURE: {
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

    case authActionTypes.REFRESH_TOKEN_FAILURE: {
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
