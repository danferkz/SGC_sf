<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">

      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Puerta Personalizada</h2>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Tipo de Madera -->
        <div>
          <label for="woodType" class="block text-sm font-medium text-gray-700">Tipo de Madera</label>
          <select id="woodType" v-model="formData.woodType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de madera</option>
            <option value="pino">Pino</option>
            <option value="roble">Roble</option>
            <option value="cedro">Cedro</option>
            <option value="caoba">Caoba</option>
          </select>
        </div>

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="height" class="block text-sm font-medium text-gray-700">Alto (cm)</label>
            <input type="number" id="height" v-model="formData.height" required min="100" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md">
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md">
          </div>
        </div>

        <!-- Color -->
        <div>
          <label for="color" class="block text-sm font-medium text-gray-700">Color</label>
          <div class="mt-1 flex items-center space-x-3">
            <span class="inline-block h-8 w-8 rounded-full border" :style="{ backgroundColor: formData.color }"></span>
            <input type="color" id="color" v-model="formData.color"
              class="h-8 w-8 border-gray-300 rounded-md shadow-sm focus:ring-amber-500 focus:border-amber-500">
            <input type="text" v-model="formData.color"
              class="flex-1 focus:ring-amber-500 focus:border-amber-500 block shadow-sm sm:text-sm border-gray-300 rounded-md">
          </div>
        </div>

        <!-- Estilo de Puerta -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Estilo de Puerta</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="simple" type="radio" v-model="formData.doorStyle" value="simple"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="simple" class="ml-3 block text-sm font-medium text-gray-700">Simple</label>
            </div>
            <div class="flex items-center">
              <input id="paneled" type="radio" v-model="formData.doorStyle" value="paneled"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="paneled" class="ml-3 block text-sm font-medium text-gray-700">Con Paneles</label>
            </div>
            <div class="flex items-center">
              <input id="glasspane" type="radio" v-model="formData.doorStyle" value="glasspane"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="glasspane" class="ml-3 block text-sm font-medium text-gray-700">Con Vidrio</label>
            </div>
          </div>
        </div>

        <!-- Acabado -->
        <div>
          <label for="finish" class="block text-sm font-medium text-gray-700">Acabado</label>
          <select id="finish" v-model="formData.finish" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un acabado</option>
            <option value="natural">Natural</option>
            <option value="mate">Mate</option>
            <option value="brillante">Brillante</option>
            <option value="satinado">Satinado</option>
          </select>
        </div>

        <!-- Herrajes -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Herrajes</label>
          <div class="mt-2 space-y-2">
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="doorknob" type="checkbox" v-model="formData.hardware.doorknob"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="doorknob" class="font-medium text-gray-700">Pomo</label>
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
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="hinges" type="checkbox" v-model="formData.hardware.hinges"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="hinges" class="font-medium text-gray-700">Bisagras</label>
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
  woodType: '',
  height: 200,
  width: 80,
  color: '#8B4513',
  doorStyle: 'simple',
  finish: '',
  hardware: {
    doorknob: false,
    lock: false,
    hinges: false
  },
  comments: ''
})

const message = ref('')
const messageClass = ref('')

const validateForm = () => {
  if (!formData.woodType) return 'Selecciona un tipo de madera.'
  if (!formData.finish) return 'Selecciona un acabado.'
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
/* Aquí puedes agregar clases de estilo adicional si es necesario */
</style>