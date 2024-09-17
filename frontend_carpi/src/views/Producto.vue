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
            <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
              <div class="w-full h-48 bg-gray-300 mb-4 rounded-lg overflow-hidden">
                <!-- Imagen de Puertas -->
                <img src="../assets/puerta.jpg" alt="Puertas" class="w-full h-full object-cover"/>
              </div>
              <h4 class="text-xl font-semibold mb-2">Puertas</h4>
              <p>Puertas interiores y exteriores a medida</p>
            </div>
  
            <!-- Producto 2: Ventanas -->
            <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
              <div class="w-full h-48 bg-gray-300 mb-4 rounded-lg overflow-hidden">
                <!-- Imagen de Ventanas -->
                <img src="../assets/ventana.jpg" alt="Ventanas" class="w-full h-full object-cover"/>
              </div>
              <h4 class="text-xl font-semibold mb-2">Ventanas</h4>
              <p>Ventanas de diversos estilos y tamaños</p>
            </div>
  
            <!-- Producto 3: Muebles -->
            <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
              <div class="w-full h-48 bg-gray-300 mb-4 rounded-lg overflow-hidden">
                <!-- Imagen de Muebles -->
                <img src="../assets/muebles.jpg" alt="Muebles" class="w-full h-full object-cover"/>
              </div>
              <h4 class="text-xl font-semibold mb-2">Muebles</h4>
              <p>Muebles personalizados para tu hogar</p>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Footer -->
      <Footer />
    </div>
  </template>
  
  <script setup>
  // Importar componentes de Header y Footer
  import Header from '@/components/HeaderCompo.vue'
  import Footer from '@/components/FooterCompo.vue'
  </script>
  
  <style scoped>
  /* Estilos opcionales específicos para este componente */
  </style>
  