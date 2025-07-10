

<template>
  <div>
    <h2>User Registration</h2>
    <div>
      <form @submit.prevent="registerUser">
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Register Now</button>
        Have an account? <router-link to="/login">Login</router-link>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'Register',
  setup() {
    const email = ref('')
    const username = ref('')
    const password = ref('')
    const router = useRouter()

    const registerUser = async () => {
      try {
        const response = axios.post('http://localhost:5000/api/register', {
          email: email.value,
          username: username.value,
          password: password.value,
        })
        if (response.status === 201) {
          alert("Registration success")
          router.push('/login')
        } else {
          alert("Registration failed. Please check your inputs");
        }
      } catch (error) {
        console.error(error);
      }
    }
    return { email, username, password, registerUser }
  }
}
</script>

<style scoped>
div {
  margin: 20px 40px;
}
</style>
