<template>
  <div id="app">
    <h1>Pipeline CI/CD Demo</h1>
    <p>Estado: {{ status }}</p>
    <div v-if="items.length">
      <h2>Datos del Backend:</h2>
      <ul>
        <li v-for="item in items" :key="item.id">
          {{ item.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      status: 'Cargando...',
      items: []
    };
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:5000/api/data');
      const data = await response.json();
      this.items = data.items;
      this.status = 'Conectado';
    } catch (error) {
      this.status = 'Error conectando al backend';
      console.error(error);
    }
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
}

h1 {
  color: #42b983;
}
</style>