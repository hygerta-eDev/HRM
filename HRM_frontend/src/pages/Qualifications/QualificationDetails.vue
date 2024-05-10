<template>
    <div class="p-4 sm:ml-64">
      <h1>Department Details</h1>
      <!-- <div v-if="department">
        <p><strong>Name:</strong> {{ department.name }}</p>
        <p><strong>Description:</strong> {{ department.description }}</p>
       
      </div>
      <router-link :to="{ name: 'Departments' }">Back to Departments</router-link> -->
    </div>
  </template>


<!-- <template>
    <div class="mt-10 p-4 sm:ml-64 text-black">    
        <div class="flex justify-between items-center mb-4 mt-5">
          <h2 class="text-2xl font-bold"> JobPositions</h2>
          <button @click="createJobPosition(department.id)" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New JobPosition</button>
        </div>
    </div>
    <hr>

    <div v-if="departmentsWithJobPositions.length > 0" class=" p-4 sm:ml-64 text-black">
      <div v-for="(department, index) in departmentsWithJobPositions" :key="index">
        <div class="flex justify-between items-center mb-4 mt-5">
          <h2 class="text-2xl font-bold">{{ department.name }} JobPositions</h2>
        </div>
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Department</th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="jobPosition in department.jobPositions" :key="jobPosition.id">
              <td class="px-6 py-4 whitespace-nowrap">{{ jobPosition.id }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ jobPosition.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ jobPosition.slug }}</td>
              <td class="px-6 py-4 whitespace-nowrap">{{ department.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap">
                <button @click="showDeleteConfirmation(jobPosition.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">DELETE</button>
                <button @click="editJobPosition(jobPosition.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <DeleteConfirmationModal itemType="jobPosition" v-if="jobPositionToDelete !== null" :jobPositionId="jobPositionToDelete" @cancel="cancelDelete" @ok="confirmDelete" />
    </div>
    <div v-else class="mt-10 p-4 sm:ml-64 text-black">
      <p>No departments with job positions found.</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  import DeleteConfirmationModal from '../../components/Delete.vue';
  import CreateJobPosition from './CreateJobPosition.vue';
  
  const departmentsWithJobPositions = ref([]);
  
  const router = useRouter();
  const jobPositionToDelete = ref(null);
  
  const createJobPosition = (departmentId) => {
    router.push({ name: 'CreateJobPosition', params: { departmentId } });
  };
  
  const editJobPosition = (jobPositionId) => {
    router.push(`/jobPositions/edit-jobPosition/${jobPositionId}`);
  };
  
  const getAllJobPosition = async () => {
    try {
      const departmentsResponse = await api.get('/departments');
      const jobPositionsResponse = await api.get('/jobPosition/');
  
      const departments = departmentsResponse.data;
      const jobPositions = jobPositionsResponse.data;
  
      departmentsWithJobPositions.value = departments.map(department => {
        const departmentJobPositions = jobPositions.filter(jobPosition => jobPosition.department_id === department.id);
        if (departmentJobPositions.length > 0) {
          return {
            ...department,
            jobPositions: departmentJobPositions
          };
        }
      }).filter(Boolean);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  const deleteJobPosition = async (jobPositionId) => {
    try {
      await api.delete(`jobPositions/delete_jobPosition/${jobPositionId}`);
      getAllJobPosition();
      console.log('JobPosition deleted successfully');
    } catch (error) {
      console.error('Error deleting jobPosition:', error);
    }
  };
  
  const showDeleteConfirmation = (jobPositionId) => {
    jobPositionToDelete.value = jobPositionId;
  };
  
  const cancelDelete = () => {
    jobPositionToDelete.value = null;
  };
  
  const confirmDelete = (jobPositionId) => {
    deleteJobPosition(jobPositionId);
  };
  onMounted(getAllJobPosition);
  </script>
   -->