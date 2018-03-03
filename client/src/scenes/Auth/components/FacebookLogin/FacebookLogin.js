import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import FacebookLogin from 'react-facebook-login';

import { authActions } from '../../../../services/auth';

class FacebookLoginButton extends Component {
  responseFacebook = (response) => {
    this.props.signIn('facebook', response);
  };

  render() {
    return (
      <div>
        <FacebookLogin
          appId="1180108425454095" // TODO: hardcode it somewhere else
          fields="name,email,picture"
          callback={this.responseFacebook}
          // onFailure?
        />
        <button onClick={() => this.props.signOut()}>SIGN OUT</button>
      </div>
    );
  }
}

FacebookLoginButton.propTypes = {
  signIn: PropTypes.func.isRequired,
  signOut: PropTypes.func.isRequired
};

const mapDispatchToProps = dispatch => ({
  signIn: (backend, payload) => dispatch(authActions.signIn(backend, payload)),
  signOut: () => dispatch(authActions.signOut())
});

export default connect(null, mapDispatchToProps)(FacebookLoginButton);
