import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'; // Importar el store
import axios from 'axios';

// Configuración de Axios
axios.defaults.baseURL = 'http://localhost:8000';
axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;

// Llamar a autoLogin antes de montar la aplicación
store.dispatch('sessions/autoLogin').then(() => {
    // Solo montar la aplicación después de que autoLogin haya terminado
    const app = createApp(App);

    // Añadir Axios a las propiedades globales
    app.config.globalProperties.$axios = axios;

    // Usar el router y el store en la aplicación
    app.use(router);
    app.use(store);

    // Montar la aplicación
    app.mount('#app');
}).catch((error) => {
    console.error('Error en autoLogin:', error);
    // Si autoLogin falla, puedes montar la aplicación de todas formas
    const app = createApp(App);

    app.config.globalProperties.$axios = axios;
    app.use(router);
    app.use(store);
    app.mount('#app');
});
