<template>
    <div class="sobre-nosotros">
      <!-- Header Componente -->
      <Header />
  
      <main class="content">
        <section class="info-section">
          <h2>Sobre Nosotros</h2>
          <p>
            En Maderera el bosque, nos apasiona trabajar con la madera y crear piezas únicas que
            combinen belleza y funcionalidad. Con más de 20 años de experiencia, nos hemos
            convertido en expertos en el arte de la carpintería.
          </p>
          <p>
            Nuestro equipo de artesanos altamente calificados se dedica a producir muebles de
            alta calidad, puertas, ventanas y todo tipo de trabajos en madera, siempre
            respetando el medio ambiente y utilizando materiales sostenibles.
          </p>
        </section>
  
        <!-- Galería de imágenes -->
        <section class="image-gallery">
          <h3>Galería de Imágenes</h3>
          <div v-for="(image, index) in images" :key="index" class="image-container">
            <img :src="image.src" :alt="image.alt" />
          </div>
        </section>
  
        <section class="services">
          <h3>Nuestros Servicios</h3>
          <ul>
            <li>Diseño y fabricación de muebles a medida</li>
            <li>Restauración de muebles antiguos</li>
            <li>Carpintería para interiores y exteriores</li>
            <li>Asesoramiento personalizado</li>
          </ul>
        </section>
      </main>
  
      <!-- Footer Componente -->
      <Footer />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  // Importamos los componentes Header y Footer
  import Header from "@/components/HeaderCompo.vue";
  import Footer from "@/components/FooterCompo.vue";
  // Importamos las imágenes de assets
  import tallerImage from '@/assets/taller.jpg';
  import artesanoImage from '@/assets/artesano.jpg';
  import mueblesImage from '@/assets/muebles_2.jpeg';
  
  const images = ref([
    { src: tallerImage, alt: 'Taller de carpintería' },
    { src: artesanoImage, alt: 'Artesano trabajando' },
    { src: mueblesImage, alt: 'Muebles terminados' },
  ]);
  </script>
  
  <style scoped>
  .sobre-nosotros {
    font-family: 'Arial', sans-serif;
    color: #5D4037;
    background-color: #FFF3E0;
  }
  
  .content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }
  
  h2, h3 {
    color: #E65100;
  }
  
  .info-section {
    background-color: #FFECB3;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 2rem;
  }
  
  .image-gallery {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }
  
  .image-container {
    width: calc(33.33% - 1rem);
    margin-bottom: 1rem;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .image-container img {
    width: 100%;
    height: auto;
    object-fit: cover;
  }
  
  .services {
    background-color: #FFE0B2;
    padding: 2rem;
    border-radius: 8px;
  }
  
  ul {
    list-style-type: none;
    padding-left: 0;
  }
  
  li {
    margin-bottom: 0.5rem;
    padding-left: 1.5rem;
    position: relative;
  }
  
  li::before {
    content: '🌳';
    position: absolute;
    left: 0;
  }
  
  @media (max-width: 768px) {
    .image-container {
      width: 100%;
    }
  }
  </style>
  