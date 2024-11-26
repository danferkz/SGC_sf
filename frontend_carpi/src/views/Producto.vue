<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Header -->
    <Header />

    <!-- Productos Section -->
    <section id="productos" class="py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Nuestros Productos</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Producto 1: Puertas -->
          <router-link to="/puerta"
            class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
            <div class="image-container">
              <!-- Imagen de Puertas -->
              <img src="../assets/puerta (1).png" alt="Puertas" class="product-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">Puertas</h4>
            <p>Puertas interiores y exteriores a medida</p>
          </router-link>

          <!-- Producto 2: Ventanas -->
          <router-link to="/ventana"
            class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
            <div class="image-container">
              <!-- Imagen de Ventanas -->
              <img src="../assets/ventana (1).png" alt="Ventanas" class="product-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">Ventanas</h4>
            <p>Ventanas de diversos estilos y tamaños</p>
          </router-link>

          <!-- Producto 3: Muebles -->
          <router-link to="/mueble"
            class="bg-amber-50 p-6 rounded-lg shadow-md text-center hover:bg-amber-100 transition">
            <div class="image-container">
              <!-- Imagen de Muebles -->
              <img src="../assets/muebles (1).png" alt="Muebles" class="product-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">Muebles</h4>
            <p>Muebles personalizados para tu hogar</p>
          </router-link>
        </div>
      </div>
    </section>
    <!-- Footer -->
    <Footer class="footer" />
  </div>
</template>

<script setup>
import Header from '@/components/HeaderCompo.vue'
import Footer from '@/components/FooterCompo.vue'
</script>

<style scoped>
.image-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #e2e8f0;
  /* Fallback color */
  border-radius: 0.5rem;
  overflow: hidden;
}

.product-image {
  max-width: 100%;
  height: auto;
  border-radius: 0.5rem;
}

.footer {
  position: relative;
  width: 100%;
  margin-top: auto;
}
</style>
