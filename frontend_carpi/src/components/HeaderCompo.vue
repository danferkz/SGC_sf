<template>
    <div>
        <div class="navbar bg-base-100 shadow-lg">
            <div class="navbar-start">
                <div class="dropdown">
                    <label tabindex="0" class="btn btn-ghost btn-circle">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h7" />
                        </svg>
                    </label>
                    <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
                        <li><a href="#productos">Productos</a></li>
                        <li><a href="#pedidos">Pedidos</a></li>
                        <li><router-link to="/login">Login</router-link></li>
                    </ul>
                </div>
                <a class="btn btn-ghost normal-case text-xl">Carpidsfsdfsdfsdfdsfsdfsdfsdfsfdsfsdfsdntería - Dego</a>
            </div>
            <div class="navbar-center hidden lg:flex">
                <ul class="menu menu-horizontal px-1">
                    <li><a href="#productos">Productos</a></li>
                    <li><a href="#pedidos">Pedidos</a></li>
                    <li><router-link to="/login">Login</router-link></li>
                </ul>
            </div>
            <div class="navbar-end">
                <button class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
                <button class="btn btn-ghost btn-circle">
                    <div class="indicator">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                        </svg>
                        <span class="badge badge-xs badge-primary indicator-item"></span>
                    </div>
                </button>
            </div>
        </div>
    </div>

    <!-- Mobile Menu 
     <template>
    <div>
        <header class="bg-amber-800 bg-opacity-90 text-white py-4 px-6 shadow-lg">
            <div class="container mx-auto flex justify-between items-center">
                <h1 class="text-2xl font-bold">Carpintería Artesanal</h1>
                <nav>
                    <ul class="flex space-x-6">
                        <li><a href="#productos" class="hover:text-amber-200 transition">Productos</a></li>
                        <li><a href="#pedidos" class="hover:text-amber-200 transition">Pedidos</a></li>
                        <li><router-link to="/login" class="hover:text-amber-200 transition">Login</router-link></li>
                    </ul>
                </nav>
            </div>
        </header>
    </div>
</template>

<script setup>
</script>

<style lang="scss" scoped>
</style>
     -->
</template>

<script setup>
</script>

<style scoped></style>