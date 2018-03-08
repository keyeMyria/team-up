import React, { Fragment } from 'react';
import PropTypes from 'prop-types';

import '@/views/Auth/components/Form/styles.css'; // TODO: clean styles
import Form from './components/Form';

const Login = props => (
  <Fragment>
    <Form
      cssClass="authBox"
      onSubmit={(formData) => {
        props.signIn('team-up', formData); // CLOSE ON SUCCESS, ERROR ON FAILURE
      }}
      onClose={props.onClose}
      onFacebookSignIn={payload => props.signIn('facebook', payload)} // TODO: close on finish
      onRegister={props.onRegister}
    />

    {/* TEMPORARY INLINE STYLING */}
    <div
      className="authBox"
      style={{
        position: 'relative',
        top: '20px',
        padding: '14px 28px'
      }}
    >
      <div className="spacedRow">
        Don&apos;t have an account?
        <button onClick={props.onRegister} className="btn btn-dark" style={{ marginLeft: 'auto' }}>
          Sign Up
        </button>
      </div>
    </div>
    {/* TEMPORARY */}
  </Fragment>
);

Login.propTypes = {
  signIn: PropTypes.func.isRequired,
  onClose: PropTypes.func.isRequired,
  onRegister: PropTypes.func.isRequired
};

export default Login;
