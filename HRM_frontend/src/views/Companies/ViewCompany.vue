<template>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->
    <div class="relative mb-6">
      <nav class="flex items-center text-sm text-gray-700">
        <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-home text-lg mr-2"></i> <!-- Home icon -->
          {{ $t('home') }}
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-user-cog text-lg mr-2"></i> <!-- Administrator icon -->
          {{ $t('administrator') }}
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Companies" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-building text-lg mr-2"></i> <!-- Company icon -->
          {{ $t('companies') }}
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">{{ $t('view_company') }}</span>
      </nav>
    </div>

    <div class="container mx-auto p-6">
      <div class="p-10 shadow-lg rounded-lg border border-blue-500 relative mt-12 bg-white">
        <div v-if="company" class="absolute inset-x-0 -top-10 flex justify-center">
          <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
            {{ $t('view') }} {{ company.name }}
          </h1>
        </div>
        <div v-else class="text-center mt-4">
          <p>{{ $t('loading') }}</p>
        </div>
        <div class="pt-16 px-8 pb-8">
          <div v-if="company" class="flex flex-col md:flex-row gap-6">
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">{{ $t('company_name') }}</label>
              <div class="input-container">
                <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-building"></i>
                <div class="input-content">{{ company.name }}</div>
              </div>
            </div>
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">{{ $t('description') }}</label>
              <div class="input-container">
                <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-tag"></i>
                <div class="input-content">{{ company.slug }}</div>
              </div>
            </div>
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">{{ $t('active') }}</label>
              <div class="flex items-center justify-center mt-2">
                <InputSwitch v-model="company.active" disabled class="mr-2" />
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>{{ $t('loading') }}</p>
          </div>
          <div class="mt-6 flex justify-end gap-4">
            <router-link v-if="company" :to="`/Companies/Edit/${company.id}`">
              <button class="bg-sky-600 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-sky-700 transition duration-300">{{ $t('edit') }}</button>
            </router-link>
            <router-link to="/Companies">
              <button class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-gray-600 transition duration-300">{{ $t('back') }}</button>
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
import InputSwitch from 'primevue/inputswitch';

const route = useRoute();
const company = ref(null);

const getCompany = () => {
  const companyId = Number(route.params.id);
  api.get(`/institutions/${companyId}`)
    .then(response => {
      company.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching company:', error);
    });
};

onMounted(getCompany);
</script>

<style scoped>
.input-container {
  width: 100%;
  background-color: #f9fafb; 
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-content {
  padding: 0.5rem; 
}
</style>
