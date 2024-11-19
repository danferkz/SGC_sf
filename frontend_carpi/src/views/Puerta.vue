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
            <option value="Pino">Pino - S/. 100</option>
            <option value="Roble">Roble - S/. 150</option>
            <option value="Cedro">Cedro - S/. 200</option>
            <option value="Caoba">Caoba - S/. 180</option>
          </select>
        </div>
        <!-- Barnizado-->
        <div>
          <label class="block text-sm font-medium text-gray-700">Barnizado</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="varnished-yes" type="radio" v-model="formData.varnished" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="varnished-yes" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="varnished-no" type="radio" v-model="formData.varnished" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="varnished-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
        </div>
        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="length" class="block text-sm font-medium text-gray-700">Largo (cm)</label>
            <input type="number" id="length" v-model="formData.length" required min="100" max="300"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
        </div>

        <!-- Exteriores -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Exterior</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="exterior-yes" type="radio" v-model="formData.exterior" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="exterior-yes" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="exterior-no" type="radio" v-model="formData.exterior" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="exterior-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
        </div>

       <!-- Número de hojas -->
       <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="number_of_sheets" class="block text-sm font-medium text-gray-700">Número de Hojas</label>
            <input type="number" id="number_of_sheets" v-model="formData.number_of_sheets" required min="1" max="5"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
        </div>

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md resize-none"></textarea>
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
