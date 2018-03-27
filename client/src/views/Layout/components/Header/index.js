import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames/bind';

import Toolbar from './Toolbar';
import styles from './styles.css';

const cx = classNames.bind(styles);

const Header = props => (
  <header className={cx('header')}>
    <span>Team-up</span>
    {/* TODO: create 'unprotected' (: navlinks that gets removed when the user is logged in */}
    <span>{props.isAuthenticated ? 'Logged in' : 'Logged out'}</span>
    <Toolbar isAuthenticated={props.isAuthenticated} />
    {/* <Toolbar onDrawerClick={this.sideDrawerToggleHandler} /> */}
    {/* SideDrawer -> TO BE ADDED */}
  </header>
);

Header.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired
};

export default Header;
