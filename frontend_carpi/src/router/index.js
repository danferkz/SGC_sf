import { createRouter, createWebHistory } from 'vue-router'
import ClientView from '../views/ClientView.vue'
import AdminView from '../views/LoginAdminView.vue'
import LoginClient from '../views/LoginCliente.vue'
import RegistrationView from '../views/RegistrationView.vue'
import Vista from '../views/VistaView.vue'
import EmployeeView from '../views/EmployeeView.vue'
import InternView from '../views/InternView.vue'
import HomeAdminView from '../views/HomeAdminView.vue'
import Producto from '../views/Producto.vue'
import Mueble from '../views/Mueble.vue'
import Ventana from '../views/Ventana.vue'
import Puerta from '../views/Puerta.vue'
import ClienteGestion from '../views/ClientePerfil.vue'
import Erroraoa from '../views/Erroraoa.vue'
import GestionAdmin from '../views/GestionAdminView.vue'
import ClienteDashboard from '../views/ClienteDashboard.vue';
import Gestionpedidos from '@/views/Gestionpedidos.vue';
import Gestionpresupuesto from '@/views/Gestionpresupuesto.vue';
import GestionEmpleados from '@/views/GestionEmpleados.vue';
import AdminDashboard from '../views/DashboardAdminn.vue';
import DeliveryView from '@/views/DeliveryView.vue';
import ClientePerfil from '@/views/ClientePerfil.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Cliente',
      component: ClientView
    },
    {
      path: '/adminlogin',
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
    },
    {
      path: '/ventana',
      name: 'Ventana',
      component: Ventana
    },
    {
      path: '/mueble',
      name: 'Mueble',
      component: Mueble
    },
    {
      path: '/puerta',
      name: 'Puerta',
      component: Puerta
    },
    {
      path: '/cliente',
      name: 'ClienteGestion',
      component: ClienteGestion
    },
    {
      path: '/clientedashboard',
      name: 'ClienteDashboard',
      component: ClienteDashboard
    },
    {
      path: '/gestionadmin',
      name: 'GestionAdmin',
      component: GestionAdmin
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'Error404',
      component: Erroraoa
    },
    {
      path: '/gestionpedidos',
      name: 'Gestionpedidos',
      component: Gestionpedidos
    },
    {
      path: '/gestionpresupuesto',
      name: 'Gestionpresupuesto',
      component: Gestionpresupuesto
    },
    {
      path: '/gestionempleados',
      name: 'Gestionempleados',
      component: GestionEmpleados
    },
    {
      path: '/admindashboard',
      name: 'AdminDashboard',
      component: AdminDashboard
    },
    {
      path: '/clienteperfil',
      name: 'ClientePerfil',
      component: ClientePerfil
    },
    {
      path: '/delivery',
      name: 'Delivery',
      component: DeliveryView
    }
  ]
})

export default router