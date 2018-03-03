import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

import { validate } from './validation';

import InputField from 'views/Auth/components/Form/InputField';
import FacebookLogin from '../FacebookLogin';
import 'views/Auth/components/Form/styles.css';

const LoginForm = props => {
  const { handleSubmit, pristine, submitting } = props;
  return (
    <form className={props.cssClass} onSubmit={handleSubmit}>
      <div className="formHeader">
        <div className="spacedRow">
          <Link to="/" onClick={props.onClose}>
            <span>Team</span>up
          </Link>
          <i
            className="fa fa-times"
            style={{ cursor: 'pointer' }}
            onClick={props.onClose}
          />
        </div>
      </div>

      <div className="formBody">
        <div className="subtitle">Sign in to Team-up</div>

        <Field
          type="email"
          component={InputField}
          name="email"
          id="emailField"
          placeholder="Email"
          iconClass="fa fa-envelope"
        />

        <Field
          type="password"
          component={InputField}
          name="password"
          id="passwordField"
          placeholder="Password"
          iconClass="fa fa-lock fa-lg"
        />
      </div>

      <div className="formFooter">
        <div className="spacedRow">
          <div className="social-login">
            Sign in with:
            <FacebookLogin
              onSignIn={payload => {
                props.onFacebookSignIn(payload);
                props.onClose();
              }}
            />
            <i className="fa fa-fw fa-google-plus fa-lg" />
          </div>

          <div className="form-actions">
            <button
              type="submit"
              className="btn btn-dark"
              disabled={pristine || submitting}
            >
              Sign In
            </button>
          </div>
        </div>
      </div>
    </form>
  );
};

LoginForm.propTypes = {
  onClose: PropTypes.func.isRequired,
  onFacebookSignIn: PropTypes.func.isRequired,
  cssClass: PropTypes.string,
  handleSubmit: PropTypes.func.isRequired,
  pristine: PropTypes.bool.isRequired,
  submitting: PropTypes.bool.isRequired
};

export default reduxForm({
  form: 'loginForm',
  validate
})(LoginForm);
