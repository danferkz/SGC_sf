<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Personaliza tu Sofá</h2>

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
        </div>

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
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Enviar
          </button>
        </div> -->
      </form>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/HeaderCompo.vue'
import Footer from '@/components/FooterCompo.vue'

export default {
  name: 'SofaCustomizationForm',
  components: {
    Header,
    Footer, // Aquí estamos importando el Footer
  },
  data() {
    return {
      formData: {
        sofaType: '',
        dimensions: {
          width: '',
          depth: '',
          height: ''
        },
        upholsteryMaterial: '',
        color: '#000000',
        legStyle: '',
        features: {
          reclinable: false,
          cojinesExtraibles: false,
          reposacabezas: false,
          camaConvertible: false,
        },
        comments: '',
      },
    };
  },
  methods: {
    handleSubmit() {
      console.log('Datos del formulario:', this.formData);
    },
  },
};
</script>


<style scoped>
textarea {
  resize: none; /* Desactiva el redimensionamiento */
}
</style>