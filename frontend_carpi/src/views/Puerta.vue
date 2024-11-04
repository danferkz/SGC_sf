<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <Header />
    <div class="max-w-3xl mx-auto bg-white rounded-xl shadow-lg p-8 space-y-8">

      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Puerta Personalizada</h2>

      <form @submit.prevent="handleSubmit" class="space-y-8">
        <!-- Tipo de Madera -->
        <div class="space-y-2">
          <label for="woodType" class="block text-lg font-medium text-gray-700">Tipo de Madera</label>
          <select id="woodType" v-model="formData.woodType" required
            class="block w-full py-3 px-4 border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg">
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
            <label for="height" class="block text-lg font-medium text-gray-700">Alto (cm)</label>
            <input type="number" id="height" v-model="formData.height" required min="100" max="300"
              class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg h-14">
          </div>
          <div>
            <label for="width" class="block text-lg font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
              class="block w-full py-3 px-4 border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg h-14">
          </div>
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

        <!-- Estilo de Puerta -->
        <div class="space-y-2">
          <label class="block text-lg font-medium text-gray-700">Estilo de Puerta</label>
          <div class="flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-8">
            <div class="flex items-center">
              <input id="simple" type="radio" v-model="formData.doorStyle" value="simple"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300">
              <label for="simple" class="ml-3 block text-lg font-medium text-gray-700">Simple</label>
            </div>
            <div class="flex items-center">
              <input id="paneled" type="radio" v-model="formData.doorStyle" value="paneled"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300">
              <label for="paneled" class="ml-3 block text-lg font-medium text-gray-700">Con Paneles</label>
            </div>
            <div class="flex items-center">
              <input id="glasspane" type="radio" v-model="formData.doorStyle" value="glasspane"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300">
              <label for="glasspane" class="ml-3 block text-lg font-medium text-gray-700">Con Vidrio</label>
            </div>
          </div>
        </div>

        <!-- Acabado -->
        <div class="space-y-2">
          <label for="finish" class="block text-lg font-medium text-gray-700">Acabado</label>
          <select id="finish" v-model="formData.finish" required
            class="block w-full py-3 px-4 border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-lg">
            <option value="">Selecciona un acabado</option>
            <option value="natural">Natural</option>
            <option value="mate">Mate</option>
            <option value="brillante">Brillante</option>
            <option value="satinado">Satinado</option>
          </select>
        </div>

        <!-- Herrajes -->
        <div class="space-y-2">
          <label class="block text-lg font-medium text-gray-700">Herrajes</label>
          <div class="space-y-3">
            <div class="flex items-center">
              <input id="doorknob" type="checkbox" v-model="formData.hardware.doorknob"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300 rounded-lg">
              <label for="doorknob" class="ml-3 block text-lg font-medium text-gray-700">Pomo</label>
            </div>
            <div class="flex items-center">
              <input id="lock" type="checkbox" v-model="formData.hardware.lock"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300 rounded-lg">
              <label for="lock" class="ml-3 block text-lg font-medium text-gray-700">Cerradura</label>
            </div>
            <div class="flex items-center">
              <input id="hinges" type="checkbox" v-model="formData.hardware.hinges"
                class="focus:ring-amber-500 h-5 w-5 text-amber-600 border-gray-300 rounded-lg">
              <label for="hinges" class="ml-3 block text-lg font-medium text-gray-700">Bisagras</label>
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
