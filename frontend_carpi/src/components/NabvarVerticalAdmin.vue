<template>
    <div class="flex h-screen" style="width: 60px; background-color: #f7f7f7; border-right: 1px solid #ddd;">
        <!-- Navbar vertical -->
        <nav class="bg-white text-gray-800 shadow-md transition-all duration-300 ease-in-out flex flex-col"
            :class="{ 'w-240': isExpanded, 'w-60': !isExpanded }" @mouseenter="expandNav" @mouseleave="contractNav">
            <div class="p-2 flex items-center justify-between h-12 border-b border-gray-200">
                <h1 class="text-xl font-bold truncate transition-opacity duration-300"
                    :class="{ 'opacity-0 w-0': !isExpanded, 'opacity-100': isExpanded }">
                    Admin Panel
                </h1>
                <div class="flex items-center">
                    <button @click="toggleNav" class="text-gray-500 hover:text-gray-700 focus:outline-none">
                        <svg v-if="!isExpanded" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16m-7 6h7"></path>
                        </svg>
                    </button>
                </div>
            </div>
            <ul class="flex-grow py-2">
                <li v-for="item in menuItems" :key="item.path" class="relative">
                    <router-link :to="item.path"
                        class="flex items-center px-2 py-2 hover:bg-gray-100 transition-colors duration-200"
                        :class="{ 'justify-center': !isExpanded }">
                        <span v-html="item.icon" class="w-5 h-5 flex-shrink-0"></span>
                        <span class="ml-2 whitespace-nowrap transition-opacity duration-300"
                            :class="{ 'opacity-0 absolute left-full': !isExpanded, 'opacity-100': isExpanded }">
                            {{ item.name }}
                        </span>
                    </router-link>
                </li>
                <li class="relative">
                    <button @click="logout"
                        class="flex items-center px-2 py-2 w-full text-left hover:bg-gray-100 transition-colors duration-200"
                        :class="{ 'justify-center': !isExpanded }">
                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a2 2 0 01-2 2H7a2 2 0 01-2-2V7a2 2 0 012-2h4a2 2 0 012 2v1" />
                        </svg>
                        <span class="ml-2 whitespace-nowrap transition-opacity duration-300"
                            :class="{ 'opacity-0 absolute left-full': !isExpanded, 'opacity-100': isExpanded }">
                            Log Out
                        </span>
                    </button>
                </li>
            </ul>
            <div class="p-2 border-t border-gray-200">
                <button @click="togglePin" class="text-gray-500 hover:text-gray-700 focus:outline-none w-full flex justify-center">
                    <svg v-if="!isPinned" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
                    </svg>
                    <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 13l4 4L19 7"></path>
                    </svg>
                </button>
            </div>
        </nav>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isExpanded = ref(false);
const isPinned = ref(false);
const router = useRouter();

const expandNav = () => {
    isExpanded.value = true;
};

const contractNav = () => {
    if (!isPinned.value) {
        isExpanded.value = false;
    }
};

const toggleNav = () => {
    isExpanded.value = !isExpanded.value;
};

const togglePin = () => {
    isPinned.value = !isPinned.value;
    if (isPinned.value) {
        isExpanded.value = true;
    }
};

const logout = () => {
    // Aquí puedes agregar la lógica para cerrar sesión, como limpiar tokens, etc.
    console.log('Logging out...');
    router.push('/login'); // Redirigir a la página de inicio de sesión
};

const menuItems = ref([
    {
        name: 'DASHBOARD',
        path: '/homeadmin',
        icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
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
        name: 'Administracion',
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
]);

</script>

<style scoped>
nav {
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    margin-bottom: 10px;
}

nav a {
    text-decoration: none;
    color: #333;
    transition: color 0.2s ease;
}

nav a:hover {
    color: #666;
}

nav .icon {
    font-size: 18px;
    margin-right: 10px;
}
</style>
