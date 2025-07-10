

<template>
  <div>
    <h2>Available Services</h2>
    <ul>
      <li v-for="service in services" :key="service.id">{{ service.name }} - ${{ service.price }}</li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'ServicesList',
  setup() {
    const services = ref([])

    const fetchServices = async () => {
      try {
        let response = await axios.get('http://localhost:5000/api/services')
        services.value = response.data;
      } catch (error) {
        console.error('Error in service fetch', error)
      }
    }

    onMounted(fetchServices)

    return {
      services
    }
  }
}
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
  margin: 20px;
}
li {
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 5px;
}
</style>

