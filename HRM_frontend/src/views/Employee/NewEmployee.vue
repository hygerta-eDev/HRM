<template>
  <div class="p-6">
    <h2 class="text-2xl font-semibold mb-4">New Employee</h2>
    <!-- Employee Form -->
    <div class="p-4 bg-gray-100 rounded-lg">
      <!-- Form Fields -->
      <div class="mb-4">
        <label for="firstName" class="block text-gray-700 text-sm font-bold mb-2">First Name</label>
        <input v-model="newEmployee.firstName" type="text" id="firstName" class="w-full px-3 py-2 border rounded-md" required>
      </div>
      <div class="mb-4">
        <label for="lastName" class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
        <input v-model="newEmployee.lastName" type="text" id="lastName" class="w-full px-3 py-2 border rounded-md" required>
      </div>
      <div class="mb-4">
        <label for="company" class="block text-gray-700 text-sm font-bold mb-2">Company</label>
        <select v-model="newEmployee.company" id="company" class="w-full px-3 py-2 border rounded-md" required>
          <option value="">Select Company</option>
          <option value="eTech">eTech</option>
          <option value="CyberOne">CyberOne</option>
          <option value="eDev">eDev</option>
        </select>
      </div>
      <div class="mb-4">
        <label for="position" class="block text-gray-700 text-sm font-bold mb-2">Position</label>
        <input v-model="newEmployee.position" type="text" id="position" class="w-full px-3 py-2 border rounded-md" required>
      </div>
      <!-- Form Actions -->
      <div class="text-right">
        <button @click="saveEmployee" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Save</button>
        <router-link to="/Employee" class="bg-gray-400 text-white px-4 py-2 ml-2 rounded-lg">Cancel</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

interface Employee {
  id: number;
  firstName: string;
  lastName: string;
  company: string;
  position: string;
}

export default {
  setup() {
    const router = useRouter();
    const employees = ref<Employee[]>([]); // Define the employees array

    const newEmployee = ref<Employee>({ id: 0, firstName: '', lastName: '', company: '', position: '' });

    const saveEmployee = () => {
      // Implementation to save new employee
      console.log('Saving new employee:', newEmployee.value);
      // Add the new employee to the list of employees
      employees.value.push(newEmployee.value);
      // Reset newEmployee
      newEmployee.value = { id: 0, firstName: '', lastName: '', company: '', position: '' };
      // Redirect back to the main page
      router.push('/Employee');
    };

    return {
      employees, // Expose the employees array to the template
      newEmployee,
      saveEmployee
    };
  }
}
</script>


<style scoped>
input[type="text"],
select {
  width: 100%;
}
label {
  display: block;
  margin-bottom: 6px;
  color: #4a5568;
}
button[type="submit"] {
  transition: background-color 0.3s ease;
}
button[type="submit"]:hover {
  background-color: #1e40af;
}
</style>
