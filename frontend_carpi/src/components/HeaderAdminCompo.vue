<template>
    <header class="bg-nude bg-opacity-90 text-black py-4 px-6 shadow-lg">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-3xl font-bold">Maderera El Bosque</h1>
        <nav>
          <ul class="flex space-x-6">
            <li><router-link to="/dashboard" class="hover:text-nude-200 transition">Dashboard</router-link></li>
            <li><router-link to="/pedidos" class="hover:text-nude-200 transition">Pedidos</router-link></li>
            <li><router-link to="/productos" class="hover:text-nude-200 transition">Productos</router-link></li>
            <li><router-link to="/reportes" class="hover:text-nude-200 transition">Reportes</router-link></li>
            <li><router-link to="/configuracion" class="hover:text-nude-200 transition">Configuración</router-link></li>
          </ul>
        </nav>
      </div>
    </header>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .bg-nude {
    background-color: #F5DEB3; /* Color nude */
  }
  .hover\:text-nude-200:hover {
    color: #FAEBD7; /* Color nude en hover */
  }
  .text-3xl {
    font-size: 1.875rem; /* Tamaño de fuente para el header */
  }
  .font-bold {
    font-weight: 700; /* Negrita para el nombre */
  }
  </style>
  