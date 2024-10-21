<template>
    <div class="min-h-screen bg-gray-100">
        <HeaderValid />
        <main>
            <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                <div class="bg-white shadow sm:rounded-lg">
                    <div class="px-4 py-5 sm:px-6">
                        <div class="flex items-center">
                            <div class="avatar">
                                <div class="w-24 rounded">
                                    <img src="../assets/usuario_log.png" alt="Usuario" />
                                </div>
                            </div>
                            <div class="ml-4">
                                <div v-if="currentUser">
                                    <h1 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
                                        {{ currentUser.username || "Usuario" }}
                                    </h1>
                                    <p class="text-sm font-medium text-gray-500">
                                        {{ currentUser.email || "email@example.com" }}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="border-t border-gray-200">
                        <dl class="divide-y divide-gray-200">
                            <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                                <dt class="text-sm font-medium text-gray-500 flex items-center">
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                                    </svg>
                                    Teléfono
                                </dt>
                                <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                                    {{ currentUser?.phone || "No disponible" }}
                                </dd>
                            </div>
                            <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                                <dt class="text-sm font-medium text-gray-500 flex items-center">
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2" />
                                    </svg>
                                    DNI
                                </dt>
                                <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                                    {{ currentUser?.dni || "No disponible" }}
                                </dd>
                            </div>
                            <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                                <dt class="text-sm font-medium text-gray-500 flex items-center">
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                    </svg>
                                    Sexo
                                </dt>
                                <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                                    {{ currentUser?.sex || "No disponible" }}
                                </dd>
                            </div>
                            <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                                <dt class="text-sm font-medium text-gray-500 flex items-center">
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                                    </svg>
                                    Dirección
                                </dt>
                                <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                                    {{ currentUser?.address || "No disponible" }}
                                </dd>
                            </div>
                        </dl>
                    </div>
                </div>
                <div class="mt-6">
                    <button @click="openModal('update')"
                        class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Actualizar Perfil
                    </button>
                    <button @click="openModal('password')"
                        class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-yellow-600 hover:bg-yellow-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500">
                        Cambiar Contraseña
                    </button>
                    <button @click="openModal('delete')"
                        class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                        Eliminar Cuenta
                    </button>
                    <button @click="handleLogout"
                        class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                        Cerrar Sesión
                    </button>
                </div>
            </div>
        </main>

        <!-- Modal -->
        <dialog id="my_modal" class="modal">
            <div class="modal-box">
                <h3 class="text-lg font-bold" id="modal-title">{{ modalTitle }}</h3>
                
                <!-- Update Profile Form -->
                <form v-if="modalType === 'update'" @submit.prevent="handleUpdateSubmit" class="space-y-4">
                    <div>
                        <label for="username" class="block text-sm font-medium text-gray-700">Nombre de usuario</label>
                        <input type="text" id="username" v-model="userData.username"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Correo electrónico</label>
                        <input type="email" id="email" v-model="userData.email"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="phone" class="block text-sm font-medium text-gray-700">Teléfono</label>
                        <input type="text" id="phone" v-model="userData.phone" @input="validatePhone"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                        <p v-if="phoneError" class="text-red-600 text-sm">{{ phoneError }}</p>
                    </div>
                    <div>
                        <label for="dni" class="block text-sm font-medium text-gray-700">DNI</label>
                        <input type="text" id="dni" v-model="userData.dni" @input="validateDNI"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                        <p v-if="dniError" class="text-red-600 text-sm">{{ dniError }}</p>
                    </div>
                    <div>
                        <label for="sex" class="block text-sm font-medium text-gray-700">Sexo</label>
                        <select id="sex" v-model="userData.sex"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
                            <option value="" disabled selected>Selecciona</option>
                            <option value="Masculino">Masculino</option>
                            <option value="Femenino">Femenino</option>
                        </select>
                    </div>
                    <div>
                        <label for="address" class="block text-sm font-medium text-gray-700">Dirección</label>
                        <input type="text" id="address" v-model="userData.address"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div class="flex justify-end">
                        <button type="button" @click="closeModal" class="mr-2 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gray-400 hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                            Cancelar
                        </button>
                        <button type="submit"
                            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Guardar Cambios
                        </button>
                    </div>
                </form>

                <!-- Change Password Form -->
                <form v-if="modalType === 'password'" @submit.prevent="handlePasswordSubmit" class="space-y-4">
                    <div>
                        <label for="old-password" class="block text-sm font-medium text-gray-700">Contraseña Actual</label>
                        <input type="password" id="old-password" v-model="passwordData.oldPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="new-password" class="block text-sm font-medium text-gray-700">Nueva Contraseña</label>
                        <input type="password" id="new-password" v-model="passwordData.newPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirmar Nueva Contraseña</label>
                        <input type="password" id="confirm-password" v-model="passwordData.confirmPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div class="flex justify-end">
                        <button type="button" @click="closeModal" class="mr-2 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gray-400 hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                            Cancelar
                        </button>
                        <button type="submit"
                            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Cambiar Contraseña
                        </button>
                    </div>
                </form>

                <!-- Delete Account Confirmation -->
                <div v-if="modalType === 'delete'" class="space-y-4">
                    <p>¿Estás seguro de que deseas eliminar tu cuenta? Esta acción es irreversible.</p>
                    <div class="flex justify-end">
                        <button type="button" @click="closeModal" class="mr-2 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gray-400 hover:bg-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500">
                            Cancelar
                        </button>
                        <button @click="handleDelete" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            Eliminar Cuenta
                        </button>
                    </div>
                </div>
            </div>
            <div class="modal-action">
                <button @click="closeModal" class="btn">Cerrar</button>
            </div>
        </dialog>
    </div>
</template>

<script>
import HeaderValid from "@/components/HeaderCompo.vue";
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex'; // Importa useStore para acceder al store

export default {
    components: {
        HeaderValid,
    },
    data() {
        return {
            currentUser: {}, // Reemplaza con los datos del usuario actual
            modalType: '',
            modalTitle: '',
            userData: {
                username: '',
                email: '',
                phone: '',
                dni: '',
                sex: '',
                address: '',
            },
            passwordData: {
                oldPassword: '',
                newPassword: '',
                confirmPassword: '',
            },
            phoneError: '',
            dniError: '',
        };
    },
    methods: {
        openModal(type) {
            this.modalType = type;
            this.modalTitle = type === 'update' ? 'Actualizar Perfil' : type === 'password' ? 'Cambiar Contraseña' : 'Eliminar Cuenta';
            if (type === 'update') {
                this.loadUserData(); // Cargar datos del usuario actual
            }
            const modal = document.getElementById('my_modal');
            modal.showModal();
        },
        closeModal() {
            this.modalType = '';
            this.phoneError = '';
            this.dniError = '';
            this.userData = { username: '', email: '', phone: '', dni: '', sex: '', address: '' }; // Resetear datos
            this.passwordData = { oldPassword: '', newPassword: '', confirmPassword: '' }; // Resetear contraseña
            const modal = document.getElementById('my_modal');
            modal.close();
        },
        validatePhone() {
            const phonePattern = /^[0-9]{9}$/; // Asegúrate de que el número tenga exactamente 9 dígitos
            this.phoneError = phonePattern.test(this.userData.phone) ? '' : 'El teléfono debe tener 9 dígitos.';
        },
        validateDNI() {
            const dniPattern = /^[0-9]{8}$/; // Asegúrate de que el DNI tenga exactamente 8 números
            this.dniError = dniPattern.test(this.userData.dni) ? '' : 'El DNI debe tener 8 dígitos.';
        },
        handleUpdateSubmit() {
            if (!this.phoneError && !this.dniError) {
                // Aquí va la lógica para actualizar el perfil
                console.log('Actualizando perfil...', this.userData);
                this.closeModal();
            }
        },
        handlePasswordSubmit() {
            // Aquí va la lógica para cambiar la contraseña
            console.log('Cambiando contraseña...', this.passwordData);
            this.closeModal();
        },
        handleDelete() {
            // Aquí va la lógica para eliminar la cuenta
            console.log('Eliminando cuenta...');
            this.closeModal();
        },
        handleLogout() {
            // Aquí va la lógica para cerrar sesión
            console.log('Cerrando sesión...');
        },
        loadUserData() {
            // Simulando la carga de datos del usuario
            this.userData = {
                username: this.currentUser.username || '',
                email: this.currentUser.email || '',
                phone: this.currentUser.phone || '',
                dni: this.currentUser.dni || '',
                sex: this.currentUser.sex || '',
                address: this.currentUser.address || '',
            };
        },
    },
};
</script>

<style scoped>
/* Puedes añadir aquí tus estilos */
</style>
