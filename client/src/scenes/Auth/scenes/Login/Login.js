import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { authActions } from 'services/auth';
import LoginForm from '../../components/LoginForm/LoginForm';
import FacebookLogin from '../../components/FacebookLogin/FacebookLogin';

class Login extends Component {
  render() {
    return (
      <div>
        <LoginForm
          onSubmit={formData => this.props.signIn('team-up', formData)}
        />
        {/* <FacebookLogin */}
        {/* onSignIn={payload => this.props.signIn('facebook', payload)} */}
        {/* /> */}
      </div>
    );
  }
}

Login.propTypes = {
  signIn: PropTypes.func.isRequired
};

const mapDispatchToProps = dispatch => ({
  signIn: (backend, payload) => dispatch(authActions.signIn(backend, payload))
});

export default connect(null, mapDispatchToProps)(Login);
