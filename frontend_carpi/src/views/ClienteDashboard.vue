<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 flex">
      <!-- Header -->
      <HeaderAdmin class="header-admin" />
      <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <div class="flex justify-between items-center mb-12">
          <h1 class="text-3xl font-bold text-gray-900">Gestión de Clientes</h1>
        </div>
        <div class="bg-white shadow-md rounded-lg overflow-hidden">
          <!-- Búsqueda y filtros -->
          <button @click="abrirModalAgregar" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <PlusIcon class="h-5 w-5 inline-block mr-1" />
            Agregar Cliente
          </button>
          <div class="p-4 border-b border-gray-200">
            <div class="flex flex-wrap items-center justify-between gap-4">
              <div class="flex-1 min-w-0 max-w-xs">
                <label for="busqueda" class="sr-only">Buscar clientes</label>
                <div class="relative rounded-md shadow-sm">
                  <input type="text" id="busqueda" v-model="busqueda" placeholder="Buscar clientes..." class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md">
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <SearchIcon class="h-5 w-5 text-gray-400" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Tabla de clientes -->
          <div class="overflow-auto">

  <table class="min-w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
      <tr>
        <!-- Centramos el texto de las cabeceras -->
        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Teléfono</th>
        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Dirección</th>
        <th scope="col" class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
      </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
      <tr v-for="cliente in clientesFiltrados" :key="cliente.id">
        <td class="px-6 py-4 text-center whitespace-nowrap text-sm font-medium text-gray-900">{{ cliente.nombre }}</td>
        <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-500">{{ cliente.email }}</td>
        <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-500">{{ cliente.telefono }}</td>
        <td class="px-6 py-4 text-center whitespace-nowrap text-sm text-gray-500">{{ cliente.direccion }}</td>
        <td class="px-6 py-4 text-center whitespace-nowrap text-sm font-medium">
          <button @click="editarCliente(cliente)" class="text-indigo-600 hover:text-indigo-900 mr-2">
            <PencilIcon class="h-5 w-5" />
          </button>
          <button @click="eliminarCliente(cliente)" class="text-red-600 hover:text-red-900">
            <TrashIcon class="h-5 w-5" />
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</div>

          <!-- Paginación -->
          <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
            <div class="flex justify-center sm:hidden">

              <button @click="paginaAnterior" :disabled="paginaActual === 1" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                Anterior
              </button>
              <button @click="paginaSiguiente" :disabled="paginaActual === totalPaginas" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                Siguiente
              </button>
            </div>
            <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
              <div>
                <p class="text-sm text-gray-700">
                  Mostrando <span class="font-medium">{{ (paginaActual - 1) * clientesPorPagina + 1 }}</span> a <span class="font-medium">{{ Math.min(paginaActual * clientesPorPagina, clientesFiltrados.length) }}</span> de <span class="font-medium">{{ clientesFiltrados.length }}</span> resultados
                </p>
              </div>
              <div>
                <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                  <button @click="paginaAnterior" :disabled="paginaActual === 1" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                    <span class="sr-only">Anterior</span>
                    <ChevronLeftIcon class="h-5 w-5" />
                  </button>
                  <button @click="paginaSiguiente" :disabled="paginaActual === totalPaginas" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                    <span class="sr-only">Siguiente</span>
                    <ChevronRightIcon class="h-5 w-5" />
                  </button>
                </nav>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal para agregar/editar cliente -->
      <div v-if="mostrarModal" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
        <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
          <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
            <form @submit.prevent="guardarCliente">
              <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                    <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                      {{ clienteEditando ? 'Editar Cliente' : 'Agregar Cliente' }}
                    </h3>
                    <div class="mt-2 space-y-4">
                      <div>
                        <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
                        <input type="text" id="nombre" v-model="clienteForm.nombre" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                      </div>
                      <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                        <input type="email" id="email" v-model="clienteForm.email" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                      </div>
                      <div>
                        <label for="telefono" class="block text-sm font-medium text-gray-700">Teléfono</label>
                        <input type="tel" id="telefono" v-model="clienteForm.telefono" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                      </div>
                      <div>
                        <label for="direccion" class="block text-sm font-medium text-gray-700">Dirección</label>
                        <input type="text" id="direccion" v-model="clienteForm.direccion" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                <button type="submit" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm">
                  Guardar
                </button>
                <button @click="cerrarModal" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                  Cancelar
                </button>
              </div>
            </form>
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
 <style scoped>
 /* Contenedor principal */
 .min-h-screen {
  display: flex;
  flex-direction: row;
  background-color: #FFFFFF;
}
#dashboard {
  flex-grow: 1;
  padding: 20px;
}

 /* Estilos del header admin */
 .header-admin {
   width: 250px;
   background-color: #FFFFFF;
   box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
   height: 100vh; /* Asegura que el header ocupe toda la altura */
 }
 /* Sección del dashboard */
 #dashboard {
   padding: 20px;
   background-color: #FFFFFF;
   flex: 1;
   margin-left: 120px; /* Se agrega separación de 120px entre el header y el contenido */
 }
 /* Contenedor de imagen */
 .image-container {
   width: 100%;
   display: flex;
   justify-content: center;
   align-items: center;
   border-radius: 0.5rem;
   overflow: hidden;
   height: 150px; /* Altura fija para las imágenes */
 }
 /* Imagen del dashboard */
 .dashboard-image {
   max-width: 100%;
   max-height: 100%;
   height: auto;
   width: auto;
   border-radius: 0.5rem;
 }
 /* Alineación del contenido */
 .container {
   padding: 20px;
 }
 /* Estilos de las tarjetas */
 .card {
   background-color: #FFFBEB;
   padding: 1.5rem;
   border-radius: 0.5rem;
   box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
   text-align: center;
   transition: background-color 0.3s;
 }
 .card:hover {
   background-color: #FFECB3;
 }
 /* Ajustes de la tabla */
.table-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.min-w-full {
  text-align: center; /* Centra el texto dentro de la tabla */
}

.px-6 {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.py-4 {
  padding-top: 1rem;
  padding-bottom: 1rem;
}
 </style>
 