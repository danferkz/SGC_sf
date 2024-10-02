<template>
    <div class="navbar bg-base-100">
        <div class="navbar-start">
            <div class="dropdown">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M4 6h16M4 12h16M4 18h7" />
                    </svg>
                </div>
                <ul tabindex="0"
                    class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li><router-link to="/">Homepage</router-link></li>
                    <li><router-link to="/producto">Productos</router-link></li>
                </ul>
            </div>
        </div>
        <div class="navbar-center">
            <router-link to="/" class="btn btn-ghost text-xl">Maderera El Bosque</router-link>
        </div>
        <div class="navbar-end">
            <div class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <img alt="Tailwind CSS Navbar component"
                            src="../assets/usuario_log.png" />
                    </div>
                </div>
                <ul tabindex="0"
                    class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
                    <li><router-link to="/login">login</router-link></li>
                    <li><router-link to="/cliente">Profile</router-link></li>
                    <li><router-link to="/settings">Settings</router-link></li>
                    <li><router-link to="/logout">Logout</router-link></li>
                </ul>
            </div>
        </div>
    </div>

</template>

<script setup>

</script>

<style scoped>
</style>
