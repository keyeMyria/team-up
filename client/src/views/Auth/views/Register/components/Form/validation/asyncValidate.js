import api from '@/data/accounts/api';

const asyncValidate = (values, dispatch, props, field) => {
  if (field === undefined) {
    // field is undefined on submitting, redux-forms expects a promise
    return new Promise(resolve => resolve());
    // for now, we don't need to validate all values as a whole on submit,
    // so let's just return return a promise that resolves immediately
  }

  const query = { [field]: values[field] };

  return api.validateFields(query).then((validated) => {
    if (validated && validated[field] === 'invalid') {
      // current assumption is that we get 'invalid' only if the field is not unique
      const error = `That ${field} is taken`;
      throw Object.assign({}, props.asyncErrors, { [field]: error });
    }
  });
};

export default asyncValidate;
