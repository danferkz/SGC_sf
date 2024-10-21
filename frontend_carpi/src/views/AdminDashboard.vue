<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />
    <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto">
        <div class="flex justify-between items-center mb-6">
          <h1 class="text-3xl font-bold text-gray-900">Gestión de Administradores</h1>
          <button @click="abrirModalAgregar" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <PlusIcon class="h-5 w-5 inline-block mr-1" />
            Agregar Administrador
          </button>
        </div>
        
        <div class="bg-white shadow-md rounded-lg overflow-hidden">
          <!-- Búsqueda y filtros -->
          <div class="p-4 border-b border-gray-200">
            <div class="flex flex-wrap items-center justify-between gap-4">
              <div class="flex-1 min-w-0 max-w-xs">
                <label for="busqueda" class="sr-only">Buscar administradores</label>
                <div class="relative rounded-md shadow-sm">
                  <input type="text" id="busqueda" v-model="busqueda" placeholder="Buscar administradores..." class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md">
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <SearchIcon class="h-5 w-5 text-gray-400" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Tabla de administradores -->
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Nombre</th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Rol</th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Último Acceso</th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="admin in administradoresFiltrados" :key="admin.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ admin.nombre }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ admin.email }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ admin.rol }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatearFecha(admin.ultimoAcceso) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                    <button @click="editarAdministrador(admin)" class="text-indigo-600 hover:text-indigo-900 mr-2">
                      <PencilIcon class="h-5 w-5" />
                    </button>
                    <button @click="eliminarAdministrador(admin)" class="text-red-600 hover:text-red-900">
                      <TrashIcon class="h-5 w-5" />
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Paginación -->
          <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
            <div class="flex-1 flex justify-between sm:hidden">
              <button @click="paginaAnterior" :disabled="paginaActual === 1" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font -medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                Anterior
              </button>
              <button @click="paginaSiguiente" :disabled="paginaActual === totalPaginas" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                Siguiente
              </button>
            </div>
            <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
              <div>
                <p class="text-sm text-gray-700">
                  Mostrando <span class="font-medium">{{ (paginaActual - 1) * adminsPorPagina + 1 }}</span> a <span class="font-medium">{{ Math.min(paginaActual * adminsPorPagina, administradoresFiltrados.length) }}</span> de <span class="font-medium">{{ administradoresFiltrados.length }}</span> resultados
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

        <!-- Modal para agregar/editar administrador -->
        <div v-if="mostrarModal" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
          <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
            <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
            <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
            <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
              <form @submit.prevent="guardarAdministrador">
                <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                      <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                        {{ adminEditando ? 'Editar Administrador' : 'Agregar Administrador' }}
                      </h3>
                      <div class="mt-2 space-y-4">
                        <div>
                          <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
                          <input type="text" id="nombre" v-model="adminForm.nombre" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                        </div>
                        <div>
                          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                          <input type="email" id="email" v-model="adminForm.email" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                        </div>
                        <div>
                          <label for="rol" class="block text-sm font-medium text-gray-700">Rol</label>
                          <select id="rol" v-model="adminForm.rol" required class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
                            <option value="admin">Administrador</option>
                            <option value=" superadmin">Super Administrador</option>
                          </select>
                        </div>
                        <div v-if="!adminEditando">
                          <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
                          <input type="password" id="password" v-model="adminForm.password" required class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
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
  </div>
</template>

<script setup>
import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
import { ref, computed } from 'vue'
import { SearchIcon, PlusIcon, PencilIcon, TrashIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'

const administradores = ref([
{ id: 1, nombre: 'Juan Pérez', email: 'juan@example.com', telefono: '123456789', direccion: 'Calle 123, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-01 12:00:00' },
{ id: 2, nombre: 'María García', email: 'maria@example.com', telefono: '987654321', direccion: 'Avenida 456, Ciudad', rol: 'superadmin', ultimoAcceso: '2022-01-02 13:00:00' },
{ id: 3, nombre: 'Carlos López', email: 'carlos@example.com', telefono: '456789123', direccion: 'Plaza 789, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-03 14:00:00' },
{ id: 4, nombre: 'Ana Torres', email: 'ana@example.com', telefono: '321654987', direccion: 'Calle Falsa 123, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-04 15:00:00' },
{ id: 5, nombre: 'Luis Martínez', email: 'luis@example.com', telefono: '654321987', direccion: 'Avenida Siempre Viva 456, Ciudad', rol: 'superadmin', ultimoAcceso: '2022-01-05 16:00:00' },
{ id: 6, nombre: 'Sofía Ramírez', email: 'sofia@example.com', telefono: '789456123', direccion: 'Calle de la Amargura 789, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-06 17:00:00' },
{ id: 7, nombre: 'Javier Gómez', email: 'javier@example.com', telefono: '147258369', direccion: 'Calle del Sol 101, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-07 18:00:00' },
{ id: 8, nombre: 'Lucía Fernández', email: 'lucia@example.com', telefono: '258963147', direccion: 'Avenida del Mar 202, Ciudad', rol: 'superadmin', ultimoAcceso: '2022-01-08 19:00:00' },
{ id: 9, nombre: 'Diego Castillo', email: 'diego@example.com', telefono: '369258147', direccion: 'Calle de la Luna 303, Ciudad', rol: 'admin', ultimoAcceso: '2022-01 -09 20:00:00' },
{ id: 10, nombre: 'Paola Herrera', email: 'paola@example.com', telefono: '147852369', direccion: 'Calle de los Sueños 404, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-10 21:00:00' },
{ id: 11, nombre: 'Fernando Ruiz', email: 'fernando@example.com', telefono: '258147369', direccion: 'Avenida de los Árboles 505, Ciudad', rol: 'superadmin', ultimoAcceso: '2022-01-11 22:00:00' },
{ id: 12, nombre: 'Claudia Morales', email: 'claudia@example.com', telefono: '369147258', direccion: 'Calle de las Flores 606, Ciudad', rol: 'admin', ultimoAcceso: '2022-01-12 23:00:00' },
// ... más administradores si es necesario
])

const busqueda = ref('')
const paginaActual = ref(1)
const adminsPorPagina = 5

const administradoresFiltrados = computed(() => {
return administradores.value
  .filter(admin => 
    admin.nombre.toLowerCase().includes(busqueda.value.toLowerCase()) ||
    admin.email.toLowerCase().includes(busqueda.value.toLowerCase()) ||
    admin.telefono.includes(busqueda.value)
  )
  .slice((paginaActual.value - 1) * adminsPorPagina, paginaActual.value * adminsPorPagina)
})

const totalPaginas = computed(() => Math.ceil(administradoresFiltrados.value.length / adminsPorPagina))

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
const adminEditando = ref(null)
const adminForm = ref({
nombre: '',
email: '',
telefono: '',
direccion: '',
rol: '',
password: ''
})

const abrirModalAgregar = () => {
adminEditando.value = null
adminForm.value = {
  nombre: '',
  email: '',
  telefono: '',
  direccion: '',
  rol: '',
  password: ''
}
mostrarModal.value = true
}

const editarAdministrador = (admin) => {
adminEditando.value = admin
adminForm.value = { ...admin }
mostrarModal.value = true
}

const eliminarAdministrador = (admin) => {
if (confirm(`¿Estás seguro de que quieres eliminar a ${admin.nombre}?`)) {
  administradores.value = administradores.value.filter(a => a.id !== admin.id)
}
}



const cerrarModal = () => {
mostrarModal.value = false
}

const guardarAdministrador = () => {
if (adminEditando.value) {
  // Actualizar administrador existente
  const index = administradores.value.findIndex(a => a.id === adminEditando.value.id)
  administradores.value[index] = { ...adminEditando.value, ...adminForm.value }
} else {
  // Agregar nuevo administrador
  const nuevoId = Math.max(...administradores.value.map(a => a.id)) + 1
  administradores.value.push({ id: nuevoId, ...adminForm.value })
}
cerrarModal()
}
</script>