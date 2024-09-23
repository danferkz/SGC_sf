<template>
  <div class="flex bg-beige-100 font-sans">
    <!-- Sidebar -->
    <aside class="w-64 bg-brown-200 h-screen fixed shadow-lg">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-black">Maderera El Bosque</h2>
      </div>
      <ul class="space-y-2 p-4">
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2 2m-2-2v8a2 2 0 002 2h16a2 2 0 002-2v-8a2 2 0 00-2-2m-2-2l-2-2m2 2l2 2m-2-2l-2-2"></path>
            </svg>
            Dashboard
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7m14 4H5m14 4H5"></path>
            </svg>
            Pedidos
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v8m-4-4h8"></path>
            </svg>
            Productos
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
            Reportes
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-black rounded-lg hover:bg-melon-100">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
            </svg>
            Configuración
          </a>
        </li>
      </ul>
    </aside>
    <main class="ml-64 p-6 bg-beige-100 min-h-screen flex">
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
            </tbody>
          </table>
        </section>
      </div>
      <div class="w-120 ml-10">
        <h2 class="text-2xl font-bold text-black mb-2">Calendario</h2>
        <vue-cal
          class="mt-2"
          :events="events"
          :disable-times="true"
          :disable-day-numbers="true"
          style="border: 1px solid #000; font-size: 14px; background-color: #f5f5dc; height: 400px; width: 400px;"
        />
      </div>
    </main>
  </div>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vueCal.css';

export default {
  name: "HomeAdminView",
  components: {
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
</style>
