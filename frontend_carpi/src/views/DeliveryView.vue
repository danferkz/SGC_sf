<template>
  <div class="min-h-screen bg-gradient-to-br from-LightSalmon-100 to-green-100 p-8">
    <Header />
    <div class="max-w-4xl mx-auto bg-white rounded-2xl shadow-xl overflow-hidden">
      <div class="p-8 space-y-8">
        <!-- Datos del Producto -->
        <div class="bg-LightSalmon-50 p-6 rounded-xl shadow-md">
          <h2 class="text-2xl font-bold mb-4 text-IndianRed-800">Datos del Producto</h2>
          <template v-if="producto.tipoProducto === 'Mueble'">
            <div class="space-y-2">
              <p><span class="font-semibold">ID del Producto:</span> {{ producto.productId }}</p>
              <p><span class="font-semibold">Tipo de Producto:</span> {{ producto.tipoProducto }}</p>
              <p><span class="font-semibold">Tipo de Madera:</span> {{ producto.tipoMadera }}</p>
              <p><span class="font-semibold">Barnizado:</span> {{ producto.barnizado }}</p>
              <p><span class="font-semibold">Nombre de la Pieza:</span> {{ producto.nombrePieza }}</p>
              <p><span class="font-semibold">Peso:</span> {{ producto.peso }}</p>
              <p><span class="font-semibold">¿Parte de un Set?:</span> {{ producto.parteDeSet }}</p>
              <p><span class="font-semibold">Nombre del Set:</span> {{ producto.nombreSet }}</p>
              <p><span class="font-semibold">Costo:</span> {{ producto.costo }}</p>
            </div>
          </template>
          <template v-else>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="space-y-2">
                <p><span class="font-semibold">ID del Producto:</span> {{ producto.productId }}</p>
                <p><span class="font-semibold">Tipo de Producto:</span> {{ producto.tipoProducto }}</p>
                <p><span class="font-semibold">Tipo de Madera:</span> {{ producto.tipoMadera }}</p>
                <p><span class="font-semibold">Barnizado:</span> {{ producto.barnizado }}</p>
                <p><span class="font-semibold">Largo:</span> {{ producto.largo }}</p>
              </div>
              <div class="space-y-2">
                <p><span class="font-semibold">Ancho:</span> {{ producto.ancho }}</p>
                <p><span class="font-semibold">Exterior:</span> {{ producto.exterior }}</p>
                <p><span class="font-semibold">Número de Hojas:</span> {{ producto.numHojas }}</p>
                <p><span class="font-semibold">Costo:</span> {{ producto.costo }}</p>
              </div>
            </div>
          </template>
        </div>

        <!-- Opciones de Delivery -->
        <div class="bg-IndianRed-50 p-6 rounded-xl shadow-md">
          <h2 class="text-2xl font-bold mb-4 text-IndianRed-800">Delivery</h2>
          <div class="space-y-4">
            <div class="form-control">
              <label class="label">
                <span class="label-text font-semibold">¿Desea delivery?</span>
              </label>
              <div class="flex space-x-4">
                <label class="label cursor-pointer">
                  <input v-model="deseaDelivery" type="radio" name="delivery" :value="true" class="radio radio-primary" />
                  <span class="label-text ml-2">Sí</span>
                </label>
                <label class="label cursor-pointer">
                  <input v-model="deseaDelivery" type="radio" name="delivery" :value="false" class="radio radio-primary" />
                  <span class="label-text ml-2">No</span>
                </label>
              </div>
            </div>
            <div v-if="deseaDelivery" class="space-y-4">
              <div class="form-control">
                <label class="label">
                  <span class="label-text font-semibold">Fecha de Entrega</span>
                </label>
                <input v-model="fechaEntrega" type="date" class="input input-bordered w-full h-12" />
              </div>
              <div class="form-control">
                <label class="label">
                  <span class="label-text font-semibold">Comentarios</span>
                </label>
                <textarea v-model="comentarios" class="block text-sm font-medium text-white-700 resize-none"></textarea>
              </div>
              <button @click="confirmarDelivery" class="btn btn-primary w-full">Aceptar Delivery</button>
            </div>
          </div>
        </div>

        <!-- Botón de Ordenar -->
        <div class="text-center">
          <button @click="confirmarOrden" class="btn btn-lg btn-accent hover:btn-accent-focus transition duration-300 ease-in-out transform hover:scale-105">
            Ordenar
          </button>
        </div>
      </div>
    </div>

    <!-- Modales de Confirmación -->
    <div v-if="showDeliveryModal" class="modal modal-open">
      <div class="modal-box bg-white rounded-lg shadow-xl">
        <h3 class="font-bold text-lg text-white-800">Confirmación de Delivery</h3>
        <p class="py-4">¿Desea confirmar el delivery?</p>
        <div class="modal-action">
          <button @click="aceptarDelivery" class="btn btn-primary">Aceptar</button>
          <button @click="cancelarDelivery" class="btn btn-outline">Cancelar</button>
        </div>
      </div>
    </div>
    <div v-if="showOrdenModal" class="modal modal-open">
      <div class="modal-box bg-white rounded-lg shadow-xl">
        <h3 class="font-bold text-lg text-green-800">Confirmación de Orden</h3>
        <p class="py-4">¿Desea confirmar la orden?</p>
        <div class="modal-action">
          <button @click="aceptarOrden" class="btn btn-accent">Aceptar</button>
          <button @click="cancelarOrden" class="btn btn-outline">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Header from "@/components/HeaderCompo.vue";

const getToken = () => {
  return localStorage.getItem('token');
};

export default {
  components: {
    Header,
  },
  setup() {
    const router = useRouter();

    const producto = ref({
      productId: '',
      tipoProducto: '',
      tipoMadera: '',
      barnizado: '',
      largo: '',
      ancho: '',
      exterior: '',
      numHojas: '',
      costo: '',
      nombrePieza: '',
      peso: '',
      parteDeSet: '',
      nombreSet: ''
    });

    const deseaDelivery = ref(false);
    const fechaEntrega = ref('');
    const comentarios = ref('');
    const showDeliveryModal = ref(false);
    const showOrdenModal = ref(false);

    onMounted(async () => {
      try {
        const productId = localStorage.getItem('product_id');
        const token = getToken();

        const response = await axios.get(
          `http://localhost:8000/api/products/product/${productId}`,
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        const data = response.data;

        if (data.product_type === 'furniture') {
          producto.value = {
            productId: data.product_id,
            tipoProducto: 'Mueble',
            tipoMadera: data.wood_type,
            barnizado: data.is_varnished ? 'Sí' : 'No',
            nombrePieza: data.piece_name || 'N/A',
            peso: `${data.weight} Kg`,
            parteDeSet: data.is_part_of_set ? 'Sí' : 'No',
            nombreSet: data.set_name || 'N/A',
            costo: `$${parseFloat(data.cost_price).toFixed(2)}`
          };
        } else {
          producto.value = {
            productId : data.product_id,
            tipoProducto: data.product_type === 'door' ? 'Puerta' : 'Ventana',
            tipoMadera: data.wood_type,
            barnizado: data.is_varnished ? 'Sí' : 'No',
            largo: `${data.length} cm`,
            ancho: `${data.width} cm`,
            exterior: data.is_exterior ? 'Sí' : 'No',
            numHojas: data.number_of_sheets,
            costo: `$${parseFloat(data.cost_price).toFixed(2)}`
          };
        }
      } catch (error) {
        console.error('Error fetching product:', error);
      }
    });

    const confirmarDelivery = () => {
      showDeliveryModal.value = true;
    };

    const aceptarDelivery = () => {
      showDeliveryModal.value = false;
    };

    const cancelarDelivery = () => {
      showDeliveryModal.value = false;
    };

    const confirmarOrden = () => {
      showOrdenModal.value = true;
    };

    const aceptarOrden = () => {
      showOrdenModal.value = false;
      router.push({ name: 'ClientePerfil' });
    };

    const cancelarOrden = () => {
      showOrdenModal.value = false;
    };

    return {
      producto,
      deseaDelivery,
      fechaEntrega,
      comentarios,
      showDeliveryModal,
      showOrdenModal,
      confirmarDelivery,
      aceptarDelivery,
      cancelarDelivery,
      confirmarOrden,
      aceptarOrden,
      cancelarOrden
    };
  }
};
</script>

<style>
/* Añade estilos según tus necesidades */
</style>