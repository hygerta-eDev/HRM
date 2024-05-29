
   <template>
    <div class="container mx-auto p-6">
      <div class="edit-department p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">View Job Position</h1>
        <div v-if="jobPosition" class="jobposition-details flex flex-wrap">
          <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Title</label>
            <div class="input-container">
              <div class="input-content">{{ jobPosition.name }}</div>
            </div>
          </div>
          <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Description</label>
            <div class="input-container">
              <div class="input-content">{{ jobPosition.slug }}</div>
            </div>
          </div>
          <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>
            <div class="input-container">
              <div class="input-content">{{ departmentName }}</div>
            </div>
          </div>
          <div class="w-full md:w-1/4 mb-4 md:mb-0 px-2">
            <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
            <div class="flex items-center mt-3 ml-36">
              <InputSwitch v-model="jobPosition.active" disabled />
            </div>
          </div>
        </div>
        <div v-else class="loading text-center mt-4">
          <p>Loading...</p>
        </div>
        <div class="text-right mt-4">
          <router-link v-if="jobPosition" :to="`/JobPositions/Edit/${jobPosition.id}`">
            <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">Edit</button>
          </router-link>
          <router-link :to="`/JobPositions`">
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
  const jobPosition = ref(null);
  const departmentName = ref('');
  
  const getJobPosition = () => {
    const jobId = Number(route.params.id);
    api.get(`/jobPosition/${jobId}`)
      .then(response => {
        jobPosition.value = response.data;
        fetchDepartmentName(jobPosition.value.department_id);
      })
      .catch(error => {
        console.error('Error fetching job position:', error);
      });
  };
  
  const fetchDepartmentName = (departmentId) => {
    api.get(`/departments/${departmentId}`)
      .then(response => {
        departmentName.value = response.data.name;
      })
      .catch(error => {
        console.error('Error fetching department name:', error);
        departmentName.value = 'Unknown Department';
      });
  };
  
  onMounted(getJobPosition);
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
  