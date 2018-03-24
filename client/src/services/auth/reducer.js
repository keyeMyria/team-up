import { actionTypes } from './actions';

const authState = {
  authenticated: false,
  loading: true,
  token: null,
  error: null
};

const reducer = (state = authState, action) => {
  switch (action.type) {
    case actionTypes.SIGN_UP_SUCCESS: {
      // to be implemented
      return {
        ...state
      };
    }

    case actionTypes.SIGN_UP_FAILURE: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    case actionTypes.AUTO_SIGN_IN: {
      return {
        ...state,
        loading: true
      };
    }

    case actionTypes.SIGN_IN: {
      return {
        ...state,
        loading: true
      };
    }

    case actionTypes.SIGN_IN_SUCCESS: {
      const { token } = action;
      return {
        ...state,
        authenticated: true,
        loading: false,
        token
      };
    }

    case actionTypes.SIGN_IN_FAILURE: {
      const { error } = action;
      return {
        ...state,
        loading: false,
        error
      };
    }

    case actionTypes.SIGN_OUT_SUCCESS:
      return {
        ...state,
        authenticated: false,
        token: null
      };

    case actionTypes.SIGN_OUT_FAILURE: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    case actionTypes.REFRESH_TOKEN_SUCCESS: {
      const { refreshedToken } = action;
      return {
        ...state,
        token: refreshedToken
      };
    }

    case actionTypes.REFRESH_TOKEN_FAILURE: {
      const { error } = action;
      return {
        ...state,
        error
      };
    }

    default:
      return state;
  }
};

export default reducer;
