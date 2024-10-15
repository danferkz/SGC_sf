<template>
    <div class="hero bg-[#FFFBEB] min-h-screen">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="text-center lg:text-left lg:w-1/2">
                <h1 class="text-5xl font-bold text-[#000000]">Inicio de Sesión Administrador</h1>
                <p class="mt-2 text-center text-sm text-gray-600">
                    Accede a tu cuenta de Administrador de la Carpintería Maderera El Bosque
                </p>
            </div>
            <div class="card bg-white w-full max-w-md shrink-0 shadow-2xl">
                <form @submit.prevent="handleLogin" class="card-body">
                    <div class="form-control">
                        <label for="user" class="label">
                            <span class="label-text text-[#000000]">Usuario</span>
                        </label>
                        <input id="user" v-model="username" type="text" placeholder="Usuario" class="input input-bordered"
                            required />
                    </div>
                    <div class="form-control relative">
                        <label for="password" class="label">
                            <span class="label-text text-[#000000]">Contraseña</span>
                        </label>
                        <input 
                            :type="showPassword ? 'text' : 'password'"
                            id="password" 
                            v-model="password" 
                            placeholder="Contraseña"
                            class="input input-bordered" 
                            required 
                        />
                        <!-- Botón para mostrar/ocultar contraseña -->
                        <button type="button" @click="togglePasswordVisibility" class="absolute right-3 top-10">
                            <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12A3 3 0 119 12a3 3 0 016 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-1.274 4.057-5.065 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                            </svg>
                            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A8.944 8.944 0 0112 19c-4.477 0-8.268-2.943-9.542-7C3.732 7.943 7.523 5 12 5c1.109 0 2.174.2 3.167.575M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3l18 18" />
                            </svg>
                        </button>
                    </div>
                    
                    <div v-if="error" class="text-red-500 text-sm mt-2">
                        {{ error }}
                    </div>

                    <!-- Enlace para restablecer la contraseña -->
                    <div class="form-control mt-2">
                        <a href="/forgot-password" class="text-sm text-blue-600 hover:underline">¿Olvidaste tu contraseña?</a>
                    </div>

                    <div class="form-control mt-6">
                        <button type="submit" class="btn bg-amber-600 hover:bg-amber-700 text-white flex items-center justify-center">
                            <span v-if="!isLoading">Iniciar Sesión</span>
                            <svg v-else class="animate-spin h-5 w-5 text-white ml-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v4m0 4v8m0-4h8m-4-4h-8" />
                            </svg>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    
</template>


<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const username = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();

const API_BASE_URL = 'http://localhost:8000';

const handleLogin = async () => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/users/admins/login/`, {
            username: username.value,
            password: password.value
        });
        
        // Guardar el token en el almacenamiento local
        localStorage.setItem('token', response.data.access);
        localStorage.setItem('refreshToken', response.data.refresh);
        
        // Configurar el token para futuras solicitudes
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
        
        // Redirigir al dashboard o a la página principal de administrador
        router.push('/homeadmin');
    } catch (err) {
        if (err.response && err.response.data) {
            error.value = err.response.data.detail || 'Error al iniciar sesión. Por favor, intente de nuevo.';
        } else {
            error.value = 'Error de conexión. Por favor, intente de nuevo más tarde.';
        }
    }
};
</script>

<style scoped>
.hero {
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.card {
    padding: 2rem;
    border-radius: 0.5rem;
}
</style>