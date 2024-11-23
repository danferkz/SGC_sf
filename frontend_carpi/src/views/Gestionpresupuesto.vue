<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
      <!-- Header -->
      <HeaderAdmin class="header-admin" />

      <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
          <div class="max-w-7xl mx-auto">
              <h3 class="text-3xl font-bold text-center mb-12">Presupuesto de Compras</h3>

              <div class="bg-white shadow-md rounded-lg overflow-hidden">
                  <!-- Filtros -->
                  <div class="p-4 border-b border-gray-200 flex flex-wrap items-center justify-between gap-4">
                      <div class="flex items-center space-x-4">
                          <div>
                              <label for="fechaInicio" class="block text-sm font-medium text-gray-700">Fecha Inicio:</label>
                              <input type="date" id="fechaInicio" v-model="filtros.fechaInicio" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                          </div>
                          <div>
                              <label for="fechaFin" class="block text-sm font-medium text-gray-700">Fecha Fin:</label>
                              <input type="date" id="fechaFin" v-model="filtros.fechaFin" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                          </div>
                      </div>
                      <div>
                          <label for="tipoProducto" class="block text-sm font-medium text-gray-700">Tipo de Producto:</label>
                          <select id="tipoProducto" v-model="filtros.tipoProducto" class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md">
                              <option value="">Todos</option>
                              <option value="Ventana">Ventana</option>
                              <option value="Puerta">Puerta</option>
                              <option value="Mesa">Mesa</option>
                              <option value="Mueble">Mueble</option>
                          </select>
                      </div>
                  </div>

                  <!-- Tabla de compras -->
                  <div class="overflow-x-auto">
                      <table class="min-w-full divide-y divide-gray-200">
                          <thead class="bg-gray-50">
                              <tr>
                                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cliente</th>
                                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Producto</th>
                                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fecha</th>
                                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Precio</th>
                              </tr>
                          </thead>
                          <tbody class="bg-white divide-y divide-gray-200">
                              <tr v-for="compra in comprasFiltradas" :key="compra.id">
                                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ compra.cliente }}</td>
                                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ compra.producto }}</td>
                                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatearFecha(compra.fecha) }}</td>
                                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatearPrecio(compra.precio) }}</td>
                              </tr>
                          </tbody>
                      </table>
                  </div>

                  <!-- Total -->
                  <div class="bg-gray-50 px-6 py-4 border-t border-gray-200">
                      <div class="text-right">
                          <p class="text-lg font-semibold text-gray-700">Total: {{ formatearPrecio(totalCompras) }}</p>
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

    // Datos de ejemplo (reemplazar con datos reales de la API)
    const compras = ref([
  { id: 1, cliente: 'Juan Pérez', producto: 'Ventana', fecha: '2023-05-15', precio: 500 },
  { id: 2, cliente: 'María García', producto: 'Puerta', fecha: '2023-05-14', precio: 800 },
  { id: 3, cliente: 'Carlos López', producto: 'Mesa', fecha: '2023-05-13', precio: 600 },
  { id: 4, cliente: 'Ana Martínez', producto: 'Mueble', fecha: '2023-05-12', precio: 1200 },
  { id: 5, cliente: 'Pedro Sánchez', producto: 'Ventana', fecha: '2023-05-11', precio: 450 },
])

const filtros = ref({
  fechaInicio: '',
  fechaFin: '',
  tipoProducto: '',
})

const comprasFiltradas = computed(() => {
  return compras.value.filter(compra => {
    const fechaCompra = new Date(compra.fecha)
    const cumpleFechaInicio = !filtros.value.fechaInicio || fechaCompra >= new Date(filtros.value.fechaInicio)
    const cumpleFechaFin = !filtros.value.fechaFin || fechaCompra <= new Date(filtros.value.fechaFin)
    const cumpleTipoProducto = !filtros.value.tipoProducto || compra.producto === filtros.value.tipoProducto

    return cumpleFechaInicio && cumpleFechaFin && cumpleTipoProducto
  })
})

const totalCompras = computed(() => {
  return comprasFiltradas.value.reduce((total, compra) => total + compra.precio, 0)
})

const formatearFecha = (fecha) => {
  return new Date(fecha).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' })
}

const formatearPrecio = (precio) => {
  return new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(precio)
}
</script>