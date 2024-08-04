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
        <router-link to="/Companies" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-building text-lg mr-2"></i> <!-- Company icon -->
          Companies
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">Edit Company</span>
      </nav>
    </div>
    <div class="container mx-auto p-6">

    <!-- Main Content -->
    <div class="p-10 shadow-lg rounded-lg border border-blue-500 bg-white relative mt-12">
      <div v-if="company" class="absolute inset-x-0 -top-10 flex justify-center">
        <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
          Edit Company
        </h1>
      </div>
      <div v-if="company" class="pt-16 px-8 pb-8">
        <div class="flex flex-col md:flex-row gap-6">
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Company Name</label>
            <input v-model="company.name" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Slug</label>
            <input v-model="company.slug" type="text" class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Active</label>
            <div class="flex items-center">
              <InputSwitch v-model="company.active" class="ml-2" />
            </div>
          </div>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <button @click="updateCompany" class="bg-blue-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-600 transition duration-300">Save</button>
          <router-link to="/Companies">
            <button @click="cancelEdit" class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-gray-600 transition duration-300">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>Loading...</p>
      </div>
    </div>
    </div>
  </div>
</template>

  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  import InputSwitch from 'primevue/inputswitch';

  
  const route = useRoute();
  const router = useRouter();
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
  
  const updateCompany = () => {
  if (company.value) {
    api.put(`/institutions/${company.value.id}`, company.value)
      .then(response => {
        console.log('Company updated successfully:', response.data);
        router.push('/Companies');  
        setTimeout(() => {
          toast.success("Company edited successfully!", {
            autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });   
        }, 250);

      })
      .catch(error => {
        console.error('Error updating company:', error);
      });
  }
};

  const cancelEdit = () => {
    // Redirect back to company list or view page
  };
  
  onMounted(getCompany);
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  