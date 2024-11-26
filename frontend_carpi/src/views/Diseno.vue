<template>
    <div class="diseno">
        <!-- COMPONENTE HEADER -->
        <Header />

        <main class="content">
            <h2>Nuestro Proceso de Diseño</h2>

            <section class="proceso-diseno">
                <div v-for="(paso, index) in pasosProceso" :key="index" class="paso-diseno">
                    <div class="paso-numero">{{ index + 1 }}</div>
                    <div class="paso-contenido">
                        <h3>{{ paso.titulo }}</h3>
                        <p>{{ paso.descripcion }}</p>
                    </div>
                </div>
            </section>

            <section class="servicios-diseno">
                <h3>Servicios de Diseño Personalizado</h3>
                <div class="servicios-grid">
                    <div v-for="servicio in serviciosDiseno" :key="servicio.id" class="servicio-card">
                        <img :src="servicio.imagen" :alt="servicio.titulo" class="servicio-imagen">
                        <h4>{{ servicio.titulo }}</h4>
                        <p>{{ servicio.descripcion }}</p>
                    </div>
                </div>
            </section>

            <section class="ejemplos-diseno">
                <h3>Ejemplos de Nuestros Diseños</h3>
                <div class="ejemplos-slider">
                    <div v-for="ejemplo in ejemplosDiseno" :key="ejemplo.id" class="ejemplo-slide">
                        <img :src="ejemplo.imagen" :alt="ejemplo.titulo" class="ejemplo-imagen">
                        <div class="ejemplo-info">
                            <h4>{{ ejemplo.titulo }}</h4>
                            <p>{{ ejemplo.descripcion }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <section class="cta-diseno">
                <h3>¿Listo para dar vida a tu idea?</h3>
                <p>Nuestro equipo de diseñadores está listo para ayudarte a crear el mueble perfecto para tu espacio.
                </p>
                <a href="#" class="boton-cta">Solicitar Consulta de Diseño</a>
            </section>
        </main>

        <!-- COMPONENTE FOOTER -->
        <Footer />
    </div>
</template>

<script setup>
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";
import { ref } from 'vue';

const pasosProceso = ref([
    {
        titulo: "Consulta Inicial",
        descripcion: "Nos reunimos contigo para entender tus necesidades, gustos y el espacio donde se ubicará el mueble."
    },
    {
        titulo: "Conceptualización",
        descripcion: "Nuestros diseñadores crean bocetos y conceptos basados en tus requerimientos y nuestras sugerencias."
    },
    {
        titulo: "Diseño Detallado",
        descripcion: "Desarrollamos diseños 3D detallados y planos técnicos para tu aprobación."
    },
    {
        titulo: "Selección de Materiales",
        descripcion: "Te ayudamos a elegir las mejores maderas y acabados para tu proyecto."
    },
    {
        titulo: "Fabricación",
        descripcion: "Nuestros artesanos expertos fabrican tu mueble con precisión y cuidado."
    },
    {
        titulo: "Entrega e Instalación",
        descripcion: "Entregamos e instalamos tu mueble, asegurándonos de que todo esté perfecto."
    }
]);

const serviciosDiseno = ref([
    {
        id: 1,
        titulo: "Diseño de Muebles a Medida",
        descripcion: "Creamos muebles únicos que se ajustan perfectamente a tu espacio y estilo de vida.",
        imagen: "/placeholder.svg?height=200&width=300"
    },
    {
        id: 2,
        titulo: "Renovación de Espacios",
        descripcion: "Transformamos tus espacios con soluciones de carpintería innovadoras y funcionales.",
        imagen: "/placeholder.svg?height=200&width=300"
    },
    {
        id: 3,
        titulo: "Diseño de Interiores en Madera",
        descripcion: "Diseñamos interiores completos utilizando la calidez y belleza de la madera.",
        imagen: "/placeholder.svg?height=200&width=300"
    }
]);

const ejemplosDiseno = ref([
    {
        id: 1,
        titulo: "Cocina Moderna",
        descripcion: "Cocina integral con isla central y acabados en roble.",
        imagen: "/placeholder.svg?height=400&width=600"
    },
    {
        id: 2,
        titulo: "Biblioteca Clásica",
        descripcion: "Biblioteca de pared completa con escalera móvil.",
        imagen: "/placeholder.svg?height=400&width=600"
    },
    {
        id: 3,
        titulo: "Oficina en Casa",
        descripcion: "Espacio de trabajo ergonómico con almacenamiento integrado.",
        imagen: "/placeholder.svg?height=400&width=600"
    }
]);
</script>

<style scoped>
/* El estilo no cambia */
</style>


<style scoped>
.diseno {
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

h2,
h3 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
}

.proceso-diseno {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin-bottom: 3rem;
}

.paso-diseno {
    width: calc(33.333% - 2rem);
    margin-bottom: 2rem;
    display: flex;
    align-items: flex-start;
}

.paso-numero {
    background-color: #FF9800;
    color: #FFF3E0;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 1.2rem;
    margin-right: 1rem;
}

.paso-contenido {
    flex: 1;
}

.servicios-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
}

.servicio-card {
    background-color: #FFECB3;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.servicio-card:hover {
    transform: translateY(-5px);
}

.servicio-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.servicio-card h4 {
    color: #E65100;
    margin: 1rem;
}

.servicio-card p {
    margin: 0 1rem 1rem;
}

.ejemplos-slider {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2rem;
    padding-bottom: 1rem;
}

.ejemplo-slide {
    flex: 0 0 80%;
    scroll-snap-align: start;
    background-color: #FFE0B2;
    border-radius: 8px;
    overflow: hidden;
}

.ejemplo-imagen {
    width: 100%;
    height: 300px;
    object-fit: cover;
}

.ejemplo-info {
    padding: 1rem;
}

.ejemplo-info h4 {
    color: #E65100;
    margin-bottom: 0.5rem;
}

.cta-diseno {
    background-color: #FFECB3;
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
    margin-top: 3rem;
}

.boton-cta {
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

.boton-cta:hover {
    background-color: #E65100;
}

.footer {
    background-color: #FF9800;
    color: #FFF3E0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}

@media (max-width: 768px) {
    .paso-diseno {
        width: 100%;
    }

    .ejemplos-slider {
        flex-direction: column;
    }

    .ejemplo-slide {
        flex: 0 0 100%;
    }
}
</style>