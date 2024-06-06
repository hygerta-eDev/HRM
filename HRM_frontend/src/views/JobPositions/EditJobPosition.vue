<template>
  <div class="container mx-auto p-6">
    <div class="edit-job-position p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">

      <h1 class="text-2xl font-bold mb-6">Edit Job Position</h1>
      <div v-if="jobPosition" class="job-position-details flex flex-wrap">
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Job Position Title</label>
          <input v-model="jobPosition.name" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="jobPosition.slug" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>
          <select v-model="jobPosition.department_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="" disabled>Select a Department</option>
            <option v-for="department in activeDepartments" :key="department.id" :value="department.id">{{ department.name }}</option>
          </select>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0  px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-36">
            <InputSwitch class="" v-model="jobPosition.active" />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="updateJobPosition" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/JobPositions`">
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
const jobPosition = ref(null);
const activeDepartments = ref([]);

const getActiveDepartments = () => {
  api.get('departments/active_departments')
    .then(response => {
      activeDepartments.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching active departments:', error);
    });
};
onMounted(getActiveDepartments);

const getJobPosition = () => {
  const jobPositionId = Number(route.params.id);
  api.get(`/jobPosition/${jobPositionId}`)
    .then(response => {
      jobPosition.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching job position:', error);
    });
};

const updateJobPosition = () => {
  if (jobPosition.value) {
    api.put(`/jobPosition/update_jobPosition/${jobPosition.value.id}`, jobPosition.value)
      .then(response => {
        console.log('Job position updated successfully:', response.data);
        router.push('/JobPositions');  
        setTimeout(() => {
          toast.success("Job position edited successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });   
        }, 250);
      })
      .catch(error => {
        console.error('Error updating job position:', error);
      });
  }
};

const cancelEdit = () => {
  // Redirect back to job position list or view page
};

onMounted(getJobPosition);
</script>

<style scoped>
.loading {
  text-align: center;
  margin-top: 20px;
  font-style: italic;
  color: #666;
}
</style>
