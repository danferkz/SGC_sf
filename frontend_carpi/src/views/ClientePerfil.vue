<template>
  <div class="min-h-screen bg-gray-100 text-gray-800">
    <!-- Header General -->
    <Header />

    <div class="max-w-4xl mx-auto mt-8">
      <!-- Profile Card -->
      <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
        <div class="flex items-center gap-4 mb-8">
          <div class="w-20 h-20 bg-gray-200 rounded-full flex items-center justify-center">
            <UserIcon class="w-12 h-12 text-gray-500" />
          </div>
          <div>
            <h2 class="text-2xl font-bold">{{ user.name }}</h2>
            <p class="text-gray-600">{{ user.email }}</p>
          </div>
        </div>

        <!-- Profile Information -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
          <div class="flex items-center gap-4">
            <PhoneIcon class="w-5 h-5 text-gray-500" />
            <span class="font-medium">Teléfono:</span>
            <span class="text-gray-600">{{ user.phone || 'No disponible' }}</span>
          </div>
          <div class="flex items-center gap-4">
            <CreditCardIcon class="w-5 h-5 text-gray-500" />
            <span class="font-medium">DNI:</span>
            <span class="text-gray-600">{{ user.dni || 'No disponible' }}</span>
          </div>
          <div class="flex items-center gap-4">
            <UserIcon class="w-5 h-5 text-gray-500" />
            <span class="font-medium">Sexo:</span>
            <span class="text-gray-600">{{ user.gender || 'No disponible' }}</span>
          </div>
          <div class="flex items-center gap-4">
            <HomeIcon class="w-5 h-5 text-gray-500" />
            <span class="font-medium">Dirección:</span>
            <span class="text-gray-600">{{ user.address || 'No disponible' }}</span>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-wrap gap-4">
          <button @click="openModal('updateProfile')" class="btn btn-primary">Actualizar Perfil</button>
          <button @click="openModal('changePassword')" class="btn btn-warning">Cambiar Contraseña</button>
          <button @click="openModal('deleteAccount')" class="btn btn-error">Eliminar Cuenta</button>
          <button @click="openModal('logout')" class="btn">Cerrar Sesión</button>
        </div>
      </div>

      <!-- Orders Table -->
      <div class="bg-white rounded-lg shadow-lg p-6">
    <h3 class="text-xl font-bold mb-4">Pedidos Realizados</h3>
    <div class="overflow-x-auto">
      <table class="table w-full">
        <thead>
          <tr class="bg-gray-100">
            <th class="text-left p-2">ID del Pedido</th>
            <th class="text-left p-2">Fecha Prometida</th>
            <th class="text-left p-2">Precio Total</th>
            <th class="text-left p-2">Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orders" :key="order.orders_id" class="border-b">
            <td class="p-2">{{ order.orders_id }}</td>
            <td class="p-2">{{ formatDate(order.promised_date) }}</td>
            <td class="p-2">S/. {{ Number(order.total_price).toFixed(2) }}</td>
            <td class="p-2">
              <span 
                class="px-2 py-1 rounded-full text-sm font-medium"
                :class="{
                  'bg-green-100 text-green-800': order.status === 'completed',
                  'bg-yellow-100 text-yellow-800': order.status === 'pending',
                  'bg-blue-100 text-blue-800': order.status === 'in_process'
                }"
              >
                {{ translateStatus(order.status) }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
    </div>

    <!-- Modals -->
    <div v-if="showModal" class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center">
      <div class="bg-white p-6 rounded-lg shadow-lg w-96">
        <h3 class="text-xl font-bold mb-4">{{ modalTitle }}</h3>
        
        <!-- Update Profile Modal -->
        <div v-if="currentAction === 'updateProfile'">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Nombre de usuario</label>
            <input 
              v-model="userData.username" 
              type="text" 
              @input="userData.username = userData.username.replace(/\s/g, '')"
              placeholder="Sin espacios"
              class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Correo electrónico</label>
            <input v-model="userData.email" type="email" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Teléfono</label>
            <input 
              v-model="userData.phone" 
              type="tel" 
              maxlength="9"
              @input="userData.phone = userData.phone.replace(/\D/g, '').slice(0, 9)"
              placeholder="Máximo 9 dígitos"
              class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
            <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">DNI</label>
            <input 
              v-model="userData.dni" 
              type="number"
              min="0"
              maxlength="8"
              oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
              class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3"
            >
            </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Sexo</label>
            <select v-model="userData.sex" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
              <option value="">Selecciona</option>
              <option value="male">Masculino</option>
              <option value="female">Femenino</option>
              <option value="other">Otro</option>
            </select>
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Dirección</label>
            <input v-model="userData.address" type="text" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
        </div>

        <!-- Change Password Modal -->
        <div v-if="currentAction === 'changePassword'">
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Contraseña Actual</label>
            <input v-model="passwordData.oldPassword" type="password" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Nueva Contraseña</label>
            <input v-model="passwordData.newPassword" type="password" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-gray-700">Confirmar Nueva Contraseña</label>
            <input v-model="passwordData.confirmPassword" type="password" class="h-10 mt-1 block w-full rounded-md border border-gray-200 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 px-3">
          </div>
        </div>

        <!-- Delete Account and Logout Modals -->
        <p v-if="currentAction === 'deleteAccount' || currentAction === 'logout'" class="mb-6">{{ modalMessage }}</p>

        <div class="flex justify-end gap-4">
          <button @click="closeModal" class="btn btn-secondary">Cancelar</button>
          <button @click="handleAction" class="btn btn-primary">{{ modalAction }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router' 
import { UserIcon, PhoneIcon, CreditCardIcon, HomeIcon } from 'lucide-vue-next'
import Header from '@/components/HeaderCompo.vue'
import axios from 'axios'
const router = useRouter()


import { useStore } from 'vuex';

// Accede al store de Vuex
const store = useStore();


const user = ref({
  name: 'Usuario',
  email: 'email@example.com',
  phone: 'No disponible',
  dni: 'No disponible',
  gender: 'No disponible',
  address: 'No disponible'
})

const orders = ref([])

const showModal = ref(false)
const modalTitle = ref('')
const modalMessage = ref('')
const modalAction = ref('')
const currentAction = ref('')

const userData = ref({
  username: '',
  email: '',
  phone: '',
  dni: '',
  sex: '',
  address: ''
})

const passwordData = ref({
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

// Función para obtener el token del localStorage
const obtenerToken = () => {
  return localStorage.getItem("token");
}

const fetchUserProfile = async () => {
  try {
    const token = obtenerToken(); // Obtener el token
    
    const response = await fetch('http://127.0.0.1:8000/api/users/clients/profile', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Error al obtener los datos del perfil');
    }

    const data = await response.json();
    console.log('Datos del perfil recibidos:', data.id);

    // Guardar el ID del usuario en localStorage
    localStorage.setItem('userId', data.id);

    // Actualiza el estado del usuario con los datos recibidos
    user.value = {
      id: data.id,
      name: data.username,
      email: data.email,
      phone: data.phone || 'No disponible',
      dni: data.dni || 'No disponible',
      gender: data.gender || 'No disponible',
      address: data.address || 'No disponible'
    };

    // También actualiza userData si es necesario
    userData.value = {
      username: data.username,
      email: data.email,
      phone: data.phone || '',
      dni: data.dni || '',
      sex: data.gender || '',
      address: data.address || ''
    };

    } catch (error) {
      console.error('Error fetching user profile:', error);
      // Manejo de errores, por ejemplo, mostrar un mensaje al usuario
    }
  };
  
  const updateUserProfile = async () => {
    try {
      const token = obtenerToken(); // Obtener el token
      const userId = user.value.id; // Asumiendo que has agregado el id al objeto user

      const response = await fetch(`http://127.0.0.1:8000/api/users/clients/update/${userId}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          username: userData.value.username,
          email: userData.value.email,
          dni: userData.value.dni,
          gender: userData.value.sex === 'male' ? 'M' : userData.value.sex === 'female' ? 'F' : null,
          address: userData.value.address,
          phone: userData.value.phone
        })
      });

      if (!response.ok) {
        throw new Error('Error al actualizar el perfil');
      }

      const updatedData = await response.json();
      console.log('Perfil actualizado:', updatedData);

      // Actualiza el estado del usuario con los nuevos datos
      user.value = {
        ...user.value,
        ...updatedData // Suponiendo que la respuesta incluye todos los campos actualizados
      };

      alert('Perfil actualizado con éxito');
      // Recarga la página después de actualizar exitosamente
      router.go(0);
    } catch (error) {
      console.error('Error al actualizar el perfil:', error);
      alert('No se pudo actualizar el perfil. Intenta nuevamente más tarde.');
    }
  };

const updatePassword = async () => {
  // Validar que la nueva contraseña y la confirmación coincidan
  if (passwordData.value.newPassword !== passwordData.value.confirmPassword) {
    alert('Las nuevas contraseñas no coinciden.');
    return;
  }

  try {
    const token = obtenerToken(); // Obtener el token

    const response = await fetch('http://127.0.0.1:8000/api/users/change-password/', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        old_password: passwordData.value.oldPassword,
        new_password: passwordData.value.newPassword
      })
    });

    // Verificar si la respuesta es exitosa
    if (response.ok) {
      // Solo intenta leer el cuerpo si la respuesta tiene contenido
      const data = await response.text(); // Leer como texto
      if (data) {
        const jsonData = JSON.parse(data); // Convertir a JSON si hay contenido
        console.log('Contraseña cambiada:', jsonData);
      } else {
        console.log('Contraseña cambiada, pero sin respuesta JSON');
      }
      alert('Contraseña actualizada con éxito');

      // Limpiar los campos de la contraseña después de la actualización
      passwordData.value = {
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      };
    } else {
      // Manejo de error cuando la respuesta no es exitosa
      const errorData = await response.text(); // Leer como texto
      console.error('Error al cambiar la contraseña:', errorData);
      alert('No se pudo cambiar la contraseña. ' + (errorData || 'Error desconocido.'));
    }
  } catch (error) {
    console.error('Error al cambiar la contraseña:', error);
    alert('Ocurrió un error al intentar cambiar la contraseña. Por favor, inténtalo de nuevo más tarde.');
  }
};

const deleteUserAccount = async () => {
  try {
    const token = obtenerToken(); // Obtener el token

    const response = await fetch('http://127.0.0.1:8000/api/users/clients/self-delete/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      throw new Error('Error al eliminar la cuenta');
    }

    // Si la cuenta se elimina con éxito, redirige al usuario
    alert('Cuenta eliminada con éxito');
    localStorage.removeItem("token"); // Elimina el token del localStorage
    router.push('/'); // Redirige a la página principal
  } catch (error) {
    console.error('Error al eliminar la cuenta:', error);
    alert('No se pudo eliminar la cuenta. Intenta nuevamente más tarde.');
  }
};

const handleLogout = () => {
    store.dispatch('sessions/logout'); // Llama a la acción de logout en Vuex
    router.push('/'); // Redirige a la página principal
};

const openModal = (action) => {
  currentAction.value = action

  switch (action) {
    case 'updateProfile':
      modalTitle.value = 'Actualizar Perfil'
      modalAction.value = 'Actualizar'
      break
    case 'changePassword':
      modalTitle.value = 'Cambiar Contraseña'
      modalAction.value = 'Cambiar'
      break
    case 'deleteAccount':
      modalTitle.value = 'Eliminar Cuenta'
      modalMessage.value = '¿Estás seguro de que quieres eliminar tu cuenta? Esta acción no se puede deshacer.'
      modalAction.value = 'Eliminar'
      break
    case 'logout':
      modalTitle.value = 'Cerrar Sesión'
      modalMessage.value = '¿Estás seguro de que quieres cerrar sesión?'
      modalAction.value = 'Cerrar'
      break
  }
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
  currentAction.value = ''
  userData.value = { username: '', email: '', phone: '', dni: '', sex: '', address: '' }
  passwordData.value = { oldPassword: '', newPassword: '', confirmPassword: '' }
}

const handleAction = async () => {
  switch (currentAction.value) {
    case 'updateProfile':
      await updateUserProfile();
      console.log('Perfil actualizado', userData.value)
      // Aquí iría la lógica para actualizar el perfil en el backend
      break
    case 'changePassword':
    await updatePassword();
      console.log('Contraseña cambiada', passwordData.value)
      // Aquí iría la lógica para cambiar la contraseña en el backend
      break
    case 'deleteAccount':
      await deleteUserAccount();
      console.log('Cuenta eliminada')
      // Aquí iría la lógica para eliminar la cuenta en el backend
      break
    case 'logout':
      await handleLogout();
      console.log('Sesión cerrada')
       // Redirige a la página principal
      break
  }
  closeModal()
}

const fetchOrders = async () => {
  try {
    const token = obtenerToken(); // Obtener el token
    const response = await axios.get('http://localhost:8000/api/orders/orders-list-client/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    orders.value = response.data.results; // Guardar los pedidos en la referencia
  } catch (error) {
    console.error('Error al obtener los pedidos:', error);
  }
}

// Modificar onMounted para incluir la llamada a fetchOrders
onMounted(async () => {
  await fetchUserProfile();
  await fetchOrders(); // Llamada a fetchOrders

  // Using a flag in localStorage to control one-time reload
  if (!localStorage.getItem('pageLoaded')) {
    localStorage.setItem('pageLoaded', 'true');
    router.go(0);
  } else {
    localStorage.removeItem('pageLoaded');
  }
});

// Métodos para formatear la fecha y traducir el estado
const formatDate = (date) => {
  return new Date(date).toLocaleDateString('es-ES');
};

const translateStatus = (status) => {
  const statusMap = {
    'pending': 'Pendiente',
    'completed': 'Completado',
    'in_process': 'En Proceso'
  };
  return statusMap[status] || status;
};
</script>

<style scoped>
.fixed {
  position: fixed;
}
.bg-gray-500 {
  background-color: rgba(0, 0, 0, 0.5);
}
</style>