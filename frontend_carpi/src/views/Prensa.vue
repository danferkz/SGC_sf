<template>
    <div class="prensa">
      <header class="header">
        <h1>Maderera el bosque</h1>
      </header>
      <main class="content">
        <h2>Prensa y Medios</h2>
        
        <section class="noticias-destacadas">
          <h3>Noticias Destacadas</h3>
          <div class="noticias-grid">
            <article v-for="noticia in noticiasDestacadas" :key="noticia.id" class="noticia-card">
              <img :src="noticia.imagen" :alt="noticia.titulo" class="noticia-imagen">
              <div class="noticia-contenido">
                <h4>{{ noticia.titulo }}</h4>
                <p class="noticia-fecha">{{ noticia.fecha }}</p>
                <p>{{ noticia.resumen }}</p>
                <a :href="noticia.enlace" target="_blank" rel="noopener noreferrer" class="leer-mas">Leer más</a>
              </div>
            </article>
          </div>
        </section>
  
        <section class="menciones-prensa">
          <h3>Menciones en Prensa</h3>
          <ul class="menciones-lista">
            <li v-for="mencion in mencionesPrensaOrdenadas" :key="mencion.id" class="mencion-item">
              <div class="mencion-fecha">{{ mencion.fecha }}</div>
              <div class="mencion-contenido">
                <h4>{{ mencion.titulo }}</h4>
                <p>{{ mencion.descripcion }}</p>
                <a :href="mencion.enlace" target="_blank" rel="noopener noreferrer" class="leer-mas">Ver artículo completo</a>
              </div>
            </li>
          </ul>
        </section>
  
        <section class="kit-prensa">
          <h3>Kit de Prensa</h3>
          <p>Descarga nuestro kit de prensa para obtener información detallada sobre Maderera el bosque, incluyendo nuestra historia, logotipos y fotos de alta resolución.</p>
          <a href="#" class="boton-descarga" @click.prevent="descargarKitPrensa">Descargar Kit de Prensa</a>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; 2023 Maderera el bosque. Todos los derechos reservados.</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
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
  
  .footer {
    background-color: #FF9800;
    color: #FFF3E0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
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