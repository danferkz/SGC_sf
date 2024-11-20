<template>
  <div class="min-h-screen bg-gray-100 text-gray-800 flex">
    <!-- Header -->
    <HeaderAdmin class="header-admin" />

    <section id="dashboard" class="flex-1 py-16 px-6 bg-white">
      <div class="container mx-auto">
        <h3 class="text-3xl font-bold text-center mb-12">Empleados</h3>

        <!-- Wrapper -->
        <div class="bg-gray-100 flex justify-center">
          <div class="bg-white shadow-md rounded-lg overflow-hidden w-full max-w-7xl">
            <!-- Botón para abrir modal de crear staff -->
            <div class="p-4 flex justify-end">
              <button
                @click="abrirModal('crearStaff')"
                class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"
              >
                Crear Staff
              </button>
            </div>

            <!-- Tabla de empleados -->
            <div class="overflow-x-auto">
              <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                  <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      ID_Empleado
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Fecha de Contrato
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Especialidad
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Estado
                    </th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="empleado in empleados" :key="empleado.user_id">
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {{ empleado.user_id }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {{ empleado.hire_date }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {{ empleado.specialty }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span
                        :class="['px-2 inline-flex text-xs leading-5 font-semibold rounded-full', empleado.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800']"
                      >
                        {{ empleado.is_active ? 'Activo' : 'Inactivo' }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal Crear Staff -->
    <div
      v-if="modalActivo === 'crearStaff'"
      class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50"
    >
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-lg font-semibold mb-4">Crear Staff</h2>
        <form @submit.prevent="crearStaff">
          <div class="mb-4">
            <label class="block text-gray-700">Username</label>
            <input
              v-model="nuevoStaff.username"
              type="text"
              class="w-full border rounded-md px-4 py-2"
              required
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Email</label>
            <input
              v-model="nuevoStaff.email"
              type="email"
              class="w-full border rounded-md px-4 py-2"
              required
            />
          </div>
          <div class="flex justify-end space-x-4">
            <button
              @click="cerrarModal"
              class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"
            >
              Continuar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal Crear Empleado -->
    <div
      v-if="modalActivo === 'crearEmpleado'"
      class="fixed inset-0 bg-gray-600 bg-opacity-50 flex items-center justify-center z-50"
    >
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-lg font-semibold mb-4">Crear Empleado</h2>
        <form @submit.prevent="crearEmpleado">
          <div class="mb-4">
            <label class="block text-gray-700">Fecha de Contrato</label>
            <input
              v-model="nuevoEmpleado.hire_date"
              type="date"
              class="w-full border rounded-md px-4 py-2"
              required
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700">Especialidad</label>
            <input
              v-model="nuevoEmpleado.specialty"
              type="text"
              class="w-full border rounded-md px-4 py-2"
              required
            />
          </div>
          <div class="flex justify-end space-x-4">
            <button
              @click="cerrarModal"
              class="bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
            >
              Guardar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderAdmin from "@/components/NabvarVerticalAdmin.vue";
import axios from "axios";

export default {
  components: {
    HeaderAdmin,
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
    },
    async crearStaff() {
      try {
        const token = this.obtenerToken();
        if (!token) {
          alert("No se encontró un token de autenticación.");
          return;
        }
        const response = await axios.post(
          "http://127.0.0.1:8000/api/users/staff/create/",
          this.nuevoStaff,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        const staffCreado = response.data;
        this.nuevoEmpleado.user_id = staffCreado.id;
        this.nuevoStaff = { username: "", email: "" };
        this.modalActivo = "crearEmpleado";
      } catch (error) {
        console.error("Error al crear staff:", error);
        alert("Error al crear el staff. Verifica los datos.");
      }
    },
    async crearEmpleado() {
      try {
        const token = this.obtenerToken();
        if (!token) {
          alert("No se encontró un token de autenticación.");
          return;
        }
        await axios.post(
          "http://127.0.0.1:8000/api/employees/create/",
          this.nuevoEmpleado,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        this.empleados.push({ ...this.nuevoEmpleado });
        this.nuevoEmpleado = {
          user_id: null,
          hire_date: "",
          specialty: "",
          is_active: true,
        };
        this.cerrarModal();
      } catch (error) {
        console.error("Error al crear empleado:", error);
        alert("Error al crear el empleado.");
      }
    },
  },
};
</script>
