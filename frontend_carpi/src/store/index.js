import { createStore } from 'vuex';
import sessions from './modules/sessions';
import createPersistedState from 'vuex-persistedstate';

export default createStore({
    modules: {
        sessions,
    },
    plugins: [createPersistedState()], // Persistencia del estado en localStorage o sessionStorage
});
