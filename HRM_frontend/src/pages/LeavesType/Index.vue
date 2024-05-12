<template>
    <div class="mt-10 p-4 sm:ml-64 text-black">
      <div class="flex justify-between items-center mb-4 mt-5">
        <h2 class="text-2xl font-bold">All LeaveTypes</h2>
        <button @click="CreateLeavesType" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New LeavesType</button>
      </div>
      <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"> Days</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">actions</th>
        </tr>
      </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="leaveType in leaveTypes" :key="leaveType.id">
            <td class="px-6 py-4 whitespace-nowrap">{{ leaveType.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ leaveType.slug }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ leaveType.limit }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <button @click="showDeleteConfirmation(leaveType.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800" >DELETE</button>
              <button @click="editLeaveType(leaveType.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Delete Confirmation Modal -->
      <DeleteConfirmationModal itemType="leaveType" v-if="leaveTypeToDelete !== null" :leaveTypeId="leaveTypeToDelete" @cancel="cancelDelete" @ok="confirmDelete" />
    </div>
  </template>
  
  <script setup>
  import { toast } from 'vue3-toastify';

  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  // import CreateDepartment from './CreateDepartment.vue';
  import DeleteConfirmationModal from '../../components/Delete.vue';
// import CreateLeavesType from './CreateLeavesType.vue';
  
  const leaveTypes = ref([]);
  const router = useRouter();
  const leaveTypeToDelete = ref(null);
  
  const CreateLeavesType = () => {
    router.push({ name: 'CreateLeavesType' });
  };
  
  const editLeaveType = (leaveTypeId) => {
    router.push(`/leaveTypes/edit-leaveType/${leaveTypeId}`);
  };
  
  const getAllLeaveTypes = () => {
    api.get('/leaveType/')
      .then(response => {
        console.log('All leaveTypes:', response.data);
        leaveTypes.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching leaveTypes:', error);
      });
  };
  
  const deleteLeaveType = async (leaveTypeId) => {
  try {
    await api.delete(`/leaveType/${leaveTypeId}`);
    // Remove the deleted department from the leavesTypes array
    leaveTypes.value = leavesTypes.value.filter(leaveType => leaveType.id !== leaveTypeId);
    console.log('Department deleted successfully');
  } catch (error) {
    console.error('Error deleting department:', error);
  }
};
  
  const showDeleteConfirmation = (leaveTypeId) => {
  leaveTypeToDelete.value = leaveTypeId;
};

const cancelDelete = () => {
  leaveTypeToDelete.value = null;
};

const confirmDelete = (leaveTypeId) => {
    deleteDepartment(leaveTypeId);
// cancelDelete();
};
// const confirmDelete = (departmentId) => {
//   deleteDepartment(departmentId);
// };
  onMounted(getAllLeaveTypes);
  </script>
  