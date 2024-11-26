<template>
    <div class="carpinteria">
        <!-- Header Componente -->
        <Header />

        <main class="content">
            <h2>Nuestros Servicios de Carpintería</h2>

            <section class="servicios">
                <div v-for="servicio in servicios" :key="servicio.id" class="servicio-card">
                    <img :src="servicio.imagen" :alt="servicio.nombre" class="servicio-imagen">
                    <h3>{{ servicio.nombre }}</h3>
                    <p>{{ servicio.descripcion }}</p>
                </div>
            </section>

            <section class="proyectos-destacados">
                <h2>Proyectos Destacados</h2>
                <div class="proyecto-grid">
                    <div v-for="proyecto in proyectosDestacados" :key="proyecto.id" class="proyecto-card">
                        <img :src="proyecto.imagen" :alt="proyecto.nombre" class="proyecto-imagen">
                        <div class="proyecto-info">
                            <h3>{{ proyecto.nombre }}</h3>
                            <p>{{ proyecto.descripcion }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <section class="galeria">
                <h2>Galería de Trabajos</h2>
                <div class="galeria-grid">
                    <div v-for="(imagen, index) in galeriaImagenes" :key="index" class="galeria-item">
                        <img :src="imagen" :alt="`Trabajo de carpintería ${index + 1}`" @click="abrirModal(index)">
                    </div>
                </div>
            </section>

            <div v-if="modalAbierto" class="modal" @click="cerrarModal">
                <img :src="galeriaImagenes[imagenActual]" :alt="`Trabajo de carpintería ${imagenActual + 1}`"
                    class="modal-imagen">
            </div>
        </main>

        <!-- Footer Componente -->
        <Footer />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";

const servicios = ref([
    { id: 1, nombre: 'Muebles a Medida', descripcion: 'Diseñamos y fabricamos muebles personalizados para tu hogar u oficina.', imagen: '/placeholder.svg?height=200&width=300' },
    { id: 2, nombre: 'Restauración', descripcion: 'Devolvemos la vida a tus muebles antiguos o dañados.', imagen: '/placeholder.svg?height=200&width=300' },
    { id: 3, nombre: 'Carpintería Estructural', descripcion: 'Realizamos trabajos de carpintería para construcciones y remodelaciones.', imagen: '/placeholder.svg?height=200&width=300' },
    { id: 4, nombre: 'Acabados en Madera', descripcion: 'Ofrecemos una variedad de acabados para proteger y embellecer tus muebles.', imagen: '/placeholder.svg?height=200&width=300' },
]);

const proyectosDestacados = ref([
    { id: 1, nombre: 'Cocina Integral Moderna', descripcion: 'Diseño y fabricación de cocina integral con isla central.', imagen: '/placeholder.svg?height=300&width=400' },
    { id: 2, nombre: 'Biblioteca Clásica', descripcion: 'Restauración y ampliación de biblioteca de roble del siglo XIX.', imagen: '/placeholder.svg?height=300&width=400' },
]);

const galeriaImagenes = ref([
    '/placeholder.svg?height=200&width=200',
    '/placeholder.svg?height=200&width=200',
    '/placeholder.svg?height=200&width=200',
    '/placeholder.svg?height=200&width=200',
    '/placeholder.svg?height=200&width=200',
    '/placeholder.svg?height=200&width=200',
]);

const modalAbierto = ref(false);
const imagenActual = ref(0);

const abrirModal = (index) => {
    imagenActual.value = index;
    modalAbierto.value = true;
};

const cerrarModal = () => {
    modalAbierto.value = false;
};
</script>

<style scoped>
.carpinteria {
    font-family: 'Arial', sans-serif;
    color: #5D4037;
    background-color: #FFF3E0;
}

.header {
    background-color: #FF9800;
    padding: 2rem;
    text-align: center;
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

h2 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
}

.servicios {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.servicio-card {
    background-color: #FFECB3;
    border-radius: 8px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.servicio-imagen {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.proyectos-destacados {
    margin-bottom: 3rem;
}

.proyecto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.proyecto-card {
    background-color: #FFE0B2;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.proyecto-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.proyecto-info {
    padding: 1.5rem;
}

.galeria-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1rem;
}

.galeria-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.galeria-item img:hover {
    transform: scale(1.05);
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-imagen {
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
}

.footer {
    background-color: #FF9800;
    color: #FFF3E0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}

@media (max-width: 768px) {

    .servicios,
    .proyecto-grid {
        grid-template-columns: 1fr;
    }
}
</style>