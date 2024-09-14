import { createRouter, createWebHistory } from 'vue-router'

import ClientView from '../views/ClientView.vue'
import AdminView from '../views/AdminView.vue'
import LoginClient from '../views/LoginView.vue'
import RegistrationView from '../views/RegistrationView.vue'
import Vista from '../views/VistaView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Cliente',
      component: ClientView
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminView
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginClient
    },
    {
      path: '/registro',
      name: 'Registro',
      component: RegistrationView
    },
    {
      path: '/vista',
      name: 'Vista',
      component: Vista
    }

  ]
})

export default router
