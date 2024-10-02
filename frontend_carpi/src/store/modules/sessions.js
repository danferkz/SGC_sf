// store/modules/auth.js
import axios from 'axios';

const state = {
    token: localStorage.getItem('token') || null,
    user: null,
};

const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
        if (token) {
            localStorage.setItem('token', token);
        } else {
            localStorage.removeItem('token');
        }
    },
    SET_USER(state, user) {
        state.user = user;
    },
};

const actions = {
    async login({ commit }, credentials) {
        try {
            const response = await axios.post('/api/login', credentials);
            commit('SET_TOKEN', response.data.access); // Guardo el token en Vuex y localStorage
            commit('SET_USER', response.data.user);
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`; // Configuro Axios
        } catch (error) {
            console.error('Error en login:', error.response.data);
        }
    },
    logout({ commit }) {
        commit('SET_TOKEN', null);
        commit('SET_USER', null);
        delete axios.defaults.headers.common['Authorization'];
    },
    autoLogin({ commit }) {
        const token = localStorage.getItem('token');
        if (token) {
            commit('SET_TOKEN', token);
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`; // Configuro Axios con el token recuperado
        }
    },
};

export default {
    namespaced: true,
    state,
    mutations,
    actions,
};
