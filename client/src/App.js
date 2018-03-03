import React, { Component } from 'react';
import { Route, Redirect, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import { authActions } from 'services/auth';

import Auth from 'views/Auth';
import SignOut from 'views/Layout/components/Header/Toolbar/NavItems/NavItem/SignOut';

class App extends Component {
  componentDidMount() {
    this.props.tryAutoSignIn();
  }

  render() {
    return (
      <div className="App">
        <Switch>
          {/* TEMPORARY ROUTE */}
          <Route
            exact
            path="/"
            render={() => (
              <header className="App-header">
                <h1 className="App-title">Welcome to Team-up</h1>
              </header>
            )}
          />
          <Redirect to="/" />
        </Switch>

        {/* temporary - for testing authentication */}
        <div>
          {!this.props.isAuthenticated && <Auth />}
          {this.props.isAuthenticated && <SignOut />}
        </div>
      </div>
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
