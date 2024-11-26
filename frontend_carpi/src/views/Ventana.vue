<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Header with margin-bottom for spacing -->
    <Header class="mb-16" /> <!-- Added mb-16 to create space below the header -->

    <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-8">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-900">Diseña tu Puerta Personalizada</h2>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Tipo de Madera -->
        <div>
          <label for="woodType" class="block text-sm font-medium text-gray-700">Tipo de Madera</label>
          <select id="woodType" v-model="formData.woodType" required
            class="mt-1 block w-full pl-3 pr-10 py-2 text-base border border-gray-300 focus:outline-none focus:ring-amber-500 focus:border-amber-500 sm:text-sm rounded-md">
            <option value="">Selecciona un tipo de madera</option>
            <option value="Pino">Pino - S/. 100</option>
            <option value="Roble">Roble - S/. 150</option>
            <option value="Cedro">Cedro - S/. 200</option>
            <option value="Caoba">Caoba - S/. 180</option>
          </select>
          <p v-if="errors.woodType" class="text-red-500 text-xs italic">{{ errors.woodType }}</p>
        </div>

        <!-- Barnizado -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Barnizado</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="varnished-yes" type="radio" v-model="formData.varnished" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="varnished-yes" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="varnished-no" type="radio" v-model="formData.varnished" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="varnished-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
          <p v-if="errors.varnished" class="text-red-500 text-xs italic">{{ errors.varnished }}</p>
        </div>

        <!-- Dimensiones -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="length" class="block text-sm font-medium text-gray-700">Largo (cm)</label>
            <input type="number" id="length" v-model="formData.length" required min="100" max="300"
            class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
            <p v-if="errors.length" class="text-red-500 text-xs italic">{{ errors.length }}</p>
          </div>
          <div>
            <label for="width" class="block text-sm font-medium text-gray-700">Ancho (cm)</label>
            <input type="number" id="width" v-model="formData.width" required min="60" max="150"
            class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
            <p v-if="errors.width" class="text-red-500 text-xs italic">{{ errors.width }}</p>
          </div>
        </div>

        <!-- Exterior -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Exterior</label>
          <div class="mt-2 flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-10">
            <div class="flex items-center">
              <input id="exterior-yes" type="radio" v-model="formData.exterior" value="Si"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="exterior-yes" class="ml-3 block text-sm font-medium text-gray-700">Si</label>
            </div>
            <div class="flex items-center">
              <input id="exterior-no" type="radio" v-model="formData.exterior" value="No"
                class="focus:ring-amber-500 h-4 w-4 text-amber-600 border-gray-300" required>
              <label for="exterior-no" class="ml-3 block text-sm font-medium text-gray-700">No</label>
            </div>
          </div>
          <p v-if="errors.exterior" class="text-red-500 text-xs italic">{{ errors.exterior }}</p>
        </div>

        <!-- Número de hojas -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="number_of_sheets" class="block text-sm font-medium text-gray-700">Número de Hojas</label>
            <input type="number" id="number_of_sheets" v-model="formData.number_of_sheets" required min="1" max="5"
            class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
            <p v-if="errors.number_of_sheets" class="text-red-500 text-xs italic">{{ errors.number_of_sheets }}</p>
          </div>
        </div>

        <!-- Comentarios Adicionales -->
        <div>
          <label for="comments" class="block text-sm font-medium text-gray-700">Comentarios Adicionales</label>
          <textarea id="comments" v-model="formData.comments" rows="3"
          class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md resize-none p-1.5"></textarea>
        </div>

        <!-- Botones: Validar Datos y Calcular Precio -->
        <div class="flex justify-center items-center mt-6">
          <button type="button" @click="handleSubmit"
            class="py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500">
            Validar Datos
          </button>
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

      <section id="productos" class="py-16 px-6 bg-white">
        <div class="container mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Producto 1: Puertas -->
            <router-link to="/puerta" class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
              <h4 class="text-xl font-semibold mb-2">Puertas</h4>
            </router-link>

            <!-- Producto 2: Ventanas -->
            <router-link to="/ventana" class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
              <h4 class="text-xl font-semibold mb-2">Ventanas</h4>
            </router-link>

            <!-- Producto 3: Muebles -->
            <router-link to="/mueble" class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
              <h4 class="text-xl font-semibold mb-2">Muebles</h4>
            </router-link>
          </div>
        </div>
      </section>
    </div>

    <!-- Footer with margin-top for spacing -->
    <Footer class="footer mt-28" /> <!-- Added mt-16 to create space above the footer -->
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";
import { useRouter } from 'vue-router';

export default {
  components: {
    Header,
    Footer,
  },
  setup() {
    const router = useRouter();
    
    // Verificar si el token está presente
    onMounted(() => {
      const token = localStorage.getItem('token');
      if (!token) {
        router.push('/registro'); // Redirige si no hay token
      }
    });

    const formData = reactive({
      woodType: '',
      varnished: '',
      length: '',
      width: '',
      exterior: '',
      number_of_sheets: '',
      comments: '',
    });

    const errors = reactive({
      woodType: '',
      varnished: '',
      length: '',
      width: '',
      exterior: '',
      number_of_sheets: '',
    });

    const showValidatedWindow = ref(false);
    const price = ref(0);

    const validateForm = () => {
      let isValid = true;
      Object.keys(errors).forEach(key => errors[key] = '');
      
      if (!formData.woodType) {
        errors.woodType = 'El tipo de madera es obligatorio.';
        isValid = false;
      }
      if (!formData.varnished) {
        errors.varnished = 'Debes seleccionar si está barnizado.';
        isValid = false;
      }
      if (!formData.length || formData.length < 100 || formData.length > 300) {
        errors.length = 'El largo debe estar entre 100 y 300 cm.';
        isValid = false;
      }
      if (!formData.width || formData.width < 60 || formData.width > 150) {
        errors.width = 'El ancho debe estar entre 60 y 150 cm.';
        isValid = false;
      }
      if (!formData.exterior) {
        errors.exterior = 'Debes seleccionar si es exterior.';
        isValid = false;
      }
      if (!formData.number_of_sheets || formData.number_of_sheets < 1 || formData.number_of_sheets > 5) {
        errors.number_of_sheets = 'El número de hojas debe estar entre 1 y 5.';
        isValid = false;
      }

      return isValid;
    };

    const handleSubmit = async () => {
      if (validateForm()) {
        try {
          // Calcular el precio antes de mostrar la ventana modal
          await handleCalculatePrice();
          showValidatedWindow.value = true;
        } catch (error) {
          console.error('Error al calcular el precio:', error);
          alert('Hubo un error al calcular el precio. Por favor, verifica los datos.');
        }
      }
    };

    const createProduct = async () => {
      try {
        const token = localStorage.getItem('token');
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
          console.log('Respuesta del servidor:', response.data.product_id);
          localStorage.setItem('product_id', response.data.product_id);
          alert('Producto creado exitosamente');
          showValidatedWindow.value = false;
          router.push('/delivery');
        } else {
          alert('Hubo un error al crear el producto.');
        }
      } catch (error) {
        console.error('Error al crear el producto:', error);
        alert('Hubo un error al crear el producto.');
      }
    };

    const handleCalculatePrice = async () => {
      try {
        const token = localStorage.getItem('token');
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
        throw error; // Re-lanzar el error para manejarlo en handleSubmit
      }
    };

    return {
      formData,
      errors,
      showValidatedWindow,
      price,
      handleCalculatePrice,
      createProduct,
      handleSubmit,
    };
  },
};
</script>
