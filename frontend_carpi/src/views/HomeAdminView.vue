<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />
    <!-- Dashboard Section -->
    <section id="dashboard" class="flex-1 py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Dashboard</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Gestión de Clientes -->
          <router-link to="/gestionclientes"
            class="card">
            <div class="image-container" style="background-color: #FFFBEB;">
              <img src="../assets/gestioncliente_icon.png" alt="Clientes" class="dashboard-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">CLIENTES</h4>
            <p>Gestiona tus clientes</p>
          </router-link>
          <!-- Gestión de Pedidos -->
          <router-link to="/gestionpedidos"
            class="card">
            <div class="image-container" style="background-color: #FFFBEB;">
              <img src="../assets/gestionpedidos_icon.png" alt="Pedidos" class="dashboard-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">PEDIDOS</h4>
            <p>Gestiona tus pedidos</p>
          </router-link>
          <!-- Gestión de Administradores -->
          <router-link to="/gestionadminstradores"
            class="card">
            <div class="image-container" style="background-color: #FFFBEB;">
              <img src="../assets/gestionadminstradores_icon.png" alt="Administradores" class="dashboard-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">ADMINISTRACION</h4>
            <p>Gestiona los administradores</p>
          </router-link>
          <!-- Gestión de Presupuestos -->
          <router-link to="/presupuesto"
            class="card">
            <div class="image-container" style="background-color: #FFFBEB;">
              <img src="../assets/gestionpresupuesto_icon.png" alt="Presupuestos" class="dashboard-image" />
            </div>
            <h4 class="text-xl font-semibold mb-2">PRESUPUESTOS</h4>
            <p>Gestiona los presupuestos</p>
          </router-link>
        </div>
      </div>
    </section>
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