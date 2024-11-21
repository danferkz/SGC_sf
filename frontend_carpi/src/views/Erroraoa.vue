<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-[#FFFBEB] p-4">
        <div class="text-center max-w-lg">
            <div class="mb-8 relative inline-block">
                <CircleSlash class="w-32 h-32 text-[#D97706]" />
                <Lock
                    class="w-16 h-16 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-black" />
            </div>
            <h1 class="text-6xl font-bold text-black mb-4">Página no encontrada</h1>
            <p class="text-2xl text-black mb-4">Lo sentimos, la página que buscas no existe.</p>
            <p class="text-lg text-black mb-8">
                Por favor, verifica la URL o vuelve a la página principal.
            </p>
            <router-link to="/" class="text-lg font-semibold text-[#D97706] hover:underline">
                Volver al inicio
            </router-link>
        </div>
        <div class="mt-12 w-full max-w-2xl">
            <div class="flex justify-between">
                <TreePine v-for="i in 5" :key="i" :class="`w-${[16, 20, 24, 20, 16][i - 1]} h-${[16, 20, 24, 20, 16][i - 1]
                    } text-[#D97706] tree`" />
            </div>
        </div>
    </div>
</template>


<script>

</script>

<style scoped>
.tree {
    transition: transform 0.3s ease-in-out;
}

.tree:hover {
    transform: scale(1.1);
}
</style>