// Side effects Services
export function getAuthToken() {
  return JSON.parse(localStorage.getItem('authToken'));
}

export function getAuthTokenExpirationDate() {
  return new Date(localStorage.getItem('tokenExpirationDate'));
}

export function setAuthToken(token) {
  localStorage.setItem('authToken', JSON.stringify(token));

  const date = new Date(Date.now() + (token.expires_in * 1000));
  localStorage.setItem('tokenExpirationDate', date);
}

export function removeAuthToken() {
  localStorage.removeItem('authToken');
}
