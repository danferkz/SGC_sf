<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 flex">
        <!-- Header -->
        <HeaderAdmin class="header-admin" />

        <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
            <div class="max-w-7xl mx-auto">
                <!-- Título principal -->
                <h3 class="text-3xl font-bold text-center mb-12">Panel de Administración de usuarios Administrador</h3>

                <!-- Botón para agregar usuario -->
                <div class="flex justify-end mb-6">
                    <button @click="openCreateModal"
                        class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none">
                        CREAR ADMINISTRADOR
                    </button>
                </div>

                <!-- Tabla de usuarios -->
                <div class="bg-white shadow-md rounded-lg overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        ID</th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Nombre</th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Email</th>
                                    <th
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Acciones</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr v-for="user in users" :key="user.id">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ user.id
                                        }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ user.username }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ user.email }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex space-x-2">
                                            <button @click="openDetailModal(user)"
                                                class="text-indigo-600 hover:text-indigo-900">
                                                <PencilIcon class="h-5 w-5" />
                                            </button>
                                            <button @click="openDeleteModal(user)"
                                                class="text-red-600 hover:text-red-900">
                                                <TrashIcon class="h-5 w-5" />
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Paginación -->
                <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
                    <div class="flex justify-center pb-4 space-x-2">
                        <button @click="previousPage" :disabled="!prevPageUrl"
                            class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                            <ChevronLeftIcon class="h-5 w-5" />
                        </button>
                        <button
                            class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                            Página {{ currentPage }}
                        </button>
                        <button @click="nextPage" :disabled="!nextPageUrl"
                            class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                            <ChevronRightIcon class="h-5 w-5" />
                        </button>
                    </div>
                </div>

            </div>
        </div>

        <!-- Modal para crear/editar usuario -->
        <div v-if="showModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
                <h3 class="text-lg font-semibold mb-4">
                    {{ isEditing ? 'Editar Usuario' : 'Crear Usuario' }}
                </h3>
                <form @submit.prevent="isEditing ? updateUser() : createAdmin()">
                    <div class="mb-4">
                        <label class="block text-gray-700">Nombre</label>
                        <input v-model="currentUser.username" type="text" class="w-full border rounded-md px-4 py-2"
                            placeholder="Nombre del usuario" required
                            @input="currentUser.username = currentUser.username.replace(/\s/g, '')" />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700">Email</label>
                        <input v-model="currentUser.email" type="email" class="w-full border rounded-md px-4 py-2"
                            placeholder="Email del usuario" required />
                    </div>
                    <div class="mb-4" v-if="!isEditing">
                        <label class="block text-gray-700">Contraseña</label>
                        <input v-model="currentUser.password" type="password" class="w-full border rounded-md px-4 py-2"
                            placeholder="Contraseña del usuario" required />
                    </div>
                    <div class="mb-4" v-if="!isEditing">
                        <label class="block text-gray-700">Confirmar Contraseña</label>
                        <input v-model="currentUser.password2" type="password"
                            class="w-full border rounded-md px-4 py-2" placeholder="Confirmar Contraseña" required />
                    </div>
                    <div class="flex justify-end space-x-4">
                        <button type="button" @click="closeModal"
                            class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">
                            Cancelar
                        </button>
                        <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700">
                            {{ isEditing ? 'Actualizar' : 'Crear' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Modal para mostrar detalles -->
        <div v-if="showDetailModal"
            class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
                <h3 class="text-lg font-semibold mb-4">Detalle del Usuario</h3>
                <p class="mb-2"><strong>ID:</strong> {{ currentUser.id }}</p>
                <p class="mb-2"><strong>Nombre:</strong> {{ currentUser.username }}</p>
                <p class="mb-2"><strong>Email:</strong> {{ currentUser.email }}</p>
                <div class="flex justify-end mt-4">
                    <button type="button" @click="closeDetailModal"
                        class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">
                        Cerrar
                    </button>
                </div>
            </div>
        </div>

        <!-- Modal de confirmación para eliminar -->
        <div v-if="showDeleteModal"
            class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
                <h3 class="text-lg font-semibold text-red-600 mb-4">Confirmar Eliminación</h3>
                <p class="text-gray-700 mb-6">
                    ¿Estás seguro de que quieres eliminar al usuario
                    <span class="font-semibold ">{{ currentUser.username }}</span>? Esta acción no se puede deshacer.
                </p>
                <div class="flex justify-end space-x-4">
                    <button type="button" @click="closeDeleteModal"
                        class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">
                        Cancelar
                    </button>
                    <button @click="deleteUser" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700">
                        Eliminar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, reactive, onMounted } from 'vue'
import HeaderAdmin from "@/components/NabvarVerticalAdmin.vue"
import { PencilIcon, TrashIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'

// Endpoints corregidos para coincidir con tu API
const API_URL = 'http://127.0.0.1:8000/api/users'
const ENDPOINTS = {
    LIST: `${API_URL}/admins/`,                 // Endpoint base para listar
    CREATE: `${API_URL}/admins/create/`,        // Endpoint para crear
    DELETE: `${API_URL}/admins/delete/`,        // Endpoint para eliminar
    UPDATE: `${API_URL}/admins/update/`,        // Endpoint para actualizar
    DETAIL: `${API_URL}/admins/detail/`         // Endpoint para detalles
}

// Variables reactivas
const users = ref([])
const currentPage = ref(1)
const nextPageUrl = ref(null)
const prevPageUrl = ref(null)
const showModal = ref(false)
const showDeleteModal = ref(false)
const showDetailModal = ref(false)
const isEditing = ref(false)
const currentUser = reactive({ id: null, username: '', email: '', password: '', password2: '' })

const token = localStorage.getItem('token')

// Headers comunes
const getHeaders = () => ({
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json'
})

// Función para obtener la lista de administradores
const fetchAdmins = async (page = 1) => {
    try {
        const url = `${ENDPOINTS.LIST}?page=${page}`
        const response = await fetch(url, {
            method: 'GET',
            headers: getHeaders()
        })
        
        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.message || 'Error al obtener administradores')
        }
        
        const data = await response.json()
        users.value = data.results
        nextPageUrl.value = data.next
        prevPageUrl.value = data.previous
        currentPage.value = page
    } catch (error) {
        console.error('Error en fetchAdmins:', error)
        alert('Error al cargar los administradores')
    }
}

// Función para crear un administrador
const createAdmin = async () => {
    try {
        const response = await fetch(ENDPOINTS.CREATE, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({
                username: currentUser.username,
                email: currentUser.email,
                password: currentUser.password,
                password2: currentUser.password2
            })
        })

        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.message || 'Error al crear administrador')
        }

        await response.json()
        await fetchAdmins(currentPage.value)
        alert('Administrador creado exitosamente')
        closeModal()
    } catch (error) {
        console.error('Error en createAdmin:', error)
        alert(error.message || 'Error al crear el administrador')
    }
}

// Función para eliminar un administrador
const deleteUser = async () => {
    try {
        const response = await fetch(`${ENDPOINTS.DELETE}${currentUser.id}/`, {
            method: 'DELETE',
            headers: getHeaders()
        })

        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.message || 'Error al eliminar administrador')
        }

        await fetchAdmins(currentPage.value)
        alert('Administrador eliminado exitosamente')
        closeDeleteModal()
    } catch (error) {
        console.error('Error en deleteUser:', error)
        alert(error.message || 'Error al eliminar el administrador')
    }
}

// Funciones de paginación
const nextPage = () => {
    if (nextPageUrl.value) {
        const nextPageNumber = currentPage.value + 1
        fetchAdmins(nextPageNumber)
    }
}

const previousPage = () => {
    if (prevPageUrl.value) {
        const prevPageNumber = currentPage.value - 1
        fetchAdmins(prevPageNumber)
    }
}

// Funciones de modal
const openCreateModal = () => {
    isEditing.value = false
    Object.assign(currentUser, { id: null, username: '', email: '', password: '', password2: '' })
    showModal.value = true
}

const openDeleteModal = (user) => {
    Object.assign(currentUser, user)
    showDeleteModal.value = true
}

const openDetailModal = (user) => {
    Object.assign(currentUser, user)
    showDetailModal.value = true
}

const closeModal = () => {
    showModal.value = false
    Object.assign(currentUser, { id: null, username: '', email: '', password: '', password2: '' })
}

const closeDeleteModal = () => {
    showDeleteModal.value = false
    Object.assign(currentUser, { id: null, username: '', email: '', password: '', password2: '' })
}

const closeDetailModal = () => {
    showDetailModal.value = false
    Object.assign(currentUser, { id: null, username: '', email: '', password: '', password2: '' })
}

// Inicialización
onMounted(() => {
    fetchAdmins(1)
})
</script>