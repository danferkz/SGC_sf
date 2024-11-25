<template>
    <div class="construccion">
      <header class="header">
        <h1>Maderera el bosque</h1>
      </header>
      <main class="content">
        <h2>Servicios de Construcción en Madera</h2>
        
        <section class="servicios-construccion">
          <div v-for="servicio in serviciosConstruccion" :key="servicio.id" class="servicio-card">
            <img :src="servicio.imagen" :alt="servicio.titulo" class="servicio-imagen">
            <div class="servicio-info">
              <h3>{{ servicio.titulo }}</h3>
              <p>{{ servicio.descripcion }}</p>
            </div>
          </div>
        </section>
  
        <section class="proyectos-destacados">
          <h3>Proyectos Destacados</h3>
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
  
        <section class="cta-construccion">
          <h3>¿Listo para comenzar tu proyecto?</h3>
          <p>Nuestro equipo de expertos está listo para ayudarte a hacer realidad tu visión en madera.</p>
          <a href="#" class="boton-cta">Solicitar Presupuesto</a>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; 2023 Maderera el bosque. Todos los derechos reservados.</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const serviciosConstruccion = ref([
    {
      id: 1,
      titulo: "Estructuras de Madera",
      descripcion: "Diseñamos y construimos estructuras de madera duraderas y estéticamente atractivas para diversos proyectos.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 2,
      titulo: "Acabados en Madera",
      descripcion: "Ofrecemos una amplia gama de acabados en madera para interiores y exteriores, desde pisos hasta revestimientos.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 3,
      titulo: "Restauración de Edificios",
      descripcion: "Restauramos y renovamos estructuras de madera históricas, preservando su belleza y valor patrimonial.",
      imagen: "/placeholder.svg?height=300&width=400"
    }
  ]);
  
  const proyectosDestacados = ref([
    {
      id: 1,
      titulo: "Casa de Campo Sustentable",
      descripcion: "Construcción de una casa de campo completamente en madera, utilizando técnicas sostenibles y materiales locales.",
      imagen: "/placeholder.svg?height=400&width=600"
    },
    {
      id: 2,
      titulo: "Restauración de Iglesia Colonial",
      descripcion: "Restauración completa de la estructura y elementos decorativos de madera de una iglesia colonial del siglo XVIII.",
      imagen: "/placeholder.svg?height=400&width=600"
    },
    {
      id: 3,
      titulo: "Centro Comercial Eco-friendly",
      descripcion: "Diseño y construcción de un innovador centro comercial con estructura principal y acabados en madera certificada.",
      imagen: "/placeholder.svg?height=400&width=600"
    }
  ]);
  
  const procesoConstruccion = ref([
    {
      titulo: "Consulta y Planificación",
      descripcion: "Nos reunimos contigo para entender tus necesidades y objetivos, y desarrollamos un plan detallado del proyecto."
    },
    {
      titulo: "Diseño y Aprobación",
      descripcion: "Nuestro equipo de diseño crea planos detallados y visualizaciones 3D para tu aprobación."
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
  
  h2, h3 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
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
  
  .footer {
    background-color: #FF9800;
    color: #FFF3E0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
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