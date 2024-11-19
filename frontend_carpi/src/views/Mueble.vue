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
            <!--<div class="flex items-center">
              <input id="glasspane" type="radio" v-model="formData.doorStyle" value="glasspane"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="glasspane" class="ml-3 block text-sm font-medium text-gray-700">Con Vidrio</label>
            </div> -->
          </div>
        </div>

        <!-- Material de Tapicería -->
        <div>
          <label for="upholsteryMaterial" class="block text-sm font-medium text-gray-700">Material de Tapicería</label>
          <select id="upholsteryMaterial" v-model="formData.upholsteryMaterial" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un material</option>
            <option value="cuero">Cuero</option>
            <option value="tela">Tela</option>
            <option value="terciopelo">Terciopelo</option>
          </select>
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

        <!-- Estilo de Patas -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Estilo de Patas</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="metal" type="radio" v-model="formData.legStyle" value="metal"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="metal" class="ml-3 block text-sm font-medium text-gray-700">Metal</label>
            </div>
            <div class="flex items-center">
              <input id="madera" type="radio" v-model="formData.legStyle" value="madera"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="madera" class="ml-3 block text-sm font-medium text-gray-700">Madera</label>
            </div>
            <div class="flex items-center">
              <input id="plastico" type="radio" v-model="formData.legStyle" value="plástico"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="plastico" class="ml-3 block text-sm font-medium text-gray-700">Plástico</label>
            </div>
          </div>
        </div>

        <!-- Características adicionales -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Características Adicionales</label>
          <div class="mt-2 space-y-2">
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="reclinable" type="checkbox" v-model="formData.features.reclinable"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="reclinable" class="font-medium text-gray-700">Reclinable</label>
              </div>
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="cojinesExtraibles" type="checkbox" v-model="formData.features.cojinesExtraibles"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="cojinesExtraibles" class="font-medium text-gray-700">Cojines Extraíbles</label>
              </div>
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="reposacabezas" type="checkbox" v-model="formData.features.reposacabezas"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="reposacabezas" class="font-medium text-gray-700">Reposacabezas</label>
              </div>
            </div>
            <div class="flex items-start">
              <div class="flex items-center h-5">
                <input id="camaConvertible" type="checkbox" v-model="formData.features.camaConvertible"
                  class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300 rounded">
              </div>
              <div class="ml-3 text-sm">
                <label for="camaConvertible" class="font-medium text-gray-700">Cama Convertible</label>
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
            Enviar
          </button>
        </div>
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