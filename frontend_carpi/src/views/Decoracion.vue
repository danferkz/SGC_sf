<template>
    <div class="decoracion">
      <header class="header">
        <h1>Maderera el bosque</h1>
      </header>
      <main class="content">
        <h2>Decoración en Madera</h2>
        
        <section class="servicios-decoracion">
          <h3>Nuestros Servicios de Decoración</h3>
          <div class="servicios-grid">
            <div v-for="servicio in serviciosDecoracion" :key="servicio.id" class="servicio-card">
              <img :src="servicio.imagen" :alt="servicio.titulo" class="servicio-imagen">
              <div class="servicio-info">
                <h4>{{ servicio.titulo }}</h4>
                <p>{{ servicio.descripcion }}</p>
              </div>
            </div>
          </div>
        </section>
  
        <section class="estilos-decoracion">
          <h3>Estilos de Decoración en Madera</h3>
          <div class="estilos-carousel">
            <div v-for="estilo in estilosDecoracion" :key="estilo.id" class="estilo-slide">
              <img :src="estilo.imagen" :alt="estilo.nombre" class="estilo-imagen">
              <div class="estilo-info">
                <h4>{{ estilo.nombre }}</h4>
                <p>{{ estilo.descripcion }}</p>
              </div>
            </div>
          </div>
        </section>
  
        <section class="proyectos-destacados">
          <h3>Proyectos de Decoración Destacados</h3>
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
  
        <section class="proceso-decoracion">
          <h3>Nuestro Proceso de Decoración</h3>
          <ol class="proceso-lista">
            <li v-for="(paso, index) in procesoDecoracion" :key="index" class="proceso-item">
              <h4>{{ paso.titulo }}</h4>
              <p>{{ paso.descripcion }}</p>
            </li>
          </ol>
        </section>
  
        <section class="cta-decoracion">
          <h3>¿Listo para transformar tu espacio?</h3>
          <p>Nuestro equipo de expertos en decoración está listo para ayudarte a crear el ambiente perfecto con la calidez de la madera.</p>
          <a href="#" class="boton-cta">Solicitar Consulta de Decoración</a>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; 2023 Maderera el bosque. Todos los derechos reservados.</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const serviciosDecoracion = ref([
    {
      id: 1,
      titulo: "Paneles Decorativos",
      descripcion: "Creamos paneles de madera personalizados para añadir textura y calidez a tus paredes.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 2,
      titulo: "Muebles Decorativos",
      descripcion: "Diseñamos y fabricamos muebles únicos que se convierten en el centro de atención de cualquier espacio.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 3,
      titulo: "Accesorios en Madera",
      descripcion: "Complementamos tu decoración con accesorios de madera hechos a mano, desde lámparas hasta objetos decorativos.",
      imagen: "/placeholder.svg?height=300&width=400"
    }
  ]);
  
  const estilosDecoracion = ref([
    {
      id: 1,
      nombre: "Rústico Moderno",
      descripcion: "Combina la calidez de la madera natural con líneas limpias y modernas.",
      imagen: "/placeholder.svg?height=400&width=600"
    },
    {
      id: 2,
      nombre: "Escandinavo",
      descripcion: "Minimalismo y funcionalidad con maderas claras y diseños simples.",
      imagen: "/placeholder.svg?height=400&width=600"
    },
    {
      id: 3,
      nombre: "Industrial Chic",
      descripcion: "Mezcla de madera recuperada con elementos metálicos para un look urbano y sofisticado.",
      imagen: "/placeholder.svg?height=400&width=600"
    }
  ]);
  
  const proyectosDestacados = ref([
    {
      id: 1,
      titulo: "Restaurante Bosque Encantado",
      descripcion: "Decoración completa con paneles de madera tallados a mano y mobiliario personalizado.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 2,
      titulo: "Oficina Creativa Madera",
      descripcion: "Transformación de un espacio de trabajo con elementos decorativos en madera reciclada.",
      imagen: "/placeholder.svg?height=300&width=400"
    },
    {
      id: 3,
      titulo: "Hogar Zen",
      descripcion: "Proyecto residencial con énfasis en la serenidad y la naturaleza a través de elementos de madera.",
      imagen: "/placeholder.svg?height=300&width=400"
    }
  ]);
  
  const procesoDecoracion = ref([
    {
      titulo: "Consulta Inicial",
      descripcion: "Nos reunimos contigo para entender tu visión, estilo y necesidades específicas."
    },
    {
      titulo: "Diseño Conceptual",
      descripcion: "Creamos bocetos y moodboards para visualizar el concepto de decoración."
    },
    {
      titulo: "Selección de Materiales",
      descripcion: "Elegimos las maderas y acabados perfectos para tu proyecto de decoración."
    },
    {
      titulo: "Fabricación Personalizada",
      descripcion: "Nuestros artesanos crean piezas únicas según el diseño aprobado."
    },
    {
      titulo: "Instalación y Styling",
      descripcion: "Instalamos los elementos decorativos y realizamos el styling final del espacio."
    }
  ]);
  </script>
  
  <style scoped>
  .decoracion {
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
  
  .servicios-grid, .proyectos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
  }
  
  .servicio-card, .proyecto-card {
    background-color: #FFECB3;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .servicio-card:hover, .proyecto-card:hover {
    transform: translateY(-5px);
  }
  
  .servicio-imagen, .proyecto-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  .servicio-info, .proyecto-info {
    padding: 1rem;
  }
  
  .estilos-carousel {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2rem;
    padding-bottom: 1rem;
    margin-bottom: 3rem;
  }
  
  .estilo-slide {
    flex: 0 0 80%;
    scroll-snap-align: start;
    background-color: #FFE0B2;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .estilo-imagen {
    width: 100%;
    height: 300px;
    object-fit: cover;
  }
  
  .estilo-info {
    padding: 1rem;
  }
  
  .proceso-lista {
    list-style-type: none;
    padding: 0;
    counter-reset: proceso-counter;
  }
  
  .proceso-item {
    background-color: #FFE0B2;
    margin-bottom: 1rem;
    padding: 1rem;
    border-radius: 8px;
    counter-increment: proceso-counter;
    position: relative;
    padding-left: 3rem;
  }
  
  .proceso-item::before {
    content: counter(proceso-counter);
    position: absolute;
    left: 1rem;
    top: 1rem;
    background-color: #FF9800;
    color: #FFF3E0;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
  }
  
  .cta-decoracion {
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
    .estilos-carousel {
      flex-direction: column;
    }
  
    .estilo-slide {
      flex: 0 0 100%;
    }
  }
  </style>