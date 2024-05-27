
<template>
    <div class="container mx-auto p-6">
      <div class="edit-company p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
  
      <h1 class="text-2xl font-bold mb-6">Edit Company</h1>
      <div v-if="company" class="company-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company Name</label>
          <input v-model="company.name" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="company.slug" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0  px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-48">
            <InputSwitch class="" v-model="company.active"  />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="updateCompany" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/Companies`">
            <button @click="cancelEdit" class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="loading">
        <p>Loading...</p>
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
  