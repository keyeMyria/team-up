import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import classNames from 'classnames/bind';

import Header from './components/Header';
import Footer from './components/Footer';
import styles from './styles.css';

const cx = classNames.bind(styles);

const Layout = props => (
  <div className={cx('container')}>
    <div className={cx('header')}>
      <Header isAuthenticated={props.isAuthenticated} />
    </div>
    <main className={cx('content')}>{props.children}</main>
    <div className={cx('footer')}>
      <Footer />
    </div>
  </div>
);

Layout.propTypes = {
  children: PropTypes.element.isRequired,
  isAuthenticated: PropTypes.bool.isRequired
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.authenticated
});

export default connect(mapStateToProps)(Layout);
