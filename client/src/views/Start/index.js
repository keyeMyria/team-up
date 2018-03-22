import React, {Component, Fragment} from 'react';
import classNames from 'classnames/bind';

import styles from './styles.css';

const cx = classNames.bind(styles);

class Start extends Component {
  render() {
    return (
      <Fragment>
        <div className={cx('container')}>
            PRIMARY PAGE
        </div>
      </Fragment>
    );
  }
}

export default Start;
