<template>
    <div class="trabajos">
      <Header />
  
      <main class="content">
        <h2>Nuestros Trabajos</h2>
        
        <div class="filtros">
          <button 
            v-for="categoria in categorias" 
            :key="categoria"
            @click="filtrarPor(categoria)"
            :class="{ active: categoriaActual === categoria }"
            class="filtro-btn"
          >
            {{ categoria }}
          </button>
        </div>
  
        <div class="trabajos-grid">
          <div 
            v-for="trabajo in trabajosFiltrados" 
            :key="trabajo.id" 
            class="trabajo-card"
            @click="seleccionarTrabajo(trabajo)"
          >
            <img :src="trabajo.imagen" :alt="trabajo.titulo" class="trabajo-imagen">
            <div class="trabajo-info">
              <h3>{{ trabajo.titulo }}</h3>
              <p>{{ trabajo.descripcionCorta }}</p>
            </div>
          </div>
        </div>
  
        <div v-if="trabajoSeleccionado" class="modal" @click="cerrarModal">
          <div class="modal-content" @click.stop>
            <button class="cerrar-btn" @click="cerrarModal" aria-label="Cerrar modal">&times;</button>
            <img :src="trabajoSeleccionado.imagen" :alt="trabajoSeleccionado.titulo" class="modal-imagen">
            <h3>{{ trabajoSeleccionado.titulo }}</h3>
            <p>{{ trabajoSeleccionado.descripcionLarga }}</p>
            <ul class="detalles-lista">
              <li><strong>Cliente:</strong> {{ trabajoSeleccionado.cliente }}</li>
              <li><strong>Fecha:</strong> {{ trabajoSeleccionado.fecha }}</li>
              <li><strong>Categoría:</strong> {{ trabajoSeleccionado.categoria }}</li>
            </ul>
          </div>
        </div>
      </main>
  
      <Footer />
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import Header from "@/components/HeaderCompo.vue";
  import Footer from "@/components/FooterCompo.vue";
  
  const categorias = ['Todos', 'Muebles', 'Restauración', 'Estructural', 'Decoración'];
  const categoriaActual = ref('Todos');
  
  const trabajos = ref([
    {
      id: 1,
      titulo: 'Cocina Integral Moderna',
      descripcionCorta: 'Diseño y fabricación de cocina integral con isla central.',
      descripcionLarga: 'Proyecto completo de cocina integral con diseño moderno. Incluye gabinetes de madera de roble, isla central con tope de granito, y electrodomésticos integrados.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Familia Rodríguez',
      fecha: 'Marzo 2023',
      categoria: 'Muebles'
    },
    {
      id: 2,
      titulo: 'Restauración de Cómoda Antigua',
      descripcionCorta: 'Restauración de cómoda de caoba del siglo XIX.',
      descripcionLarga: 'Restauración completa de una cómoda de caoba del siglo XIX. Se repararon daños estructurales, se restauró el acabado original y se reemplazaron los herrajes manteniendo el estilo de la época.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Museo de Antigüedades',
      fecha: 'Abril 2023',
      categoria: 'Restauración'
    },
    {
      id: 3,
      titulo: 'Pérgola para Jardín',
      descripcionCorta: 'Diseño y construcción de pérgola de madera para jardín.',
      descripcionLarga: 'Pérgola de madera de cedro tratada para exteriores. Diseño personalizado para integrar iluminación LED y soporte para plantas trepadoras.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Residencia Flores',
      fecha: 'Mayo 2023',
      categoria: 'Estructural'
    },
    {
      id: 4,
      titulo: 'Estantería Flotante',
      descripcionCorta: 'Fabricación e instalación de estantería flotante para sala de estar.',
      descripcionLarga: 'Conjunto de estanterías flotantes fabricadas en madera de pino con acabado natural. Diseño minimalista que combina funcionalidad y estética moderna.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Oficina CreativeMind',
      fecha: 'Junio 2023',
      categoria: 'Decoración'
    },
    {
      id: 5,
      titulo: 'Mesa de Comedor Extensible',
      descripcionCorta: 'Diseño y fabricación de mesa de comedor extensible en nogal.',
      descripcionLarga: 'Mesa de comedor extensible fabricada en madera de nogal. Diseño elegante con capacidad para 6-10 personas. Incluye mecanismo de extensión suave y acabado resistente a manchas.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Familia Martínez',
      fecha: 'Julio 2023',
      categoria: 'Muebles'
    },
    {
      id: 6,
      titulo: 'Restauración de Puerta Colonial',
      descripcionCorta: 'Restauración de puerta colonial de doble hoja.',
      descripcionLarga: 'Restauración completa de una puerta colonial de doble hoja. Se repararon daños por insectos, se restauraron tallas originales y se aplicó un tratamiento protector contra la intemperie.',
      imagen: '/placeholder.svg?height=300&width=400',
      cliente: 'Casa Histórica Central',
      fecha: 'Agosto 2023',
      categoria: 'Restauración'
    }
  ]);
  
  const trabajosFiltrados = computed(() => {
    if (categoriaActual.value === 'Todos') {
      return trabajos.value;
    }
    return trabajos.value.filter(trabajo => trabajo.categoria === categoriaActual.value);
  });
  
  const trabajoSeleccionado = ref(null);
  
  const filtrarPor = (categoria) => {
    categoriaActual.value = categoria;
  };
  
  const seleccionarTrabajo = (trabajo) => {
    trabajoSeleccionado.value = trabajo;
  };
  
  const cerrarModal = () => {
    trabajoSeleccionado.value = null;
  };
  </script>
  
  <style scoped>
  .trabajos {
    font-family: 'Arial', sans-serif;
    color: #5D4037;
    background-color: #FFF3E0;
  }
  
  .header {
    background-color: #FF9800;
    padding: 2rem;
    text-align: center;
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
  
  h2 {
    color: #E65100;
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .filtros {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 2rem;
  }
  
  .filtro-btn {
    background-color: #FFE0B2;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .filtro-btn:hover, .filtro-btn.active {
    background-color: #FF9800;
    color: #FFF3E0;
  }
  
  .trabajos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2rem;
  }
  
  .trabajo-card {
    background-color: #FFECB3;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: transform 0.3s ease;
  }
  
  .trabajo-card:hover {
    transform: translateY(-5px);
  }
  
  .trabajo-imagen {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  .trabajo-info {
    padding: 1rem;
  }
  
  .trabajo-info h3 {
    margin-top: 0;
    color: #E65100;
  }
  
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-content {
    background-color: #FFF3E0;
    padding: 2rem;
    border-radius: 8px;
    max-width: 600px;
    width: 90%;
    max-height: 90vh;
    overflow-y: auto;
    position: relative;
  }
  
  .cerrar-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #5D4037;
  }
  
  .modal-imagen {
    width: 100%;
    height: auto;
    border-radius: 8px;
    margin-bottom: 1rem;
  }
  
  .detalles-lista {
    list-style-type: none;
    padding: 0;
  }
  
  .detalles-lista li {
    margin-bottom: 0.5rem;
  }
  
  .footer {
    background-color: #FF9800;
    color: #FFF3E0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
  }
  
  @media (max-width: 768px) {
    .filtros {
      flex-direction: column;
      align-items: center;
    }
  
    .filtro-btn {
      width: 100%;
      max-width: 200px;
    }
  }
  </style>
  