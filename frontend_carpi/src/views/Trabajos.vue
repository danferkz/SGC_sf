<template>
    <div class="trabajos font-sans text-brown-800 bg-orange-100">
        <Header class="" />

        <main class="content max-w-5xl mx-auto p-8">
            <h2 class="text-orange-800 text-center text-3xl mb-8">Nuestros Trabajos</h2>

            <div class="filtros flex justify-center flex-wrap gap-4 mb-8">
                <button
                    v-for="categoria in categorias"
                    :key="categoria"
                    @click="filtrarPor(categoria)"
                    :class="{
                        'bg-orange-300 text-white': categoriaActual === categoria,
                        'bg-orange-200': categoriaActual !== categoria
                    }"
                    class="filtro-btn border-none py-2 px-4 rounded-full cursor-pointer transition duration-300 ease-in-out"
                >
                    {{ categoria }}
                </button>
            </div>

            <div class="trabajos-grid grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                <div
                    v-for="trabajo in trabajosFiltrados"
                    :key="trabajo.id"
                    class="trabajo-card bg-yellow-200 rounded-lg overflow-hidden shadow-lg cursor-pointer transition-transform duration-300 ease-in-out hover:transform hover:-translate-y-1"
                    @click="seleccionarTrabajo(trabajo)"
                >
                    <img :src="trabajo.imagen" :alt="trabajo.titulo" class="trabajo-imagen w-full h-48 object-cover">
                    <div class="trabajo-info p-4">
                        <h3 class="text-orange-800">{{ trabajo.titulo }}</h3>
                        <p>{{ trabajo.descripcionCorta }}</p>
                    </div>
                </div>
            </div>

            <div v-if="trabajoSeleccionado" class="modal fixed inset-0 bg-black bg-opacity-80 flex justify-center items-center z-50" @click="cerrarModal">
                <div class="modal-content bg-orange-100 p-8 rounded-lg max-w-lg w-full max-h-[90vh] overflow-y-auto relative" @click.stop>
                    <button class="cerrar-btn absolute top-2 right-2 bg-transparent border-none text-brown-800 text-2xl cursor-pointer" @click="cerrarModal" aria-label="Cerrar modal">&times;</button>
                    <img :src="trabajoSeleccionado.imagen" :alt="trabajoSeleccionado.titulo" class="modal-imagen w-full h-auto rounded-lg mb-4">
                    <h3 class="text-orange-800">{{ trabajoSeleccionado.titulo }}</h3>
                    <p>{{ trabajoSeleccionado.descripcionLarga }}</p>
                    <ul class="detalles-lista list-none p-0">
                        <li><strong>Cliente:</strong> {{ trabajoSeleccionado.cliente }}</li>
                        <li><strong>Fecha:</strong> {{ trabajoSeleccionado.fecha }}</li>
                        <li><strong>Categoría:</strong> {{ trabajoSeleccionado.categoria }}</li>
                    </ul>
                </div>
            </div>
        </main>

        <Footer class="footer mt-40" /> 
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";
import Ventanadoble from '@/assets/Ventanadoble.jpeg';
import puertaconst from '@/assets/PuertasConstr.jpg';
import tv from '@/assets/tv.jpeg';
import Mueblecost from '@/assets/Mueblecost.jpeg';

const categorias = ['Todos', 'Muebles'];
const categoriaActual = ref('Todos');

const trabajos = ref([
    {
        id: 1,
        titulo: 'Puerta de Madera Personalizada',
        descripcionCorta: 'Diseño y fabricación de puerta de madera a medida con acabados personalizados.',
        descripcionLarga: 'Puerta de madera maciza de roble, con diseño exclusivo y acabados personalizados según las preferencias del cliente. Ideal para entradas principales o interiores. Incluye herrajes de alta calidad y acabado en barniz mate.',
        imagen: puertaconst,
        cliente: 'Familia Sánchez',
        fecha: 'Julio 2023',
        categoria: 'Puertas'
    },
    {
        id: 2,
        titulo: 'Ventanas de Madera con Doble Cristal',
        descripcionCorta: 'Fabricación e instalación de ventanas de madera con doble cristal para mayor aislamiento.',
        descripcionLarga: 'Ventanas de madera de pino con doble cristal para mejorar la eficiencia energética. El diseño combina estética y funcionalidad, ofreciendo una excelente resistencia a las inclemencias del tiempo y un aislamiento acústico superior.',
        imagen: Ventanadoble,
        cliente: 'Residencial Altavista',
        fecha: 'Agosto 2023',
        categoria: 'Ventanas'
    },
    {
        id: 3,
        titulo: 'Mueble de TV en Madera Maciza',
        descripcionCorta: 'Mueble de TV personalizado en madera maciza con compartimentos para almacenamiento.',
        descripcionLarga: 'Mueble de TV hecho a medida en madera de roble, con acabados en barniz natural. Incluye compartimentos de almacenamiento y espacio para dispositivos electrónicos. Diseño minimalista y moderno que se adapta a cualquier estilo de sala de estar.',
        imagen: tv,
        cliente: 'Oficina XYZ',
        fecha: 'Septiembre 2023',
        categoria: 'Muebles'
    },
    {
        id: 4,
        titulo: 'Mueble de Almacenamiento para Oficina',
        descripcionCorta: 'Diseño y fabricación de mueble de almacenamiento para oficina con acabados en madera de pino.',
        descripcionLarga: 'Mueble de almacenamiento multifuncional para oficina, hecho en madera de pino con acabados en aceite natural. Con estantes ajustables y espacio suficiente para archivadores y materiales de oficina. Perfecto para mantener un ambiente ordenado y profesional.',
        imagen: Mueblecost,
        cliente: 'Creative Solutions',
        fecha: 'Octubre 2023',
        categoria: 'Muebles'
    }
]);

const trabajosFiltrados = computed(() => {
    if (categoriaActual.value === 'Todos') {
        return trabajos.value;
    }
    return trabajos.value.filter(trabajo => trabajo.categoria === categoriaActual.value);
});

const trabajoSeleccionado = ref(null);

const filtrarPor = (categoria) => {
    categoriaActual.value = categoria;
};

const seleccionarTrabajo = (trabajo) => {
    trabajoSeleccionado.value = trabajo;
};

const cerrarModal = () => {
    trabajoSeleccionado.value = null;
};
</script>

<style scoped>
/* No se requieren estilos personalizados ya que Tailwind CSS maneja el diseño */
</style>