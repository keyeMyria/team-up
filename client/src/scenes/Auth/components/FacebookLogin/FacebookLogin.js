import React from 'react';
import FacebookLogin from 'react-facebook-login';

import './FacebookLogin.css';

const facebookLoginButton = props => (
  <div>
    <FacebookLogin
      appId={process.env.REACT_APP_FB_APP_ID}
      fields="name, email, picture"
      callback={props.onSignIn}
      cssClass="loginBtn loginBtn--facebook"
      textButton="Log in With Facebook"
      // onFailure?
    />
  </div>
);

export default facebookLoginButton;
