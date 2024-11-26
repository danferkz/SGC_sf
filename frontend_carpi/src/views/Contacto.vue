<template>
    <div class="font-sans text-brown-700 bg-orange-50">
        <!-- Header with margin-bottom for spacing -->
        <Header class="mb-16" />

        <!-- Main content with increased padding for vertical spacing -->
        <main class="max-w-7xl mx-auto py-32 px-12">
            <h2 class="text-orange-800 text-3xl text-center mb-8">Contacto</h2>

            <div class="flex flex-wrap gap-8 justify-between">
                <section class="flex-1 min-w-[300px]">
                    <h3 class="text-orange-800 text-2xl text-center mb-6">Envíanos un mensaje</h3>
                    <form @submit.prevent="enviarFormulario" class="space-y-4">
                        <div>
                            <label for="nombre" class="block font-bold mb-2">Nombre:</label>
                            <input type="text" id="nombre" v-model="formData.nombre" required class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
                        </div>
                        <div>
                            <label for="email" class="block font-bold mb-2">Email:</label>
                            <input type="email" id="email" v-model="formData.email" required class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
                        </div>
                        <div>
                            <label for="telefono" class="block font-bold mb-2">Teléfono:</label>
                            <input type="tel" id="telefono" v-model="formData.telefono" class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
                        </div>
                        <div>
                            <label for="asunto" class="block font-bold mb-2">Asunto:</label>
                            <select id="asunto" v-model="formData.asunto" required class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md h-12 p-1.5">
                                <option value="">Seleccione un asunto</option>
                                <option value="consulta">Consulta general</option>
                                <option value="presupuesto">Solicitud de presupuesto</option>
                                <option value="cita">Agendar una cita</option>
                                <option value="otro">Otro</option>
                            </select>
                        </div>
                        <div>
                            <label for="mensaje" class="block font-bold mb-2">Mensaje:</label>
                            <textarea id="mensaje" v-model="formData.mensaje" required class="mt-1 block w-full shadow-sm sm:text-sm border border-gray-300 focus:ring-amber-500 focus:border-amber-500 rounded-md resize-none p-1.5"></textarea>
                        </div>
                        <button type="submit" class="bg-orange-600 text-orange-50 rounded px-4 py-2 text-lg hover:bg-orange-700 transition duration-300">Enviar mensaje</button>
                    </form>
                </section>

                <section class="flex-1 min-w-[300px]">
                    <h3 class="text-orange-800 text-2xl text-center mb-6">Información de contacto</h3>
                    <div class="space-y-4">
                        <div>
                            <strong>Dirección:</strong>
                            <p>Av. de los Árboles 123, Ciudad Bosque, CP 12345</p>
                        </div>
                        <div>
                            <strong>Teléfono:</strong>
                            <p>+1 (234) 567-8900</p>
                        </div>
                        <div>
                            <strong>Email:</strong>
                            <p>info@madereraelbosque.com</p>
                        </div>
                        <div>
                            <strong>Horario de atención:</strong>
                            <p>Lunes a Viernes: 9:00 AM - 6:00 PM</p>
                            <p>Sábados: 10:00 AM - 2:00 PM</p>
                        </div>
                    </div>
                </section>
            </div>
        </main>

        <!-- Footer with margin-top for spacing -->
        <Footer class="mt-28" />
    </div>
</template>


<script setup>
import { ref } from 'vue';
import Header from "@/components/HeaderCompo.vue";
import Footer from "@/components/FooterCompo.vue";

const formData = ref({
    nombre: '',
    email: '',
    telefono: '',
    asunto: '',
    mensaje: ''
});

const enviarFormulario = () => {
    // Aquí iría la lógica para enviar el formulario
    console.log('Formulario enviado:', formData.value);
    // Reiniciar el formulario después del envío
    formData.value = {
        nombre: '',
        email: '',
        telefono: '',
        asunto: '',
        mensaje: ''
    };
    alert('Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.');
};
</script>

<style scoped>
/* No se requieren estilos adicionales ya que Tailwind CSS maneja el diseño */
</style>