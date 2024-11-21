<template>
    <div class="min-h-screen bg-gradient-to-br from-LightSalmon-100 to-green-100 p-8">
      <!-- Componente Header añadido -->
      <Header />
  
      <div class="max-w-4xl mx-auto bg-white rounded-2xl shadow-xl overflow-hidden">
        <div class="p-8 space-y-8">
          <!-- Primer cuadro: Datos del producto -->
          <div class="bg-LightSalmon-50 p-6 rounded-xl shadow-md">
            <h2 class="text-2xl font-bold mb-4 text-IndianRed-800">Datos del Producto</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="space-y-2">
                <p><span class="font-semibold">Tipo de Madera:</span> {{ producto.tipoMadera }}</p>
                <p><span class="font-semibold">Barnizado:</span> {{ producto.barnizado }}</p>
                <p><span class="font-semibold">Largo:</span> {{ producto.largo }} cm</p>
              </div>
              <div class="space-y-2">
                <p><span class="font-semibold">Ancho:</span> {{ producto.ancho }} cm</p>
                <p><span class="font-semibold">Exterior:</span> {{ producto.exterior }}</p>
                <p><span class="font-semibold">Número de Hojas:</span> {{ producto.numHojas }}</p>
              </div>
            </div>
          </div>
  
          <!-- Segundo cuadro: Opciones de Delivery -->
          <div class="bg-IndianRed-50 p-6 rounded-xl shadow-md">
            <h2 class="text-2xl font-bold mb-4 text-IndianRed-800">Delivery</h2>
            <div class="space-y-4">
              <div class="form-control">
                <label class="label">
                  <span class="label-text font-semibold">¿Desea delivery?</span>
                </label>
                <div class="flex space-x-4">
                  <label class="label cursor-pointer">
                    <input v-model="deseaDelivery" type="radio" name="delivery" :value="true" class="radio radio-primary" />
                    <span class="label-text ml-2">Sí</span>
                  </label>
                  <label class="label cursor-pointer">
                    <input v-model="deseaDelivery" type="radio" name="delivery" :value="false" class="radio radio-primary" />
                    <span class="label-text ml-2">No</span>
                  </label>
                </div>
              </div>
              <div v-if="deseaDelivery" class="space-y-4">
                <div class="form-control">
                  <label class="label">
                    <span class="label-text font-semibold">Fecha de Entrega</span>
                  </label>
                  <input v-model="fechaEntrega" type="date" class="input input-bordered w-full h-12" />
                </div>
                <div class="form-control">
                  <label class="label">
                    <span class="label-text font-semibold">Comentarios</span>
                  </label>
                  <textarea v-model="comentarios" class="block text-sm font-medium text-white-700 resize-none"></textarea>
                </div>
                <button @click="confirmarDelivery" class="btn btn-primary w-full">Aceptar Delivery</button>
              </div>
            </div>
          </div>
  
          <!-- Botón de Ordenar -->
          <div class="text-center">
            <button @click="confirmarOrden" class="btn btn-lg btn-accent hover:btn-accent-focus transition duration-300 ease-in-out transform hover:scale-105">
              Ordenar
            </button>
          </div>
        </div>
      </div>
  
      <!-- Modal de Confirmación de Delivery -->
      <div v-if="showDeliveryModal" class="modal modal-open">
        <div class="modal-box bg-white rounded-lg shadow-xl">
          <h3 class="font-bold text-lg text-white-800">Confirmación de Delivery</h3>
          <p class="py-4">¿Desea confirmar el delivery?</p>
          <div class="modal-action">
            <button @click="aceptarDelivery" class="btn btn-primary">Aceptar</button>
            <button @click="cancelarDelivery" class="btn btn-outline">Cancelar</button>
          </div>
        </div>
      </div>
  
      <!-- Modal de Confirmación de Orden -->
      <div v-if="showOrdenModal" class="modal modal-open">
        <div class="modal-box bg-white rounded-lg shadow-xl">
          <h3 class="font-bold text-lg text-green-800">Confirmación de Orden</h3>
          <p class="py-4">¿Desea confirmar la orden?</p>
          <div class="modal-action">
            <button @click="aceptarOrden" class="btn btn-accent">Aceptar</button>
            <button @click="cancelarOrden" class="btn btn-outline">Cancelar</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router' // Importar el router
  import Header from "@/components/HeaderCompo.vue"; // Importar Header
  import ClientePerfil from '@/views/ClientePerfil.vue'; // Importar ClientePerfil
  
  const router = useRouter(); // Crear instancia del router
  
  const producto = ref({
    tipoMadera: 'Roble',
    barnizado: 'Natural',
    largo: 200,
    ancho: 100,
    exterior: 'Sí',
    numHojas: 2
  })
  
  const deseaDelivery = ref(false)
  const fechaEntrega = ref('')
  const comentarios = ref('')
  
  const showDeliveryModal = ref(false)
  const showOrdenModal = ref(false)
  
  function confirmarDelivery() {
    showDeliveryModal.value = true
  }
  
  function aceptarDelivery() {
    // Lógica para aceptar el delivery
    showDeliveryModal.value = false
  }
  
  function cancelarDelivery() {
    showDeliveryModal.value = false
  }
  
  function confirmarOrden() {
    showOrdenModal.value = true
  }
  
  function aceptarOrden() {
    // Redirigir a ClientePerfil
    showOrdenModal.value = false
    router.push({ name: 'ClientePerfil' }) // Navegar a la vista ClientePerfil
  }
  
  function cancelarOrden() {
    showOrdenModal.value = false
  }
  </script>
  

