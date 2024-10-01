<template>
    <div class="bg-[#FFFBEB] min-h-screen flex items-center justify-center">
        <div class="hero-content flex-col lg:flex-row-reverse">
            <div class="text-center lg:text-left lg:w-1/2">
                <h1 class="text-5xl font-bold text-[#000000]">Registro</h1>
            </div>
            <div class="card bg-white w-full max-w-sm shrink-0 shadow-2xl">
                <form @submit.prevent="handleRegistration" class="card-body">
                    <div class="form-control">
                        <label for="full-name" class="label">
                            <span class="label-text text-[#000000]">Nombre completo</span>
                        </label>
                        <input id="full-name" v-model="fullName" type="text" placeholder="Nombre completo"
                            class="input input-bordered" required />
                    </div>
                    <div class="form-control">
                        <label for="phone" class="label">
                            <span class="label-text text-[#000000]">Número de teléfono</span>
                        </label>
                        <input id="phone" v-model="phone" type="tel" placeholder="Número de teléfono"
                            class="input input-bordered" required />
                        <span v-if="phoneError" class="error-message text-red-500">{{ phoneError }}</span>
                    </div>
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
                        <span v-if="emailError" class="error-message text-red-500">{{ emailError }}</span>
                    </div>
                    <div class="form-control">
                        <label for="password" class="label">
                            <span class="label-text text-[#000000]">Contraseña</span>
                        </label>
                        <input id="password" v-model="password" type="password" placeholder="Contraseña"
                            class="input input-bordered" required />
                        <span v-if="passwordError" class="error-message text-red-500">{{ passwordError }}</span>
                    </div>
                    <div class="form-control">
                        <label for="confirm-password" class="label">
                            <span class="label-text text-[#000000]">Confirmar contraseña</span>
                        </label>
                        <input id="confirm-password" v-model="confirmPassword" type="password"
                            placeholder="Confirmar contraseña" class="input input-bordered" required />
                        <span v-if="confirmPasswordError" class="error-message text-red-500">{{ confirmPasswordError }}</span>
                    </div>
                    <div class="form-control mt-6">
                        <button type="submit" class="btn bg-[#D97706] hover:bg-[#B45309] text-white">
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
import axios from 'axios';

export default {
    setup() {
        const router = useRouter();

        // Reactive variables for form inputs
        const fullName = ref('');
        const phone = ref('');
        const username = ref('');
        const email = ref('');
        const password = ref('');
        const confirmPassword = ref('');
        const errorMessage = ref('');
        const phoneError = ref('');
        const emailError = ref('');
        const passwordError = ref(''); // Nueva variable para errores de contraseña
        const confirmPasswordError = ref(''); // Nueva variable para errores de confirmación de contraseña

        const validatePhoneNumber = (number) => {
            const regex = /^[0-9]{10,15}$/;
            return regex.test(number);
        };

        const validateEmail = (email) => {
            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return regex.test(email);
        };

        const handleRegistration = async () => {
            // Reset error messages
            errorMessage.value = '';
            phoneError.value = '';
            emailError.value = '';
            passwordError.value = ''; // Reiniciar error de contraseña
            confirmPasswordError.value = ''; // Reiniciar error de confirmación de contraseña

            // Validar número de teléfono
            if (!validatePhoneNumber(phone.value)) {
                phoneError.value = 'Por favor, ingresa un número de teléfono válido (10-15 dígitos).';
                return;
            }

            // Validar correo electrónico
            if (!validateEmail(email.value)) {
                emailError.value = 'Por favor, ingresa un correo electrónico válido.';
                return;
            }

            // Validar contraseña
            if (password.value.length < 8) {
                passwordError.value = 'La contraseña debe tener al menos 8 caracteres.';
                return;
            }

            // Verificar que las contraseñas coincidan
            if (password.value !== confirmPassword.value) {
                confirmPasswordError.value = 'Las contraseñas no coinciden.';
                return;
            }

            const formData = {
                fullName: fullName.value,
                phone: phone.value,
                username: username.value,
                email: email.value,
                password: password.value,
                password2: confirmPassword.value,
            };

            try {
                const response = await axios.post('http://localhost:8000/api/users/clients/create/', formData);
                console.log('User registered:', response.data);
                router.push('/login');
            } catch (error) {
                errorMessage.value = error.response?.data?.password ? error.response.data.password : 'Error al registrar el usuario. Por favor, intenta nuevamente.';
                console.error('Error during registration:', error);
            }
        };

        return {
            fullName,
            phone,
            username,
            email,
            password,
            confirmPassword,
            errorMessage,
            phoneError,
            emailError,
            passwordError, // Agregar al retorno
            confirmPasswordError, // Agregar al retorno
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
