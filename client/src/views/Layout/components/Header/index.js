import React from 'react';
import { connect } from 'react-redux';

const Header = props => {
  return (
    <div id="header">
      {/* <Toolbar
          isAuth={this.props.isAuthenticated}
          onDrawerClick={this.sideDrawerToggleHandler}
        /> */}
      {/* SideDrawer -> TO BE ADDED */}
      <h1>Welcome to Team-up</h1>
    </div>
  );
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.authenticated
});

export default connect(mapStateToProps)(Header);
