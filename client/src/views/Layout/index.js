import React, { Component, Fragment } from 'react';

import Header from './components/Header';
import Footer from './components/Footer';

// import styles from './styles.css';

class Layout extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <main className="content">{this.props.children}</main>
        <Footer />
      </Fragment>
    );
  }
}

export default Layout;
