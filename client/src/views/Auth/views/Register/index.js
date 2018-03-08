import React from 'react';
import PropTypes from 'prop-types';

import Form from './components/Form';

const Register = props => (
  <Form
    cssClass="authBox"
    onSubmit={(formData) => {
      props.signUp(formData);
      props.onClose(); // TODO: differentiate actions on formSubmit and formClose?
    }}
    onClose={props.onClose}
    onLogin={props.onLogin}
  />
);

Register.propTypes = {
  signUp: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
  onLogin: PropTypes.func.isRequired
};

export default Register;
