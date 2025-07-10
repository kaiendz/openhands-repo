
<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <div>
      <router-link to="/register">Not registered? Sign Up</router-link>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'Login',
  setup() {
    const email = ref('')
    const password = ref('')
    const store = useStore()
    const router = useRouter()

    const login = async () => {
      console.log('Login with:', { email: email.value, password: password.value })
      try {
        await store.dispatch('login', { email: email.value, password: password.value })
        router.push('/')
      } catch (error) {
        console.error('Login Error:', error)
      }
    }
    return { email, password, login }
  },
}
</script>

<style scoped>
div {
  margin: 20px;
}
</style>

