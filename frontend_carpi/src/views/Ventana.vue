<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8 space-y-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Ventana Personalizada</h2>

      <form @submit.prevent="handleSubmit" class="space-y-8">

        <!-- Tipo de Ventana -->
        <div class="space-y-2">
          <label for="windowType" class="block text-lg font-medium text-gray-700">Tipo de Ventana</label>
          <select id="windowType" v-model="formData.windowType" required
            class="block w-full py-3 px-4 border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg">
            <option value="">Selecciona un tipo de ventana</option>
            <option value="corrediza">Corrediza</option>
            <option value="abatible">Abatible</option>
            <option value="batiente">Batiente</option>
            <option value="plegable">Plegable</option>
          </select>
        </div>

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="height" class="block text-lg font-medium text-gray-700">Alto (cm)</label>
            <input type="number" id="height" v-model="formData.height" required min="50" max="300"
              class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg h-14">
          </div>
          <div>
            <label for="width" class="block text-lg font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="50" max="300"
              class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg h-14">
          </div>
        </div>

        <!-- Tipo de Vidrio -->
        <div class="space-y-2">
          <label for="glassType" class="block text-lg font-medium text-gray-700">Tipo de Vidrio</label>
          <select id="glassType" v-model="formData.glassType" required
            class="block w-full py-3 px-4 border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg">
            <option value="">Selecciona un tipo de vidrio</option>
            <option value="templado">Templado</option>
            <option value="laminado">Laminado</option>
            <option value="doble">Doble Cristal</option>
            <option value="reflectante">Reflectante</option>
          </select>
        </div>

        <!-- Color -->
        <div class="space-y-2">
          <label for="color" class="block text-lg font-medium text-gray-700">Color</label>
          <div class="flex items-center space-x-3">
            <span class="inline-block h-10 w-10 rounded-full border" :style="{ backgroundColor: formData.color }"></span>
            <input type="color" id="color" v-model="formData.color"
              class="h-10 w-10 border-gray-300 rounded-lg shadow-sm focus:ring-amber-500 focus:border-amber-500">
            <input type="text" v-model="formData.color"
              class="flex-1 py-3 px-4 focus:ring-amber-500 focus:border-amber-500 block shadow-sm sm:text-lg border-gray-300 rounded-lg">
          </div>
        </div>

        <!-- Herrajes -->
        <div class="space-y-2">
          <label class="block text-lg font-medium text-gray-700">Herrajes</label>
          <div class="space-y-3">
            <div class="flex items-center">
              <input id="handle" type="checkbox" v-model="formData.hardware.handle"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300 rounded-lg">
              <label for="handle" class="ml-3 block text-lg font-medium text-gray-700">Manija</label>
            </div>
            <div class="flex items-center">
              <input id="lock" type="checkbox" v-model="formData.hardware.lock"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300 rounded-lg">
              <label for="lock" class="ml-3 block text-lg font-medium text-gray-700">Cerradura</label>
            </div>
          </div>
        </div>

        <!-- Comentarios Adicionales -->
        <div class="space-y-2">
          <label for="comments" class="block text-lg font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="4"
            class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg"></textarea>
        </div>

        <!-- Botón de Envío -->
        <div>
          <button type="submit"
            class="w-full flex justify-center py-3 px-6 border border-transparent rounded-lg shadow-lg text-lg font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
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
