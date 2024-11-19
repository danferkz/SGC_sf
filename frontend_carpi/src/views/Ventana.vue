<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
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
          </div>
        </div>

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="length" class="block text-sm font-medium text-gray-700">Largo (cm)</label>
            <input type="number" id="length" v-model="formData.length" required min="50" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="50" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
        </div>

        <!-- Tipo de Vidrio -->
        <div>
          <label for="glassType" class="block text-sm font-medium text-gray-700">Tipo de Vidrio</label>
          <select id="glassType" v-model="formData.glassType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de vidrio</option>
            <option value="templado">Templado</option>
            <option value="laminado">Laminado</option>
            <option value="doble">Doble Cristal</option>
            <option value="reflectante">Reflectante</option>
          </select>
        </div>

        <!-- Color -->
        <!-- <div>
          <label for="color" class="block text-sm font-medium text-gray-700">Color</label>
          <div class="mt-1 flex items-center space-x-3">
            <span class="inline-block h-8 w-8 rounded-full border" :style="{ backgroundColor: formData.color }"></span>
            <input type="color" id="color" v-model="formData.color"
              class="h-8 w-8 border-gray-300 rounded-md shadow-sm focus:ring-amber-500 focus:border-amber-500">
            <input type="text" v-model="formData.color"
              class="flex-1 focus:ring-amber-500 focus:border-amber-500 block shadow-sm sm:text-sm border-gray-300 rounded-md">
          </div>
        </div> -->

        <!-- Herrajes -->
        <div>
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
        </div>

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md"></textarea>
        </div>

        <!-- Botón de Envío -->
        <div>
          <button type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Realizar Pedido
          </button>
        </div>
      </form>

      <!-- Mensaje de Éxito o Error -->
      <div v-if="message" :class="['mt-4 text-center', messageClass]">
        {{ message }}
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const formData = reactive({
  windowType: '',
  height: 120,
  width: 100,
  glassType: '',
  color: '#FFFFFF',
  hardware: {
    handle: false,
    lock: false,
  },
  comments: ''
})

const message = ref('')
const messageClass = ref('')

const validateForm = () => {
  if (!formData.windowType) return 'Selecciona un tipo de ventana.'
  if (!formData.glassType) return 'Selecciona un tipo de vidrio.'
  return ''
}

const handleSubmit = () => {
  const validationError = validateForm()
  if (validationError) {
    message.value = validationError
    messageClass.value = 'text-red-600'
  } else {
    message.value = '¡Pedido realizado con éxito!'
    messageClass.value = 'text-green-600'
    // Aquí puedes realizar la lógica para enviar el pedido
  }
}

import Header from '@/components/HeaderCompo.vue'
import Footer from '@/components/FooterCompo.vue'
</script>

<style scoped>

textarea {
  resize: none; /* Desactiva el redimensionamiento */
}

</style>