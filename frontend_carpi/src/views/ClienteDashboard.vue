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
                <tr v-for="cliente in clientesFiltrados" :key="cliente.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.nombre }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.email }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.telefono }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ cliente.direccion }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <button
                      @click="editarCliente(cliente)"
                      class="text-indigo-600 hover:text-indigo-900 mr-2"
                    >
                      <PencilIcon class="h-5 w-5" />
                    </button>
                    <button
                      @click="eliminarCliente(cliente)"
                      class="text-red-600 hover:text-red-900"
                    >
                      <TrashIcon class="h-5 w-5" />
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Nuevo Control de Paginación -->
          <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
            <div class="flex justify-center pb-4 space-x-2">
              <button
                @click="paginaAnterior"
                :disabled="!previousPage"
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path
                    fill-rule="evenodd"
                    d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
              <button
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                Página {{ currentPage }}
              </button>
              <button
                @click="siguientePagina"
                :disabled="!nextPage"
                class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                  <path
                    fill-rule="evenodd"
                    d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
import { ref, computed } from 'vue'
import { SearchIcon, PlusIcon, PencilIcon, TrashIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'

// Datos de ejemplo (reemplazar con datos reales de la API)
const clientes = ref([
  { id: 1, nombre: 'Juan Pérez', email: 'juan@example.com', telefono: '123456789', direccion: 'Calle 123, Ciudad' },
  { id: 2, nombre: 'María García', email: 'maria@example.com', telefono: '987654321', direccion: 'Avenida 456, Ciudad' },
  { id: 3, nombre: 'Carlos López', email: 'carlos@example.com', telefono: '456789123', direccion: 'Plaza 789, Ciudad' },
  // ... más clientes
])

const busqueda = ref('')
const paginaActual = ref(1)
const clientesPorPagina = 10

const clientesFiltrados = computed(() => {
  return clientes.value
    .filter(cliente =>
      cliente.nombre.toLowerCase().includes(busqueda.value.toLowerCase()) ||
      cliente.email.toLowerCase().includes(busqueda.value.toLowerCase()) ||
      cliente.telefono.includes(busqueda.value)
    )
})

const totalPaginas = computed(() => Math.ceil(clientesFiltrados.value.length / clientesPorPagina))

const paginaAnterior = () => {
  if (paginaActual.value > 1) {
    paginaActual.value--
  }
}

const paginaSiguiente = () => {
  if (paginaActual.value < totalPaginas.value) {
    paginaActual.value++
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
  if (confirm(`¿Estás seguro de que quieres eliminar a ${cliente.nombre}?`)) {
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

