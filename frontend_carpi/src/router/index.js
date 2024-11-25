import { createRouter, createWebHistory } from 'vue-router';
import axios from 'axios';

import ClientView from '../views/ClientView.vue';
import AdminView from '../views/LoginAdminView.vue';
import LoginClient from '../views/LoginCliente.vue';
import RegistrationView from '../views/RegistrationView.vue';
import Vista from '../views/VistaView.vue';
import EmployeeView from '../views/EmployeeView.vue';
import InternView from '../views/InternView.vue';
import HomeAdminView from '../views/HomeAdminView.vue';
import Producto from '../views/Producto.vue';
import Mueble from '../views/Mueble.vue';
import Ventana from '../views/Ventana.vue';
import Puerta from '../views/Puerta.vue';
import ClienteGestion from '../views/ClientePerfil.vue';
import Erroraoa from '../views/Erroraoa.vue';
import GestionAdmin from '../views/GestionAdminView.vue';
import ClienteDashboard from '../views/ClienteDashboard.vue';
import Gestionpedidos from '@/views/Gestionpedidos.vue';
import Gestionpresupuesto from '@/views/Gestionpresupuesto.vue';
import GestionEmpleados from '@/views/GestionEmpleados.vue';
import AdminDashboard from '../views/DashboardAdminn.vue';
import DeliveryView from '@/views/DeliveryView.vue';
import ClientePerfil from '@/views/ClientePerfil.vue';
import SobreNosotros from '@/views/SobreNosotros.vue';
import Contacto from '@/views/Contacto.vue';
import Carpinteria from '@/views/Carpinteria.vue';


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
      path: '/sobrenosotros',
      name: 'Sobre Nosotros',
      component: SobreNosotros
    },
    {
      path: '/contacto',
      name: 'Contacto',
      component: Contacto
    },
    {
      path: '/carpinteria',
      name: 'Carpinteria',
      component: Carpinteria
    },
    {
      path: '/producto',
      name: 'Producto',
      component: Producto
    },
    {
      path: '/homeadmin',
      name: 'Home Admin',
      component: HomeAdminView,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/clientedashboard',
      name: 'ClienteDashboard',
      component: ClienteDashboard,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/gestionpedidos',
      name: 'Gestionpedidos',
      component: Gestionpedidos,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/gestionadmin',
      name: 'GestionAdmin',
      component: GestionAdmin,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/gestionpresupuesto',
      name: 'Gestionpresupuesto',
      component: Gestionpresupuesto,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/gestionempleados',
      name: 'GestionEmpleados',
      component: GestionEmpleados,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/admindashboard',
      name: 'AdminDashboard',
      component: AdminDashboard,
      beforeEnter: async (to, from, next) => {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.get('http://127.0.0.1:8000/api/users/admins/check-admin/', {
              headers: { Authorization: `Bearer ${token}` }
            });
            if (response.data.is_admin) {
              next();  // Permite el acceso a la ruta
            } else {
              next({ name: 'Error404' });  // Redirige si no es admin
            }
          } catch (error) {
            next({ name: 'Login' });  // Redirige si el token no es válido
          }
        } else {
          next({ name: 'Login' });  // Redirige si no hay token
        }
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'Error404',
      component: Erroraoa
    },
    {
      path: '/delivery',
      name: 'Delivery',
      component: DeliveryView
    },
    {
      path: '/clienteperfil',
      name: 'ClientePerfil',
      component: ClientePerfil
    },
    {
      path: '/mueble',
      name: 'Mueble',
      component: Mueble
    },
    {
      path: '/ventana',
      name: 'Ventana',
      component: Ventana
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
  ]
});

export default router;
