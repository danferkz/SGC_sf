<!-- ClienteView.vue (HOME) -->
<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Header -->
    <Header />


    
    <!-- Hero Section -->
    <section>
      <div class="hero">
        <img src="../assets/home.png" alt="Hero Image" class="object-cover h-full w-full">
        <div class="hero-overlay bg-opacity-60"></div>
        <div class="hero-content text-neutral-content text-center">
          <div class="max-w-md">
            <h1 class="mb-5 text-5xl font-bold">Tus sueños, nuestra madera</h1>
            <p class="mb-5">
              Creamos muebles únicos que reflejan tu estilo. Desde la imaginación hasta la realidad,
              transformamos la madera en obras maestras personalizadas para tu hogar.
            </p>
            <a href="#contacto">
              <button class="btn btn-primary">Solicita tu diseño</button>
            </a>
          </div>
        </div>
      </div>
    </section>


    <!-- Productos Section -->
    <section id="productos" class="py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Nuestros Productos</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Producto 1 -->
          <div class="card bg-base-100 w-96 shadow-xl mb-4">
            <router-link to="/puerta" class="block">
              <figure>
                <img src="../assets/puerta.png" alt="Puertas" />
              </figure>
              <div class="card-body">
                <h2 class="card-title">Puertas</h2>
                <p>Puertas interiores y exteriores a medida</p>
              </div>
            </router-link>
          </div>
          <!-- Producto 2 -->
          <div class="card bg-base-100 w-96 shadow-xl mb-4">
            <router-link to="/ventana" class="block">
              <figure>
                <img src="../assets/ventana.png" alt="Ventanas" />
              </figure>
              <div class="card-body">
                <h2 class="card-title">Ventanas</h2>
                <p>Ventanas de diversos estilos y tamaños</p>
              </div>
            </router-link>
          </div>
          <!-- Producto 3 -->
          <div class="card bg-base-100 w-96 shadow-xl mb-4">
            <router-link to="/mueble" class="block">
              <figure>
                <img src="../assets/muebles.png" alt="Muebles" />
              </figure>
              <div class="card-body">
                <h2 class="card-title">Muebles</h2>
                <p>Muebles personalizados para tu hogar</p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Pedidos Section -->
    <section id="pedidos" class="py-16 px-6 bg-amber-100">
      <div class="container mx-auto text-center">
        <h3 class="text-3xl font-bold mb-8">Proceso de Pedidos</h3>
        <ul class="timeline timeline-snap-icon max-md:timeline-compact timeline-vertical">
          <li>
            <div class="timeline-middle">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <div class="timeline-start mb-10 md:text-end">
              <time class="font-mono italic">1</time>
              <div class="text-lg font-black">Solicitud</div>
              Contacta con nosotros y describe tu proyecto
            </div>
            <hr />
          </li>
          <li>
            <hr />
            <div class="timeline-middle">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <div class="timeline-end mb-10">
              <time class="font-mono italic">2</time>
              <div class="text-lg font-black">Diseño</div>
              Creamos un diseño personalizado según tus necesidades
            </div>
            <hr />
          </li>
          <li>
            <hr />
            <div class="timeline-middle">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <div class="timeline-start mb-10 md:text-end">
              <time class="font-mono italic">3</time>
              <div class="text-lg font-black">Fabricación</div>
              Producimos tu pedido con los mejores materiales
            </div>
            <hr />
          </li>
          <li>
            <hr />
            <div class="timeline-middle">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
                <path fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
                  clip-rule="evenodd" />
              </svg>
            </div>
            <div class="timeline-end mb-10">
              <time class="font-mono italic">4</time>
              <div class="text-lg font-black">Entrega</div>
              Entregamos tu pedido, con opción a domicilio
            </div>
          </li>
        </ul>
      </div>
    </section>

    <!-- Contacto Section -->
    <section id="contacto" class="py-16 px-6 bg-white">
      <div class="container mx-auto max-w-2xl">
        <div class="bg-amber-50 p-12 rounded-lg shadow-md text-center">
          <div
            class="w-24 h-24 mx-auto mb-6 bg-amber-800 text-white rounded-full flex items-center justify-center text-4xl">
            📝</div>
          <h3 class="text-3xl font-bold mb-4">¿Estás interesado?</h3>
          <p class="text-xl mb-8">Por favor, regístrese para su pedido</p>
          <router-link to="/registro" button class="btn btn-primary">Regístrese
            Aquí</router-link>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
// importar el componente Header
import Header from '@/components/HeaderCompo.vue'
import Footer from '@/components/FooterCompo.vue'


function scrollToContacto() {
  const contactoSection = document.getElementById('contacto');
  contactoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
</script>

<style scoped>
.hero-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 50%;
  object-fit: cover;
}

#productos {
  padding: 4rem 2rem;
  /* added padding to the section */
  text-align: center;
  /* center all products */
}

#productos .container {
  max-width: 1200px;
  /* set a max width for the container */
  margin: 0 auto;
  /* center the container */
}

#productos .grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  /* set the grid to 1 column on small screens */
  gap: 2rem;
  /* add a gap between grid items */
  justify-items: center;
  /* center all grid items */
}

#productos .card {
  background-color: #f9fafb;
  /* set a light gray background color */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  /* add a subtle box shadow */
  border-radius: 10px;
  /* add a rounded corner */
  overflow: hidden;
  /* hide any overflow */
  max-width: 300px;
  /* set a max width for the card */
  margin: 0 auto;
  /* center the card */
}

#productos .card figure {
  margin: 0;
  /* remove margin from figure */
}

#productos .card figure div {
  width: 40px;
  /* set a fixed width for the icon */
  height: 40px;
  /* set a fixed height for the icon */
  margin: 0 auto;
  /* center the icon */
  font-size: 24px;
  /* increase font size for the icon */
}

#productos .card-body {
  padding: 1.5rem;
  /* add padding to the card body */
  text-align: center;
  /* center the card body content */
}

#productos .card-title {
  font-size: 18px;
  /* increase font size for the title */
  font-weight: bold;
  /* make the title bold */
  margin-bottom: 10px;
  /* add margin bottom to the title */
}

#productos p {
  font-size: 16px;
  /* increase font size for the paragraph */
  color: #666;
  /* set a dark gray text color */
  text-align: center;
  /* center the paragraph */
}

/* Media queries for responsiveness */

@media (min-width: 768px) {
  #productos .grid {
    grid-template-columns: repeat(2, 1fr);
    /* set the grid to 2 columns on medium screens */
  }
}

@media (min-width: 1200px) {
  #productos .grid {
    grid-template-columns: repeat(3, 1fr);
    /* set the grid to 3 columns on large screens */
  }
}

/* Media queries for responsiveness */

@media (min-width: 768px) {
  #productos .grid {
    grid-template-columns: repeat(2, 1fr);
    /* set the grid to 2 columns on medium screens */
  }
}

@media (min-width: 1200px) {
  #productos .grid {
    grid-template-columns: repeat(3, 1fr);
    /* set the grid to 3 columns on large screens */
  }
}
</style>
