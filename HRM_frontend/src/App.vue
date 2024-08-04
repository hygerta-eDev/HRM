<template>
  <div>
    <!-- Button to toggle the sidebar -->
    <button @click="toggleSidebar">Toggle Sidebar</button>

    <!-- Main container whose margin changes with the sidebar state -->
    <div :class="containerClass">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref,computed } from 'vue';

const isSidebarOpen = ref(false);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};

const containerClass = computed(() => {
  return isSidebarOpen.value ? 'ml-64' : 'ml-8';
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.ml-64 {
  margin-left: 64px; /* Sidebar width */
}

.ml-8 {
  margin-left: 8px; /* Adjust as needed when the sidebar is closed */
}
</style>
