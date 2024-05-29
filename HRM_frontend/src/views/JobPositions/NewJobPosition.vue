<template>
  <div class="container mx-auto p-6">
    <div class="create-JobPosition p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Create New JobPosition</h1>
      <div class="JobPosition-details flex flex-wrap">
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">JobPosition Name</label>
          <input v-model="newJobPosition.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Description</label>
          <input v-model="newJobPosition.slug" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>
          <select v-model="newJobPosition.department_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="" disabled>Select a Department</option>
            <option v-for="department in activeDepartments" :key="department.id" :value="department.id">{{ department.name }}</option>
          </select>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-36">
            <InputSwitch v-model="newJobPosition.active" />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndCreateJobPosition" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
          <router-link :to="`/jobPositions`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import InputSwitch from 'primevue/inputswitch';
import { toast } from 'vue3-toastify';

const router = useRouter();
const newJobPosition = ref({
  name: '',
  slug: '',
  department_id: '',
  active: false
});
const activeDepartments = ref([]);

const activeDepartment = () => {
  api.get('/departments/active_departments')
    .then(response => {
      activeDepartments.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching active departments:', error);
    });
};

onMounted(activeDepartment);

const validateAndCreateJobPosition = () => {
  if (!newJobPosition.value.name || !newJobPosition.value.slug || !newJobPosition.value.department_id) {
    toast.error("Please fill in all required fields.", {
      autoClose: 3000,
      position: toast.POSITION.TOP_RIGHT,
    });
    return; 
  }

  newJobPosition.value.user_id = 1;
  api.post('/jobPosition/create_jobPosition', newJobPosition.value)
    .then(response => {
      console.log('JobPosition created successfully:', response.data);

      router.push('/JobPositions');
      setTimeout(() => {
        toast.success("JobPosition created successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });      
      }, 250);
    })
    .catch(error => {
      console.error('Error creating JobPosition:', error);
      toast.error("Failed to create JobPosition!", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
    });
};
</script>

<style scoped>
.create-JobPosition {
  margin-top: 20px;
}
</style>