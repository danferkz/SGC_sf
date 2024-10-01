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
                        <span v-if="fullNameError" class="error-message text-red-500">{{ fullNameError }}</span>
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
                        <span v-if="usernameError" class="error-message text-red-500">{{ usernameError }}</span>
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
                        <div class="relative">
                            <input id="password" v-model="password" :type="passwordVisible ? 'text' : 'password'" placeholder="Contraseña"
                                class="input input-bordered" required />
                            <button type="button" @click="togglePasswordVisibility('password')" class="absolute inset-y-0 right-0 flex items-center pr-3">
                                <span v-if="passwordVisible">👁️</span>
                                <span v-else>🙈</span>
                            </button>
                        </div>
                        <span v-if="passwordError" class="error-message text-red-500">{{ passwordError }}</span>
                    </div>
                    <div class="form-control">
                        <label for="confirm-password" class="label">
                            <span class="label-text text-[#000000]">Confirmar contraseña</span>
                        </label>
                        <div class="relative">
                            <input id="confirm-password" v-model="confirmPassword" :type="confirmPasswordVisible ? 'text' : 'password'" 
                                placeholder="Confirmar contraseña" class="input input-bordered" required />
                            <button type="button" @click="togglePasswordVisibility('confirmPassword')" class="absolute inset-y-0 right-0 flex items-center pr-3">
                                <span v-if="confirmPasswordVisible">👁️</span>
                                <span v-else>🙈</span>
                            </button>
                        </div>
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
        const fullNameError = ref('');
        const phoneError = ref('');
        const usernameError = ref('');
        const emailError = ref('');
        const passwordError = ref('');
        const confirmPasswordError = ref('');

        const passwordVisible = ref(false);
        const confirmPasswordVisible = ref(false);

        const togglePasswordVisibility = (field) => {
            if (field === 'password') {
                passwordVisible.value = !passwordVisible.value;
            } else if (field === 'confirmPassword') {
                confirmPasswordVisible.value = !confirmPasswordVisible.value;
            }
        };

        const validatePhoneNumber = (phone) => {
            const phoneRegex = /^\d{10,15}$/;
            return phoneRegex.test(phone);
        };

        const validateEmail = (email) => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        };

        const validateUsername = (username) => {
            const usernameRegex = /^[a-zA-Z0-9_]+$/; // Solo permite letras, números y guiones bajos
            return usernameRegex.test(username);
        };

        const handleRegistration = async () => {
            // Reset error messages
            errorMessage.value = '';
            fullNameError.value = '';
            phoneError.value = '';
            usernameError.value = '';
            emailError.value = '';
            passwordError.value = '';
            confirmPasswordError.value = '';

            // Validaciones de campos obligatorios
            if (!fullName.value) {
                fullNameError.value = 'El nombre completo es obligatorio.';
            }

            if (!validatePhoneNumber(phone.value)) {
                phoneError.value = 'Por favor, ingresa un número de teléfono válido (10-15 dígitos).';
            }

            if (!validateUsername(username.value)) {
                usernameError.value = 'El nombre de usuario solo puede contener letras, números y guiones bajos.';
            } else if (!username.value) {
                usernameError.value = 'El nombre de usuario es obligatorio.';
            }

            if (!validateEmail(email.value)) {
                emailError.value = 'Por favor, ingresa un correo electrónico válido.';
            }

            if (!password.value) {
                passwordError.value = 'La contraseña es obligatoria.';
            } else if (password.value.length < 8) {
                passwordError.value = 'La contraseña debe tener al menos 8 caracteres.';
            }

            if (password.value !== confirmPassword.value) {
                confirmPasswordError.value = 'Las contraseñas no coinciden.';
            }

            // Si hay errores, no continuar con la creación de usuario
            if (fullNameError.value || phoneError.value || usernameError.value || emailError.value || passwordError.value || confirmPasswordError.value) {
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
            fullNameError,
            phoneError,
            usernameError,
            emailError,
            passwordError,
            confirmPasswordError,
            passwordVisible,
            confirmPasswordVisible,
            togglePasswordVisibility,
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
