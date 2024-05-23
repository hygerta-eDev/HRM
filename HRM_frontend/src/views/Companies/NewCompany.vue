<template>
    <div class="p-6 container flex justify-center items-center min-h-screen">
      <div class="w-full max-w-lg">
        <h2 class="text-lg font-semibold mb-4 text-center">New Company</h2>
        <div class="bg-white rounded-lg p-6">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Company Name</label>
            <input v-model="newCompanyData.name" type="text" class="w-full px-3 py-2 border rounded-md">
          </div>
          <div class="text-right">
            <button @click="createCompany" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Save</button>
            <router-link to="/companies">
              <button class="bg-gray-400 text-white px-4 py-2 ml-2 rounded-lg">Cancel</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  interface Company {
    id: number;
    name: string;
  }
  
  export default {
    setup() {
      const router = useRouter();
      const newCompanyData = ref<Company>({ id: 0, name: '' });
  
      // Assuming companies is a ref containing the list of companies
      const companies = ref<Company[]>([
        { id: 1, name: 'eTech' },
        { id: 2, name: 'CyberOne' },
        { id: 3, name: 'eDev' }
      ]);
  
      const createCompany = () => {
        // Dummy ID generation, replace with actual ID from the server
        newCompanyData.value.id = Math.floor(Math.random() * 1000) + 1;
        
        // Add the new company to the list of companies
        companies.value.push({ ...newCompanyData.value });
  
        // Navigate back to the company list view
        router.push('/companies');
      };
  
      return {
        newCompanyData,
        createCompany
      };
    }
  }
  </script>
  
  
  <style scoped>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }
  
  .max-w-lg {
    width: 100%;
    max-width: 32rem;
  }
  
  </style>
  