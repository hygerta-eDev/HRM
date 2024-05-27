
<template>
    <div class="container mx-auto p-6">
      <div class="edit-Department p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
  
      <h1 class="text-2xl font-bold mb-6">Edit Department</h1>
      <div v-if="Department" class="Department-details flex flex-wrap">
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department Name</label>
          <input v-model="Department.name" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="Department.slug" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company</label>
          <select v-model="Department.institution_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="" disabled>Select a Company</option>
            <option v-for="company in activeCompanies" :key="company.id" :value="company.id">{{ company.name }}</option>
          </select>
        </div>
        <div class="w-full md:w-1/4 mb-4 md:mb-0  px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-36">
            <InputSwitch class="" v-model="Department.active"  />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="updateDepartment" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/Departments`">
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
  const Department = ref(null);
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

  const getDepartment = () => {
    const DepartmentId = Number(route.params.id);
    api.get(`/departments/${DepartmentId}`)
      .then(response => {
        Department.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching Department:', error);
      });
  };
  
  const updateDepartment = () => {
  if (Department.value) {
    api.put(`/departments/update_department/${Department.value.id}`, Department.value)
      .then(response => {
        console.log('Department updated successfully:', response.data);
        router.push('/Departments');  
        setTimeout(() => {
          toast.success("Department edited successfully!", {
            autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });   
        }, 250);

      })
      .catch(error => {
        console.error('Error updating Department:', error);
      });
  }
};

  const cancelEdit = () => {
    // Redirect back to Department list or view page
  };
  
  onMounted(getDepartment);
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  