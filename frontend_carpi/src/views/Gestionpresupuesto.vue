<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 flex">
        <!-- Header -->
        <HeaderAdmin class="header-admin" />

        <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
            <div class="max-w-7xl mx-auto">
                <h3 class="text-3xl font-bold text-center mb-12">Ganancias Diarias</h3>

                <!-- Filtro de fecha -->
                <div class="mb-6 bg-white p-4 rounded-lg shadow-sm">
                    <div class="flex items-center gap-4">
                        <div class="flex-1 max-w-xs">
                            <label for="selectedDate" class="block text-sm font-medium text-gray-700 mb-1">
                                Seleccionar Fecha
                            </label>
                            <input 
                                type="date" 
                                id="selectedDate"
                                v-model="selectedDate"
                                :max="today"
                                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                                       focus:border-indigo-300 focus:ring focus:ring-indigo-200 
                                       focus:ring-opacity-50"
                            >
                        </div>
                        <button 
                            @click="resetToToday"
                            class="mt-6 px-4 py-2 bg-gray-100 text-gray-700 rounded-md 
                                   hover:bg-gray-200 focus:outline-none focus:ring-2 
                                   focus:ring-gray-500 focus:ring-opacity-50"
                        >
                            Volver a Hoy
                        </button>
                    </div>
                </div>

                <div class="bg-white shadow-md rounded-lg overflow-hidden">
                    <!-- Tabla de órdenes -->
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Cliente</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        ID Orden</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Estado</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Fecha Entrega</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Fecha Creación</th>
                                    <th scope="col"
                                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                        Total</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr v-if="filteredOrders.length === 0">
                                    <td colspan="6" class="px-6 py-4 text-center text-gray-500">
                                        No hay órdenes para la fecha seleccionada
                                    </td>
                                </tr>
                                <tr v-else v-for="order in filteredOrders" :key="order.orders_id">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                                        {{ order.client_detail.username }}
                                        <span class="block text-xs text-gray-500">{{ order.client_detail.email }}</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ order.orders_id }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span :class="getStatusClass(order.status)" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                                            {{ formatStatus(order.status) }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ order.promised_date }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ formatearFecha(order.created_at) }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ formatearPrecio(order.total_price) }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Total -->
                    <div class="bg-gray-50 px-6 py-4 border-t border-gray-200">
                        <div class="text-right space-y-2">
                            <p class="text-sm text-gray-600">
                                Número de órdenes: {{ filteredOrders.length }}
                            </p>
                            <p class="text-lg font-semibold text-gray-700">
                                Total: {{ formatearPrecio(totalFiltrado) }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const orders = ref([])
const error = ref(null)
const today = new Date().toISOString().split('T')[0]
const selectedDate = ref(today)

// Función para obtener las órdenes
const fetchOrders = async () => {
    try {
        const token = localStorage.getItem('token')
        if (!token) {
            throw new Error('No se encontró el token de autenticación')
        }

        const response = await axios.get('http://localhost:8000/api/orders/orders-list-admin/', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        orders.value = response.data.results
    } catch (e) {
        error.value = 'Error al cargar las órdenes: ' + e.message
        console.error('Error:', e)
    }
}

// Filtrar órdenes por fecha seleccionada
const filteredOrders = computed(() => {
    return orders.value.filter(order => {
        const orderDate = new Date(order.created_at).toISOString().split('T')[0]
        return orderDate === selectedDate.value
    })
})

// Calcular total de órdenes filtradas
const totalFiltrado = computed(() => {
    return filteredOrders.value.reduce((sum, order) => {
        return sum + parseFloat(order.total_price)
    }, 0)
})

// Formatear fecha
const formatearFecha = (fecha) => {
    return new Date(fecha).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    })
}

// Formatear precio
const formatearPrecio = (precio) => {
    return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'EUR'
    }).format(precio)
}

// Formatear estado
const formatStatus = (status) => {
    const statusMap = {
        'pending': 'Pendiente',
        'in_progress': 'En Progreso',
        'completed': 'Completado',
        'cancelled': 'Cancelado'
    }
    return statusMap[status] || status
}

// Obtener clase CSS para el estado
const getStatusClass = (status) => {
    const statusClasses = {
        'pending': 'bg-yellow-100 text-yellow-800',
        'in_progress': 'bg-blue-100 text-blue-800',
        'completed': 'bg-green-100 text-green-800',
        'cancelled': 'bg-red-100 text-red-800'
    }
    return statusClasses[status] || 'bg-gray-100 text-gray-800'
}

// Resetear a la fecha actual
const resetToToday = () => {
    selectedDate.value = today
}

// Cargar datos al montar el componente
onMounted(() => {
    fetchOrders()
})
</script>