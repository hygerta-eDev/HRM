<template>
    <div class="mt-10 p-4 sm:ml-64 text-black">
      <div class="flex justify-between items-center mb-4 mt-5">
        <h2 class="text-2xl font-bold">All Ethnicities</h2>
        <button @click="createEthnicity" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New Ethnicity</button>
      </div>
      <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">actions</th>

        </tr>        
      </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="(ethnicity,ethnicityIndex) in ethnicities" :key="ethnicityIndex">
            <td class="px-6 py-4 whitespace-nowrap">{{ ethnicityIndex + 1 }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ ethnicity.name }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <button @click="showDeleteConfirmation(ethnicity.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800" >DELETE</button>
              <button @click="editEthnicity(ethnicity.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Delete Confirmation Modal -->
      <!-- <DeleteConfirmationModal itemType="ethnicity" v-if="departmentToDelete !== null" :departmentId="departmentToDelete" @cancel="cancelDelete" @ok="confirmDelete" /> -->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  import CreateEthnicity from './CreateEthnicity.vue';
  import DeleteConfirmationModal from '../../components/Delete.vue';
  
  const ethnicities = ref([]);
  const router = useRouter();
  // const ethnicityToDelete = ref(null);
  
  const createEthnicity = () => {
    router.push({ name: 'CreateEthnicity' });
  };
  
  const editEthnicity = (ethnicityId) => {
    router.push(`/ethnicities/edit-ethnicity/${ethnicityId}`);
  };
  
  const getAllEthnicities = () => {
    api.get('/ethnicities/')
      .then(response => {
        console.log('All Ethnicities:', response.data);
        ethnicities.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching Ethnicities:', error);
      });
  };
  
  const deleteEthnicity = async (ethnicityId) => {
  try {
    await api.delete(`Ethnicities/delete_Ethnicity/${ethnicityId}`);
    // Remove the deleted department from the departments array
    ethnicities.value = ethnicities.value.filter(ethnicity => ethnicity.id !== ethnicityId);
    console.log('Ethnicity deleted successfully');
  } catch (error) {
    console.error('Error deleting ethnicity:', error);
  }
};
  
  const showDeleteConfirmation = (ethnicityId) => {
    ethnicityToDelete.value = ethnicityId;
};

const cancelDelete = () => {
  ethnicityToDelete.value = null;
};

const confirmDelete = (ethnicityId) => {
    deleteEthnicity(ethnicityId);
// cancelDelete();
};
// const confirmDelete = (departmentId) => {
//   deleteDepartment(departmentId);
// };
  onMounted(getAllEthnicities);
  </script>
  