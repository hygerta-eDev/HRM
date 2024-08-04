<template>
  <div class="p-8">
    <div class="p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
      <div class="bg-white w-full shadow-md mt-5 rounded border-separate border-spacing-y-2 h-20 flex items-center justify-center">
        <h2 class="text-2xl font-bold">Employees List</h2>
      </div>
      <table class="table-auto bg-white w-full shadow-md mt-5 rounded border-separate border-spacing-y-2">
        <thead class="bg-sky-600">
          <tr>
            <th class="px-4 py-2 border-b w-1/4">Employee ID</th>
            <th class="px-4 py-2 border-b w-1/4">Name</th>
            <th class="px-4 py-2 border-b w-1/4">Position</th>
            <th class="px-4 py-2 border-b w-1/4">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(employee, index) in employees"
            :key="employee.id"
            class="border-b border-gray-300 hover:bg-blue-100"
            :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
          >
            <td class="border px-4 py-2">{{ employee.id }}</td>
            <td class="border px-4 py-2">{{ employee.name }}</td>
            <td class="border px-4 py-2">{{ employee.position }}</td>
            <td class="border px-4 py-2">
              <button @click="createAssessment(employee.id)" class="bg-blue-500 text-white py-1 px-3 rounded-lg hover:bg-blue-600">
                Create Assessment
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  data() {
    return {
      employees: []  // To be populated with data from the API
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    async fetchEmployees() {
      try {
        const response = await api.get('/employees/');
        this.employees = response.data;
      } catch (error) {
        console.error('Error fetching employees:', error);
      }
    },
    createAssessment(id) {
      // Logic to navigate to the assessment creation page with the selected employee ID
      this.$router.push({ name: 'NewAssessment', params: { id } });
    }
  }
};
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>
