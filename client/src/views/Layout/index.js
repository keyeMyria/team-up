import React, {Component, Fragment} from 'react';
import classNames from 'classnames/bind';

import Header from './components/Header';
import Footer from './components/Footer';
import styles from './styles.css';

const cx = classNames.bind(styles);

class Layout extends Component {
  render() {
    return (
      <Fragment>
        <div className={cx('container')}>
          <div className={cx('header')}>
            <Header/>
          </div>
          <main className={cx('content')}>{this.props.children}</main>
          <div className={cx('footer')}>
            <Footer/>
          </div>
        </div>
      </Fragment>
    );
  }
}

export default Layout;
