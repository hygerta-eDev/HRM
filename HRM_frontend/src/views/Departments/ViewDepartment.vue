<template>
  <div class="container mx-auto p-6">
    <div class="edit-department p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
      <h1 class="text-2xl font-bold mb-6">View Department</h1>
      <div v-if="department" class="department-details flex flex-wrap">
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department Name</label>
          <div class="input-container">
            <div class="input-content">{{ department.name }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <div class="input-container">
            <div class="input-content">{{ department.slug }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company</label>
          <div class="input-container">
            <div class="input-content">{{ companyName }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-36">
            <InputSwitch v-model="department.active" disabled />
          </div>
        </div>
      </div>
      <div v-else class="loading text-center mt-4">
        <p>Loading...</p>
      </div>
      <div class="text-right mt-4">
        <router-link v-if="department" :to="`/Departments/Edit/${department.id}`">
          <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">Edit</button>
        </router-link>
        <router-link :to="`/Departments`">
          <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow ml-2">Back</button>
        </router-link>
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
const department = ref(null);
const companyName = ref('');

const getDepartment = () => {
  const departmentId = Number(route.params.id);
  api.get(`/departments/${departmentId}`)
    .then(response => {
      department.value = response.data;
      fetchCompanyName(department.value.institution_id);
    })
    .catch(error => {
      console.error('Error fetching department:', error);
    });
};

const fetchCompanyName = (companyId) => {
  api.get(`/institutions/${companyId}`)
    .then(response => {
      companyName.value = response.data.name;
    })
    .catch(error => {
      console.error('Error fetching company name:', error);
      companyName.value = 'Unknown Company';
    });
};

onMounted(getDepartment);
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
