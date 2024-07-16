<template>
    <div class="container mx-auto p-6">
      <div class="add-employee-to-training p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">Add Employee to Training</h1>
  
        <!-- Form for adding employee to training -->
        <form @submit.prevent="addEmployeeToTraining">
          <div class="mb-4">
            <label for="employeeId" class="block text-gray-700 text-sm font-bold mb-2">Employee ID</label>
            <input type="number" id="employeeId" v-model.number="form.employee_id" class="input-field" required>
          </div>
  
          <div class="mb-4">
            <label for="trainingId" class="block text-gray-700 text-sm font-bold mb-2">Training ID</label>
            <input type="number" id="trainingId" v-model.number="form.training_id" class="input-field" required>
          </div>
  
          <div class="flex justify-end">
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">Add Employee to Training</button>
          </div>
        </form>
  
        <!-- Success or error message display -->
        <div v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</div>
        <div v-if="successMessage" class="text-green-500 mt-4">{{ successMessage }}</div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { api } from '@/api'; // Assuming you have an API module
  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css';
  
  const form = ref({
    employee_id: 0,
    training_id: 0,
    created_at: new Date().toISOString(), // Set to current timestamp
    user_id: 0, // Use a select dropdown component for selecting this
  });
  
  
  let errorMessage = '';
  let successMessage = '';
  
  const addEmployeeToTraining = () => {
    // Ensure form is valid before submitting
    if (!validateForm()) {
      return;
    }
    form.value.user_id=1
    // Make API call to add employee to training
    api.post('/employee-training', form.value)
      .then(response => {
        // Handle success
        successMessage = 'Employee added to training successfully!';
        clearForm();
      })
      .catch(error => {
        // Handle error
        errorMessage = 'Failed to add employee to training. Please try again.';
        console.error('Error adding employee to training:', error);
      });
  };
  
  const validateForm = () => {
    // Example validation: ensure required fields are filled
    if (!form.value.employee_id || !form.value.training_id || !form.value.created_at || !form.value.user_id) {
      errorMessage = 'Please fill in all fields.';
      return false;
    }
    return true;
  };
  
  const clearForm = () => {
    form.value = {
      employee_id: 0,
      training_id: 0,
      created_at: '',
      user_id: 0,
    };
    errorMessage = '';
  };
  
  </script>
  
  <style scoped>
  .input-field {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #a0aec0;
    border-radius: 0.25rem;
  }
  </style>
  