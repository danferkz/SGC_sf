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
                        actualizar Perfil
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
                <form @submit.prevent="handleSubmit" class="space-y-4">
                    <div v-if="modalType !== 'delete'">
                        <label for="username" class="block text-sm font-medium text-gray-700">Nombre de usuario</label>
                        <input type="text" id="username" v-model="userData.username"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
                    </div>
                    <div v-if="modalType !== 'delete'">
                        <label for="email" class="block text-sm font-medium text-gray-700">Correo</label>
                        <input type="email" id="email" v-model="userData.email"
                            class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                            required>
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
import HeaderValid from "@/components/HeaderCompo.vue";
import { mapGetters } from "vuex";
import { onMounted } from "vue";

export default {
    components: {
        HeaderValid,
    },
    data() {
        return {
            userData: {
                name: "",
                description: "",
                dni: "",
                sex: "",
                address: "",
                phone: "",
                password: "",
            },
            modalType: "",
            modalTitle: "",
            dniError: "",
            phoneError: "",
        };
    },
    computed: {
        ...mapGetters("sessions", ["currentUser"]),
    },
    beforeRouteEnter(to, from, next) {
        next(async (vm) => {
            if (!vm.currentUser) {
                // Intenta hacer autoLogin si el usuario no está ya en el estado
                await vm.$store.dispatch("sessions/autoLogin");
            }
        });
    },
    methods: {
        openModal(type) {
            this.modalType = type;
            this.modalTitle = type === "update" ? "Editar Perfil" : "Eliminar Cuenta";
            this.dniError = "";
            this.phoneError = "";
            document.getElementById("my_modal").showModal();
        },
        closeModal() {
            document.getElementById("my_modal").close();
        },
        validateDNI() {
            const dniPattern = /^\d{8}$/; // 8 dígitos
            if (!this.userData.dni.match(dniPattern)) {
                this.dniError = "El DNI debe tener exactamente 8 dígitos y solo números.";
            } else {
                this.dniError = "";
            }
        },
        validatePhone() {
            const phonePattern = /^\d{9}$/; // 9 dígitos
            if (!this.userData.phone.match(phonePattern)) {
                this.phoneError = "El teléfono debe tener exactamente 9 dígitos y solo números.";
            } else {
                this.phoneError = "";
            }
        },
        async handleSubmit() {
            if (!this.dniError && !this.phoneError) {
                try {
                    // Recoge los datos del usuario
                    const updatedUser = {
                        username: this.userData.name,
                        email: this.currentUser.email, // Utiliza el email actual
                        password: this.userData.password,
                        password2: this.userData.password, // Asumiendo que password2 es igual a password
                        DNI: this.userData.dni,
                        sexo: this.userData.sex,
                        direccion: this.userData.address,
                        telefono: this.userData.phone,
                    };

                    // Realiza la solicitud PUT al backend
                    const response = await this.$axios.put(
                        `/clients/update/${this.currentUser.id}/`,
                        updatedUser
                    );

                    // Si la actualización es exitosa, cierra el modal y actualiza la información del usuario
                    this.closeModal();

                    // Actualiza la información del usuario en Vuex
                    this.$store.commit("sessions/setCurrentUser", response.data);

                    // Muestra un mensaje de éxito (opcional)
                    this.$toast.success("Perfil actualizado correctamente");
                } catch (error) {
                    // Muestra un error si falla la actualización
                    console.error("Error al actualizar el perfil:", error);
                    this.$toast.error("Hubo un problema al actualizar el perfil");
                }
            }
        },
        handleLogout() {
            this.$store.dispatch("sessions/logout");
            this.$router.push("/login"); // Ajusta según tu ruta
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
                style
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
