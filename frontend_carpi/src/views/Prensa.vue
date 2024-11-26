<template>
    <HeaderCompo />
    <div class="bg-gray-50 text-gray-800">
        <main class="max-w-6xl mx-auto px-4 py-8">
            <h2 class="text-3xl font-bold text-center mb-8">Prensa y Medios</h2>

            <!-- Noticias Destacadas -->
            <section class="mb-12">
                <h3 class="text-2xl font-semibold mb-4">Noticias Destacadas</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <article v-for="noticia in noticiasDestacadas" :key="noticia.id"
                        class="bg-white shadow-lg rounded-lg overflow-hidden">
                        <img :src="noticia.imagen" :alt="noticia.titulo" class="w-full h-48 object-cover" />
                        <div class="p-4">
                            <h4 class="text-lg font-semibold mb-2">{{ noticia.titulo }}</h4>
                            <p class="text-sm text-gray-500 mb-2">{{ noticia.fecha }}</p>
                            <p class="text-gray-700 mb-4">{{ noticia.resumen }}</p>
                            <a :href="noticia.enlace" target="_blank" rel="noopener noreferrer"
                                class="text-blue-600 font-medium hover:underline">
                                Leer más
                            </a>
                        </div>
                    </article>
                </div>
            </section>

            <!-- Menciones en Prensa -->
            <section class="mb-12">
                <h3 class="text-2xl font-semibold mb-4">Menciones en Prensa</h3>
                <ul class="space-y-6">
                    <li v-for="mencion in mencionesPrensaOrdenadas" :key="mencion.id"
                        class="bg-white shadow-md rounded-lg p-4 flex flex-col">
                        <div class="text-sm text-gray-500 mb-2">{{ mencion.fecha }}</div>
                        <div>
                            <h4 class="text-lg font-semibold mb-2">{{ mencion.titulo }}</h4>
                            <p class="text-gray-700 mb-4">{{ mencion.descripcion }}</p>
                            <a :href="mencion.enlace" target="_blank" rel="noopener noreferrer"
                                class="text-blue-600 font-medium hover:underline">
                                Ver artículo completo
                            </a>
                        </div>
                    </li>
                </ul>
            </section>

            <!-- Kit de Prensa -->
            <section class="mb-12 text-center">
                <h3 class="text-2xl font-semibold mb-4">Kit de Prensa</h3>
                <p class="text-gray-700 mb-6">
                    Descarga nuestro kit de prensa para obtener información detallada
                    sobre Maderera el Bosque, incluyendo nuestra historia, logotipos y
                    fotos de alta resolución.
                </p>
                <a href="#" class="bg-blue-600 text-white py-2 px-6 rounded-md shadow-md hover:bg-blue-700"
                    @click.prevent="descargarKitPrensa">
                    Descargar Kit de Prensa
                </a>
            </section>
        </main>

        <!-- Footer -->
        <Footer class="footer" />
    </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import HeaderCompo from '@/components/HeaderCompo.vue';
import Footer from "@/components/FooterCompo.vue";

const noticiasDestacadas = ref([
    {
        id: 1,
        titulo: "Maderera el bosque gana premio a la innovación en diseño sustentable",
        fecha: "15 de Noviembre, 2023",
        resumen: "Nuestro proyecto de muebles reciclados ha sido reconocido por su contribución a la economía circular en la industria de la madera.",
        imagen: "/placeholder.svg?height=200&width=300",
        enlace: "#"
    },
    {
        id: 2,
        titulo: "Colaboración exclusiva con diseñador internacional",
        fecha: "3 de Octubre, 2023",
        resumen: "Maderera el bosque se asocia con el renombrado diseñador Max Wood para crear una línea de muebles de lujo ecológicos.",
        imagen: "/placeholder.svg?height=200&width=300",
        enlace: "#"
    },
    {
        id: 3,
        titulo: "Expansión de nuestras instalaciones para aumentar la producción sostenible",
        fecha: "20 de Septiembre, 2023",
        resumen: "Inauguramos una nueva planta de producción que utiliza energía 100% renovable, duplicando nuestra capacidad de fabricación.",
        imagen: "/placeholder.svg?height=200&width=300",
        enlace: "#"
    }
]);

const mencionesPrensaOrdenadas = computed(() => {
    return [
        {
            id: 1,
            fecha: "5 de Diciembre, 2023",
            titulo: "Maderera el bosque lidera la transformación ecológica del sector",
            descripcion: "Artículo en 'Eco Construcción' sobre nuestras prácticas sostenibles y su impacto en la industria.",
            enlace: "#"
        },
        {
            id: 2,
            fecha: "18 de Noviembre, 2023",
            titulo: "La artesanía moderna: Entrevista con el fundador de Maderera el bosque",
            descripcion: "Perfil en profundidad en la revista 'Diseño y Madera' sobre nuestra filosofía y proceso de trabajo.",
            enlace: "#"
        },
        {
            id: 3,
            fecha: "2 de Octubre, 2023",
            titulo: "Los 10 mejores fabricantes de muebles sostenibles",
            descripcion: "Maderera el bosque ocupa el tercer lugar en la lista anual de 'Green Living Magazine'.",
            enlace: "#"
        },
        {
            id: 4,
            fecha: "14 de Septiembre, 2023",
            titulo: "Cómo Maderera el bosque está revolucionando la carpintería tradicional",
            descripcion: "Reportaje especial en el periódico local sobre nuestra combinación de técnicas tradicionales y tecnología moderna.",
            enlace: "#"
        }
    ].sort((a, b) => new Date(b.fecha) - new Date(a.fecha));
});

const descargarKitPrensa = () => {
    // Aquí iría la lógica para descargar el kit de prensa
    alert("Descargando Kit de Prensa...");
};
</script>

<style scoped>
.prensa {
    font-family: 'Arial', sans-serif;
    color: #5D4037;
    background-color: #FFF3E0;
}



h1 {
    color: #FFF3E0;
    font-size: 2.5rem;
    margin: 0;
}

.content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

h2,
h3 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
}

.noticias-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.noticia-card {
    background-color: #FFECB3;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.noticia-card:hover {
    transform: translateY(-5px);
}

.noticia-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.noticia-contenido {
    padding: 1rem;
}

.noticia-fecha {
    font-style: italic;
    color: #8D6E63;
    margin-bottom: 0.5rem;
}

.menciones-lista {
    list-style-type: none;
    padding: 0;
}

.mencion-item {
    background-color: #FFE0B2;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
}

.mencion-fecha {
    min-width: 120px;
    font-weight: bold;
    color: #E65100;
}

.mencion-contenido {
    flex-grow: 1;
}

.kit-prensa {
    background-color: #FFECB3;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    margin-top: 3rem;
}

.boton-descarga {
    display: inline-block;
    background-color: #FF9800;
    color: #FFF3E0;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 1rem;
    transition: background-color 0.3s ease;
}

.boton-descarga:hover {
    background-color: #E65100;
}

.leer-mas {
    display: inline-block;
    color: #E65100;
    text-decoration: none;
    font-weight: bold;
    margin-top: 0.5rem;
}

.leer-mas:hover {
    text-decoration: underline;
}



@media (max-width: 768px) {
    .mencion-item {
        flex-direction: column;
    }

    .mencion-fecha {
        margin-bottom: 0.5rem;
    }
}
</style>