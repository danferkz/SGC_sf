<template>
    <div>
        <HeaderCompo />

        <!-- Profile Header -->
        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div class="bg-white shadow sm:rounded-lg">
                <div class="px-4 py-5 sm:px-6">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <div class="avatar">
                                <div class="w-24 rounded">
                                    <img src="../assets/usuario_log.png" />
                                </div>
                            </div>
                            <div class="ml-4">
                                <h1 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
                                    Juan Pérez
                                </h1>
                                <p class="text-sm font-medium text-gray-500">@juanperez</p>
                                <p class="text-sm font-medium text-gray-500">juan@example.com</p>
                            </div>
                        </div>
                        <div class="mt-4 flex md:mt-0">
                            <button @click="openModal('update')"
                                class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                                Editar Perfil
                            </button>
                            <button @click="openModal('delete')"
                                class="ml-3 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                                Eliminar Cuenta
                            </button>
                        </div>
                    </div>
                </div>
                <div class="border-t border-gray-200 px-4 py-5 sm:px-6">
                    <!-- Subtítulo -->
                    <h2 class="text-xl font-semibold text-gray-800 mb-4">Datos del Usuario</h2>
                    <dl class="grid grid-cols-1 gap-x-4 gap-y-8 sm:grid-cols-2">
                        <div class="sm:col-span-1">
                            <dt class="text-sm font-medium text-gray-500">Teléfono</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ userData.phone }}</dd>
                        </div>
                        <div class="sm:col-span-1 flex items-center">
                            <div>
                                <dt class="text-sm font-medium text-gray-500">Miembro desde</dt>
                                <dd class="mt-1 text-sm text-gray-900">Enero 2023</dd>
                            </div>
                            <!-- Botón Completar Datos -->
                            <div class="ml-20">
                                <button @click="openModal('create')"
                                    class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                                    Completar Datos
                                </button>
                            </div>
                        </div>
                        <div class="sm:col-span-1">
                            <dt class="text-sm font-medium text-gray-500">DNI</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ userData.dni }}</dd>
                        </div>
                        <div class="sm:col-span-1">
                            <dt class="text-sm font-medium text-gray-500">Sexo</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ userData.sex }}</dd>
                        </div>
                        <div class="sm:col-span-2">
                            <dt class="text-sm font-medium text-gray-500">Dirección</dt>
                            <dd class="mt-1 text-sm text-gray-900">{{ userData.address }}</dd>
                        </div>
                    </dl>
                </div>
                <!-- Nuevo Botón "Ir a Productos" -->
                <div class="px-4 py-4 sm:px-6">
                    <button @click="goToProducts"
                        class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white bg-black hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-black">
                        Ir a Productos
                    </button>
                </div>
            </div>
        </div>

        <!-- Modal -->
        <dialog id="my_modal" class="modal">
            <div class="modal-box">
                <h3 class="text-lg font-bold" id="modal-title">{{ modalTitle }}</h3>
                <form @submit.prevent="handleSubmit" class="space-y-4">
                    <div v-if="modalType !== 'delete'">
                        <label for="name" class="block text-sm font-medium text-gray-700">Nombre</label>
                        <input type="text" id="name" v-model="userData.name"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div v-if="modalType !== 'delete'">
                        <label for="description" class="block text-sm font-medium text-gray-700">Descripción</label>
                        <textarea id="description" v-model="userData.description"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm resize-none"
                            required></textarea>
                    </div>
                    <div v-if="modalType !== 'delete'">
                        <label for="dni" class="block text-sm font-medium text-gray-700">DNI</label>
                        <input type="text" id="dni" v-model="userData.dni"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required @input="validateDNI" @keypress="onlyNumber" @keydown="limitDNI">
                        <p v-if="dniError" class="text-red-500 text-sm mt-1">{{ dniError }}</p>
                    </div>
                    <div v-if="modalType !== 'delete'">
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
                    <div v-if="modalType !== 'delete'">
                        <label for="address" class="block text-sm font-medium text-gray-700">Dirección</label>
                        <textarea id="address" v-model="userData.address" rows="3"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm resize-none"
                            required></textarea>
                    </div>
                    <div v-if="modalType !== 'delete'">
                        <label for="phone" class="block text-sm font-medium text-gray-700">Teléfono</label>
                        <input type="tel" id="phone" v-model="userData.phone"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required @input="validatePhone" @keypress="onlyNumber" @keydown="limitPhone">
                        <p v-if="phoneError" class="text-red-500 text-sm mt-1">{{ phoneError }}</p>
                    </div>
                    <div v-if="modalType !== 'delete'">
                        <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
                        <input type="password" id="password" v-model="userData.password"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div v-if="modalType === 'delete'" class="text-sm text-gray-500">
                        ¿Estás seguro de que quieres eliminar tu cuenta? Esta acción no se puede deshacer.
                    </div>
                </form>
                <div class="modal-actions">
                    <button @click="closeModal" class="btn">Cancelar</button>
                    <button @click="handleSubmit" :class="[
                        'mt-2 inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 text-base font-medium text-white',
                        'bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2',
                        { 'bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500': modalType !== 'delete', 'bg-red-600 hover:bg-red-700 focus:ring-red-500': modalType === 'delete' }
                    ]">
                        {{ modalType === 'delete' ? 'Eliminar' : 'Guardar' }}
                    </button>
                </div>
            </div>
        </dialog>
    </div>
</template>


<script>
export default {
    data() {
        return {
            userData: {
                name: '',
                description: '',
                dni: '',
                sex: '',
                address: '',
                phone: '',
                password: '',
            },
            modalType: '',
            modalTitle: '',
            dniError: '',
            phoneError: '',
        };
    },
    methods: {
        openModal(type) {
            this.modalType = type;
            this.modalTitle = type === 'update' ? 'Editar Perfil' : 'Eliminar Cuenta';
            this.dniError = '';
            this.phoneError = '';
            document.getElementById('my_modal').showModal();
        },
        closeModal() {
            document.getElementById('my_modal').close();
        },
        validateDNI() {
            const dniPattern = /^\d{8}$/; // 8 dígitos
            if (!this.userData.dni.match(dniPattern)) {
                this.dniError = 'El DNI debe tener exactamente 8 dígitos y solo números.';
            } else {
                this.dniError = '';
            }
        },
        validatePhone() {
            const phonePattern = /^\d{9}$/; // 9 dígitos
            if (!this.userData.phone.match(phonePattern)) {
                this.phoneError = 'El teléfono debe tener exactamente 9 dígitos y solo números.';
            } else {
                this.phoneError = '';
            }
        },
        handleSubmit() {
            if (!this.dniError && !this.phoneError) {
                this.closeModal();
            }
        },
        goToProducts() {
            this.$router.push('/producto');
        },
        onlyNumber(event) {
            const char = String.fromCharCode(event.which);
            if (!/[0-9]/.test(char)) {
                event.preventDefault(); // Impide la entrada de caracteres que no son números
            }
        },
        limitDNI(event) {
            if (this.userData.dni.length >= 8 && event.key !== "Backspace") {
                event.preventDefault(); // Impide la entrada si ya tiene 8 dígitos
            }
        },
        limitPhone(event) {
            if (this.userData.phone.length >= 9 && event.key !== "Backspace") {
                event.preventDefault(); // Impide la entrada si ya tiene 9 dígitos
            }
        },
    },
};
</script>

<style scoped></style>
