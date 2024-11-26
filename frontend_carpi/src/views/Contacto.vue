<template>
    <div class="contacto">
        <Header />

        <main class="content">
            <h2>Contacto</h2>

            <div class="contacto-container">
                <section class="formulario-contacto">
                    <h3>Envíanos un mensaje</h3>
                    <form @submit.prevent="enviarFormulario">
                        <div class="form-group">
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" v-model="formData.nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email:</label>
                            <input type="email" id="email" v-model="formData.email" required>
                        </div>
                        <div class="form-group">
                            <label for="telefono">Teléfono:</label>
                            <input type="tel" id="telefono" v-model="formData.telefono">
                        </div>
                        <div class="form-group">
                            <label for="asunto">Asunto:</label>
                            <select id="asunto" v-model="formData.asunto" required>
                                <option value="">Seleccione un asunto</option>
                                <option value="consulta">Consulta general</option>
                                <option value="presupuesto">Solicitud de presupuesto</option>
                                <option value="cita">Agendar una cita</option>
                                <option value="otro">Otro</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="mensaje">Mensaje:</label>
                            <textarea id="mensaje" v-model="formData.mensaje" required></textarea>
                        </div>
                        <button type="submit" class="boton-enviar">Enviar mensaje</button>
                    </form>
                </section>

                <section class="info-contacto">
                    <h3>Información de contacto</h3>
                    <div class="info-item">
                        <strong>Dirección:</strong>
                        <p>Av. de los Árboles 123, Ciudad Bosque, CP 12345</p>
                    </div>
                    <div class="info-item">
                        <strong>Teléfono:</strong>
                        <p>+1 (234) 567-8900</p>
                    </div>
                    <div class="info-item">
                        <strong>Email:</strong>
                        <p>info@madereraelbosque.com</p>
                    </div>
                    <div class="info-item">
                        <strong>Horario de atención:</strong>
                        <p>Lunes a Viernes: 9:00 AM - 6:00 PM</p>
                        <p>Sábados: 10:00 AM - 2:00 PM</p>
                    </div>

                </section>
            </div>
        </main>
        <!-- Footer -->
        <Footer class="footer" />
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
.contacto {
    font-family: 'Arial', sans-serif;
    color: #5D4037;
    background-color: #FFF3E0;
}



h1 {
    color: #FFF3E0;
    font-size: 2.5rem;
    margin: 0;
}

.content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

h2,
h3 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
}

.contacto-container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: space-between;
}

.formulario-contacto,
.info-contacto {
    flex: 1;
    min-width: 300px;
}

.form-group {
    margin-bottom: 1rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

input,
select,
textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #FFE0B2;
    border-radius: 4px;
    background-color: #FFF3E0;
}

textarea {
    height: 150px;
}

.boton-enviar {
    background-color: #FF9800;
    color: #FFF3E0;
    border: none;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.boton-enviar:hover {
    background-color: #E65100;
}

.info-item {
    margin-bottom: 1rem;
}

.mapa {
    margin-top: 2rem;
}

.mapa-imagen {
    width: 100%;
    height: auto;
    border-radius: 8px;
}

@media (max-width: 768px) {
    .contacto-container {
        flex-direction: column;
    }
}
</style>