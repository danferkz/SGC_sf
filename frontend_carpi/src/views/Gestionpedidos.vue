<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />

    <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
      <div class="max-w-7xl mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Pedidos</h3>

        <!-- Wrapper general -->
        <div class="bg-gray-100 flex justify-center">
          <div class="bg-white shadow-md rounded-lg overflow-hidden w-full max-w-7xl">
            <!-- Filtros y búsqueda -->
            <div class="p-4 border-b border-gray-40 flex flex-wrap items-center justify-between gap-4">
              <!-- Filtro por estado -->
              <div class="flex items-center space-x-2">
                <label for="estado" class="text-sm font-medium text-gray-600">Estado:</label>
                <select
                  id="estado"
                  v-model="filtroEstado"
                  class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                >
                  <option value="">Todos</option>
                  <option value="pending">Pendiente</option>
                  <option value="in_progress">En Progreso</option>
                  <option value="completed">Completado</option>
                  <option value="delivered">Entregado</option>
                  <option value="cancelled">Cancelado</option>
                </select>
              </div>

              <!-- Búsqueda -->
              <div class="flex-1 max-w-sm">
                <label for="busqueda" class="sr-only">Buscar pedidos</label>
                <div class="relative">
                  <input
                    type="text"
                    id="busqueda"
                    v-model="busqueda"
                    placeholder="Buscar pedidos..."
                    class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md"
                  />
                  <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    <SearchIcon class="h-5 w-5 text-gray-400" />
                  </div>
                </div>
              </div>
            </div>

            <!-- Tabla de pedidos -->
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                  <tr>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order ID</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Username</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Promised Date</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Total Price</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="pedido in pedidosFiltrados" :key="pedido.orders_id">
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ pedido.orders_id }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pedido.client_detail?.username || 'N/A' }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        :class="[ 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full', estadoClases[pedido.status] || ' bg-gray-100 text-gray-800' ]"
                      >
                        {{ pedido.status }}
                      </span>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatearFecha(pedido.promised_date) }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pedido.total_price }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium flex space-x-2">
                      <button @click="verDetalles(pedido)" class="text-indigo-600 hover:text-indigo-900">
                        <EyeIcon class="h-5 w-5" />
                      </button>
                      <button @click="editarPedido(pedido)" class="text-yellow-600 hover:text-yellow-900">
                        <PencilIcon class="h-5 w-5" />
                      </button>
                      <button @click="eliminarPedido(pedido)" class="text-red-600 hover:text-red-900">
                        <TrashIcon class="h-5 w-5" />
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Paginación -->
            <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
              <div class="flex justify-center pb-4 space-x-2">
                <button
                  @click="paginaAnterior"
                  :disabled="!prevPageUrl"
                  class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  <ChevronLeftIcon class="h-5 w-5" />
                </button>
                <button
                  class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  Página {{ paginaActual }}
                </button>
                <button
                  @click="paginaSiguiente"
                  :disabled="!nextPageUrl"
                  class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
                >
                  <ChevronRightIcon class="h-5 w-5" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Detalles del Pedido -->
    <div v-if="isOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg w-full max-w-3xl">
        <div class="p-4 border-b border-gray-200 flex justify-between items-center">
          <h3 class="text-lg font-semibold">Detalles del Pedido #{{ selectedPedido?.orders_id }}</h3>
          <button @click="isOpen = false" class="text-gray-500 hover:text-gray-700">
            <XIcon class="h-5 w-5" />
          </button>
        </div>
        
        <div class="p-4">
          <div v-if="loading" class="flex justify-center items-center py-8">
            <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
          </div>

          <div v-else>
            <!-- Información de Entrega -->
            <div class="mb-6 bg-gray-50 p-4 rounded-lg">
              <h4 class="font-medium mb-3 text-indigo-600">Información de Entrega</h4>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <p class="text-sm text-gray-600">Fecha de Entrega</p>
                  <p class="font-medium">{{ formatearFecha(orderDetails?.delivery_date) }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Opción de Entrega</p>
                  <p class="font-medium">{{ orderDetails?.delivery_option ? 'Sí' : 'No' }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Costo Adicional</p>
                  <p class="font-medium">${{ orderDetails?.additional_cost }}</p>
                </div>
                <div v-if="orderDetails?.delivery_notes">
                  <p class="text-sm text-gray-600">Notas de Entrega</p>
                  <p class="font-medium">{{ orderDetails?.delivery_notes || 'Sin notas' }}</p>
                </div>
              </div>
            </div>

            <!-- Detalles del Producto - Puerta/Ventana -->
            <div v-if="orderDetails?.door_window_detail" class="mb-6 bg-blue-50 p-4 rounded-lg">
              <h4 class="font-medium mb-3 text-blue-600">
                Detalles de {{ orderDetails.door_window_detail.product_type === 'door' ? 'Puerta' : 'Ventana' }}
              </h4>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <p class="text-sm text-gray-600">ID del Producto</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.product_id }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Tipo de Madera</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.wood_type }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Precio de Costo</p>
                  <p class="font-medium">${{ orderDetails.door_window_detail.cost_price }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Barnizado</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.is_varnished ? 'Sí' : 'No' }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Dimensiones</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.length }}cm x {{ orderDetails.door_window_detail.width }}cm</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Uso Exterior</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.is_exterior ? 'Sí' : 'No' }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Número de Hojas</p>
                  <p class="font-medium">{{ orderDetails.door_window_detail.number_of_sheets }}</p>
                </div>
              </div>
            </div>

            <!-- Detalles del Producto - Mueble -->
            <div v-if="orderDetails?.furniture_detail" class="mb-6 bg-green-50 p-4 rounded-lg">
              <h4 class="font-medium mb-3 text-green-600">Detalles del Mueble</h4>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <p class="text-sm text-gray-600">ID del Producto</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.product_id }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Nombre de la Pieza</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.piece_name }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Tipo de Madera</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.wood_type }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Precio de Costo</p>
                  <p class="font-medium">${{ orderDetails.furniture_detail.cost_price }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Barnizado</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.is_varnished ? 'Sí' : 'No' }}</p>
                </div>
                <div>
                  <p class="text-sm text-gray-600">Peso</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.weight }}kg</p>
                </div>
                <div v-if="orderDetails.furniture_detail.is_part_of_set">
                  <p class="text-sm text-gray-600">Set</p>
                  <p class="font-medium">{{ orderDetails.furniture_detail.set_name }}</p>
                </div>
              </div>
            </div>

            <!-- Estado del Pedido -->
            <div class="bg-gray-50 p-4 rounded-lg">
              <div class="flex justify-between items-center">
                <div>
                  <p class="text-sm text-gray-600">Estado del Pedido</p>
                  <span :class="['px-2 py-1 text-xs font-semibold rounded-full mt-1 inline-block', estadoClases[selectedPedido?.status]]">
                    {{ selectedPedido?.status }}
                  </span>
                </ div>
                <button
                  @click="isOpen = false"
                  class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300"
                >
                  Cerrar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Actualización de Estado -->
    <div v-if="isStatusModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg w-full max-w-md p-6">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-semibold">Actualizar Estado del Pedido #{{ selectedPedido?.orders_id }}</h3>
          <button @click="isStatusModalOpen = false" class="text-gray-500 hover:text-gray-700">
            <XIcon class="h-5 w-5" />
          </button>
        </div>

        <div class="mb-4">
          <label for="newStatus" class="block text-sm font-medium text-gray-700 mb-2">
            Nuevo Estado
          </label>
          <select
            id="newStatus"
            v-model="newStatus"
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
          >
            <option value="pending">Pendiente</option>
            <option value="in_progress">En Progreso</option>
            <option value="completed">Completado</option>
            <option value="delivered">Entregado</option>
            <option value="cancelled">Cancelado</option>
          </select>
        </div>

        <div class="flex justify-end space-x-3">
          <button
            @click="isStatusModalOpen = false"
            class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300"
          >
            Cancelar
          </button>
          <button
            @click="actualizarEstado"
            :disabled="statusUpdating"
            class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 disabled:opacity-50"
          >
            {{ statusUpdating ? 'Actualizando...' : 'Actualizar Estado' }}
          </button>
        </div>

        <!-- Mensaje de éxito o error -->
        <div v-if="statusMessage" :class="[
          'mt-3 p-2 rounded text-sm',
          statusSuccess ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
        ]">
          {{ statusMessage }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
import { ref, computed, onMounted, watch } from 'vue'
import axios from 'axios'
import { SearchIcon, EyeIcon, PencilIcon, TrashIcon, ChevronLeftIcon, ChevronRightIcon, XIcon } from 'lucide-vue-next'

const pedidos = ref([])
const filtroEstado = ref('')
const busqueda = ref('')
const paginaActual = ref(1)
const nextPageUrl = ref(null)
const prevPageUrl = ref(null)
const isOpen = ref(false)
const selectedPedido = ref(null)
const loading = ref(false)
const orderDetails = ref(null)
const isStatusModalOpen = ref(false)
const newStatus = ref('')
const statusUpdating = ref(false)
const statusMessage = ref('')
const statusSuccess = ref(false)

// Función para cargar pedidos desde la API
const cargarPedidos = async (url = 'http://localhost:8000/api/orders/orders-list-admin/') => {
  try {
    const token = localStorage.getItem('token')
    const response = await axios.get(url, {
      headers: { Authorization: `Bearer ${token}` }
    })
    pedidos.value = response.data.results
    nextPageUrl.value = response.data.next
    prevPageUrl.value = response.data.previous
    paginaActual.value = new URL(url).searchParams.get('page') || 1
  } catch (error) {
    console.error('Error al cargar pedidos:', error)
  }
}

// Computed para los pedidos filtrados
const pedidosFiltrados = computed(() => {
  return pedidos.value.filter(pedido => {
    return (
      (filtroEstado.value === '' || pedido.status === filtroEstado.value) &&
      (busqueda.value === '' ||
        pedido.client_detail?.username.toLowerCase().includes(busqueda.value.toLowerCase()) ||
        pedido.orders_id.includes(busqueda.value))
    )
  })
})

const estadoClases = {
  pending: 'bg-yellow-100 text-yellow-800',
  in_progress: 'bg-blue-100 text-blue-800',
  completed: 'bg-green-100 text-green-800',
  delivered: 'bg-purple-100 text-purple-800',
  cancelled: 'bg-red-100 text-red-800'
}

// Función para ir a la siguiente página
const paginaSiguiente = () => {
  if (nextPageUrl.value) {
    cargarPedidos(nextPageUrl.value)
  }
}

// Función para ir a la página anterior
const paginaAnterior = () => {
  if (prevPageUrl.value) {
    cargarPedidos(prevPageUrl.value)
  }
}

const formatearFecha = fecha => {
  if (!fecha) return 'No disponible'
  const opciones = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(fecha).toLocaleDateString('es-ES', opciones)
}

// Funciones para ver, editar y eliminar pedidos
const verDetalles = async (pedido) => {
  selectedPedido.value = pedido
  isOpen.value = true
  if (pedido.delivery_detail?.delivery_id) {
    await fetchOrderDetails(pedido.delivery_detail.delivery_id)
  } else {
    orderDetails.value = null
  }
}

// Función para cargar detalles de la orden usando el delivery_id
const fetchOrderDetails = async (deliveryId) => {
  loading.value = true
  try {
    const token = localStorage.getItem('token')
    const response = await axios.get(
      `http://localhost:8000/api/deliveries/deliveries-detail/${deliveryId}/`,
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )
    orderDetails.value = response.data
  } catch (error) {
    console.error('Error al cargar los detalles de la entrega:', error)
    orderDetails.value = null
  } finally {
    loading.value = false
  }
}

const editarPedido = (pedido) => {
  selectedPedido.value = pedido
  newStatus.value = pedido.status
  isStatusModalOpen.value = true
}

const actualizarEstado = async () => {
  if (!selectedPedido.value || !newStatus.value) return

  statusUpdating.value = true
  statusMessage.value = ''
  
  try {
    const token = localStorage.getItem('token')
    await axios.patch(
      `http://localhost:8000/api/orders/orders-update/${selectedPedido.value.orders_id}/update-status/`,
      { status: newStatus.value },
      {
        headers: { Authorization: `Bearer ${token}` }
      }
    )

    // Actualizar el estado en la lista local
    const pedidoIndex = pedidos.value.findIndex(p => p.orders_id === selectedPedido.value.orders_id)
    if (pedidoIndex !== -1) {
      pedidos.value[pedidoIndex].status = newStatus.value
    }

    statusSuccess.value = true
    statusMessage.value = 'Estado actualizado correctamente'
    
    // Cerrar el modal después de un breve delay
    setTimeout(() => {
      isStatusModalOpen.value = false
      statusMessage.value = ''
    }, 1500)
    
  } catch (error) {
    console.error('Error al actualizar el estado:', error)
    statusSuccess.value = false
    statusMessage.value = 'Error al actualizar el estado. Por favor, intente nuevamente.'
  } finally {
    statusUpdating.value = false
  }
}

// Limpiar los detalles cuando se cierra el modal
watch(isOpen, (newValue) => {
  if (!newValue) {
    orderDetails.value = null
    selectedPedido.value = null
  }
})

watch(isStatusModalOpen, (newValue) => {
  if (!newValue) {
    statusMessage.value = ''
    statusSuccess.value = false
    if (!isOpen.value) { // Only clear if details modal is also closed
      selectedPedido.value = null
    }
  }
})

onMounted(() => {
  cargarPedidos()
})
</script>