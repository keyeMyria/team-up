import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import Modal from 'react-modal';
import classNames from 'classnames/bind';

import { authActions } from '@/services/auth';

import Login from './views/Login';
import Register from './views/Register';
import styles from './styles.css';

const cx = classNames.bind(styles);

Modal.setAppElement('body');

class Auth extends Component {
  state = {
    modalIsOpen: false,
    panelOpen: 'login'
  };

  openModal = () => {
    this.setState({ modalIsOpen: true });
  };

  afterOpenModal = () => {};

  closeModal = () => {
    this.setState({ modalIsOpen: false, panelOpen: 'login' });
  };

  switchPanel = (panelName) => {
    this.setState({ panelOpen: panelName });
  };

  AUTH_PANELS = {
    login: (
      <Login
        signIn={this.props.signIn}
        onClose={this.closeModal}
        onRegister={() => this.switchPanel('register')}
        onForgotPassword={() => this.switchPanel('forgotPassword')}
      />
    ),
    register: (
      <Register
        onClose={this.closeModal}
        onLogin={() => this.switchPanel('login')}
        signUp={this.props.signUp}
      />
    )
    // forgotPassword: <ForgotPassword />,
  };

  render() {
    return (
      <div>
        {/* PUT THE BUTTON OUT OF THIS COMPONENT? */}
        <button onClick={this.openModal}>Login</button>
        <Modal
          isOpen={this.state.modalIsOpen}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          className={`${cx('modal')} animated fadeIn`}
          overlayClassName={cx('overlay')}
          contentLabel="Authentication Modal"
        >
          {this.AUTH_PANELS[this.state.panelOpen]}
        </Modal>
      </div>
    );
  }
}

Auth.propTypes = {
  signIn: PropTypes.func.isRequired,
  signUp: PropTypes.func.isRequired
};

const mapDispatchToProps = dispatch => ({
  signIn: (backend, payload) => dispatch(authActions.signIn(backend, payload)),
  signUp: credentials => dispatch(authActions.signUp(credentials))
});

export default connect(null, mapDispatchToProps)(Auth);
