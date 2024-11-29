<template>
    <HeaderCompo />
    <div class="font-sans text-brown-800 bg-orange-50">
        <header class="header">
        </header>
        <main class="max-w-7xl mx-auto p-12">
            <!-- SERVICIOS DE CONSTRUCCIÓN -->
            <h2 class="text-2xl font-bold text-orange-800 text-center mb-6">Servicios de Construcción en Madera</h2>
            <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
                <div v-for="servicio in serviciosConstruccion" :key="servicio.id" class="bg-yellow-200 rounded-lg overflow-hidden shadow-lg transition-transform transform hover:-translate-y-1">
                    <img :src="servicio.imagen" :alt="servicio.titulo" class="w-full h-64 object-cover">
                    <div class="p-6">
                        <h3 class="text-xl font-semibold mb-3">{{ servicio.titulo }}</h3>
                        <p class="text-lg">{{ servicio.descripcion }}</p>
                    </div>
                </div>
            </section>

            <!-- PROYECTOS DESTACADOS -->
            <h2 class="text-2xl font-bold text-orange-800 text-center mb-6">Proyectos Destacados</h2>
            <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
                <div v-for="proyecto in proyectosDestacados" :key="proyecto.id" class="bg-orange-200 rounded-lg overflow-hidden shadow-md">
                    <img :src="proyecto.imagen" :alt="proyecto.titulo" class="w-full h-48 object-cover">
                    <div class="p-4">
                        <h4 class="text-lg font-semibold">{{ proyecto.titulo }}</h4>
                        <p>{{ proyecto.descripcion }}</p>
                    </div>
                </div>
            </section>

            <!-- PROCESO DE CONSTRUCCIÓN -->
            <section class="mb-12">
                <h3 class="text-xl font-bold mb-4">Nuestro Proceso de Construcción</h3>
                <ul class="timeline timeline-snap-icon max-md:timeline-compact timeline-vertical">
                    <li v-for="(paso, index) in procesoConstruccion" :key="index">
                        <hr />
                        <div class="timeline-middle">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" />
                            </svg>
                        </div>
                        <div class="timeline-start mb-10 md:text-end">
                            <time class="font-mono italic">{{ paso.titulo }}</time>
                            <div class="text-lg font-black">{{ paso.titulo }}</div>
                            {{ paso.descripcion }}
                        </div>
                        <hr />
                    </li>
                </ul>
            </section>

            <!-- LLAMADO A LA ACCIÓN -->
            <section class="bg-orange-200 rounded-lg p-8 text-center mt-12">
                <h3 class="text-xl font-bold">¿Listo para comenzar tu proyecto?</h3>
                <p>Nuestro equipo de expertos está listo para ayudarte a hacer realidad tu visión en madera.</p>
                <button 
                    @click="solicitarPresupuesto" 
                    class="inline-block bg-orange-600 text-white py-2 px-4 rounded mt-4 font-bold transition-colors duration-300 hover:bg-orange-700"
                >
                    Solicitar Presupuesto
                </button>
            </section>
        </main>

        <!-- Footer -->
        <Footer class="footer" />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import HeaderCompo from '@/components/HeaderCompo.vue';
import Footer from "@/components/FooterCompo.vue";
import iglesia from '@/assets/Muebledeinglesia.jpg';
import cost from '@/assets/Mueblecost.jpeg';
import puertasegura from '@/assets/puertasegura.jpeg';
import puertaconst from '@/assets/PuertasConstr.jpg';
import catedral from '@/assets/Ventanacatedral.jpeg';
import ventanaconst from '@/assets/Ventanacostr.jpeg';

const router = useRouter();

const solicitarPresupuesto = () => {
    router.push('/client'); // Redirige a la vista ClientView
};

const serviciosConstruccion = ref([
    {
        id: 1,
        titulo: "Construcción de Ventanas",
        descripcion: "Diseñamos y construimos ventanas de madera, ofreciendo una amplia variedad de estilos y acabados para complementar cualquier espacio.",
        imagen: cost
    },
    {
        id: 2,
        titulo: "Construcción de Muebles",
        descripcion: "Creamos muebles a medida con madera de alta calidad, combinando funcionalidad y diseño para adaptarse a las necesidades de cada cliente.",
        imagen: puertaconst
    },
    {
        id: 3,
        titulo: "Construcción de Puertas",
        descripcion: "Fabricamos puertas personalizadas con materiales de alta calidad, diseñadas para adaptarse a cualquier estilo arquitectónico y brindar seguridad.",
        imagen: ventanaconst
    }
]);

const proyectosDestacados = ref([
    {
        id: 1,
        titulo: "Muebles de Madera para Iglesias",
        descripcion: "Diseñamos y fabricamos muebles de madera exclusivos para iglesias, combinando tradición, resistencia y estética para ambientes sagrados.",
        imagen: catedral
    },
    {
        id: 2,
        titulo: "Ventanas para Catedrales",
        descripcion: "Creación de ventanas de madera para catedrales y espacios religiosos, con diseños artísticos y materiales que resisten el paso del tiempo.",
        imagen: iglesia
    },
    {
        id: 3,
        titulo: "Puertas Más Seguras de Perú",
        descripcion: "Ofrecemos puertas de seguridad premium, fabricadas con madera de alta calidad y sistemas de seguridad avanzados para protección total.",
        imagen: puertasegura
    }
]);

const procesoConstruccion = ref([
    {
        titulo: "Consulta y Planificación",
        descripcion: "Nos reunimos contigo para entender tus necesidades y objetivos, y desarrollamos un plan detallado del proyecto."
    },
    {
        titulo: "Diseño y Aprobación",
        descripcion: "Nuestro equipo de diseño crea planos detallados para tu aprobación."
    },
    {
        titulo: "Selección de Materiales",
        descripcion: "Elegimos cuidadosamente las mejores maderas y materiales sostenibles para tu proyecto."
    },
    {
        titulo: "Fabricación",
        descripcion: "Fabricamos los componentes necesarios en nuestro taller, asegurando la más alta calidad y precisión."
    },
    {
        titulo: "Construcción in situ",
        descripcion: "Nuestro equipo de expertos carpinteros y constructores lleva a cabo la construcción en el sitio del proyecto."
    },
    {
        titulo: "Control de Calidad",
        descripcion: "Realizamos rigurosas inspecciones de calidad en cada etapa del proceso de construcción."
    },
    {
        titulo: "Entrega y Garantía",
        descripcion: "Entregamos el proyecto terminado y ofrecemos garantía y servicio post-venta para tu tranquilidad."
    }
]);
</script>

<style scoped>
/* Aquí puedes agregar estilos adicionales si es necesario */
</style>
