import React, { Component } from 'react';
import { Route, Redirect, Switch, Link } from 'react-router-dom';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

import Login from '../scenes/Auth/scenes/Login/Login';
import logo from './logo.svg';
import './App.css';

import { authActions } from '../services/auth';

class App extends Component {
  componentDidMount() {
    this.props.tryAutoSignIn();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Team-up</h1>
        </header>

        <Switch>
          <Route
            exact
            path="/"
            render={() => (
              <Link to="/login">
                <h3>Go to /login</h3>
              </Link>
            )}
          />
          <Route exact path="/login" component={Login} />
          <Redirect to="/" />
        </Switch>
      </div>
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
