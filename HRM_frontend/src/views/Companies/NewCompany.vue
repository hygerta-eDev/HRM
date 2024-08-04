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
        <span class="font-semibold">New Company</span>
      </nav>
    </div>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->

      <div class="shadow-lg rounded-lg border border-blue-500 relative mt-12">
        <div class="absolute inset-x-0 -top-5 flex justify-center">
          <h1 class="text-3xl font-bold text-gray-800 bg-white px-4 relative z-10">
            Create New Company
          </h1>
        </div>
        <div class="pt-12 px-8 pb-8">
          <div class="flex flex-col md:flex-row p-10 gap-6">
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">Company Name</label>
              <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-building"></i>
              <input v-model="newCompany.name" type="text" class="w-full pl-12 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">Slug</label>
              <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-tag"></i>
              <input v-model="newCompany.slug" type="text" class="w-full pl-12 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div class="flex-1 relative">
              <label class="block text-sm font-semibold mb-2 text-gray-700">Active</label>
              <div class="flex items-center justify-center mt-2">
                <InputSwitch v-model="newCompany.active" class="mr-2" />
              </div>
            </div>
          </div>
          <div class="mt-6 flex justify-end gap-4">
            <button @click="validateAndCreateCompany" class="bg-sky-600 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-sky-700 transition duration-300">Create</button>
            <router-link :to="`/Companies`">
              <button class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md hover:bg-gray-600 transition font-bold duration-300">Cancel</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import InputSwitch from 'primevue/inputswitch';
import { toast } from 'vue3-toastify';
import { api } from '@/api';
const router = useRouter();
const newCompany = ref({
  name: '',
  slug: '',
  active: false
});

const validateAndCreateCompany = () => {
  if (!newCompany.value.name || !newCompany.value.slug) {
    toast.error("Please fill in all required fields.", {
      autoClose: 3000,
      position: toast.POSITION.TOP_RIGHT,
    });
    return;
  }

  newCompany.value.user_id = 1;
  api.post('/institutions/create_institution', newCompany.value)
    .then(response => {
      console.log('Company created successfully:', response.data);

      router.push('/Companies');
      setTimeout(() => {
        toast.success("Company created successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      }, 250);
    })
    .catch(error => {
      console.error('Error creating company:', error);
      toast.error("Failed to create company!", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
    });
};
</script>

<style scoped>
.relative {
  position: relative;
}
.absolute {
  position: absolute;
}
.top-0 {
  top: 0;
}
.left-0 {
  left: 0;
}
.mb-4 {
  margin-bottom: 1rem;
}
</style>
