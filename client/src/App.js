import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Route } from 'react-router-dom';
import PropTypes from 'prop-types';

import { authActions } from '@/services/auth';

import Layout from '@/views/Layout';
import Start from '@/views/Start';

// TEMPORARY IMPORTS - TESTING
import Auth from '@/views/Auth';
import SignOut from '@/views/Layout/components/Header/Toolbar/NavItems/NavItem/SignOut';

class App extends Component {
  componentDidMount() {
    this.props.tryAutoSignIn();
  }

  render() {
    return (
      <Layout>
        <Route exact path='/' component={Start}/>
      </Layout>
    );
  }
}

App.propTypes = {
  tryAutoSignIn: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool.isRequired
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.authenticated
});

const mapDispatchToProps = dispatch => ({
  tryAutoSignIn: () => dispatch(authActions.autoSignIn())
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
