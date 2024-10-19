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
                    <div class="form-control">
                        <label for="password" class="label">
                            <span class="label-text text-[#000000]">Contraseña</span>
                        </label>
                        <input id="password" v-model="password" type="password" placeholder="Contraseña"
                            class="input input-bordered" required />
                    </div>
                    <div v-if="error" class="text-red-500 text-sm mt-2">
                        {{ error }}
                    </div>
                    <div class="form-control mt-6">
                        <button type="submit" class="btn bg-amber-600 hover:bg-amber-700 text-white">
                            Iniciar Sesión
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