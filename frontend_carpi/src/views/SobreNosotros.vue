<template>
    <div class="font-sans text-brown-800 bg-orange-50">
        <!-- Header Componente -->
        <Header class="mb-6" />

        <main class="max-w-7xl mx-auto p-16">
            <section class="bg-yellow-200 p-12 rounded-lg mb-16">
                <h2 class="text-orange-600 text-4xl mb-6">Sobre Nosotros</h2>
                <p class="text-lg mb-4 leading-relaxed">
                    En Maderera el bosque, nos apasiona trabajar con la madera y crear piezas únicas que
                    combinen belleza y funcionalidad. Con más de 20 años de experiencia, nos hemos
                    convertido en expertos en el arte de la carpintería.
                </p>
                <p class="text-lg leading-relaxed">
                    Nuestro equipo de artesanos altamente calificados se dedica a producir muebles de
                    alta calidad, puertas, ventanas y todo tipo de trabajos en madera, siempre
                    respetando el medio ambiente y utilizando materiales sostenibles.
                </p>
            </section>

            <!-- Galería de imágenes -->
            <h2 class="text-orange-600 text-4xl mb-8">Galería de Imágenes</h2>
            <section class="flex flex-wrap justify-between gap-8 mb-12">
                <div v-for="(image, index) in images" :key="index" class="w-full md:w-[45%] lg:w-[30%]">
                    <div class="overflow-hidden rounded-lg shadow transition-transform duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg">
                        <img :src="image.src" :alt="image.alt" class="w-full h-96 object-cover" />
                    </div>
                </div>
            </section>

            <section class="bg-orange-200 p-8 rounded-lg">
                <h3 class="text-orange-600">Nuestros Servicios</h3>
                <ul class="list-none pl-0">
                    <li class="mb-2 pl-6 relative">
                        Diseño y fabricación de muebles a medida
                        <span class="absolute left-0">🌳</span>
                    </li>
                    <li class="mb-2 pl-6 relative">
                        Restauración de muebles antiguos
                        <span class="absolute left-0">🌳</span>
                    </li>
                    <li class="mb-2 pl-6 relative">
                        Carpintería para interiores y exteriores
                        <span class="absolute left-0">🌳</span>
                    </li>
                    <li class="mb-2 pl-6 relative">
                        Asesoramiento personalizado
                        <span class="absolute left-0">🌳</span>
                    </li>
                </ul>
            </section>
        </main>

        <!-- Footer Componente -->
        <Footer />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";
import taller from '@/assets/taller.jpg';
import artesano from '@/assets/artesano.jpg';
import muebles_2 from '@/assets/muebles_2.jpeg';

const images = ref([
    { src: taller, alt: 'Taller de carpintería' },
    { src: artesano, alt: 'Artesano trabajando' },
    { src: muebles_2, alt: 'Muebles terminados' },
]);
</script>

<style scoped>
/* Puedes eliminar el estilo CSS existente, ya que ahora estamos usando Tailwind CSS */
</style>