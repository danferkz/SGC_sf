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
              <input id="varnished-yes" type="radio" v-model="formData.varnished" :value="true"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="varnished-yes" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="varnished-no" type="radio" v-model="formData.varnished" :value="false"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="varnished-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
        </div>

        <!-- Nombre de la Pieza -->
        <div>
          <label for="pieceName" class="block text-sm font-medium text-gray-700">Nombre de la Pieza</label>
          <input type="text" id="pieceName" v-model="formData.piece_name" required
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
        </div>

        <!-- Peso -->
        <div>
          <label for="weight" class="block text-sm font-medium text-gray-700">Peso (kg)</label>
          <input type="number" id="weight" v-model="formData.weight" required min="0"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12">
        </div>

        <!-- Parte de un Juego -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Parte de un Juego</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="part-of-set-yes" type="radio" v-model="formData.is_part_of_set" :value="true"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="part-of-set-yes" class="ml-3 block text-sm font-medium text-gray-700"> Si</label>
            </div>
            <div class="flex items-center">
              <input id="part-of-set-no" type="radio" v-model=" formData.is_part_of_set" :value="false"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300">
              <label for="part-of-set-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
        </div>

        <!-- Nombre del Juego -->
        <div v-if="formData.is_part_of_set">
          <label for="setName" class="block text-sm font-medium text-gray-700">Nombre del Juego</label>
          <input type="text" id="setName" v-model="formData.set_name"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12" required>
        </div>

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
            class="mt-1 block w-full shadow-sm sm:text-sm border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md resize-none"></textarea>
        </div>

        <!-- Botones: Validar Datos y Calcular Precio -->
        <div class="flex justify-between items-center mt-6">
          <button type="button" @click="validateAndShow" 
            class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Validar Datos
          </button>
          <div class="flex items-center space-x-2">
            <button type="button" @click="validateAndCalculatePrice"
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
            <p><strong>Nombre de la Pieza:</strong> {{ formData.piece_name }}</p>
            <p><strong>Peso:</strong> {{ formData.weight }} kg</p>
            <p><strong>Parte de un Juego:</strong> {{ formData.is_part_of_set }}</p>
            <p v-if="formData.is_part_of_set"><strong>Nombre del Juego:</strong> {{ formData.set_name }}</p>
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
      woodType: '', // Tipo de madera
      varnished: false , // Estado de barnizado
      piece_name: '', // Nombre de la pieza
      weight: null, // Peso de la pieza
      is_part_of_set: false, // Indica si es parte de un set
      set_name: '', // Nombre del set (si aplica)
      comments: '', // Comentarios adicionales
    });

    const showValidatedWindow = ref(false);
    const price = ref(0);

    const getToken = () => {
      return localStorage.getItem('token');
    };

    const validateForm = () => {
      if (!formData.woodType) {
        alert('Por favor, selecciona un tipo de madera.');
        return false;
      }
      if (!formData.piece_name) {
        alert('Por favor, ingresa el nombre de la pieza.');
        return false;
      }
      if (formData.weight === null || formData.weight < 0) {
        alert('Por favor, ingresa un peso válido.');
        return false;
      }
      if (formData.is_part_of_set && !formData.set_name) {
        alert('Por favor, ingresa el nombre del juego.');
        return false;
      }
      return true;
    };

    const createProduct = async () => {
      if (!validateForm()) return;

      try {
        const token = getToken();
        if (!token) {
          alert('No se encontró un token de autenticación.');
          return;
        }

        if (!price.value || price.value <= 0) {
          alert('El precio debe ser mayor que cero y debe estar definido.');
          return;
        }

        const payload = {
          wood_type: formData.woodType,
          is_varnished: formData.varnished,
          piece_name: formData.piece_name,
          weight: parseFloat(formData.weight),
          is_part_of_set: formData.is_part_of_set,
          set_name: formData.is_part_of_set ? formData.set_name : null,
          cost_price: parseFloat(price.value),
        };

        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        const response = await axios.post('http://localhost:8000/api/products/product-furniture-create/', payload, config);
        
        if (response.status === 201) {
          alert('Producto creado exitosamente');
          showValidatedWindow.value = false;
        } else {
          alert('Hubo un error al crear el producto.');
        }
      } catch (error) {
        console.error('Error al crear el producto:', error.response?.data || error);
        alert('Hubo un error al crear el producto.');
      }
    };

    const handleCalculatePrice = async () => {
      if (!validateForm()) return;

      try {
        const token = getToken();
        if (!token) {
          alert('No se encontró un token de autenticación. Por favor, inicia sesión.');
          return;
        }

        const payload = {
          wood_type: formData.woodType,
          is_varnished: formData.varnished,
          piece_name: formData.piece_name,
          weight: parseFloat(formData.weight),
          is_part_of_set: formData.is_part_of_set,
          set_name: formData.is_part_of_set ? formData.set_name : null,
        };

        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        const response = await axios.post(
          'http://localhost:8000/api/products/calcular-precio-mueble/',
          payload,
          config
        );

        if (response.data && response.data.cost_price) {
          price.value = response.data.cost_price.toFixed(2);
        } else {
          alert('No se pudo obtener el precio calculado.');
        }
      } catch (error) {
        console.error('Error al calcular el precio:', error.response?.data || error);
        alert('Hubo un error al calcular el precio. Por favor, verifica los datos.');
      }
    };

    const validateAndShow = () => {
      if (validateForm()) {
        showValidatedWindow.value = true;
      }
    };

    const validateAndCalculatePrice = () => {
      if (validateForm()) {
        handleCalculatePrice();
      }
    };

    return {
      formData,
      showValidatedWindow,
      price,
      handleCalculatePrice,
      createProduct,
      validateAndShow,
      validateAndCalculatePrice,
    };
  },
};
</script>