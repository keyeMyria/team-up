import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames/bind';

import styles from '@/views/Auth/styles.css';
import Form from './components/Form';

const cx = classNames.bind(styles);

const Register = props => (
  <Form
    cssClass={cx('authBox')}
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
