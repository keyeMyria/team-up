import React from 'react';
import { NavLink } from 'react-router-dom';
import classNames from 'classnames/bind';

import styles from './styles.css';

const cx = classNames.bind(styles);

const NavItems = () => (
  <nav className={cx('navBar')}>
    <ul>
      <li>
        <NavLink exact to="/" className={cx('navLink')} activeClassName={cx('navLink--active')}>
          Home
        </NavLink>
      </li>
      <li>
        <NavLink exact to="/test" className={cx('navLink')} activeClassName={cx('navLink--active')}>
          Test
        </NavLink>
      </li>
      <li>
        <NavLink
          exact
          to="/login"
          className={cx('navLink')}
          activeClassName={cx('navLink--active')}
        >
          Login
        </NavLink>
      </li>
    </ul>
  </nav>
);

export default NavItems;
