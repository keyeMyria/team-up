// usage
// global.localStorage = new LocalStorageMock();

class LocalStorageMock {
  store = {};

  clear() {
    this.store = {};
  }

  getItem(key) {
    return this.store[key] || null;
  }

  setItem(key, value) {
    this.store[key] = value;
  }

  removeItem(key) {
    delete this.store[key];
  }
}

export default LocalStorageMock;
