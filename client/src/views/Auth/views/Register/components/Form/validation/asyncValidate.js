import api from 'views/Auth/components/Form/api';

export const asyncValidate = (values, dispatch, props, field) => {
  const query = { [field]: values[field] };

  return api.validateFields(query).then(validated => {
    if (validated && validated[field] === 'invalid') {
      const error = `That ${field} is taken`;
      throw Object.assign({}, props.asyncErrors, { [field]: error });
    }
  });
};
