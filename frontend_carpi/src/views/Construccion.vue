<template>
    <HeaderCompo />
    <div class="construccion">
        <header class="header">
        </header>
        <main class="content">
            <!-- SERVICIOS DE CONSTRUCCIÓN -->
            <h2 class="subtitulo">Servicios de Construcción en Madera</h2>
            <section class="servicios-construccion">
                <div v-for="servicio in serviciosConstruccion" :key="servicio.id" class="servicio-card">
                    <img :src="servicio.imagen" :alt="servicio.titulo" class="servicio-imagen">
                    <div class="servicio-info">
                        <h3>{{ servicio.titulo }}</h3>
                        <p>{{ servicio.descripcion }}</p>
                    </div>
                </div>
            </section>

            <!-- PROYECTOS DESTACADOS -->
            <h2 class="subtitulo">Proyectos Destacados</h2>
            <section class="proyectos-destacados">
                <div class="proyectos-grid">
                    <div v-for="proyecto in proyectosDestacados" :key="proyecto.id" class="proyecto-card">
                        <img :src="proyecto.imagen" :alt="proyecto.titulo" class="proyecto-imagen">
                        <div class="proyecto-info">
                            <h4>{{ proyecto.titulo }}</h4>
                            <p>{{ proyecto.descripcion }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- PROCESO DE CONSTRUCCIÓN -->
            <section class="proceso-construccion">
                <h3>Nuestro Proceso de Construcción</h3>
                <div class="proceso-timeline">
                    <div v-for="(paso, index) in procesoConstruccion" :key="index" class="paso-construccion">
                        <div class="paso-numero">{{ index + 1 }}</div>
                        <div class="paso-contenido">
                            <h4>{{ paso.titulo }}</h4>
                            <p>{{ paso.descripcion }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- LLAMADO A LA ACCIÓN -->
            <section class="cta-construccion">
                <h3>¿Listo para comenzar tu proyecto?</h3>
                <p>Nuestro equipo de expertos está listo para ayudarte a hacer realidad tu visión en madera.</p>
                <a href="#" class="boton-cta">Solicitar Presupuesto</a>
            </section>
        </main>

        <!-- Footer -->
        <Footer class="footer" />
    </div>
</template>



<script setup>
import { ref } from 'vue';
import HeaderCompo from '@/components/HeaderCompo.vue';
import Footer from "@/components/FooterCompo.vue";
import iglesia from '@/assets/Muebledeinglesia.jpg';
import cost from '@/assets/Mueblecost.jpeg';
import puertasegura from '@/assets/puertasegura.jpeg';
import puertaconst from '@/assets/PuertasConstr.jpg';
import catedral from '@/assets/Ventanacatedral.jpeg';
import ventanaconst from '@/assets/Ventanacostr.jpeg';
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
.construccion {
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
    margin-bottom: 1.5rem;
}

.servicios-construccion {
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

.servicio-info {
    padding: 1rem;
}

.proyectos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
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
    padding: 1rem;
}

.proceso-construccion {
    margin-bottom: 3rem;
}

.proceso-timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 0;
}

/* TÍTULO PRINCIPAL */
.header h1 {
    font-size: 2.5rem;
    text-align: center;
    margin: 1rem 0;
    color: #3c3c3c;
}

/* SUBTÍTULOS DESTACADOS */
.subtitulo {
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
    margin: 2rem 0 1rem;
    color: #2e2e2e;
}

/* SECCIONES GENERALES */
.servicios-construccion,
.proyectos-destacados {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 1rem auto;
    padding: 0 2rem;
}

.servicio-card,
.proyecto-card {
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    text-align: center;
}

.servicio-imagen,
.proyecto-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.servicio-info,
.proyecto-info {
    padding: 1rem;
}

h3,
h4 {
    margin: 0.5rem 0;
    font-weight: bold;
}


.proceso-timeline::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 2px;
    background-color: #FF9800;
    transform: translateX(-50%);
}

.paso-construccion {
    position: relative;
    margin-bottom: 2rem;
    padding-left: 3rem;
}

.paso-numero {
    position: absolute;
    left: 0;
    top: 0;
    width: 40px;
    height: 40px;
    background-color: #FF9800;
    color: #FFF3E0;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}

.paso-contenido {
    background-color: #FFECB3;
    padding: 1rem;
    border-radius: 8px;
}

.cta-construccion {
    background-color: #FFE0B2;
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



@media (max-width: 768px) {
    .proceso-timeline::before {
        left: 20px;
    }

    .paso-construccion {
        padding-left: 60px;
    }

    .paso-numero {
        left: 0;
    }
}
</style>