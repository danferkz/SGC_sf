import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
//import * as HeroIcons from '@heroicons/vue/outline'
//import { ShoppingBagIcon, DocumentTextIcon, UserIcon } from '@heroicons/vue/outline'
//import store from './store'
//import axios from 'axios'


// Configuración de Axios
//axios.defaults.baseURL = 'http://localhost:8000';
//axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;

const app = createApp(App)

// Añadir Axios a las propiedades globales
//app.config.globalProperties.$axios = axios;

// Registrar los íconos globalmente
//app.component('ShoppingBagIcon', ShoppingBagIcon)
//app.component('DocumentTextIcon', DocumentTextIcon)
//app.component('UserIcon', UserIcon)
// Registrar automáticamente todos los íconos
//Object.keys(HeroIcons).forEach(icon => {
//   app.component(icon, HeroIcons[icon])
//})

app.use(router)
//app.use(store)
app.mount('#app')

