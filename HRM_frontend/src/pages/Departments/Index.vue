<template>
    <div class="mt-10 p-4 sm:ml-64 text-black">
      <div class="flex justify-between items-center mb-4 mt-5">
        <h2 class="text-2xl font-bold">All Departments</h2>
        <button @click="createDepartment" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New Department</button>
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
          <tr v-for="department in departments" :key="department.id">
            <td class="px-6 py-4 whitespace-nowrap">{{ department.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ department.name }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ department.slug }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <button @click="showDeleteConfirmation(department.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800" >DELETE</button>
              <button @click="editDepartment(department.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Delete Confirmation Modal -->
      <DeleteConfirmationModal v-if="departmentToDelete !== null" :departmentId="departmentToDelete" @cancel="cancelDelete" @ok="confirmDelete" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  import CreateDepartment from './CreateDepartment.vue';
  import DeleteConfirmationModal from '../../components/Delete.vue';
  
  const departments = ref([]);
  const router = useRouter();
  const departmentToDelete = ref(null);
  
  const createDepartment = () => {
    router.push({ name: 'CreateDepartment' });
  };
  
  const editDepartment = (departmentId) => {
    router.push(`/departments/edit-department/${departmentId}`);
  };
  
  const getAllDepartment = () => {
    api.get('/departments/')
      .then(response => {
        console.log('All departments:', response.data);
        departments.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching departments:', error);
      });
  };
  
  const deleteDepartment = async (departmentId) => {
  try {
    await api.delete(`departments/delete_department/${departmentId}`);
    // Remove the deleted department from the departments array
    departments.value = departments.value.filter(department => department.id !== departmentId);
    console.log('Department deleted successfully');
  } catch (error) {
    console.error('Error deleting department:', error);
  }
};
  
  const showDeleteConfirmation = (departmentId) => {
  departmentToDelete.value = departmentId;
};

const cancelDelete = () => {
  departmentToDelete.value = null;
};

const confirmDelete = (departmentId) => {
    deleteDepartment(departmentId);
// cancelDelete();
};
// const confirmDelete = (departmentId) => {
//   deleteDepartment(departmentId);
// };
  onMounted(getAllDepartment);
  </script>
  