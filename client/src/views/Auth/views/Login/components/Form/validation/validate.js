export const validate = values => {
  const errors = {};
  if (!values.email) {
    errors.email = 'Field Required';
  }
  if (!values.password) {
    errors.password = 'Field Required';
  }
  return errors;
};
