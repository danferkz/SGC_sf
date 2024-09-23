<template>
  <div class="flex bg-beige-100 font-sans">
    <!-- Sidebar -->
    <aside class="w-64 bg-brown-200 h-screen fixed shadow-lg">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-black">Maderera El Bosque</h2>
      </div>
      <ul class="space-y-2 p-4">
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">Dashboard</a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">Pedidos</a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">Productos</a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">Reportes</a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">Configuración</a>
        </li>
      </ul>
    </aside>

    <main class="ml-64 p-6 bg-beige-100 min-h-screen flex flex-col">
      <header class="bg-nude shadow-lg fixed top-0 left-0 right-0 z-10">
        <div class="container mx-auto flex justify-center py-4">
          <nav>
            <ul class="flex space-x-6">
              <li><router-link to="/dashboard" class="text-black hover:text-nude-200">Dashboard</router-link></li>
              <li><router-link to="/pedidos" class="text-black hover:text-nude-200">Pedidos</router-link></li>
              <li><router-link to="/productos" class="text-black hover:text-nude-200">Productos</router-link></li>
              <li><router-link to="/reportes" class="text-black hover:text-nude-200">Reportes</router-link></li>
              <li><router-link to="/configuracion" class="text-black hover:text-nude-200">Configuración</router-link></li>
            </ul>
          </nav>
        </div>
      </header>

      <div class="pt-20 flex-1 flex">
        <div class="flex-1">
          <h1 class="text-3xl font-bold text-black">Bienvenido al Panel Administrativo</h1>
          <section class="mt-6">
            <h2 class="text-2xl font-bold text-black">Resumen de Actividades</h2>
            <p class="mt-2 text-black">Aquí podrás visualizar el estado actual de los pedidos, productos y reportes.</p>
          </section>
          <section class="mt-6">
            <h2 class="text-2xl font-bold text-black">Últimos Pedidos</h2>
            <table class="min-w-full border border-black mt-2">
              <thead class="bg-brown-200 text-white">
                <tr>
                  <th class="border border-black p-2">ID</th>
                  <th class="border border-black p-2">Cliente</th>
                  <th class="border border-black p-2">Estado</th>
                  <th class="border border-black p-2">Fecha</th>
                </tr>
              </thead>
              <tbody class="text-black">
                <tr>
                  <td class="border border-black p-2">1</td>
                  <td class="border border-black p-2">Juan Pérez</td>
                  <td class="border border-black p-2">En Proceso</td>
                  <td class="border border-black p-2">2024-09-20</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">2</td>
                  <td class="border border-black p-2">María López</td>
                  <td class="border border-black p-2">Completado</td>
                  <td class="border border-black p-2">2024-09-19</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">3</td>
                  <td class="border border-black p-2">Carlos Fernández</td>
                  <td class="border border-black p-2">En Proceso</td>
                  <td class="border border-black p-2">2024-09-18</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">4</td>
                  <td class="border border-black p-2">Ana García</td>
                  <td class="border border-black p-2">Completado</td>
                  <td class="border border-black p-2">2024-09-17</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">5</td>
                  <td class="border border-black p-2">Luis Martínez</td>
                  <td class="border border-black p-2">Cancelado</td>
                  <td class="border border-black p-2">2024-09-16</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">6</td>
                  <td class="border border-black p-2">Laura Pérez</td>
                  <td class="border border-black p-2">En Proceso</td>
                  <td class="border border-black p-2">2024-09-15</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">7</td>
                  <td class="border border-black p-2">Pedro Sánchez</td>
                  <td class="border border-black p-2">Completado</td>
                  <td class="border border-black p-2">2024-09-14</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">8</td>
                  <td class="border border-black p-2">Sofía Torres</td>
                  <td class="border border-black p-2">Cancelado</td>
                  <td class="border border-black p-2">2024-09-13</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">9</td>
                  <td class="border border-black p-2">Daniel Ruiz</td>
                  <td class="border border-black p-2">En Proceso</td>
                  <td class="border border-black p-2">2024-09-12</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">10</td>
                  <td class="border border-black p-2">Carla Gómez</td>
                  <td class="border border-black p-2">Completado</td>
                  <td class="border border-black p-2">2024-09-11</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">11</td>
                  <td class="border border-black p-2">Javier Núñez</td>
                  <td class="border border-black p-2">En Proceso</td>
                  <td class="border border-black p-2">2024-09-10</td>
                </tr>
                <tr>
                  <td class="border border-black p-2">12</td>
                  <td class="border border-black p-2">Gloria Fernández</td>
                  <td class="border border-black p-2">Completado</td>
                  <td class="border border-black p-2">2024-09-09</td>
                </tr>
              </tbody>
            </table>
          </section>
        </div>
        <div class="w-1/3 ml-10">
          <h2 class="text-2xl font-bold text-black mb-2">Calendario</h2>
          <vue-cal
            class="mt-2"
            :events="events"
            :disable-times="true"
            :disable-day-numbers="true"
            style="border: 1px solid #000; font-size: 14px; background-color: #f5f5dc; height: 400px; width: 100%; max-width: 800px;"
          />
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import HeaderAdminCompo from '@/components/HeaderAdminCompo.vue';
import VueCal from 'vue-cal';
import 'vue-cal/dist/vueCal.css';

export default {
  name: "HomeAdminView",
  components: {
    HeaderAdminCompo,
    VueCal,
  },
  data() {
    return {
      events: [], // Puedes agregar eventos aquí
    };
  },
};
</script>


<style scoped>
.bg-beige-100 {
  background-color: #f5f5dc; /* beige claro */
}

.bg-brown-200 {
  background-color: #d7b57a; /* marrón claro */
}

.hover\:bg-melon-100:hover {
  background-color: #ffb300; /* melón */
}

.pt-20 {
  padding-top: 5rem; /* Para ajustar el espacio debajo de la barra fija */
}
</style>

