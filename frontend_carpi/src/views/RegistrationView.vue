<template>
    <div class="bg-[#FFFBEB] min-h-screen flex items-center justify-center">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="text-center lg:text-left lg:w-1/2">
                <h1 class="text-5xl font-bold text-[#000000]">Registro</h1>
            </div>
            <div class="card bg-white w-full max-w-sm shrink-0 shadow-2xl">
                <form @submit.prevent="handleRegistration" class="card-body">
                    <div class="form-control">
                        <label for="username" class="label">
                            <span class="label-text text-[#000000]">Nombre de usuario</span>
                        </label>
                        <input id="username" v-model="username" type="text" placeholder="Nombre de usuario"
                            class="input input-bordered" required />
                    </div>
                    <div class="form-control">
                        <label for="email" class="label">
                            <span class="label-text text-[#000000]">Correo electrónico</span>
                        </label>
                        <input id="email" v-model="email" type="email" placeholder="Correo electrónico"
                            class="input input-bordered" required />
                    </div>
                    <div class="form-control">
                        <label for="password" class="label">
                            <span class="label-text text-[#000000]">Contraseña</span>
                        </label>
                        <input id="password" v-model="password" type="password" placeholder="Contraseña"
                            class="input input-bordered" required />
                    </div>
                    <div class="form-control">
                        <label for="confirm-password" class="label">
                            <span class="label-text text-[#000000]">Confirmar contraseña</span>
                        </label>
                        <input id="confirm-password" v-model="confirmPassword" type="password"
                            placeholder="Confirmar contraseña" class="input input-bordered" required />
                    </div>
                    <!-- Checkbox de Términos y Condiciones -->
                    <div class="form-control">
                        <label class="cursor-pointer flex items-center space-x-2">
                            <input type="checkbox" v-model="termsAccepted" class="checkbox checkbox-bordered" required />
                            <span class="label-text text-[#000000]">Acepto los <RouterLink to="/terms" class="text-[#D97706]">Términos y Condiciones</RouterLink></span>
                        </label>
                    </div>
                    <div class="form-control mt-6">
                        <button type="submit" class="btn bg-[#D97706] hover:bg-[#B45309] text-white" :disabled="!termsAccepted">
                            Registrarse
                        </button>
                    </div>
                    <div v-if="errorMessage" class="error-message text-red-500 mt-2">
                        {{ errorMessage }}
                    </div>
                    <div class="text-center mt-4">
                        <span class="text-[#000000]">¿Ya tienes una cuenta?</span>
                        <RouterLink to="/login" class="text-[#D97706]">Iniciar sesión</RouterLink>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios'; // Importa Axios aquí

export default {
    setup() {
        const router = useRouter();

        // Reactive variables for form inputs
        const username = ref('');
        const email = ref('');
        const password = ref('');
        const confirmPassword = ref('');
        const errorMessage = ref('');
        const termsAccepted = ref(false); // Variable para controlar si aceptó los términos

        const handleRegistration = async () => {
            // Reset error message
            errorMessage.value = '';

            // Form data
            const formData = {
                username: username.value,
                email: email.value,
                password: password.value,
                password2: confirmPassword.value, // Coincide con el campo del serializer
            };

            if (!termsAccepted.value) {
                errorMessage.value = 'Debes aceptar los Términos y Condiciones para registrarte.';
                return;
            }

            try {
                // Llamada a la API para registrar el usuario
                const response = await axios.post('http://localhost:8000/api/users/clients/create/', formData);

                // Manejar la respuesta en caso de éxito
                console.log('User registered:', response.data);

                // Redirigir a la vista de login
                router.push('/login');
            } catch (error) {
                // Manejo de errores
                errorMessage.value = error.response?.data?.password ? error.response.data.password : 'Error al registrar el usuario. Por favor, intenta nuevamente.';
                console.error('Error during registration:', error);
            }
        };

        return {
            username,
            email,
            password,
            confirmPassword,
            errorMessage,
            termsAccepted, // Retornar la variable de los términos
            handleRegistration,
        };
    },
};
</script>

<style scoped>
.error-message {
    color: red;
}
</style>
