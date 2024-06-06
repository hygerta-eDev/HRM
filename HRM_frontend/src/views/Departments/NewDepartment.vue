<template>
  <div class="container mx-auto p-6">
    <div class="create-department p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Create New Department</h1>
      <div class="department-details flex flex-wrap">
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department Name</label>
          <input v-model="newDepartment.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="newDepartment.slug" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company</label>
          <select v-model="newDepartment.institution_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="" disabled>Select a Company</option>
            <option v-for="company in activeCompanies" :key="company.id" :value="company.id">{{ company.name }}</option>
          </select>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-36">
            <InputSwitch v-model="newDepartment.active" />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndCreateDepartment" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
          <router-link :to="`/Departments`">
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
const newDepartment = ref({
  name: '',
  slug: '',
  institution_id: '',
  active: false
});
const activeCompanies = ref([]);

const getActiveCompanies = () => {
  api.get('institutions/active_institutions')
    .then(response => {
      activeCompanies.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching active companies:', error);
    });
};

onMounted(getActiveCompanies);

const validateAndCreateDepartment = () => {
  if (!newDepartment.value.name || !newDepartment.value.slug || !newDepartment.value.institution_id) {
    toast.error("Please fill in all required fields.", {
      autoClose: 3000,
      position: toast.POSITION.TOP_RIGHT,
    });
    return; 
  }

  newDepartment.value.user_id = 1;
  api.post('/departments/create_department', newDepartment.value)
    .then(response => {
      console.log('Department created successfully:', response.data);

      router.push('/Departments');
      setTimeout(() => {
        toast.success("Department created successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });      
      }, 250);
    })
    .catch(error => {
      console.error('Error creating department:', error);
      toast.error("Failed to create department!", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
    });
};
</script>

<style scoped>
.create-department {
  margin-top: 20px;
}
</style>