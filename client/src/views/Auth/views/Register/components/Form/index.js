import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

import { validate, asyncValidate } from './validation';

import InputField from 'views/Auth/components/Form/InputField';
import 'views/Auth/components/Form/styles.css';

const RegisterForm = props => {
  const { handleSubmit, pristine, submitting } = props;
  return (
    <form className={props.cssClass} onSubmit={handleSubmit}>
      <div className="formHeader">
        <div className="spacedRow">
          <a href="#logo">
            <div>
              <span>Team</span>up
            </div>
          </a>

          <i
            className="fa fa-times"
            style={{ cursor: 'pointer' }}
            onClick={props.onClose}
          />
        </div>
      </div>

      <div className="formBody">
        <div className="subtitle">Join Team-up</div>

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
          <div className="left">
            <button className="btn btn-dark" onClick={props.onLogin}>
              Sign In?
            </button>
          </div>
          <div className="right form-actions">
            <button
              type="submit"
              className="btn btn-dark"
              disabled={pristine || submitting}
            >
              Create an account
            </button>
          </div>
        </div>
      </div>
    </form>
  );
};

RegisterForm.propTypes = {
  onClose: PropTypes.func.isRequired
};

export default reduxForm({
  form: 'registerForm',
  validate,
  asyncValidate,
  asyncBlurFields: ['email']
})(RegisterForm);
