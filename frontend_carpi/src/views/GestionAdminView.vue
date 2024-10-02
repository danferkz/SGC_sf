<template>
    <div class="min-h-screen bg-base-200 p-8">
        <div class="max-w-6xl mx-auto bg-base-100 rounded-box shadow-xl p-6">
            <h1 class="text-4xl font-bold text-primary mb-8 text-center">Panel de Administración de Usuarios</h1>

            <!-- Botón para agregar usuario -->
            <button @click="openCreateModal" class="btn btn-primary mb-6">
                Agregar Usuario
            </button>

            <!-- Tabla de usuarios -->
            <div class="overflow-x-auto">
                <table class="table w-full">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre</th>
                            <th>Email</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="user in users" :key="user.id">
                            <td>{{ user.id }}</td>
                            <td>{{ user.username }}</td>
                            <td>{{ user.email }}</td>
                            <td>
                                <div class="btn-group">
                                    <button @click="openEditModal(user)" class="btn btn-sm btn-info">Editar</button>
                                    <button @click="openDeleteModal(user)" class="btn btn-sm btn-error">Eliminar</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Modal para crear/editar usuario -->
            <input type="checkbox" id="modal-crud" class="modal-toggle" v-model="showModal" />
            <div class="modal">
                <div class="modal-box">
                    <h3 class="font-bold text-lg mb-4">{{ isEditing ? 'Editar Usuario' : 'Crear Usuario' }}</h3>
                    <form @submit.prevent="isEditing ? updateUser() : createUser()">
                        <div class="form-control">
                            <label class="label" for="username">
                                <span class="label-text">Nombre</span>
                            </label>
                            <input v-model="currentUser.username" id="username" type="text" placeholder="Nombre del usuario"
                                class="input input-bordered w-full" required />
                        </div>
                        <div class="form-control mt-4">
                            <label class="label" for="email">
                                <span class="label-text">Email</span>
                            </label>
                            <input v-model="currentUser.email" id="email" type="email" placeholder="Email del usuario"
                                class="input input-bordered w-full" required />
                        </div>
                        <div class="form-control mt-4" v-if="!isEditing">
                            <label class="label" for="password">
                                <span class="label-text">Contraseña</span>
                            </label>
                            <input v-model="currentUser.password" id="password" type="password" placeholder="Contraseña del usuario"
                                class="input input-bordered w-full" required />
                        </div>
                        <div class="modal-action">
                            <button type="button" @click="closeModal" class="btn btn-ghost">Cancelar</button>
                            <button type="submit" class="btn btn-primary">{{ isEditing ? 'Actualizar' : 'Crear' }}</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Modal de confirmación para eliminar usuario -->
            <input type="checkbox" id="modal-delete" class="modal-toggle" v-model="showDeleteModal" />
            <div class="modal">
                <div class="modal-box">
                    <h3 class="font-bold text-lg text-error mb-4">Confirmar Eliminación</h3>
                    <p>¿Estás seguro de que quieres eliminar al usuario "{{ currentUser.username }}"? Esta acción no se
                        puede deshacer.</p>
                    <div class="modal-action">
                        <button @click="closeDeleteModal" class="btn btn-ghost">Cancelar</button>
                        <button @click="confirmDelete" class="btn btn-error">Eliminar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
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