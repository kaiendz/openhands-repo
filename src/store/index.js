

import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
    token: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
    clearSession(state) {
      state.user = null;
      state.token = null;
    },
  },
  actions: {
    login({ commit }, payload) {
      return new Promise((resolve, reject) => {
        // Simulate network call, replace with actual login implementation

  const persistStore = () => {
    if (state.user) {
      window.localStorage.setItem('vuex', JSON.stringify(state));
    }
  }

  state.$subscribe((mutation, state) => {
    persistStore();
  });

  window.addEventListener('beforeunload', () => {
    persistStore()
  });

  // Loading pre-existing state
  if (window.localStorage.getItem('vuex')) {
    const savedState = JSON.parse(window.localStorage.getItem('vuex'));
    Object.assign(state, savedState);
  }
  

        setTimeout(() => {
          if (payload.email !== 'user@example.com' || payload.password !== 'example') {
            reject(new Error('Failed to login'));
          } else {
            commit('setUser', { name: 'John Doe' });
            commit('setToken', 'generated-token');
            resolve();
          }
        }, 500);
      });
    },
    logout({ commit }) {
       commit('clearSession');
    },
  },
  getters: {
    isAuthenticated(state) {
      return !!state.user && !!state.token;
    },
  },
});

