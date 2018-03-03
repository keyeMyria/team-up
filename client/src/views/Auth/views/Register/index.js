import React from 'react';
// import { connect } from 'react-redux';
import PropTypes from 'prop-types';

// import { authActions } from 'services/auth';
import Form from './components/Form';

const Register = props => (
  <Form
    cssClass="authBox"
    onSubmit={formData => {
      props.signUp('team-up', formData);
      props.onClose(); // TODO: differentiate actions on formSubmit and formClose?
    }}
    onClose={props.onClose}
    onLogin={props.onLogin}
  />
);

// TODO: add signUp saga and actionCreator

// register.propTypes = {
//   signUp: PropTypes.func.isRequired
// };

// const mapDispatchToProps = dispatch => ({
//   signIn: (backend, payload) => dispatch(authActions.signIn(backend, payload))
// });

// export default connect(null, mapDispatchToProps)(register);

export default Register;
