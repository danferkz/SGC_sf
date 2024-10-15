<template>
    <div class="min-h-screen bg-gray-100 text-gray-800 flex">
      <!-- Header -->
      <HeaderAdmin class="header-admin" />
    </div>
  </template>
  
  <script setup>
  import HeaderAdmin from '@/components/NabvarVerticalAdmin.vue'
  </script>
  
  <style scoped>
  /* Contenedor principal */
  .min-h-screen {
    display: flex;
    background-color: #FFFFFF; /* Fondo blanco para el contenedor principal */
  }
  /* Estilos del header admin */
  .header-admin {
    width: 250px;
    background-color: #FFFFFF;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    height: 100vh; /* Asegura que el header ocupe toda la altura */
  }
  /* Sección del dashboard */
  #dashboard {
    padding: 20px;
    background-color: #FFFFFF;
    flex: 1;
    margin-left: 120px; /* Se agrega separación de 120px entre el header y el contenido */
  }
  /* Contenedor de imagen */
  .image-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 0.5rem;
    overflow: hidden;
    height: 150px; /* Altura fija para las imágenes */
  }
  /* Imagen del dashboard */
  .dashboard-image {
    max-width: 100%;
    max-height: 100%;
    height: auto;
    width: auto;
    border-radius: 0.5rem;
  }
  /* Alineación del contenido */
  .container {
    padding: 20px;
  }
  /* Estilos de las tarjetas */
  .card {
    background-color: #FFFBEB;
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: background-color 0.3s;
  }
  .card:hover {
    background-color: #FFECB3;
  }
  </style>