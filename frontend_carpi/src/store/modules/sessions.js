import axios from 'axios';

const state = {
    token: null,
    user: null,
};

const mutations = {
    SET_TOKEN(state, token) {
        state.token = token;
        if (token) {
            localStorage.setItem('token', token);
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            localStorage.removeItem('token');
            delete axios.defaults.headers.common['Authorization'];
        }
    },
    SET_USER(state, user) {
        state.user = user;
    },
};

const actions = {
    async login({ commit }, credentials) {
        try {
            const response = await axios.post('http://localhost:8000/api/users/clients/login/', credentials);
            const { access, user } = response.data;

            // Guardar el token y el usuario en el estado
            commit('SET_TOKEN', access);
            commit('SET_USER', user);

            return user;
        } catch (error) {
            console.error('Error en login:', error.response?.data || error.message);
            throw new Error(error.response?.data?.detail || 'Error en autenticación');
        }
    },
    async logout({ commit }) {
        commit('SET_TOKEN', null);
        commit('SET_USER', null);
    },
    async autoLogin({ commit }) {
        const token = localStorage.getItem('token');
        if (token && !tokenExpired(token)) {
            commit('SET_TOKEN', token);
            try {
                // Cambia la URL a la correcta para obtener el perfil del cliente
                const response = await axios.get('http://localhost:8000/api/users/clients/profile/'); // Ajusta la URL según tu API
                commit('SET_USER', response.data);
            } catch (error) {
                console.error('Error al obtener los datos del usuario:', error);
                commit('SET_USER', null); // Si falla, aseguramos que el usuario se desloguee
            }
        } else {
            commit('SET_TOKEN', null);
            commit('SET_USER', null);
        }
    },
};

const getters = {
    isAuthenticated: (state) => !!state.token,
    currentUser: (state) => state.user,
};

// Función para verificar si el token ha expirado
function tokenExpired(token) {
    try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        return payload.exp < Date.now() / 1000;
    } catch (error) {
        return true; // Si no puede verificar, asume que está expirado
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters,
};
