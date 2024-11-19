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
                  <th class="text-left p-2">Cantidad</th>
                  <th class="text-left p-2">Tipo de Producto</th>
                  <th class="text-left p-2">Precio</th>
                  <th class="text-left p-2">Estado</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="order in orders" :key="order.id" class="border-b">
                  <td class="p-2">{{ order.quantity }}</td>
                  <td class="p-2">{{ order.productType }}</td>
                  <td class="p-2">S/. {{ order.price.toFixed(2) }}</td>
                  <td class="p-2">
                    <span 
                      class="px-2 py-1 rounded-full text-sm font-medium"
                      :class="{
                        'bg-green-100 text-green-800': order.status === 'Completado',
                        'bg-yellow-100 text-yellow-800': order.status === 'Pendiente',
                        'bg-blue-100 text-blue-800': order.status === 'En Proceso'
                      }"
                    >
                      {{ order.status }}
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
              <input v-model="userData.username" type="text" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Correo electrónico</label>
              <input v-model="userData.email" type="email" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Teléfono</label>
              <input v-model="userData.phone" type="tel" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">DNI</label>
              <input v-model="userData.dni" type="text" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Sexo</label>
              <select v-model="userData.sex" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
                <option value="">Selecciona</option>
                <option value="male">Masculino</option>
                <option value="female">Femenino</option>
                <option value="other">Otro</option>
              </select>
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Dirección</label>
              <input v-model="userData.address" type="text" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
          </div>
  
          <!-- Change Password Modal -->
          <div v-if="currentAction === 'changePassword'">
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Contraseña Actual</label>
              <input v-model="passwordData.oldPassword" type="password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Nueva Contraseña</label>
              <input v-model="passwordData.newPassword" type="password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
            </div>
            <div class="mb-4">
              <label class="block text-sm font-medium text-gray-700">Confirmar Nueva Contraseña</label>
              <input v-model="passwordData.confirmPassword" type="password" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50">
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
  // añade que se recarge una vez para actualizr los datos
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router' 
  import { UserIcon, PhoneIcon, CreditCardIcon, HomeIcon } from 'lucide-vue-next'
  import Header from '@/components/HeaderCompo.vue'
  
  const router = useRouter()
  
  //onMounted(() => {
    // Verificamos si ya se ha recargado usando localStorage
  //  const hasReloaded = localStorage.getItem('hasPageReloaded')
    
  //  if (!hasReloaded) {
      // Establecemos la bandera antes de recargar
  //    localStorage.setItem('hasPageReloaded', 'true')
      // Recargamos la página
  //    window.location.reload()
  //  } else {
      // Limpiamos la bandera para la próxima vez
  //    localStorage.removeItem('hasPageReloaded')
  //  }
  //})
  
  const user = ref({
    name: 'Usuario',
    email: 'email@example.com',
    phone: 'No disponible',
    dni: 'No disponible',
    gender: 'No disponible',
    address: 'No disponible'
  })
  
  const orders = ref([
    { id: 1, quantity: 2, productType: 'Puerta', price: 180.00, status: 'Completado' },
  ])
  
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
  
  const handleAction = () => {
    switch (currentAction.value) {
      case 'updateProfile':
        console.log('Perfil actualizado', userData.value)
        // Aquí iría la lógica para actualizar el perfil en el backend
        break
      case 'changePassword':
        console.log('Contraseña cambiada', passwordData.value)
        // Aquí iría la lógica para cambiar la contraseña en el backend
        break
      case 'deleteAccount':
        console.log('Cuenta eliminada')
        // Aquí iría la lógica para eliminar la cuenta en el backend
        break
      case 'logout':
        console.log('Sesión cerrada')
        // Aquí iría la lógica para cerrar sesión
        break
    }
    closeModal()
  }
  </script>
  
  <style scoped>
  .fixed {
    position: fixed;
  }
  .bg-gray-500 {
    background-color: rgba(0, 0, 0, 0.5);
  }
  </style>