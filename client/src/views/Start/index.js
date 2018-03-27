import React, { Component } from 'react';
import classNames from 'classnames/bind';

import styles from './styles.css';

const cx = classNames.bind(styles);

// eslint-disable-next-line react/prefer-stateless-function
class Start extends Component {
  render() {
    return <div className={cx('container')}>PRIMARY PAGE</div>;
  }
}

export default Start;
