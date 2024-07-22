<template>
  <div class="container mx-auto p-6">
    <div class="flex justify-between">
      <!-- Training Information -->
      <div class="training-info mr-10 p-8 rounded-lg shadow-xl border border-blue-200 bg-white w-2/3">
        <h1 class="text-2xl font-bold mb-6">{{ $t('view_training') }}</h1>
        <div v-if="Training" class="Training-details">
          <!-- Display training details -->
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('training_title') }}</label>
            <input type="text" :value="Training.title" class="input-field" readonly />
          </div>
          <p>Title: tre</p>
          <div class="flex justify-between mb-4">
            <div class="w-1/2 pr-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('start_date') }}</label>
              <input type="text" :value="Training.start_date" class="input-field" readonly />
            </div>
            <div class="w-1/2 pl-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('end_date') }}</label>
              <input type="text" :value="Training.end_date" class="input-field" readonly />
            </div>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('description') }}</label>
            <textarea :value="Training.description" class="input-field" readonly></textarea>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('outcome') }}</label>
            <textarea :value="Training.outcome" class="input-field" readonly></textarea>
          </div>
          <div class="flex justify-between mb-4">
            <div class="w-1/2 pr-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('completed_at') }}</label>
              <input type="text" :value="Training.completed_at" class="input-field" readonly />
            </div>
            <div class="w-1/2 pl-2">
              <label class="block text-gray-700 text-sm font-bold mb-5 mr-4">{{ $t('active') }}</label>
              <InputSwitch v-model="Training.active" disabled />
            </div>
          </div>
        </div>
        <div v-else class="loading text-center mt-4">
          <p>{{ $t('loading') }}</p>
        </div>
      </div>

      <!-- Assigned Employees -->
      <div class="assigned-employees static p-8 rounded-lg shadow-xl border border-blue-200 bg-white w-1/3">
        <div class="flex flex-col h-full">
          <h1 class="text-2xl font-bold mb-6">{{ $t('add_employees_to_training') }}</h1>
          <div class="input-container flex-1">
            <ul>
              <li v-for="employee in assignedEmployees" :key="employee.id" class="employee-box mb-4 p-4 flex justify-between items-center rounded-lg shadow-md border border-gray-200 bg-gray-50 hover:bg-gray-100">
                <span>{{ employee.name }} {{ employee.last_name }}</span>
                <button v-if="Training && Training.active" @click="removeEmployee(employee.id)" class="text-red-500 hover:text-red-700">Remove</button>
              </li>
            </ul>
          </div>
          <div class="justify-items-center mt-auto">
            <button @click="openModal" :class="buttonClass" :disabled="!Training?.active" class="text-sm text-blue-500 hover:text-blue-700">{{ $t('add_employee_to_training') }}</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal for adding employees to training -->
    <div v-if="showModal" class="fixed inset-0 z-50 bg-gray-500 bg-opacity-75 flex items-center justify-center">
      <div class="bg-white p-8 rounded-md shadow-md w-1/2 h-1/2 overflow-auto">
        <div class="flex justify-between">
          <div class="training-info mr-5 p-8 rounded-lg shadow-xl border border-blue-200 bg-white w-2/3">
            <h3 class="text-2xl font-bold mb-10">{{ $t('add_employees_to_training') }}</h3>
            <div class="mb-4">
              <label class="block text-sm font-bold mb-2">{{ $t('select_employees') }}</label>
              <MultiSelect v-model="selectedEmployees" :options="employeeOptions" optionLabel="label" optionValue="value" :placeholder="$t('select_employees')" display="chip" class="w-full md:w-80" />
            </div>
          </div>
          <div class="assigned-employees-modal p-4 rounded-lg shadow-xl border border-blue-200 bg-white w-full overflow-auto">
            <h1 class="font-bold mb-6">{{ $t('assigned_employees') }}</h1>
            <div>
              <ul>
                <li v-for="employee in selectedEmployeesDetails" :key="employee.value" class="employee-box-small mb-2 p-2 flex justify-between items-center rounded-lg shadow-md border border-gray-200 bg-gray-50 hover:bg-gray-100">
                  {{ employee.label }}
                  <button @click="deselectEmployee(employee.value)" class="text-red-500 hover:text-red-700">✕</button>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="mt-4 flex gap-2 place-content-center">
          <button @click="addEmployees" class="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 mr-0">{{ $t('add_employees') }}</button>
          <button @click="closeModal" class="bg-gray-500 text-white py-2 px-4 rounded-md hover:bg-gray-600">{{ $t('cancel') }}</button>
        </div>
      </div>
    </div>

    <!-- Navigation buttons -->
    <div class="text-right mt-4">
      <router-link v-if="Training" :to="`/Trainings/Edit/${Training.id}`">
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">{{ $t('edit') }}</button>
      </router-link>
      <router-link :to="`/Trainings`">
        <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow ml-2">{{ $t('back') }}</button>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';
import InputSwitch from 'primevue/inputswitch';
import MultiSelect from 'primevue/multiselect';
import { toast } from 'vue3-toastify';

const route = useRoute();
const Training = ref(null);
const showModal = ref(false);
const selectedEmployees = ref([]);
const employeeOptions = ref([]);
const assignedEmployees = ref([]);

const getTraining = () => {
  const TrainingId = Number(route.params.id);
  api.get(`/training/${TrainingId}`)
    .then(response => {
      Training.value = response.data;
      // Convert dates to ISO string for proper display
      Training.value.start_date = new Date(Training.value.start_date).toISOString().split('T')[0];
      Training.value.end_date = new Date(Training.value.end_date).toISOString().split('T')[0];
      Training.value.completed_at = Training.value.completed_at ? new Date(Training.value.completed_at).toISOString().split('T')[0] : '';
    })
    .catch(error => {
      console.error('Error fetching Training:', error);
    });
};

const fetchAssignedEmployees = async () => {
  const TrainingId = Number(route.params.id);
  try {
    const response = await api.get(`/training/${TrainingId}/assigned_employees`);
    assignedEmployees.value = response.data;
  } catch (error) {
    console.error('Error fetching assigned employees:', error);
  }
};

const fetchAllEmployees = async () => {
  try {
    const employeesResponse = await api.get('/employees/active_Employees/');
    employeeOptions.value = employeesResponse.data.map(employee => ({
      value: employee.id,
      label: `${employee.name} ${employee.last_name}`
    }));
  } catch (error) {
    console.error('Error fetching employees:', error);
  }
};

const openModal = () => {
  showModal.value = true;
  fetchAllEmployees();
};

const closeModal = () => {
  showModal.value = false;
  selectedEmployees.value = []; // Reset selected employees when modal closes
};

const addEmployees = () => {
  selectedEmployees.value.forEach(employeeId => {
    const formData = {
      employee_id: employeeId,
      training_id: Training.value.id,
      created_at: new Date().toISOString(),
      created_by: 0,
      updated_at: new Date().toISOString(),
      updated_by: 0,
      deleted_at: null,
      deleted_by: 0,
    };

    api.post('/training/create_employee_training', formData)
      .then(response => {
        console.log(`Employee ${employeeId} added to training successfully:`, response.data);
        fetchAssignedEmployees(); // Refresh the list of assigned employees
      })
      .catch(error => {
        toast.error(error.response.data.detail);
        console.error(`Failed to add employee ${employeeId} to training:`, error);
      });
  });

  showModal.value = false; // Close modal
  selectedEmployees.value = []; // Optionally, reset selectedEmployees array
};

const removeEmployee = (employeeId) => {
  const TrainingId = Number(route.params.id);
  api.delete(`/training/${TrainingId}/remove_employee/${employeeId}`)
    .then(response => {
      console.log(`Employee ${employeeId} removed from training successfully:`, response.data);
      fetchAssignedEmployees(); // Refresh the list of assigned employees
    })
    .catch(error => {
      toast.error(error.response.data.detail);
      console.error(`Failed to remove employee ${employeeId} from training:`, error);
    });
};

const deselectEmployee = (employeeId) => {
  selectedEmployees.value = selectedEmployees.value.filter(id => id !== employeeId);
};

const selectedEmployeesDetails = computed(() => {
  return selectedEmployees.value.map(employeeId => {
    return employeeOptions.value.find(employee => employee.value === employeeId);
  }).filter(employee => employee); // Filter out undefined values
});

// Computed property to determine the button class based on Training.active
const buttonClass = computed(() => {
  return Training.value?.active
    ? 'bg-blue-500 text-white px-4 py-2 rounded-lg shadow '
    : 'bg-blue-100 text-gray-400 px-4 py-2 rounded-lg shadow cursor-not-allowed';
});

onMounted(() => {
  getTraining();
  fetchAssignedEmployees();
});
</script>

<style>
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.input-field {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.25rem;
}

.input-container {
  margin-bottom: 1rem;
}

.input-label {
  display: block;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.input-content {
  padding: 0.5rem;
}

.loading {
  text-align: center;
  margin-top: 20px;
  font-style: italic;
  color: #666;
}

.employee-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.5rem;
  background-color: #edf2f7;
  transition: background-color 0.2s;
}

.employee-box:hover {
  background-color: #e2e8f0;
}

.employee-box button {
  background: none;
  border: none;
  cursor: pointer;
}

.employee-box button:hover {
  color: #e53e3e;
}

.employee-box-small {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.25rem;
  background-color: #edf2f7;
  transition: background-color 0.2s;
}

.employee-box-small:hover {
  background-color: #e2e8f0;
}

.employee-box-small button {
  background: none;
  border: none;
  cursor: pointer;
}

.employee-box-small button:hover {
  color: #e53e3e;
}

.container {
  margin: auto;
  max-width: 1400px; /* Adjust max-width as per your design */
}
</style>
