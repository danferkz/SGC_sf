<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />
    <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8 flex-1">
      <div class="max-w-7xl mx-auto">
        <div class="flex justify-between items-center mb-6">
          <h1 class="text-3xl font-bold text-gray-900">Empleados</h1>
          <button @click="abrirModal('crearStaff')" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Crear Staff
          </button>
        </div>

        <div class="bg-white shadow-md rounded-lg overflow-hidden">
          <!-- Tabla de empleados -->
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Username</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fecha de Contratación</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Especialidad</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Estado</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Acciones</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="empleado in empleados" :key="empleado.user_id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ empleado.username }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ empleado.hire_date }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ empleado.specialty }}</td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span :class="[
                      'px-2 inline-flex text-xs leading-5 font-semibold rounded-full',
                      empleado.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                    ]">
                      {{ empleado.is_active ? 'Activo' : 'Inactivo' }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-500">
                    <button @click="editarEmpleado(empleado)" class="text-indigo-600 hover:text-indigo-900 mr-2">
                      <PencilIcon class="h-5 w-5" />
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Control de Paginación -->
          <div class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
            <div class="flex justify-center pb-4 space-x-2">
              <button @click="paginaAnterior" :disabled="!previousPage" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0  011.414 0z" clip-rule="evenodd" />
                </svg>
              </button>
              <button class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">Página {{ currentPage }}</button>
              <button @click="siguientePagina" :disabled="!nextPage" class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal Crear Staff -->
    <div v-if="modalActivo === 'crearStaff'" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-lg font-semibold mb-4">Crear Staff</h2>
        <form @submit.prevent="crearStaff">
            <div class="mb-4">
            <label class="block text-gray-700">Username</label>
            <input 
              v-model="nuevoStaff.username" 
              type="text" 
              class="w-full border rounded-md px-4 py-2" 
              @input="nuevoStaff.username = nuevoStaff.username.replace(/\s/g, '')"
              required 
            />
            </div>
          <div class="mb-4">
            <label class="block text-gray-700">Email</label>
            <input v-model="nuevoStaff.email" type="email" class="w-full border rounded-md px-4 py-2" required />
          </div>
          <div class="flex justify-end space-x-4">
            <button @click="cerrarModal" class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">Cancelar</button>
            <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700">Continuar</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal Crear Empleado -->
    <div v-if="modalActivo === 'crearEmpleado'" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-lg font-semibold mb-4">Crear Empleado</h2>
        <form @submit.prevent="crearEmpleado">
          <div class="mb-4">
            <label class="block text-gray-700">Fecha de Contratación</label>
            <input v-model="nuevoEmpleado.hire_date" type="date" class="w-full border rounded-md px-4 py-2" required />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Especialidad</label>
            <input v-model="nuevoEmpleado.specialty" type="text" class="w-full border rounded-md px-4 py-2" required />
          </div>
          <div class="flex justify-end space-x-4">
            <button @click="cerrarModal" class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">Cancelar</button>
            <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700">Crear Empleado</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal Editar Empleado -->
    <div v-if="modalActivo === 'editarEmpleado'" class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-lg font-semibold mb- 4">Editar Empleado</h2>
        <form @submit.prevent="actualizarEmpleado">
          <div class="mb-4">
            <label class="block text-gray-700">Especialidad</label>
            <input v-model="empleadoEditado.specialty" type="text" class="w-full border rounded-md px-4 py-2" required />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Estado</label>
            <select v-model="empleadoEditado.is_active" class="w-full border rounded-md px-4 py-2" required>
              <option :value="true">Activo</option>
              <option :value="false">Inactivo</option>
            </select>
          </div>
          <div class="flex justify-end space-x-4">
            <button @click="cerrarModal" class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300">Cancelar</button>
            <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700">Actualizar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from "@/components/NabvarVerticalAdmin.vue";
import axios from "axios";
import { PencilIcon, TrashIcon } from 'lucide-vue-next'// Asegúrate de importar el icono

export default {
  components: {
    HeaderAdmin,
    PencilIcon, // Agrega el icono como componente
  },
  data() {
    return {
      modalActivo: null,
      nuevoStaff: { username: "", email: "" },
      nuevoEmpleado: {
        user_id: null,
        hire_date: "",
        specialty: "",
        is_active: true,
      },
      empleados: [],
      nextPage: null,
      previousPage: null,
      currentPage: 1,
      empleadoEditado: {
        specialty: "",
        is_active: true,
        employee_id: null,
      },
    };
  },
  methods: {
    obtenerToken() {
      return localStorage.getItem("token");
    },
    abrirModal(modal) {
      this.modalActivo = modal;
    },
    cerrarModal() {
      this.modalActivo = null;
      this.resetForm();
    },
    resetForm() {
      this.nuevoStaff = { username: "", email: "" };
      this.nuevoEmpleado = {
        user_id: null,
        hire_date: "",
        specialty: "",
        is_active: true,
      };
      this.empleadoEditado = {
        specialty: "",
        is_active: true,
        employee_id: null,
      };
    },
    async crearStaff() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/staff/create/", this.nuevoStaff, {
          headers: {
            Authorization: `Bearer ${this.obtenerToken()}`,
          },
        });
        this.nuevoEmpleado.user_id = response.data.id; // Ajusta esto según la respuesta de la API
        this.abrirModal('crearEmpleado'); // Abre el modal para crear el empleado
      } catch (error) {
        console.error("Error al crear staff:", error.response ? error.response.data : error.message);
        alert("Error al crear el staff. Por favor, inténtelo de nuevo.");
      }
    },
    async crearEmpleado() {
      try {
        await axios.post("http://127.0.0.1:8000/api/employees/create/", this.nuevoEmpleado, {
          headers: {
            Authorization: `Bearer ${this.obtenerToken()}`,
          },
        });
        alert("Empleado creado exitosamente.");
        this.cerrarModal();
        this.obtenerEmpleados(); // Refrescar la lista de empleados
      } catch (error) {
        console.error("Error al crear empleado:", error.response ? error.response.data : error.message);
        alert("Error al crear el empleado. Por favor, inténtelo de nuevo.");
      }
    },
    async obtenerEmpleados(url = "http://127.0.0.1:8000/api/employees/list/") {
      try {
        const response = await axios.get(url);
        this.empleados = response.data.results.map((empleado) => ({
          user_id: empleado.user_data.id,
          username: empleado.user_data.username,
          hire_date: empleado.hire_date,
          specialty: empleado.specialty,
          is_active: empleado.is_active,
          employee_id: empleado.employee_id,
        }));

        this.nextPage = response.data.next;
        this.previousPage = response.data.previous;
        if (this.nextPage) {
          this.currentPage = this.extractPageNumber(this.nextPage) - 1;
        } else if (this.previousPage) {
          this.currentPage = this.extractPageNumber(this.previousPage) + 1;
        } else {
          this.currentPage = 1;
        }
      } catch (error) {
        console.error("Error al obtener empleados:", error.response ? error.response.data : error.message);
        alert("Error al obtener la lista de empleados.");
      }
    },
    async actualizarEmpleado() {
      try {
        const response = await axios.put(
          `http://127.0.0.1:8000/api/employees/update/${this.empleadoEditado.employee_id}/`,
          {
            specialty: this.empleadoEditado.specialty,
            is_active: this.empleadoEditado.is_active,
          },
          {
            headers: {
              Authorization: `Bearer ${this.obtenerToken()}`,
            },
          }
        );
        alert("Empleado actualizado exitosamente.");
        this.cerrarModal();
        this.obtenerEmpleados(); // Refrescar la lista de empleados
      } catch (error) {
        console.error("Error al actualizar empleado:", error.response ? error.response.data : error.message);
        alert("Error al actualizar el empleado. Por favor, inténtelo de nuevo.");
      }
    },
    editarEmpleado(empleado) {
      this.empleadoEditado = { ...empleado }; // Cargar los datos del empleado en el formulario de edición
      this.abrirModal('editarEmpleado'); // Abrir el modal de edición
    },
    paginaAnterior() {
      if (this.previousPage) {
        this.obtenerEmpleados(this.previousPage);
      }
    },
    siguientePagina() {
      if (this.nextPage) {
        this.obtenerEmpleados(this.nextPage);
      }
    },
    extractPageNumber(url) {
      if (!url) return null;
      const params = new URLSearchParams(url.split('?')[1]);
      return parseInt(params.get('page')) || 1;
    },
  },
  created() {
    this.obtenerEmpleados();
  },
};
</script>