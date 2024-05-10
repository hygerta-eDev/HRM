<template>
    <div class="mt-10 p-4 sm:ml-64 text-black">
      <div class="flex justify-between items-center mb-4 mt-5">
        <h2 class="text-2xl font-bold">All Employees</h2>
        <button @click="createEmployee" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Create New Employee</button>
      </div>
      <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Username</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Last Name</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Job Position</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Employee Status</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Department</th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>

        </tr>
      </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="employee in employees" :key="employee.id">
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.username }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.name }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.last_name }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.email }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.job_position_id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.active }}</td>
            <td class="px-6 py-4 whitespace-nowrap">{{ employee.department_id }}</td>

            <td class="px-6 py-4 whitespace-nowrap">
              <button @click="showDeleteConfirmation(employee.id)" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800" >DELETE</button>
              <button @click="editEmployee(employee.id)" type="submit" class="ml-5 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">EDIT</button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Delete Confirmation Modal -->
      <!-- <DeleteConfirmationModal itemType="employee" v-if="departmentToDelete !== null" :departmentId="departmentToDelete" @cancel="cancelDelete" @ok="confirmDelete" /> -->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { api } from '@/api';
  import { useRouter } from 'vue-router';
  import CreateEmployee from './CreateEmployee.vue';

  const employees = ref([]);
  const router = useRouter();
  const employeeToDelete = ref(null); // Corrected from departmentToDelete

  const createEmployee = () => {
    router.push({ name: 'CreateEmployee' });
  };

  const editEmployee = (employeeId) => {
    router.push(`/employees/edit-employee/${employeeId}`);
  };

  const getAllEmployees = () => {
    api.get('/employees/')
      .then(response => {
        console.log('All employees:', response.data);
        employees.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching employees:', error);
      });
  };

  const deleteEmployee = async (employeeId) => {
    try {
      await api.delete(`employees/delete_employee/${employeeId}`);
      // Remove the deleted employee from the employees array
      employees.value = employees.value.filter(employee => employee.id !== employeeId);
      console.log('Employee deleted successfully');
    } catch (error) {
      console.error('Error deleting employee:', error);
    }
  };

  const showDeleteConfirmation = (employeeId) => {
    employeeToDelete.value = employeeId; // Corrected from departmentToDelete
  };

  const cancelDelete = () => {
    employeeToDelete.value = null;
  };

  const confirmDelete = (employeeId) => {
    deleteEmployee(employeeId); // Corrected function name
    cancelDelete();
  };

  onMounted(getAllEmployees);
</script>
