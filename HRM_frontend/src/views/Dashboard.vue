<template>
  <div>
    <!-- Content visible to admin users -->
    <div v-if="isAdmin">
      <p>Welcome, Admin!</p>
      <!-- Admin-specific content -->
    </div>

    <!-- Content visible to regular users -->
    <div v-else-if="isUser">
      <p>Welcome, User {{ name }}!</p>
      <!-- Regular user content -->
    </div>

    <!-- Content visible to all logged-in users -->
    <div v-if="isLoggedIn">
      <p>Welcome back!</p>
    </div>

    <!-- Content for everyone -->
    <div>
      <p>This is available to everyone.</p>
    </div>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: localStorage.getItem('name') || '', // Get user's name from local storage
      roles: JSON.parse(localStorage.getItem('roles')) || [], // Parse roles from local storage
    };
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token'); // Check if user is logged in
    },
    isAdmin() {
      return this.roles.includes(1); // Check if user has admin role (assuming 1 is the admin role ID)
    },
    isUser() {
      return this.roles.includes(3); // Check if user has regular user role (assuming 3 is the user role ID)
    },
  },
  methods: {
    logout() {
      localStorage.clear(); // Clear all local storage items
      this.$router.push('/login'); // Redirect to the login page
    },
  },
};
</script>
