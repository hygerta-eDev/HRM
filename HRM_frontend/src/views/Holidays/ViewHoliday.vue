<template>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->
    <div class="relative mb-6">
      <nav class="flex items-center text-sm text-gray-700">
        <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-home text-lg mr-2"></i> <!-- Home icon -->
          Home
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-user-cog text-lg mr-2"></i> <!-- Administrator icon -->
          Administrator
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Holidays" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-calendar-alt text-lg mr-2"></i> <!-- Holidays icon -->
          Holidays
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">View Holiday</span>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="p-10 shadow-lg rounded-lg border border-blue-500 relative mt-12 bg-white">
      <div v-if="Holiday" class="absolute inset-x-0 -top-10 flex justify-center">
        <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
          view {{ Holiday.description }}
        </h1>
      </div>
      <div v-else class="text-center mt-4">
        <p>Loading...</p>
      </div>
      <div class="pt-16 px-8 pb-8">
        <div v-if="Holiday" class="flex flex-col md:flex-row gap-6">
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday date</label>
            <div class="input-container">
              <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fa-regular fa-calendar-days"></i>
              <div class="input-content">{{ Holiday.date }}</div>
            </div>
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday description</label>
            <div class="input-container">
              <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-info-circle"></i>
              <div class="input-content">{{ Holiday.description }}</div>
            </div>
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday recurring</label>
            <div class="input-container">
              <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-sync-alt"></i>
              <div class="input-content">{{ Holiday.recurring }}</div>
            </div>
          </div>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <router-link v-if="Holiday" :to="`/Holidays/Edit/${Holiday.id}`">
            <button class="bg-blue-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-600 transition duration-300">Edit</button>
          </router-link>
          <router-link to="/Holidays">
            <button class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md hover:bg-gray-600 transition font-bold duration-300">Back</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';

const route = useRoute();
const Holiday = ref(null);

const getHoliday = () => {
  const HolidayId = Number(route.params.id);
  api.get(`/holidays/${HolidayId}`)
    .then(response => {
      Holiday.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Holiday:', error);
    });
};

onMounted(getHoliday);
</script>

<style scoped>
.input-container {
  width: 100%;
  background-color: #f9fafb; /* Light gray background */
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-content {
  padding: 0.5rem; /* Maintain the same padding */
}
</style>
