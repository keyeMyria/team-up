import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import { authActions } from 'services/auth';

const signOut = props => {
  return <button onClick={props.signOut}>Sign Out</button>;
};

signOut.propTypes = {
  signOut: PropTypes.func.isRequired
};

const mapDispatchToProps = dispatch => ({
  signOut: () => dispatch(authActions.signOut())
});

export default connect(null, mapDispatchToProps)(signOut);
