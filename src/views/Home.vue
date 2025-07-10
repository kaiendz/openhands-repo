

<template>
  <div>
    <h1>Welcome To the Booking App</h1>
    <div>
      <!-- Provide links to navigate through the application -->
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Register</router-link> |
      <router-link to="/services">Services</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
div {
  margin: 20px;
}
</style>
