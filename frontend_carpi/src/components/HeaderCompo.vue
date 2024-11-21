<template>
    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <div class="dropdown">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M4 6h16M4 12h16M4 18h7" />
                    </svg>
                </div>
                <ul tabindex="0"
                    class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li><router-link to="/">Inicio</router-link></li>
                    <li><router-link to="/producto">Productos</router-link></li>
                </ul>
            </div>
        </div>
        <div class="navbar-center">
            <router-link to="/" class="btn btn-ghost text-xl">Maderera El Bosque</router-link>
        </div>
        <div class="navbar-end">
            <div class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <img alt="Tailwind CSS Navbar component"
                            src="../assets/usuario_log.png" />
                    </div>
                </div>
                <ul tabindex="0"
                    class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li v-if="!isAuthenticated"><router-link to="/login">Login</router-link></li>
                    <li v-if="!isAuthenticated"><router-link to="/registro">Registrese</router-link></li>
                    <li v-if="isAuthenticated"><router-link to="/cliente">Perfil</router-link></li>
                    <li v-if="isAuthenticated"><a @click="handleLogout">Cerrar Sesión</a></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed, watch } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

// Accede al store de Vuex
const store = useStore();
const router = useRouter();

// Computed para verificar si el usuario está autenticado
const isAuthenticated = computed(() => store.getters['sessions/isAuthenticated']);

// Método para manejar el cierre de sesión
const handleLogout = () => {
    store.dispatch('sessions/logout');
    router.push('/'); // Ajusta según tu ruta
};

// Watch para detectar cambios en la autenticación
watch(isAuthenticated, (newValue) => {
    if (!newValue) {
        router.push('/login');
    }
});



</script>

<style scoped>
</style>