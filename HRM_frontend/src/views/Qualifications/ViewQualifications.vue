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
        <router-link to="/Qualifications" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-graduation-cap text-lg mr-2"></i> <!-- Qualification icon -->
          Qualifications
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">View Qualification</span>
      </nav>
    </div>

    <div class="container mx-auto p-6">
      <div class="p-10 shadow-lg rounded-lg border border-blue-500 relative mt-12 bg-white">
        <div v-if="Qualification" class="absolute inset-x-0 -top-10 flex justify-center">
          <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
            {{ Qualification.name }}
          </h1>
        </div>
        <div v-else class="text-center mt-4">
          <p>Loading...</p>
        </div>
        <div class="pt-16 px-8 pb-8">
          <div v-if="Qualification" class="flex flex-col md:flex-row gap-6">
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">Qualification Name</label>
              <div class="input-container">
                <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-graduation-cap"></i>
                <div class="input-content">{{ Qualification.name }}</div>
              </div>
            </div>
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">Slug</label>
              <div class="input-container">
                <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-info-circle"></i>
                <div class="input-content">{{ Qualification.slug }}</div>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>Loading...</p>
          </div>
          <div class="mt-6 flex justify-end gap-4">
            <router-link v-if="Qualification" :to="`/Qualifications/Edit/${Qualification.id}`">
              <button class="bg-sky-600 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-sky-700 transition duration-300">Edit</button>
            </router-link>
            <router-link to="/Qualifications">
              <button class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md hover:bg-gray-600 transition font-bold duration-300">Back</button>
            </router-link>
          </div>
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
const Qualification = ref(null);

const getQualification = () => {
  const QualificationId = Number(route.params.id);
  api.get(`/qualification/${QualificationId}`)
    .then(response => {
      Qualification.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Qualification:', error);
    });
};

onMounted(getQualification);
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
