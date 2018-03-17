import React from 'react';
import classNames from "classnames/bind";

import styles from './styles.css'

const cx = classNames.bind(styles);

const Footer = props => {
  return <div className={cx('footer')}>Footer</div>;
};

export default Footer;
