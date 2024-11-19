<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Componente Header importado -->
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Ventana Personalizada</h2>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Tipo de Ventana -->
        <div>
          <label for="windowType" class="block text-sm font-medium text-gray-700">Tipo de Ventana</label>
          <select id="windowType" v-model="formData.windowType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de ventana</option>
            <option value="Corrediza">Corrediza - S/. 100</option>
            <option value="Abatible">Abatible - S/. 150</option>
            <option value="Batiente">Batiente - S/. 200</option>
            <option value="Plegable">Plegable - S/. 180</option>
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

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
<<<<<<<<< Temporary merge branch 1
            <label for="height" class="block text-lg font-medium text-gray-700">Alto (cm)</label>
            <input type="number" id="height" v-model="formData.height" required min="50" max="300"
              class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg h-14">
=========
            <label for="length" class="block text-sm font-medium text-gray-700">Largo (cm)</label>
            <input type="number" id="length" v-model="formData.length" required min="50" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
>>>>>>>>> Temporary merge branch 2
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="50" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
        </div>

        <!-- Exterior -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Exterior</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="true" type="radio" v-model="formData.exterior" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="true" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="false" type="radio" v-model="formData.exterior" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="false" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
            <!--<div class="flex items-center">
              <input id="glasspane" type="radio" v-model="formData.doorStyle" value="glasspane"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="glasspane" class="ml-3 block text-sm font-medium text-gray-700">Con Vidrio</label>
            </div> -->
          </div>
        </div>

        <!-- Número de hojas -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="number_of_sheets" class="block text-sm font-medium text-gray-700">Número de Hojas</label>
            <input type="number" id="number_of_sheets" v-model="formData.number_of_sheets" required min="1" max="5"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
          <!--<div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div> -->
        </div>

        <!-- Tipo de Vidrio -->
        <!--<div>
          <label for="glassType" class="block text-sm font-medium text-gray-700">Tipo de Vidrio</label>
          <select id="glassType" v-model="formData.glassType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de vidrio</option>
            <option value="templado">Templado</option>
            <option value="laminado">Laminado</option>
            <option value="doble">Doble Cristal</option>
            <option value="reflectante">Reflectante</option>
          </select>
        </div>-->

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
        </div>-->

        <!-- Herrajes -->
        <!--<div>
          <label class="block text-sm font-medium text-gray-700">Herrajes</label>
          <div class="mt-2 space-y-2">
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="handle" type="checkbox" v-model="formData.hardware.handle"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="handle" class="font-medium text-gray-700">Manija</label>
              </div>
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="lock" type="checkbox" v-model="formData.hardware.lock"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="lock" class="font-medium text-gray-700">Cerradura</label>
              </div>
            </div>
          </div>
        </div>-->

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md"></textarea>
        </div>

        <!-- Botones: Validar Datos y Calcular Precio -->
        <div class="flex justify-between items-center mt-6">
          <button type="button" @click="handleValidate"
            class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Validar Datos
>>>>>>>>> Temporary merge branch 2
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
      </form>

      <!-- Ventana modal con los datos validados -->
      <div v-if="showValidatedWindow" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
          <h3 class="text-xl font-bold mb-4 text-center">Resumen de tu Pedido</h3>
          <div class="space-y-4">
            <p><strong>Tipo de Ventana:</strong> {{ formData.windowType }}</p>
            <p><strong>Barnizado:</strong> {{ formData.varnished }}</p>
            <p><strong>Largo:</strong> {{ formData.length }} cm</p>
            <p><strong>Ancho:</strong> {{ formData.width }} cm</p>
            <p><strong>Exterior:</strong> {{ formData.exterior }}</p>
            <p><strong>Número de Hojas:</strong> {{ formData.number_of_sheets }}</p>
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
            <p><strong>Tipo de Ventana:</strong> {{ formData.windowType }}</p>
            <p><strong>Largo:</strong> {{ formData.length }} cm</p>
            <p><strong>Ancho:</strong> {{ formData.width }} cm</p>
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

<script>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import Header from '@/components/HeaderCompo.vue' // Importa el componente Header

export default {
  components: {
    Header, // Declara el componente Header
  },
  setup() {
    const formData = reactive({
      windowType: '',
      varnished: '',
      length: '',
      width: '',
      exterior: '',
      finish: '',
      exterior: '',
      comments: '',
    })

    const price = ref(0)
    const showValidatedWindow = ref(false)
    const showOrderWindow = ref(false)
    const isDelivery = ref(false)

    const router = useRouter()

    const windowPrices = {
      Corrediza: 100,
      Abatible: 150,
      Batiente: 200,
      Plegable: 180,
    }

    const handleValidate = () => {
      showValidatedWindow.value = true
    }

    const handleCalculatePrice = () => {
      price.value = windowPrices[formData.windowType] || 0
    }

    const submitOrder = () => {
      showValidatedWindow.value = false
      showOrderWindow.value = true
      router.push({ name: 'Delivery' });
    }

    const totalPrice = computed(() => {
      return isDelivery.value ? price.value + 15 : price.value
    })

    const finalizeOrder = () => {
      alert(`Pedido confirmado. Precio total: S/${totalPrice.value}`)
      showOrderWindow.value = false
      router.push({ name: 'ClientePerfil' })
    }

    return {
      formData,
      price,
      showValidatedWindow,
      showOrderWindow,
      isDelivery,
      handleValidate,
      handleCalculatePrice,
      submitOrder,
      totalPrice,
      finalizeOrder,
    }
  },
}
</script>

<style scoped>
textarea {
  resize: none; /* Desactiva el redimensionamiento */
}
</style>
