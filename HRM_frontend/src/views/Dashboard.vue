<template>
  <div class="main">
    <h1 class="">Innovation is the Key</h1>
    <h1>Welcome, {{ name }}</h1>
    <p>Your role: {{ role }}</p>
    <button @click="logout">Logout</button>
    <h1>{{ $t('hello') }}</h1>

  </div>
</template>

<script>
import { api } from '@/api';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      name: localStorage.getItem('name'),
      role: localStorage.getItem('role'),
    };
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push('/Login'); // Redirect to the login page
    },
  },
};
</script>

<style scoped>
.main {
  margin-left: -200px;
  padding: 20px; /* Added padding for better layout */
}
</style>
