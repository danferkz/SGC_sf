<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />

    <section id="dashboard" class="flex-1 py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Pedidos</h3>
        
        <!-- Mantén esta sección solo como un wrapper general -->
        <div class=" bg-gray-100 flex justify-center ">
          <div class="bg-white shadow-md rounded-lg overflow-hidden w-full max-w-7xl">
            <!-- Filtros y búsqueda -->
            <div class="p-4 border-b border-gray-200 flex flex-wrap items-center justify-between gap-4">
              <!-- Filtro por estado -->
              <div class="flex items-center space-x-2">
                <label for="estado" class="text-sm font-medium text-gray-600">Estado:</label>
                <select id="estado" v-model="filtroEstado" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
                  <option value="">Todos</option>
                  <option value="Pendiente">Pendiente</option>
                  <option value="En Proceso">En Proceso</option>
                  <option value="Completado">Completado</option>
                  <option value="Cancelado">Cancelado</option>
                </select>
              </div>

              <!-- Búsqueda de pedidos -->
              <div class="flex-1 max-w-sm">
                <label for="busqueda" class="sr-only">Buscar pedidos</label>
                <div class="relative">
                  <input type="text" id="busqueda" v-model="busqueda" placeholder="Buscar pedidos..." class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md">
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
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cliente</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Producto</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fecha</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Estado</th>
                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="pedido in pedidosFiltrados" :key="pedido.id">
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ pedido.id }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pedido.cliente }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ pedido.producto }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatearFecha(pedido.fecha) }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span :class="[ 'px-2 inline-flex text-xs leading-5 font-semibold rounded-full', estadoClases[pedido.estado] ]">
                        {{ pedido.estado }}
                      </span>
                    </td>
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
              <div class="flex-1 flex justify-between sm:hidden">
                <button @click="paginaAnterior" :disabled="paginaActual === 1" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                  Anterior
                </button>
                <button @click="paginaSiguiente" :disabled="paginaActual === totalPaginas" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                  Siguiente
                </button>
              </div>
              <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
                <p class="text-sm text-gray-700">
                  Mostrando <span class="font-medium">{{ (paginaActual - 1) * pedidosPorPagina + 1 }}</span>
                  a <span class="font-medium">{{ Math.min(paginaActual * pedidosPorPagina, pedidosFiltrados.length) }}</span>
                  de <span class="font-medium">{{ pedidosFiltrados.length }}</span> resultados
                </p>
                <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
                  <button @click="paginaAnterior" :disabled="paginaActual === 1" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                    <ChevronLeftIcon class="h-5 w-5" />
                    <span class="sr-only">Anterior</span>
                  </button>
                  <button @click="paginaSiguiente" :disabled="paginaActual === totalPaginas" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
                    <ChevronRightIcon class="h-5 w-5" />
                    <span class="sr-only">Siguiente</span>
                  </button>
                </nav>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
  </template>
  
  <script setup>
  import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
  import { ref, computed } from 'vue'
  import { SearchIcon, EyeIcon, PencilIcon, TrashIcon, ChevronLeftIcon, ChevronRightIcon } from 'lucide-vue-next'
  
  // Datos de ejemplo (reemplazar con datos reales de la API)
  const pedidos = ref([
    { id: 1, cliente: 'Juan Pérez', producto: 'Ventana', fecha: '2023-05-15', estado: 'pendiente' },
    { id: 2, cliente: 'María García', producto: 'Puerta', fecha: '2023-05-14', estado: 'en_proceso' },
    { id: 3, cliente: 'Carlos López', producto: 'Mesa', fecha: '2023-05-13', estado: 'completado' },
    // más pedidos
  ])
  
  const filtroEstado = ref('')
  const busqueda = ref('')
  const paginaActual = ref(1)
  const pedidosPorPagina = 10
  
  const pedidosFiltrados = computed(() => {
    return pedidos.value
      .filter(pedido => 
        (filtroEstado.value === '' || pedido.estado === filtroEstado.value) &&
        (busqueda.value === '' || 
          pedido.cliente.toLowerCase().includes(busqueda.value.toLowerCase()) ||
          pedido.producto.toLowerCase().includes(busqueda.value.toLowerCase()) ||
          pedido.id.toString().includes(busqueda.value)
        )
      )
      .slice((paginaActual.value - 1) * pedidosPorPagina, paginaActual.value * pedidosPorPagina)
  })
  
  const totalPaginas = computed(() => Math.ceil(pedidos.value.length / pedidosPorPagina))
  
  const estadoClases = {
    pendiente: 'bg-yellow-100 text-yellow-800',
    en_proceso: 'bg-blue-100 text-blue-800',
    completado: 'bg-green-100 text-green-800',
    cancelado: 'bg-red-100 text-red-800'
  }
  
  const formatearFecha = (fecha) => new Date(fecha).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' })
  
  const verDetalles = (pedido) => console.log('Ver detalles del pedido:', pedido)
  const editarPedido = (pedido) => console.log('Editar pedido:', pedido)
  const eliminarPedido = (pedido) => console.log('Eliminar pedido:', pedido)
  
  const paginaAnterior = () => { if (paginaActual.value > 1) paginaActual.value-- }
  const paginaSiguiente = () => { if (paginaActual.value < totalPaginas.value) paginaActual.value++ }
  </script>
  <style scoped>
  /* Contenedor principal */
  .min-h-screen {
    display: flex;
    background-color: #FFFFFF; /* Fondo blanco para el contenedor principal */
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
  </style>