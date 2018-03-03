import React from 'react';
import FacebookLogin from 'react-facebook-login';

import './styles.css';

const FbLogin = props => (
  <FacebookLogin
    appId={process.env.REACT_APP_FB_APP_ID}
    fields="name, email, picture"
    callback={props.onSignIn}
    // tag="button"
    // cssClass="loginBtn--facebook"
    tag="i"
    cssClass="fa fa-facebook loginIcon--facebook"
    textButton=""
    // onFailure?
  />
);

export default FbLogin;
