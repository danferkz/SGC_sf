<template>
    <div class="flex">
        <div
            :class="['bg-gray-800 text-white h-screen transition-all duration-300', isExpanded ? 'sidebar-expanded' : 'sidebar-collapsed']">
            <div class="p-4 flex items-center justify-between">
                <h1 class="text-xl font-bold truncate transition-opacity duration-300" v-if="isExpanded">
                    Admin Panel
                </h1>
                <button @click="toggleNav" class="focus:outline-none">
                    <svg v-if="!isExpanded" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M4 6h16M4 12h16m-7 6h7"></path>
                    </svg>
                    <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                        </path>
                    </svg>
                </button>
            </div>
            <nav class="mt-4">
                <ul>
                    <li v-for="item in menuItems" :key="item.path" class="p-4 hover:bg-gray-700">
                        <router-link :to="item.path" class="flex items-center">
                            <span v-html="item.icon" class="w-5 h-5 flex-shrink-0"></span>
                            <span v-if="isExpanded" class="ml-2">{{ item.name }}</span>
                        </router-link>
                    </li>
                    <li class="p-4 hover:bg-gray-700">
                        <button @click="logout" class="flex items-center w-full text-left">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a2 2 0 01-2 2H7a2 2 0 01-2-2V7a2 2 0 012-2h4a2 2 0 012 2v1">
                                </path>
                            </svg>
                            <span v-if="isExpanded" class="ml-2">Salir</span>
                        </button>
                    </li>
                </ul>
            </nav>
        </div>
        
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default {
    setup() {
        const isExpanded = ref(false);
        const router = useRouter();
        const store = useStore();

        const menuItems = ref([
            {
                name: 'PANEL',
                path: '/homeadmin',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m- 6 0h6" />
              </svg>`
            },
            {
                name: 'Clientes',
                path: '/clientedashboard',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>`
            },
            {
                name: 'Pedidos',
                path: '/gestionpedidos',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />

              </svg>`
            },
            {
                name: 'Administración',
                path: '/gestionadmin',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">

                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>`
            },
            {
                name: 'Presupuestos',
                path: '/gestionpresupuesto',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 10c-4.41 0-8-1.79-8-4V8c0-2.21 3.59-4 8-4s8 1.79 8 4v6c0 2.21-3.59 4-8 4z" />
              </svg>`
            },
            {
                name: 'Empleados', // Nueva sección para empleados
                path: '/gestionempleados',
                icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-3.31 0-6 2.69-6 6v1h12v-1c0-3.31-2.69-6-6-6z" />
              </svg>`
            },
        ]);

        const toggleNav = () => {
            isExpanded.value = !isExpanded.value;
        };

        const logout = () => {
            store.dispatch('sessions/logout').then(() => {
                router.push('/'); // Redirigir a la página de inicio
            }).catch((error) => {
                console.error('Error al cerrar sesión:', error);
            });
        };

        return {
            isExpanded,
            toggleNav,
            menuItems,
            logout
        };
    }
};
</script>

<style>
.sidebar-expanded {
    width: 250px;
}

.sidebar-collapsed {
    width: 64px;
}
</style>