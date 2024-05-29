<template>
  <div class="container mx-auto p-6">
    <div class="edit-Ethnicity p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">

      <h1 class="text-2xl font-bold mb-6">View Ethnicity</h1>
      <div v-if="Ethnicity" class="Ethnicity-details flex items-center">
        <div class="w-full flex-grow mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity Name</label>
          <div class="input-container">
            <div class="input-content bg-white px-3 py-2 border border-blue-200 rounded-md shadow">
              {{ Ethnicity.name }}
            </div>
          </div>
        </div>
        <div class="flex items-center mt-6 mb-4 md:mb-0 px-2">
          <router-link v-if="Ethnicity" :to="`/Ethnicities/Edit/${Ethnicity.id}`">
            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow ml-2">Edit</button>
          </router-link>
          <router-link :to="`/Ethnicities`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow ml-2">Back</button>
          </router-link>
        </div>
      </div>
      <div v-else class="loading text-center mt-4">
        <p>Loading...</p>
      </div>

    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';
import InputSwitch from 'primevue/inputswitch';

const route = useRoute();
const Ethnicity = ref(null);

const getEthnicity = () => {
  const EthnicityId = Number(route.params.id);
  api.get(`/ethnicities/${EthnicityId}`)
    .then(response => {
      Ethnicity.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Ethnicity:', error);
    });
};

onMounted(getEthnicity);
</script>

<style scoped>
.input-container {
  width: 100%;
  background-color: #fff;
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-content {
  padding: 0.5rem;
}
</style>
