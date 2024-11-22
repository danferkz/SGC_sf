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
                <textarea v-model="comentarios" class="textarea textarea-bordered h-24" placeholder="Notas sobre la entrega"></textarea>
              </div>
            </div>
          </div>
        </div>

        <!-- Botón para Aceptar Delivery -->
        <div class="flex justify-end">
          <button @click="aceptarDelivery" class="btn btn-primary">Ordenar</button>
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

export default {
  components: {
    Header,
  },
  setup() {
    const router = useRouter();
    const producto = ref({});
    const deseaDelivery = ref(false);
    const fechaEntrega = ref('');
    const comentarios = ref('');
    const rawProductData = ref(null);

    onMounted(async () => {
      try {
        const productId = localStorage.getItem('product_id');
        const token = localStorage.getItem('token');

        if (!productId || !token) {
          router.push('/login');
          return;
        }

        const response = await axios.get(
          `http://localhost:8000/api/products/product/${productId}`,
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        rawProductData.value = response.data;
        mapProductData(response.data);
      } catch (error) {
        console.error('Error fetching product:', error);
        router.push('/productos');
      }
    });

    const mapProductData = (data) => {
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
          productId: data.product_id,
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
    };

    const aceptarDelivery = async () => {
      try {
        const token = localStorage.getItem('token');
        const userId = localStorage.getItem('userId');

        // Prepare Delivery Data dynamically
        const deliveryData = {
          delivery_date: deseaDelivery.value ? fechaEntrega.value : null,
          delivery_notes: comentarios.value,
          delivery_option: deseaDelivery.value
        };

        // Dynamically add furniture or door_window based on product type
        if (rawProductData.value.product_type === 'furniture') {
          deliveryData.furniture = producto.value.productId;
        } else if (rawProductData.value.product_type === 'door') {
          deliveryData.door_window = producto.value.productId;
        } else if (rawProductData.value.product_type === 'window') {
          deliveryData.door_window = producto.value.productId;
        }

        // Create Delivery
        const deliveryResponse = await axios.post(
          'http://localhost:8000/api/deliveries/create/', 
          deliveryData, 
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json'
            }
          }
        );

        // Create Order
        if (deliveryResponse.status === 201) {
          // Use the selected delivery date and add one year to it
          const selectedDate = new Date(fechaEntrega.value);
          selectedDate.setFullYear(selectedDate.getFullYear() + 1);
          const formattedPromisedDate = selectedDate.toISOString().split('T')[0];

          const orderData = {
            client: userId,
            product: producto.value.productId,
            delivery: deliveryResponse.data.delivery_id,
            promised_date: formattedPromisedDate
          };

          const orderResponse = await axios.post(
            'http://localhost:8000/api/orders/orders-create/', 
            orderData, 
            {
              headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json'
              }
            }
          );

          if (orderResponse.status === 201) {
            router.push('/cliente');
          }
        }
      } catch (error) {
        console.error('Error creating delivery/order:', error);
        alert('Hubo un problema al procesar su pedido.');
      }
    };

    return {
      producto,
      deseaDelivery,
      fechaEntrega,
      comentarios,
      aceptarDelivery
    };
  }
};
</script>