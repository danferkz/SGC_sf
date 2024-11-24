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
          <button @click="abrirModalAgregar"
                  class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none">
            Agregar Cliente
          </button>
        </div>

        <div class="bg-white shadow-md rounded-lg overflow-hidden">
          <!-- Tabla de clientes -->
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Nombre
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Email
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Teléfono
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Dirección
                  </th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Acciones
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="cliente in clientes" :key="cliente.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.username }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.email }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.phone }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.address }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <button
                      @click="editarCliente(cliente)"
                      class="text-indigo-600 hover:text-indigo-900 mr-2"
                    >
                      <PencilIcon class="h-5 w-5" />
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Control de Paginación -->
          <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
            <div class="flex justify-center pb-4 space-x-2">
              <button
                @click="paginaAnterior"
                :disabled="!previousPage"
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Anterior
              </button>
              <button
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Página {{ paginaActual }}
              </button>
              <button
                @click="paginaSiguiente"
                :disabled="!nextPage"
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Siguiente
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para agregar/editar cliente -->
    <div v-if="mostrarModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-xl">
        <h2 class="text-xl font-bold mb-4">{{ clienteEditando ? 'Editar Cliente' : 'Agregar Cliente' }}</h2>
        <form @submit.prevent="guardarCliente">
          <div class="space-y-4">
            <input v-model="clienteForm.nombre" placeholder="Nombre" class="w-full p-2 border rounded">
            <input v-model="clienteForm.email" placeholder="Email" class="w-full p-2 border rounded">
            <input v-model="clienteForm.telefono" placeholder="Teléfono" class="w-full p-2 border rounded">
            <input v-model="clienteForm.direccion" placeholder="Dirección" class="w-full p-2 border rounded">
          </div>
          <div class="flex justify-end space-x-2 mt-4">
            <button type="button" @click="cerrarModal" class="px-4 py-2 border rounded">Cancelar</button>
            <button type="submit" class="px-4 py-2 bg-indigo-600 text-white rounded">Guardar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { PencilIcon, TrashIcon } from 'lucide-vue-next'

// Estado de los clientes y la paginación
const clientes = ref([])
const paginaActual = ref(1)
const totalPaginas = ref(0)
const nextPage = ref(null)
const previousPage = ref(null)

// Función para obtener los clientes de la API
const obtenerClientes = async (pagina = 1) => {
  const token = localStorage.getItem('token') // Obtener el token del localStorage
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/users/clients/?page=${pagina}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    clientes.value = response.data.results
    totalPaginas.value = Math.ceil(response.data.count / 10) // Suponiendo 10 clientes por página
    nextPage.value = response.data.next
    previousPage.value = response.data.previous
  } catch (error) {
    console.error('Error al obtener los clientes:', error)
  }
}

// Llamar a la función al montar el componente
onMounted(() => {
  obtenerClientes(paginaActual.value)
})

// Funciones de paginación
const paginaAnterior = () => {
  if (previousPage.value) {
    paginaActual.value--
    obtenerClientes(paginaActual.value)
  }
}

const paginaSiguiente = () => {
  if (nextPage.value) {
    paginaActual.value++
    obtenerClientes(paginaActual.value)
  }
}

const mostrarModal = ref(false)
const clienteEditando = ref(null)
const clienteForm = ref({
  nombre: '',
  email: '',
  telefono: '',
  direccion: ''
})

const abrirModalAgregar = () => {
  clienteEditando.value = null
  clienteForm.value = {
    nombre: '',
    email: '',
    telefono: '',
    direccion: ''
  }
  mostrarModal.value = true
}

const editarCliente = (cliente) => {
  clienteEditando.value = cliente
  clienteForm.value = { ...cliente }
  mostrarModal.value = true
}

const eliminarCliente = (cliente) => {
  if (confirm(`¿Estás seguro de que quieres eliminar a ${cliente.username}?`)) {
    clientes.value = clientes.value.filter(c => c.id !== cliente.id)
  }
}

const cerrarModal = () => {
  mostrarModal.value = false
  clienteEditando.value = null
  clienteForm.value = {
    nombre: '',
    email: '',
    telefono: '',
    direccion: ''
  }
}

const guardarCliente = () => {
  if (clienteEditando.value) {
    // Actualizar cliente existente
    const index = clientes.value.findIndex(c => c.id === clienteEditando.value.id)
    clientes.value[index] = { ...clienteEditando.value, ...clienteForm.value }
  } else {
    // Agregar nuevo cliente
    const nuevoId = Math.max(...clientes.value.map(c => c.id)) + 1
    clientes.value.push({ id: nuevoId, ...clienteForm.value })
  }
  cerrarModal()
}
</script>