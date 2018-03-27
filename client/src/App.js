import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Route, Redirect, Switch } from 'react-router-dom';
import PropTypes from 'prop-types';

import { authActions } from '@/services/auth';

import ProtectedRoute from '@/components/ProtectedRoute';
import Layout from '@/views/Layout';
import Start from '@/views/Start';
import Auth from '@/views/Auth';

const TestComponent = () => <h1>Test It</h1>;

class App extends Component {
  componentDidMount() {
    this.props.tryAutoSignIn();
  }

  render() {
    return (
      <Layout>
        <Switch>
          <Route exact path="/" component={Start} />
          <Route exact path="/login" component={Auth} />
          <ProtectedRoute path="/test" component={TestComponent} />
          <Redirect to="/" />
        </Switch>
      </Layout>
    );
  }
}

App.propTypes = {
  tryAutoSignIn: PropTypes.func.isRequired
};

const mapDispatchToProps = dispatch => ({
  tryAutoSignIn: () => dispatch(authActions.autoSignIn())
});

export default connect(null, mapDispatchToProps)(App);
