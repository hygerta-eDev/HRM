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
        <span class="font-semibold">Edit Qualification</span>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="p-10 shadow-lg rounded-lg border border-blue-500 bg-white relative mt-12">
      <div v-if="Qualification" class="absolute inset-x-0 -top-10 flex justify-center">
        <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
          {{Qualification.name}}
        </h1>
      </div>
      <div v-if="Qualification" class="pt-16 px-8 pb-8">
        <div class="flex flex-col md:flex-row gap-6">
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Qualification Name</label>
            <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-graduation-cap"></i>
            <input v-model="Qualification.name" type="text" class="w-full  pl-12 px-3 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Slug</label>
            <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-info-circle"></i>

            <input v-model="Qualification.slug" type="text" class="w-full  pl-12 px-3 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <button @click="updateQualification" class="bg-blue-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-600 transition duration-300">Save</button>
          <router-link to="/Qualifications">
            <button @click="cancelEdit" class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-gray-600 transition duration-300">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="text-center mt-4">
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

const route = useRoute();
const router = useRouter();
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

const updateQualification = () => {
  if (Qualification.value) {
    api.put(`/qualification/update_qualifications/${Qualification.value.id}`, Qualification.value)
      .then(response => {
        console.log('Qualification updated successfully:', response.data);
        router.push('/Qualifications');  
        setTimeout(() => {
          toast.success("Qualification edited successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });   
        }, 250);
      })
      .catch(error => {
        console.error('Error updating Qualification:', error);
      });
  }
};

const cancelEdit = () => {
  // Redirect back to qualification list or view page
};

onMounted(getQualification);
</script>

<style scoped>
.loading {
  text-align: center;
  margin-top: 20px;
  font-style: italic;
  color: #666;
}
</style>
