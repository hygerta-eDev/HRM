<script setup>
import NavBar from "../NavBar.vue";
</script>

<template>
  <div class="main-content">
      <NavBar />
      <router-view> </router-view>
  </div>
</template>



<style scoped>
.main-content {
  padding-top: 80px;
  padding-left: 220px;
}

</style>
