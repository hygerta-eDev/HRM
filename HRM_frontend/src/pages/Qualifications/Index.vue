qualification
<template>
    <div class="mt-10 p-4 sm:ml-64 text-black">
      <div class="flex justify-between items-center mb-4 mt-5">
        <h2 class="text-2xl font-bold">All Qualifications</h2>
        <button @click="createQualification" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New Qualification</button>
      </div>
      <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">actions</th>
        </tr>
      </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="qualification in qualifications" :key="qualification.id">
            <td class="px-6 py-4 whitespace-nowrap">{{ qualification.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ qualification.name }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ qualification.slug }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <button @click="showDeleteConfirmation(qualification.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800" >DELETE</button>
              <button @click="editQualification(qualification.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Delete Confirmation Modal -->
      <DeleteConfirmationModal :itemType="'qualification'" v-if="qualificationToDelete !== null" :qualificationId="qualificationToDelete" @cancel="cancelDelete" @ok="confirmDelete" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  import CreateQualification from './CreateQualification.vue';
  import DeleteConfirmationModal from '../../components/Delete.vue';
  
  const qualifications = ref([]);
  const router = useRouter();
  const qualificationToDelete = ref(null);
  
  const createQualification = () => {
    router.push({ name: 'CreateQualification' });
  };
  
  const editQualification = (qualificationId) => {
    router.push(`/qualifications/edit-qualification/${qualificationId}`);
  };
  
  const getAllQualification = () => {
    api.get('/qualification/')
      .then(response => {
        console.log('All qualifications:', response.data);
        qualifications.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching qualifications:', error);
      });
  };
  
  const deleteQualification = async (qualificationId) => {
  try {
    await api.delete(`qualifications/delete_qualification/${qualificationId}`);
    // Remove the deleted qualification from the qualifications array
    qualifications.value = qualifications.value.filter(qualification => qualification.id !== qualificationId);
    console.log('qualification deleted successfully');
  } catch (error) {
    console.error('Error deleting qualification:', error);
  }
};
  
  const showDeleteConfirmation = (qualificationId) => {
  qualificationToDelete.value = qualificationId;
};

const cancelDelete = () => {
  qualificationToDelete.value = null;
};

const confirmDelete = (qualificationId) => {
    deleteQualification(qualificationId);
// cancelDelete();
};
// const confirmDelete = (qualificationId) => {
//   deletequalification(qualificationId);
// };
  onMounted(getAllQualification);
  </script>
  