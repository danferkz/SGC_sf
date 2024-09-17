<template>
    <div>
        <Header />
        <div class="min-h-screen bg-wood-pattern flex items-center justify-center px-4">
            <div class="max-w-md w-full space-y-8 bg-[#FFFBEB] p-10 rounded-xl shadow-2xl">
                <div>
                    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                        Iniciar Sesión
                    </h2>
                    <p class="mt-2 text-center text-sm text-gray-600">
                        Accede a tu cuenta de Carpintería Maderera El Bosque
                    </p>
                </div>
                <form class="mt-8 space-y-6">
                    <div class="rounded-md shadow-sm -space-y-px">
                        <div>
                            <!-- Changed margin-bottom to 5px -->
                            <label for="email-address" class="sr-only">Correo electrónico</label>
                            <input
                                id="email-address"
                                name="email"
                                type="email"
                                autocomplete="email"
                                required
                                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white rounded-t-md focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                                placeholder="Correo electrónico"
                            />
                        </div>
                        <div>
                            <label for="password" class="sr-only">Contraseña</label>
                            <input
                                id="password"
                                name="password"
                                type="password"
                                autocomplete="current-password"
                                required
                                class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 bg-white rounded-b-md focus:outline-none focus:ring-amber-500 focus:border-amber-500 focus:z-10 sm:text-sm"
                                placeholder="Contraseña"
                            />
                        </div>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <input
                                id="remember-me"
                                name="remember-me"
                                type="checkbox"
                                class="h-4 w-4 text-amber-600 focus:ring-amber-500 border-gray-300 rounded"
                            />
                            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
                                Recordarme
                            </label>
                        </div>

                        <div class="text-sm">
                            <a href="#" class="font-medium text-amber-600 hover:text-amber-500">
                                ¿Olvidaste tu contraseña?
                            </a>
                        </div>
                    </div>

                    <div>
                        <button
                            type="submit"
                            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-amber-500"
                        >
                            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                                <LockClosedIcon class="h-5 w-5 text-amber-500 group-hover:text-amber-400" aria-hidden="true" />
                            </span>
                            Iniciar Sesión
                        </button>
                    </div>
                </form>
                <div class="text-center">
                    ¿No tienes una cuenta?
                    <router-link to="/registro" class="font-medium text-amber-600 hover:text-amber-500">
                        Regístrate aquí
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
// importa el componente header
import Header from '@/components/HeaderCompo.vue'
</script>

<style>
</style>
