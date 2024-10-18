<template>
    <div>
        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div class="bg-white shadow sm:rounded-lg">
                <div class="px-4 py-5 sm:px-6">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <div class="avatar">
                                <div class="w-24 rounded">
                                    <img src="../assets/usuario_log.png" alt="Usuario" />
                                </div>
                            </div>
                            <div class="ml-4">
                                <div v-if="currentUser">
                                    <h1 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
                                        {{ currentUser.name }}
                                    </h1>
                                    <p class="text-sm font-medium text-gray-500">
                                        {{ currentUser.email }}
                                    </p>
                                    <button @click="handleLogout" class="btn">Cerrar sesión</button>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { onMounted } from 'vue';

export default {
    computed: {
        ...mapGetters('sessions', ['currentUser']),
    },
    beforeRouteEnter(to, from, next) {
        next(async (vm) => {
            if (!vm.currentUser) {
                // Intenta hacer autoLogin si el usuario no está ya en el estado
                await vm.$store.dispatch('sessions/autoLogin');
            }
        });
    },
    methods: {
        handleLogout() {
            this.$store.dispatch('sessions/logout');
            this.$router.push('/login'); // Ajusta según tu ruta
        },
    }
};
</script>
