import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames/bind';

import styles from './styles.css';

const cx = classNames.bind(styles);

const InputField = ({
  id,
  input,
  placeholder,
  type,
  iconClass,
  meta: { asyncValidating, touched, error }
}) => (
  <div className={cx('formElement')}>
    {/* className={asyncValidating ? 'async-validating' : ''} */}
    <div className={cx('inputField')}>
      <input
        {...input}
        type={type}
        placeholder={placeholder}
        id={id}
        className={`form-control ${touched && error && 'is-invalid'}`}
      />
      <label htmlFor={id}>
        <i className={iconClass} aria-hidden />
      </label>
    </div>
    {touched &&
      error && (
        <div className="invalid-feedback" style={{ display: 'block' }}>
          {error}
        </div>
      )}
  </div>
);

InputField.propTypes = {
  /* eslint-disable react/forbid-prop-types */
  id: PropTypes.string.isRequired,
  input: PropTypes.object.isRequired,
  placeholder: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired,
  iconClass: PropTypes.string.isRequired,
  meta: PropTypes.object.isRequired
};

export default InputField;
