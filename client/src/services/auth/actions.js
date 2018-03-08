export const actionTypes = {
  SIGN_UP: 'AUTH/SIGN_UP',
  SIGN_UP_SUCCESS: 'AUTH/SIGN_UP_SUCCESS',
  SIGN_UP_FAILURE: 'AUTH/SIGN_UP_FAILURE',

  SIGN_IN: 'AUTH/SIGN_IN',
  SIGN_IN_SUCCESS: 'AUTH/SIGN_IN_SUCCESS',
  SIGN_IN_FAILURE: 'AUTH/SIGN_IN_FAILURE',

  SIGN_OUT: 'AUTH/SIGN_OUT',
  SIGN_OUT_SUCCESS: 'AUTH/SIGN_OUT_SUCCESS',
  SIGN_OUT_FAILURE: 'AUTH/SIGN_OUT_FAILURE',

  REFRESH_TOKEN: 'AUTH/REFRESH_TOKEN',
  REFRESH_TOKEN_SUCCESS: 'AUTH/REFRESH_TOKEN_SUCCESS',
  REFRESH_TOKEN_FAILURE: 'AUTH/REFRESH_TOKEN_FAILURE',

  AUTO_SIGN_IN: 'AUTH/AUTO_SIGN_IN',
  START_TOKEN_VALIDATION: 'AUTH/START_TOKEN_VALIDATION'
};

export const actions = {
  signUp: userData => ({
    type: actionTypes.SIGN_UP,
    userData
  }),

  signUpSuccess: token => ({
    type: actionTypes.SIGN_UP_SUCCESS
  }),

  signUpFailure: error => ({
    type: actionTypes.SIGN_UP_FAILURE,
    error
  }),

  signIn: (backend, payload) => ({
    type: actionTypes.SIGN_IN,
    backend,
    payload
  }),

  signInSuccess: token => ({
    type: actionTypes.SIGN_IN_SUCCESS,
    token
  }),

  signInFailure: error => ({
    type: actionTypes.SIGN_IN_FAILURE,
    error
  }),

  signOut: () => ({
    type: actionTypes.SIGN_OUT
  }),

  signOutSuccess: () => ({
    type: actionTypes.SIGN_OUT_SUCCESS
  }),

  signOutFailure: error => ({
    type: actionTypes.SIGN_OUT_FAILURE,
    error
  }),

  refreshToken: () => ({
    type: actionTypes.REFRESH_TOKEN
  }),

  refreshTokenSuccess: refreshedToken => ({
    type: actionTypes.REFRESH_TOKEN_SUCCESS,
    refreshedToken
  }),

  refreshTokenFailure: error => ({
    type: actionTypes.REFRESH_TOKEN_FAILURE,
    error
  }),

  autoSignIn: () => ({
    type: actionTypes.AUTO_SIGN_IN
  }),

  startTokenValidation: token => ({
    type: actionTypes.START_TOKEN_VALIDATION,
    token
  })
};
