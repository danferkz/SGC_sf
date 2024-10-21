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
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
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
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
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
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
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
                                    <svg class="h-5 w-5 text-gray-400 mr-2" fill="none" viewBox="0 0 24 24"
                                        stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" ststylewidth="2"
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
                        <label for="email" class="block text-sm font-medium text-gray-700">Correo</label>
                        <input type="email" id="email" v-model="userData.email"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="dni" class="block text-sm font-medium text-gray-700">DNI</label>
                        <input type="text" id="dni" v-model="userData.dni"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required @input="validateDNI" @keypress="onlyNumber" @keydown="limitDNI">
                        <p v-if="dniError" class="text-red-500 text-sm mt-1">{{ dniError }}</p>
                    </div>
                    <div>
                        <label for="sex" class="block text-sm font-medium text-gray-700">Sexo</label>
                        <select id="sex" v-model="userData.sex"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                            <option value="">Seleccionar</option>
                            <option value="masculino">Masculino</option>
                            <option value="femenino">Femenino</option>
                            <option value="otro">Otro</option>
                        </select>
                    </div>
                    <div>
                        <label for="address" class="block text-sm font-medium text-gray-700">Dirección</label>
                        <textarea id="address" v-model="userData.address" rows="3"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm resize-none"
                            required></textarea>
                    </div>
                    <div>
                        <label for="phone" class="block text-sm font-medium text-gray-700">Teléfono</label>
                        <input type="tel" id="phone" v-model="userData.phone"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required @input="validatePhone" @keypress="onlyNumber" @keydown="limitPhone">
                        <p v-if="phoneError" class="text-red-500 text-sm mt-1">{{ phoneError }}</p>
                    </div>
                    <div class="modal-actions mt-4">
                        <button type="button" @click="closeModal" class="btn">Cancelar</button>
                        <button type="submit" class="ml-3 inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            Guardar Cambios
                        </button>
                    </div>
                </form>

                <!-- Password Change Form -->
                <form v-if="modalType === 'password'" @submit.prevent="handlePasswordSubmit" class="space-y-4">
                    <div>
                        <label for="currentPassword" class="block text-sm font-medium text-gray-700">Contraseña actual</label>
                        <input type="password" id="currentPassword" v-model="passwordData.currentPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="newPassword" class="block text-sm font-medium text-gray-700">Nueva contraseña</label>
                        <input type="password" id="newPassword" v-model="passwordData.newPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div>
                        <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirmar nueva contraseña</label>
                        <input type="password" id="confirmPassword" v-model="passwordData.confirmPassword"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
                    </div>
                    <div class="modal-actions mt-4">
                        <button type="button" @click="closeModal" class="btn">Cancelar</button>
                        <button type="submit" class="ml-3 inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white bg-yellow-600 hover:bg-yellow-700 focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500">
                            Cambiar Contraseña
                        </button>
                    </div>
                </form>

                <!-- Delete Account Confirmation -->
                <div v-if="modalType === 'delete'">
                    <p class="text-sm text-gray-500">¿Estás seguro de que quieres eliminar tu cuenta? Esta acción no se puede deshacer.</p>
                    <div class="modal-actions mt-4">
                        <button @click="closeModal" class="btn">Cancelar</button>
                        <button @click="handleDeleteAccount" class="ml-3 inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white bg-red-600 hover:bg-red-700 focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            Eliminar
                        </button>
                    </div>
                </div>
            </div>
        </dialog>
    </div>
</template>

<script setup>
import HeaderValid from "@/components/HeaderCompo.vue";
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex'; // Importa useStore para acceder al store

// Estado
const modalType = ref('');
const userData = ref({
    username: '',
    email: '',
    dni: '',
    sex: '',
    address: '',
    phone: '',
});

const passwordData = ref({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
});

const dniError = ref('');
const phoneError = ref('');
const passwordError = ref('');

// Computed properties
const modalTitle = computed(() => {
    switch (modalType.value) {
        case 'update':
            return 'Actualizar Perfil';
        case 'password':
            return 'Cambiar Contraseña';
        case 'delete':
            return 'Eliminar Cuenta';
        default:
            return '';
    }
});

const store = useStore(); // Para acceder al store

// Métodos
const openModal = (type) => {
    modalType.value = type;
    if (type === 'update') {
        loadUserData();
    }
    const modal = document.getElementById('my_modal');
    modal.showModal();
};

const closeModal = () => {
    modalType.value = '';
    userData.value = {
        email: '',
        dni: '',
        sex: '',
        address: '',
        phone: '',
    };
    passwordData.value = {
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
    };
    passwordError.value = '';
    const modal = document.getElementById('my_modal');
    modal.close();
};

// Validaciones
const validateUserData = () => {
    // Aquí puedes implementar más validaciones si es necesario
    return true;
};

const validatePasswordChange = () => {
    if (passwordData.value.newPassword !== passwordData.value.confirmPassword) {
        passwordError.value = 'Las contraseñas no coinciden';
        return false;
    }
    if (passwordData.value.newPassword.length < 8) {
        passwordError.value = 'La contraseña debe tener al menos 8 caracteres';
        return false;
    }
    passwordError.value = '';
    return true;
};

// Actualizar perfil
const handleUpdateSubmit = async () => {
    try {
        if (!validateUserData()) {
            return;
        }

        const response = await fetch('/api/user/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`, 
            },
            body: JSON.stringify(userData.value)
        });

        if (!response.ok) {
            throw new Error('Error al actualizar el perfil');
        }

        toast.success('Perfil actualizado correctamente');
        closeModal();
        loadUserData(); 
    } catch (error) {
        console.error('Error:', error);
        toast.error('Error al actualizar el perfil');
    }
};

// Cambiar contraseña
const handlePasswordSubmit = async () => {
    try {
        if (!validatePasswordChange()) {
            return;
        }

        const response = await fetch('/api/user/password', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`, 
            },
            body: JSON.stringify({
                currentPassword: passwordData.value.currentPassword,
                newPassword: passwordData.value.newPassword
            })
        });

        if (!response.ok) {
            throw new Error('Error al cambiar la contraseña');
        }

        toast.success('Contraseña actualizada correctamente');
        closeModal();
    } catch (error) {
        console.error('Error:', error);
        toast.error('Error al cambiar la contraseña');
    }
};

// Eliminar cuenta
const handleDeleteAccount = async () => {
    try {
        const response = await fetch('/api/user/delete', {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`, 
            }
        });

        if (!response.ok) {
            throw new Error('Error al eliminar la cuenta');
        }

        toast.success('Cuenta eliminada correctamente');
        localStorage.removeItem('token');
        window.location.href = '/login';
    } catch (error) {
        console.error('Error:', error);
        toast.error('Error al eliminar la cuenta');
    }
};

// Cerrar sesión
const handleLogout = () => {
    localStorage.removeItem('token'); // Eliminar el token
    store.dispatch('sessions/logout'); // Despacha la acción de logout en Vuex
    window.location.href = '/login'; // Redirige al usuario a la página de inicio de sesión
};

// Validaciones de campo específicas
const validateDNI = (event) => {
    // Implementar validación de DNI
};

const validatePhone = (event) => {
    // Implementar validación de teléfono
};

const onlyNumber = (event) => {
    const keyCode = event.keyCode || event.which;
    if (keyCode < 48 || keyCode > 57) {
        event.preventDefault();
    }
};

const limitDNI = (event) => {
    if (event.target.value.length >= 8 && event.keyCode !== 8) {
        event.preventDefault();
    }
};

const limitPhone = (event) => {
    if (event.target.value.length >= 9 && event.keyCode !== 8) {
        event.preventDefault();
    }
};

// Cargar datos de usuario desde el store de sessions.js
const loadUserData = async () => {
    try {
        const currentUser = store.state.sessions.currentUser; // Obtenemos el usuario desde el store
        if (currentUser) {
            userData.value = {
                username: currentUser.username,
                email: currentUser.email,
                dni: currentUser.dni,
                sex: currentUser.sex,
                address: currentUser.address,
                phone: currentUser.phone
            };
        }
    } catch (error) {
        console.error('Error al cargar datos del usuario:', error);
    }
};

// Al montar el componente, cargamos los datos del usuario
onMounted(() => {
    loadUserData();
});
</script>

<script>
// Mueve la función beforeRouteEnter aquí, fuera del <script setup>
export default {
    beforeRouteEnter(to, from, next) {
        next(async (vm) => {
            if (!vm.$store.state.sessions.currentUser) {
                await vm.$store.dispatch('sessions/autoLogin'); // Intenta autoLogin si no hay usuario actual
            }
            vm.loadUserData(); // Cargar los datos del usuario después del autoLogin
        });
    },
};
</script>