

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

