<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Componente Header añadido aquí -->
    <Header />
    
    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Ventana Personalizada</h2>

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
            <input type="number" id="length" v-model="formData.length" required min="60" max="300"

              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
              class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
          </div>
        </div>

        <!-- Exterior -->
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

        <!-- Botones: Validar Datos y Calcular Precio -->
        <div class="flex justify-between items-center mt-6">
          <button type="button" @click="showValidatedWindow = true"
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
      </form>

      <!-- Ventana modal con los datos validados -->
      <div v-if="showValidatedWindow" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
          <h3 class="text-xl font-bold mb-4 text-center">Resumen de tu Pedido</h3>
          <div class="space-y-4">
            <p><strong>Tipo de Madera:</strong> {{ formData.woodType }}</p>
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
            <button @click="createProduct" class="px-4 py-2 bg-amber-600 text-white rounded-md">
              Crear Pedido
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue';
import axios from 'axios';
import Header from "@/components/HeaderCompo.vue";

export default {
  components: {
    Header,
  },
  setup() {
    const formData = reactive({
      woodType: '',
      varnished: '', // 'Si' o 'No'
      length: '',
      width: '',
      exterior: '', // 'Si' o 'No'
      number_of_sheets: '',
      comments: '',
    });

    const showValidatedWindow = ref(false);
    const showOrderWindow = ref(false);
    const price = ref(0);

    // Obtener el token desde el localStorage
    const getToken = () => {
      return localStorage.getItem('token');
    };

    // Crear el producto a través de la API
    const createProduct = async () => {
      try {
        const token = getToken();
        if (!token) {
          alert('No se encontró un token de autenticación.');
          return;
        }


        // Validar que el precio no sea cero o no esté definido
        if (!price.value || price.value <= 0) {
          alert('El precio debe ser mayor que cero y debe estar definido.');
          return;
        }


        const payload = {
          wood_type: formData.woodType,
          is_varnished: formData.varnished === 'Si',
          length: parseFloat(formData.length),
          width: parseFloat(formData.width),
          is_exterior: formData.exterior === 'Si',
          number_of_sheets: parseInt(formData.number_of_sheets),
          cost_price: parseFloat(price.value),
        };

        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        const response = await axios.post('http://localhost:8000/api/products/product-window-create/', payload, config);
        
        if (response.status === 201) {
          alert('Producto creado exitosamente');
          showValidatedWindow.value = false;
        } else {
          alert('Hubo un error al crear el producto.');
        }
      } catch (error) {
        console.error('Error al crear el producto:', error);
        alert('Hubo un error al crear el producto.');
      }
    };

    // Calcular el precio a través de la API
    const handleCalculatePrice = async () => {
      try {
        const token = getToken();
        if (!token) {
          alert('No se encontró un token de autenticación. Por favor, inicia sesión.');
          return;
        }

        const payload = {
          wood_type: formData.woodType,
          is_varnished: formData.varnished === 'Si',
          length: parseFloat(formData.length),
          width: parseFloat(formData.width),
          is_exterior: formData.exterior === 'Si',
          number_of_sheets: parseInt(formData.number_of_sheets),
        };

        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        const response = await axios.post(
          'http://localhost:8000/api/products/calcular-precio-ventana/',
          payload,
          config
        );

        price.value = response.data.cost_price.toFixed(2);
      } catch (error) {
        console.error('Error al calcular el precio:', error);
        alert('Hubo un error al calcular el precio. Por favor, verifica los datos.');
      }
    };

    return {
      formData,
      showValidatedWindow,
      showOrderWindow,
      price,
      handleCalculatePrice,
      createProduct,
    };
  },
};
</script>

<style scoped>
/* Estilos específicos si los necesitas */
</style>