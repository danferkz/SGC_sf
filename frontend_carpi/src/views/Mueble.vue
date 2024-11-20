<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Mueble Personalizado</h2>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        
        <!-- Tipo de Madera -->
        <div>
          <label for="woodType" class="block text-sm font-medium text-gray-700">Tipo de Madera</label>
          <select id="woodType" v-model="formData.woodType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de madera</option>
            <option value="Pino">Pino - S/. 100</option>
            <option value="Roble">Roble - S/. 150</option>
            <option value="Cedro">Cedro - S/. 200</option>
            <option value="Caoba">Caoba - S/. 180</option>
          </select>
        </div>

        <!-- Barnizado -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Barnizado</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="true" type="radio" v-model="formData.varnished" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="is_varnished" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="false" type="radio" v-model="formData.varnished" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="no_varnished" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
            <!--<div class="flex items-center">
              <input id="glasspane" type="radio" v-model="formData.doorStyle" value="glasspane"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="glasspane" class="ml-3 block text-sm font-medium text-gray-700">Con Vidrio</label>
            </div> -->
          </div>
        </div>

        <!-- Tipo de Sofá -->
        <div>
          <label for="sofaType" class="block text-sm font-medium text-gray-700">Tipo de Sofá</label>
          <select id="sofaType" v-model="formData.sofaType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de sofá</option>
            <option value="Modular">Modular</option>
            <option value="Seccional">Seccional</option>
            <option value="Sofacama">Sofá Cama</option>
            <option value="Reclinable">Reclinable</option>
          </select>
        </div>

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="weight" class="block text-sm font-medium text-gray-700">Peso (cm)</label>
            <input type="number" id="weight" v-model="formData.dimensions.weight" required min="100" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
          <!--<div>
            <label for="depth" class="block text-sm font-medium text-gray-700">Profundidad (cm)</label>
            <input type="number" id="depth" v-model="formData.dimensions.depth" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div> -->
          <!--<div>
            <label for="height" class="block text-sm font-medium text-gray-700">Alto (cm)</label>
            <input type="number" id="height" v-model="formData.dimensions.height" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div> -->
        </div>

        <!-- Material de Tapicería -->
        <!-- <div>
          <label for="upholsteryMaterial" class="block text-sm font-medium text-gray-700">Material de Tapicería</label>
          <select id="upholsteryMaterial" v-model="formData.upholsteryMaterial" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un material</option>
            <option value="cuero">Cuero</option>
            <option value="tela">Tela</option>
            <option value="terciopelo">Terciopelo</option>
          </select>
        </div> -->

        <!-- Color -->
        <!--<div>
          <label for="color" class="block text-sm font-medium text-gray-700">Color</label>
          <div class="mt-1 flex items-center space-x-3">
            <span class="inline-block h-8 w-8 rounded-full border" :style="{ backgroundColor: formData.color }"></span>
            <input type="color" id="color" v-model="formData.color"
              class="h-8 w-8 border-gray-300 rounded-md shadow-sm focus:ring-amber-500 focus:border-amber-500">
            <input type="text" v-model="formData.color"
              class="flex-1 focus:ring-amber-500 focus:border-amber-500 block shadow-sm sm:text-sm border-gray-300 rounded-md h-12">
          </div>
        </div> -->

        <!-- Parte del Set -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Parte del Set</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="true" type="radio" v-model="formData.is_part_of_set" value="Sí"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="true" class="ml-3 block text-sm font-medium text-gray-700">Sí</label>
            </div>
            <div class="flex items-center">
              <input id="false" type="radio" v-model="formData.is_part_of_set" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="false" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
            <!-- <div class="flex items-center">
              <input id="plastico" type="radio" v-model="formData.legStyle" value="plástico"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="plastico" class="ml-3 block text-sm font-medium text-gray-700">Plástico</label>
            </div> -->
          </div>
        </div>

        <!-- Nombre del Set -->
        <div>
          <label for="set_name" class="block text-sm font-medium text-gray-700">Nombre del Set</label>
          <textarea id="set_name" v-model="formData.set_name" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-200 focus:ring-amber-200 focus:border-amber-200 rounded-md resize-none"></textarea>
        </div>   

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md resize-none"></textarea>
        </div>

        <!-- Nuevos botones: Validar Datos y Calcular Precio -->
        <div class="flex justify-between items-center mt-6">
          <button type="button" @click="handleValidate"
            class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Validar Datos
          </button>
          <div class="flex items-center space-x-2">
            <button type="button" @click="handleCalculatePrice"
              class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
              Calcular Precio
            </button>
            <div class="flex items-center">
              <span class="mr-1">S/</span>
              <input type="number" v-model="price" placeholder="Precio en soles" readonly
                class="w-32 focus:ring-amber-500 focus:border-amber-500 block shadow-sm sm:text-sm border-gray-300 rounded-md h-12">
            </div>
          </div>
        </div>

        <!-- Botón de Envío -->
        <!--<div>
          <button type="submit"
            class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Enviar Pedido
          </button>
        </div> -->
      </form>

      <!-- Ventana modal con los datos validados -->
      <div v-if="showValidatedWindow" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
          <h3 class="text-xl font-bold mb-4 text-center">Resumen de tu Pedido</h3>
          <div class="space-y-4">
            <p><strong>Tipo de Madera:</strong> {{ formData.woodType }}</p>
            <p><strong>Barnizado:</strong> {{ formData.varnished }}</p>
            <p><strong>Tipo de Sofá:</strong> {{ formData.sofaType }}</p>
            <p><strong>Peso:</strong> {{ formData.dimensions.weight }}</p>
            <p><strong>Parte del Set:</strong> {{ formData.is_part_of_set }}</p>
            <p><strong>Nombre del Set:</strong> {{ formData.set_name }}</p>
            <p><strong>Precio Estimado:</strong> S/{{ price }}</p>
          </div>
          <div class="mt-4 flex justify-center space-x-4">
            <button @click="showValidatedWindow = false" class="px-4 py-2 bg-gray-300 text-gray-700 rounded-md">
              Cerrar
            </button>
            <button @click="submitOrder" class="px-4 py-2 bg-amber-600 text-white rounded-md">
              Crear Pedido
            </button>
          </div>
        </div>
      </div>

      <!-- Nueva ventana modal de orden -->
      <div v-if="showOrderWindow" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
          <h3 class="text-xl font-bold mb-4 text-center">Orden</h3>
          <div class="space-y-4">
            <p><strong>Tipo de Sofá:</strong> {{ formData.sofaType }}</p>
            <p><strong>Largo:</strong> {{ formData.dimensions.height }} cm</p>
            <p><strong>Ancho:</strong> {{ formData.dimensions.width }} cm</p>
            <p><strong>Profundidad:</strong> {{ formData.dimensions.depth }} cm</p>
            <div class="flex items-center space-x-2">
              <input type="checkbox" id="delivery" v-model="isDelivery" class="rounded text-amber-600 focus:ring-amber-500">
              <label for="delivery">Delivery (S/ 15)</label>
            </div>
            <p><strong>Precio Total:</strong> S/{{ totalPrice }}</p>
          </div>
          <div class="mt-4 flex justify-center space-x-4">
            <button @click="showOrderWindow = false" class="px-4 py-2 bg-gray-300 text-gray-700 rounded-md">
              Cancelar
            </button>
            <button @click="finalizeOrder" class="px-4 py-2 bg-amber-600 text-white rounded-md">
              Confirmar Pedido
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router' // Importar el enrutador
import Header from '@/components/HeaderCompo.vue'

const formData = reactive({
  woodType: '',
  varnished: '',
  sofaType: '',
  is_part_of_set: '',
  features: {
    reclinable: false,
    cojinesExtraibles: false,
    reposacabezas: false,
    camaConvertible: false,
  },
  dimensions: {
    weight: '',
  },
  upholsteryMaterial: '',
  
  set_name: '',
  comments: '',
})

const price = ref(0)
const showValidatedWindow = ref(false)
const showOrderWindow = ref(false)  // Nueva ventana
const isDelivery = ref(false)

const woodPrices = reactive({
  Pino: 100,
  Roble: 150,
  Cedro: 200,
  Caoba: 180,
})

// Computed property to calculate total price
const totalPrice = computed(() => {
  let basePrice = woodPrices[formData.sofaType] || 0;
  let deliveryPrice = isDelivery.value ? 15 : 0;
  return basePrice + deliveryPrice;
})

const router = useRouter() // Usar el enrutador de Vue

const handleFinalizeOrder = () => {
  //showOrderWindow.value = true;  // Muestra la ventana de la orden
}

const handleSubmit = () => {
  alert('Pedido enviado correctamente');
}

const handleValidate = () => {
  showValidatedWindow.value = true;  // Muestra la ventana de validación
}

const handleCalculatePrice = () => {
  let basePrice = woodPrices[formData.woodType] || 0;
  price.value = basePrice;
}

const finalizeOrder = () => {
      alert(`Pedido confirmado. Precio total: S/${totalPrice.value}`)
      showOrderWindow.value = false
      router.push({ name: 'ClientePerfil' }) // Redirigir a la página de ClientePerfil
}

const submitOrder = () => {
      showValidatedWindow.value = false
      showOrderWindow.value = true
      router.push({ name: 'Delivery' });
}
</script>
