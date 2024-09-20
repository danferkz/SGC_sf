<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Header -->
    <Header />

    <!-- Hero Section -->
    <section class="py-20 px-6 bg-gradient-to-b from-amber-800 to-amber-600 text-white">
      <div class="container mx-auto text-center">
        <h2 class="text-5xl font-bold mb-6">Gestión Integral de Carpintería</h2>
        <p class="text-xl mb-8">Producción y comercialización de puertas, ventanas y muebles de alta calidad</p>
        <a href="#contacto" class="bg-white text-amber-800 py-3 px-8 rounded-full text-lg font-semibold hover:bg-amber-100 transition">Solicitar Presupuesto</a>
      </div>
    </section>

    <!-- Productos Section -->
    <section id="productos" class="py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Nuestros Productos</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Producto 1 -->
          <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
            <div class="w-16 h-16 mx-auto mb-4 bg-amber-800 text-white rounded-full flex items-center justify-center">🚪</div>
            <h4 class="text-xl font-semibold mb-2">Puertas</h4>
            <p>Puertas interiores y exteriores a medida</p>
          </div>
          <!-- Producto 2 -->
          <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
            <div class="w-16 h-16 mx-auto mb-4 bg-amber-800 text-white rounded-full flex items-center justify-center">🪟</div>
            <h4 class="text-xl font-semibold mb-2">Ventanas</h4>
            <p>Ventanas de diversos estilos y tamaños</p>
          </div>
          <!-- Producto 3 -->
          <div class="bg-amber-50 p-6 rounded-lg shadow-md text-center">
            <div class="w-16 h-16 mx-auto mb-4 bg-amber-800 text-white rounded-full flex items-center justify-center">🪑</div>
            <h4 class="text-xl font-semibold mb-2">Muebles</h4>
            <p>Muebles personalizados para tu hogar</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Pedidos Section -->
    <section id="pedidos" class="py-16 px-6 bg-amber-100">
      <div class="container mx-auto text-center">
        <h3 class="text-3xl font-bold mb-8">Proceso de Pedidos</h3>
        <div class="flex flex-col md:flex-row justify-center items-center space-y-6 md:space-y-0 md:space-x-12">
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 bg-amber-800 text-white rounded-full flex items-center justify-center text-2xl font-bold mb-4">1</div>
            <h4 class="text-xl font-semibold mb-2">Solicitud</h4>
            <p class="text-sm">Contacta con nosotros y describe tu proyecto</p>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 bg-amber-800 text-white rounded-full flex items-center justify-center text-2xl font-bold mb-4">2</div>
            <h4 class="text-xl font-semibold mb-2">Diseño</h4>
            <p class="text-sm">Creamos un diseño personalizado según tus necesidades</p>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 bg-amber-800 text-white rounded-full flex items-center justify-center text-2xl font-bold mb-4">3</div>
            <h4 class="text-xl font-semibold mb-2">Fabricación</h4>
            <p class="text-sm">Producimos tu pedido con los mejores materiales</p>
          </div>
          <div class="flex flex-col items-center">
            <div class="w-16 h-16 bg-amber-800 text-white rounded-full flex items-center justify-center text-2xl font-bold mb-4">4</div>
            <h4 class="text-xl font-semibold mb-2">Entrega</h4>
            <p class="text-sm">Entregamos tu pedido, con opción a domicilio</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contacto Section -->
    <section id="contacto" class="py-16 px-6 bg-white">
      <div class="container mx-auto max-w-2xl">
        <div class="bg-amber-50 p-12 rounded-lg shadow-md text-center">
          <div class="w-24 h-24 mx-auto mb-6 bg-amber-800 text-white rounded-full flex items-center justify-center text-4xl">📝</div>
          <h3 class="text-3xl font-bold mb-4">¿Estás interesado?</h3>
          <p class="text-xl mb-8">Por favor, regístrese para su pedido</p>
          <router-link to="/registro" class="bg-amber-800 text-white py-4 px-12 rounded-full text-lg font-semibold hover:bg-amber-700 transition">Regístrese Aquí</router-link>
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
</script>

