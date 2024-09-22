import { createRouter, createWebHistory } from 'vue-router'

import ClientView from '../views/ClientView.vue'
import AdminView from '../views/AdminView.vue'
import LoginClient from '../views/LoginView.vue'
import RegistrationView from '../views/RegistrationView.vue'
import Vista from '../views/VistaView.vue'
import EmployeeView from '../views/EmployeeView.vue'
import InternView from '../views/InternView.vue'
import Producto from '../views/Producto.vue'
import HomeAdminView from '../views/HomeAdminView.vue'


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
    },
    {
      path: '/empleado',
      name: 'Empleado',
      component: EmployeeView
    },
    {
      path: '/interno',
      name: 'Interno',
      component: InternView
    },
    {
      path: '/producto',
      name: 'Producto',
      component: Producto
    },
    {
      path: '/homeadmin',
      name: 'Home Admin',
      component: HomeAdminView
    }
      

  ]
})

export default router
