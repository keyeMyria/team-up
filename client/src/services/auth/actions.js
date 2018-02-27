export const authActionTypes = {
  SIGN_IN: 'AUTH/SIGN_IN',
  SIGN_IN_SUCCESS: 'AUTH/SIGN_IN_SUCCESS',
  SIGN_IN_FAILURE: 'AUTH/SIGN_IN_FAILURE',

  SIGN_OUT: 'AUTH/SIGN_OUT',
  SIGN_OUT_SUCCESS: 'AUTH/SIGN_OUT_SUCCESS',
  SIGN_OUT_FAILURE: 'AUTH/SIGN_OUT_FAILURE',

  REFRESH_TOKEN: 'AUTH/REFRESH_TOKEN',
  REFRESH_TOKEN_SUCCESS: 'AUTH/REFRESH_TOKEN_SUCCESS',
  REFRESH_TOKEN_FAILURE: 'AUTH/REFRESH_TOKEN_FAILURE',

  AUTO_SIGN_IN: 'AUTH/AUTO_SIGN_IN'
};

export const authActions = {
  signIn: (backend, payload) => ({
    type: authActionTypes.SIGN_IN,
    backend,
    payload
  }),

  signInSuccess: token => ({
    type: authActionTypes.SIGN_IN_SUCCESS,
    token
  }),

  signInFailure: error => ({
    type: authActionTypes.SIGN_IN_FAILURE,
    error
  }),

  signOut: () => ({
    type: authActionTypes.SIGN_OUT
  }),

  signOutSuccess: () => ({
    type: authActionTypes.SIGN_OUT_SUCCESS
  }),

  signOutFailure: error => ({
    type: authActionTypes.SIGN_OUT_FAILED,
    error
  }),

  refreshToken: () => ({
    type: authActionTypes.REFRESH_TOKEN
  }),

  refreshTokenSuccess: refreshedToken => ({
    type: authActionTypes.REFRESH_TOKEN_SUCCESS,
    refreshedToken
  }),

  refreshTokenFailure: error => ({
    type: authActionTypes.REFRESH_TOKEN_FAILURE,
    error
  }),

  autoSignIn: () => ({
    type: authActionTypes.AUTO_SIGN_IN
  })
};
