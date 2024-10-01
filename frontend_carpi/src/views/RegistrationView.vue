<template>
    <div class="min-h-screen bg-wood-pattern flex items-center justify-center px-4">
        <div class="max-w-md w-full space-y-8 bg-[#FFFBEB] p-10 rounded-xl shadow-2xl">
            <div>
                <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                    Crear una cuenta
                </h2>
                <p class="mt-2 text-center text-sm text-gray-600">
                    Únete a Carpintería Artesanal
                </p>
            </div>
            <form class="mt-8 space-y-6" @submit.prevent="handleRegistration">
                <div class="rounded-md shadow-sm -space-y-px">
                    <div>
                        <label for="name" class="sr-only">Nombre completo</label>
                        <input
                            id="name"
                            name="name"
                            type="text"
                            required
                            v-model="name"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white rounded-t-md focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            placeholder="Nombre completo"
                        >
                    </div>
                    <div class="mb-[3px]">
                        <label for="email-address" class="sr-only">Correo electrónico</label>
                        <input
                            id="email-address"
                            name="email"
                            type="email"
                            autocomplete="email"
                            required
                            v-model="email"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            :class="{ 'border-red-500': emailError }"
                            placeholder="Correo electrónico"
                        >
                        <p v-if="emailError" class="text-red-500 text-xs mt-1">Correo electrónico inválido</p>
                    </div>
                    <div class="mb-[3px]">
                        <label for="address" class="sr-only">Dirección</label>
                        <input
                            id="address"
                            name="address"
                            type="text"
                            required
                            v-model="address"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            placeholder="Dirección"
                        >
                    </div>
                    <div class="mb-[3px]">
                        <label for="phone-number" class="sr-only">Número telefónico</label>
                        <input
                            id="phone-number"
                            name="phone-number"
                            type="tel"
                            required
                            v-model="phoneNumber"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            :class="{ 'border-red-500': phoneError }"
                            placeholder="Número telefónico"
                        >
                        <p v-if="phoneError" class="text-red-500 text-xs mt-1">Número telefónico inválido</p>
                    </div>
                    <div class="mb-[3px]">
                        <label for="password" class="sr-only">Contraseña</label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            autocomplete="new-password"
                            required
                            v-model="password"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            placeholder="Contraseña"
                        >
                    </div>
                    <div class="mb-[3px]">
                        <label for="confirm-password" class="sr-only">Confirmar contraseña</label>
                        <input
                            id="confirm-password"
                            name="confirm-password"
                            type="password"
                            autocomplete="new-password"
                            required
                            v-model="confirmPassword"
                            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white rounded-b-md focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                            :class="{ 'border-red-500': passwordMismatch }"
                            placeholder="Confirmar contraseña"
                        >
                        <p v-if="passwordMismatch" class="text-red-500 text-xs mt-1">Las contraseñas no coinciden</p>
                    </div>
                </div>

                <!-- Nueva sección para términos y condiciones -->
                <div class="flex items-center">
                    <input
                        id="terms"
                        name="terms"
                        type="checkbox"
                        v-model="termsAccepted"
                        class="h-4 w-4 text-amber-600 focus:ring-amber-500 border-gray-300 rounded"
                        required
                    >
                    <label for="terms" class="ml-2 block text-sm text-gray-900">
                        Acepto los <a href="#" class="text-amber-600 hover:text-amber-500">términos y condiciones</a>
                    </label>
                </div>
                <p v-if="!termsAccepted && submitAttempt" class="text-red-500 text-xs mt-1">
                    Debes aceptar los términos y condiciones
                </p>

                <div>
                    <button
                        type="submit"
                        class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500"
                    >
                        <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                            <UserPlusIcon class="h-5 w-5 text-amber-500 group-hover:text-amber-400" aria-hidden="true" />
                        </span>
                        Registrarse
                    </button>
                </div>
            </form>
            <div class="text-center">
                <p class="mt-2 text-sm text-gray-600">
                    ¿Ya tienes una cuenta?
                    <a href="#" class="font-medium text-amber-600 hover:text-amber-500">
                        Inicia sesión aquí
                    </a>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const name = ref('');
const email = ref('');
const address = ref('');
const phoneNumber = ref('');
const password = ref('');
const confirmPassword = ref('');
const termsAccepted = ref(false);

const emailError = ref(false);
const phoneError = ref(false);
const passwordMismatch = ref(false);
const submitAttempt = ref(false);

const handleRegistration = () => {
    submitAttempt.value = true;
    emailError.value = !validateEmail(email.value);
    phoneError.value = !validatePhoneNumber(phoneNumber.value);
    passwordMismatch.value = password.value !== confirmPassword.value;

    if (!emailError.value && !phoneError.value && !passwordMismatch.value && termsAccepted.value) {
        // Lógica para manejar el registro exitoso
        console.log('Registro exitoso');
    }
};

const validateEmail = (email) => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
};

const validatePhoneNumber = (phone) => {
    const phonePattern = /^[0-9]+$/;
    return phonePattern.test(phone);
};
</script>

<style>
/* Estilo personalizado si es necesario */
</style>
