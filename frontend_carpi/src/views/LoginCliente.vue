<template>
    <div class="min-h-screen bg-gray-100 text-gray-800">
        <!-- Header General -->
        <HeaderCompo />
        <div class="bg-[#FFFBEB] min-h-screen flex items-center justify-center">
            <div class="hero-content flex-col lg:flex-row-reverse">
                <div class="text-center lg:text-left lg:w-1/2">
                <h1 class="text-5xl font-bold text-[#000000]">Autenticar</h1>
            </div>
            <div class="card bg-white w-full max-w-sm shrink-0 shadow-2xl">
                <form @submit.prevent="handleLogin" class="card-body">
                    <div class="form-control">
                        <label for="username" class="label">
                            <span class="label-text text-[#000000]">Usuario</span>
                        </label>
                        <input 
                            id="username" 
                            v-model="username" 
                            type="text" 
                            placeholder="Usuario"
                            class="input input-bordered" 
                            required
                            minlength="3"
                            maxlength="50"
                            pattern="[a-zA-Z0-9_-]+"
                        />
                    </div>
                    <div class="form-control">
                        <label for="password" class="label">
                            <span class="label-text text-[#000000]">Contraseña</span>
                        </label>
                        <input 
                            id="password" 
                            v-model="password" 
                            type="password" 
                            placeholder="Contraseña"
                            class="input input-bordered" 
                            required 
                        />
                    </div>
                    <div v-if="errorMessage" class="text-red-500 text-center mt-2">
                        {{ errorMessage }}
                    </div>
                    <div class="form-control mt-6">
                        <button 
                            type="submit" 
                            class="btn bg-[#D97706] hover:bg-[#B45309] text-white"
                        >
                            Iniciar sesión
                        </button>
                    </div>
                    <div class="text-center mt-4">
                        <span class="text-[#000000]">¿No tienes una cuenta?</span>
                        <router-link 
                            to="/registro" 
                            class="font-medium text-[#D97706] hover:text-[#B45309] ml-1"
                        >
                            Regístrate aquí
                        </router-link>
                    </div>
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import HeaderCompo from '@/components/HeaderCompo.vue'; // Importa el componente HeaderCompo

const router = useRouter();

// Reactive variables for form inputs
const username = ref('');
const password = ref('');
const errorMessage = ref(''); // Para manejar errores

const handleLogin = async () => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/login/client/', {
            username: username.value,
            password: password.value,
        });
        
        // Maneja la respuesta y almacena el token
        const { access } = response.data; // Solo se necesita el token de acceso
        console.log('Token:', access); // Mostrar el token en la consola
        localStorage.setItem('token', access);
        
        // Redirigir después de un inicio de sesión exitoso
        router.push('/cliente'); // Cambia '/cliente' a la ruta que desees
    } catch (error) {
        console.error('Error durante el login:', error.response ? error.response.data : error);
        errorMessage.value = error.response?.data?.detail || 'Error al iniciar sesión.';
    }
};
</script>

<style scoped>
/* Aquí puedes agregar estilos específicos para este componente si es necesario */
</style>