import React from 'react';
import { connect } from 'react-redux';

const Header = props => {
  return (
    <div>
      {/* <Toolbar
          isAuth={this.props.isAuthenticated}
          onDrawerClick={this.sideDrawerToggleHandler}
        /> */}
      {/* SideDrawer -> TO BE ADDED */}
    </div>
  );
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.authenticated
});

export default connect(mapStateToProps)(Header);
