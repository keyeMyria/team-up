import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';
import classNames from 'classnames/bind';

import styles from '@/views/Auth/styles/form.css';

import InputField from '@/views/Auth/components/InputField';
import { validate, asyncValidate } from './validation';

const cx = classNames.bind(styles);

const RegisterForm = (props) => {
  const { handleSubmit, pristine, submitting } = props;
  return (
    <form className={props.cssClass} onSubmit={handleSubmit}>
      <div className={cx('formHeader')}>
        <div className="spacedRow">
          <a href="#logo">
            <div>
              <span>Team</span>up
            </div>
          </a>

          <i className="fa fa-times" style={{ cursor: 'pointer' }} onClick={props.onClose} />
        </div>
      </div>

      <div className={cx('formBody')}>
        <div className={cx('subtitle')}>Join Team-up</div>

        <Field
          type="email"
          component={InputField}
          name="email"
          id="emailField"
          placeholder="Email"
          iconClass="fa fa-envelope"
        />

        <Field
          type="text"
          component={InputField}
          name="username"
          id="usernameField"
          placeholder="Username"
          iconClass="fa fa-user"
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

      <div className={cx('formFooter')}>
        <div className="spacedRow">
          <button className="btn btn-dark" onClick={props.onLogin}>
            Sign In?
          </button>
          <div className={cx('form-actions')}>
            <button type="submit" className="btn btn-dark" disabled={pristine || submitting}>
              Create an account
            </button>
          </div>
        </div>
      </div>
    </form>
  );
};

RegisterForm.propTypes = {
  onClose: PropTypes.func.isRequired,
  onLogin: PropTypes.func.isRequired,
  cssClass: PropTypes.string,
  handleSubmit: PropTypes.func.isRequired,
  pristine: PropTypes.bool.isRequired,
  submitting: PropTypes.bool.isRequired
};

RegisterForm.defaultProps = {
  cssClass: ''
};

export default reduxForm({
  form: 'registerForm',
  validate,
  asyncValidate,
  asyncBlurFields: ['email', 'username']
})(RegisterForm);
