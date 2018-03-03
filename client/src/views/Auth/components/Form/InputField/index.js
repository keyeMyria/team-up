import React from 'react';

import './styles.css';

const InputField = ({
  id,
  input,
  placeholder,
  type,
  iconClass,
  meta: { asyncValidating, touched, error }
}) => (
  <div className="formElement">
    {/* className={asyncValidating ? 'async-validating' : ''} */}
    <div className="inputField">
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

export default InputField;
