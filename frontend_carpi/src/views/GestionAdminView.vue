<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 flex">
        <!-- Header -->
        <HeaderAdmin class="header-admin" />

        <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
            <div class="max-w-7xl mx-auto">
                <!-- Título principal -->
                <h3 class="text-3xl font-bold text-center mb-12">Panel de Administración de Usuarios</h3>

                <!-- Botón para agregar usuario -->
                <div class="flex justify-end mb-6">
                    <button @click="openCreateModal"
                        class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none">
                        Agregar Usuario
                    </button>
                </div>

                <!-- Tabla de usuarios -->
                <div class="bg-white shadow-md rounded-lg overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr v-for="user in users" :key="user.id">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ user.id }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ user.username }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ user.email }}</td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex space-x-2">
                                            <button @click="openEditModal(user)"
                                                class="bg-blue-500 text-white px-3 py-1 rounded-md hover:bg-blue-600 text-sm">
                                                Editar
                                            </button>
                                            <button @click="openDeleteModal(user)"
                                                class="bg-red-500 text-white px-3 py-1 rounded-md hover:bg-red-600 text-sm">
                                                Eliminar
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
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
                <form @submit.prevent="isEditing ? updateUser () : createUser ()">
                    <div class="mb-4">
                        <label class="block text-gray-700">Nombre</label>
                        <input v-model="currentUser .username" type="text" class="w-full border rounded-md px-4 py-2"
                            placeholder="Nombre del usuario" required />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700">Email</label>
                        <input v-model="currentUser .email" type="email" class="w-full border rounded-md px-4 py-2"
                            placeholder="Email del usuario" required />
                    </div>
                    <div class="mb-4" v-if="!isEditing">
                        <label class="block text-gray-700">Contraseña</label>
                        <input v-model="currentUser .password" type="password" class="w-full border rounded-md px-4 py-2"
                            placeholder="Contraseña del usuario" required />
                    </div>
                    <div class="flex justify-end space-x-4">
                        <button type=" button" @click="closeModal"
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

        <!-- Modal de confirmación para eliminar usuario -->
        <div v-if="showDeleteModal"
            class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
                <h3 class="text-lg font-semibold text-red-600 mb-4">Confirmar Eliminación</h3>
                <p class="text-gray-700 mb-6">
                    ¿Estás seguro de que quieres eliminar al usuario
                    <span class="font-semibold">{{ currentUser .username }}</span>? Esta acción no se puede deshacer.
                </p>
                <div class="flex justify-end space-x-4">
                    <button type="button" @click="closeDeleteModal"
                        class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">
                        Cancelar
                    </button>
                    <button @click="confirmDelete" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700">
                        Eliminar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>



<script setup>
import HeaderAdmin from "@/components/NabvarVerticalAdmin.vue";
import { ref } from 'vue'
import axios from 'axios'

// Estado
const users = ref([])
const showModal = ref(false)
const showDeleteModal = ref(false)
const isEditing = ref(false)
const currentUser = ref({ id: null, username: '', email: '', password: '' })

// Métodos
const fetchUsers = async () => {
    try {
        const response = await axios.get('http://localhost:8000/users/admin/', {
            headers: {
                Authorization: `Bearer <ACCESS_TOKEN>`
            }
        })
        users.value = response.data
    } catch (error) {
        console.error('Error fetching users:', error)
    }
}

const openCreateModal = () => {
    currentUser.value = { id: null, username: '', email: '', password: '' }
    isEditing.value = false
    showModal.value = true
}

const openEditModal = (user) => {
    currentUser.value = { ...user, password: '' }
    isEditing.value = true
    showModal.value = true
}

const closeModal = () => {
    showModal.value = false
    currentUser.value = { id: null, username: '', email: '', password: '' }
}

const createUser = async () => {
    try {
        const response = await axios.post('http://localhost:8000/users/admin/', {
            username: currentUser.value.username,
            email: currentUser.value.email,
            password: currentUser.value.password,
            is_staff: true,
            is_superuser: false
        }, {
            headers: {
                Authorization: `Bearer <ACCESS_TOKEN>`
            }
        })
        users.value.push(response.data)
        closeModal()
    } catch (error) {
        console.error('Error creating user:', error)
    }
}

const updateUser = async () => {
    try {
        const response = await axios.put(`http://localhost:8000/users/admin/${currentUser.value.id}/`, {
            username: currentUser.value.username,
            email: currentUser.value.email
        }, {
            headers: {
                Authorization: `Bearer <ACCESS_TOKEN>`
            }
        })
        const index = users.value.findIndex(u => u.id === currentUser.value.id)
        if (index !== -1) {
            users.value[index] = response.data
        }
        closeModal()
    } catch (error) {
        console.error('Error updating user:', error)
    }
}

const openDeleteModal = (user) => {
    currentUser.value = { ...user }
    showDeleteModal.value = true
}

const closeDeleteModal = () => {
    showDeleteModal.value = false
    currentUser.value = { id: null, username: '', email: '', password: '' }
}

const confirmDelete = async () => {
    try {
        await axios.delete(`http://localhost:8000/users/admin/${currentUser.value.id}/`, {
            headers: {
                Authorization: `Bearer <ACCESS_TOKEN>`
            }
        })
        users.value = users.value.filter(u => u.id !== currentUser.value.id)
        closeDeleteModal()
    } catch (error) {
        console.error('Error deleting user:', error)
    }
}


// Fetch users on component mount
fetchUsers()
</script>