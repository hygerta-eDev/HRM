<template>
    <Navbar/>
    <Sidebar />
    <main class="flex-1 p-8 sm:ml-64">
      <div class="mt-10 p-12 text-black">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-bold">Create JobPosition</h2>
          <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
        </div>
        <form @submit.prevent="createJobPosition" class="space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center sm:space-x-4">                
            <div class="flex-1">
              <label for="name" class="block mb-2  text-sm font-medium text-black dark:text-black">Name:</label>
              <input type="text" id="name" v-model="jobPosition.name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
              <label for="slug" class="block mb-2 text-sm font-medium text-black dark:text-black">Description:</label>
              <textarea id="slug" v-model="jobPosition.slug" class="bg-gray-50  border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
            </div>
            <div class="flex-1">
              <label for="department_id" class="block mb-2 text-sm font-medium text-black dark:text-black">Department:</label>
              <select id="department_id" v-model="jobPosition.department_id" class="h-16 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="department in departments" :key="department.id" :value="department.id">{{ department.name }}</option>
              </select>
            </div>
            <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Create</button>
          </div>
        </form>
      </div>
    </main>
  </template>
  
  <script setup>
  import Sidebar from '../../components/Sidebar.vue'
  import Navbar from '../../components/Navbar.vue';
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
//   import { getCurrentDateTime } from '@/utils'; 
  
  const router = useRouter();
  const jobPosition = ref({
    name: '',
    slug: '',
    department_id: null // Initialize department_id as null
  });
  const departments = ref([]); // Array to hold departments
  
  const backToIndex = () => {
    router.push({ name: 'JobPositions' });
  };
  const getCurrentDateTime = () => {
  const now = new Date();
  return now.toISOString();
};
  const createJobPosition = async () => {
  try {
    // Set created_at field to the current date and time
    jobPosition.value.created_at = getCurrentDateTime(); // Assuming getCurrentDateTime is a utility function returning current date and time
  
    const response = await api.post('/jobPosition/create_jobPosition', jobPosition.value);
    router.push('/jobPositions'); // Redirect to departments list after creating job position
    console.log('JobPosition created successfully:', response.data);
  } catch (error) {
    console.error('There was a problem creating the job position:', error);
    if (error.response && error.response.data) {
      console.log('Error details:', error.response.data);
    }
  }

};

  // Fetch departments from API on component mount
  onMounted(async () => {
    try {
      const response = await api.get('/departments'); // Assuming your endpoint to fetch departments is /departments
      departments.value = response.data; // Assign fetched departments to departments array
    } catch (error) {
      console.error('Error fetching departments:', error);
    }
  });

  </script>
  