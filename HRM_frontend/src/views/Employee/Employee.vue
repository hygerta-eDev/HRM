<!-- <template>
  <div class="p-6 container">
    <div class="filter-buttons flex justify-center space-x-4 mb-6">
      <button @click="selectedCompany = 'eTech'" :class="{'bg-blue-500 text-white': selectedCompany === 'eTech', 'bg-gray-300': selectedCompany !== 'eTech'}" class="px-4 py-2 rounded-lg">eTech</button>
      <button @click="selectedCompany = 'CyberOne'" :class="{'bg-blue-500 text-white': selectedCompany === 'CyberOne', 'bg-gray-300': selectedCompany !== 'CyberOne'}" class="px-4 py-2 rounded-lg">CyberOne</button>
      <button @click="selectedCompany = 'eDev'" :class="{'bg-blue-500 text-white': selectedCompany === 'eDev', 'bg-gray-300': selectedCompany !== 'eDev'}" class="px-4 py-2 rounded-lg">eDev</button>
    </div>
    <div v-if="selectedCompany">
      <h2 class="text-lg font-semibold mb-4">{{ selectedCompany }} Employees</h2>
      <div class="overflow-x-auto">
        <table class="employee-table w-full border-collapse border border-gray-300">
          <thead>
            <tr class="bg-gray-200">
              <th class="px-4 py-2">First Name</th>
              <th class="px-4 py-2">Last Name</th>
              <th class="px-4 py-2">Company</th>
              <th class="px-4 py-2">Position</th>
              <th class="px-4 py-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="employee in filteredEmployees" :key="employee.id" class="hover:bg-gray-100">
              <td class="px-4 py-2">{{ employee.firstName }}</td>
              <td class="px-4 py-2">{{ employee.lastName }}</td>
              <td class="px-4 py-2">{{ employee.company }}</td>
              <td class="px-4 py-2">{{ employee.position }}</td>
              <td class="px-4 py-2 actions">
                <router-link to="/Employee/ViewEmployee">
                  <button @click="viewEmployee(employee)" class="bg-green-500 text-white px-2 py-1 rounded-lg">View</button>
                </router-link>
                <router-link to="/Employee/EditEmployee">
                  <button @click="editEmployee(employee)" class="bg-yellow-500 text-white px-2 py-1 rounded-lg ml-2">Edit</button>
                </router-link>
                <button @click="deleteEmployee(employee.id)" class="bg-red-500 text-white px-2 py-1 rounded-lg ml-2">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <router-link to="/Employee/NewEmployee">
      <button class="bg-blue-500 text-white px-4 py-2 mt-4 rounded-lg">New Employee</button>
    </router-link>
    
    <div v-if="showViewEmployeeModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 backdrop-blur-sm flex justify-center items-center">
      <div class="bg-white rounded-lg p-6 w-full max-w-lg">
        <h3 class="text-xl font-semibold mb-4">Employee Details</h3>
        <p><strong>First Name:</strong> {{ selectedEmployee?.firstName }}</p>
        <p><strong>Last Name:</strong> {{ selectedEmployee?.lastName }}</p>
        <p><strong>Company:</strong> {{ selectedEmployee?.company }}</p>
        <p><strong>Position:</strong> {{ selectedEmployee?.position }}</p>
        <div class="text-right mt-4">
          <button @click="showViewEmployeeModal = false" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Close</button>
        </div>
      </div>
    </div>
    
    <div v-if="showEditEmployeeModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 backdrop-blur-sm flex justify-center items-center">
      <div class="bg-white rounded-lg p-6 w-full max-w-lg">
        <h3 class="text-xl font-semibold mb-4">Edit Employee</h3>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">First Name</label>
          <input v-model="editEmployeeData.firstName" type="text" class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
          <input v-model="editEmployeeData.lastName" type="text" class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company</label>
          <select v-model="editEmployeeData.company" class="w-full px-3 py-2 border rounded-md">
            <option value="eTech">eTech</option>
            <option value="CyberOne">CyberOne</option>
            <option value="eDev">eDev</option>
          </select>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">Position</label>
          <input v-model="editEmployeeData.position" type="text" class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="text-right">
          <button @click="updateEmployee" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Save</button>
          <button @click="cancelEditEmployee" class="bg-gray-400 text-white px-4 py-2 ml-2 rounded-lg">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, computed } from 'vue';
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
    const selectedCompany = ref<string>(''); // Selected company
    const showViewEmployeeModal = ref<boolean>(false);
    const showEditEmployeeModal = ref<boolean>(false);
    const selectedEmployee = ref<Employee | null>(null); // Employee selected for viewing
    const editEmployeeData = ref<Employee>({ id: 0, firstName: '', lastName: '', company: '', position: '' });

    // Dummy data for employees (replace this with your actual data)
    const employees = ref<Employee[]>([
      { id: 1, firstName: 'John', lastName: 'Doe', company: 'eTech', position: 'Developer' },
      { id: 2, firstName: 'Alice', lastName: 'Smith', company: 'eTech', position: 'Designer' },
      { id: 3, firstName: 'Bob', lastName: 'Brown', company: 'CyberOne', position: 'Manager' },
      { id: 4, firstName: 'Carol', lastName: 'Davis', company: 'eDev', position: 'Developer' },
    ]);

    const filteredEmployees = computed(() => {
      return employees.value.filter(employee => employee.company === selectedCompany.value);
    });

    const viewEmployee = (employee: Employee) => {
      selectedEmployee.value = employee;
      showViewEmployeeModal.value = true;
    };

    const editEmployee = (employee: Employee) => {
      editEmployeeData.value = { ...employee };
      showEditEmployeeModal.value = true;
    };

    const updateEmployee = () => {
      const index = employees.value.findIndex(e => e.id === editEmployeeData.value.id);
      if (index !== -1) {
        employees.value[index] = { ...editEmployeeData.value };
      }
      showEditEmployeeModal.value = false;
    };

    const cancelEditEmployee = () => {
      showEditEmployeeModal.value = false;
    };

    const deleteEmployee = (id: number) => {
      employees.value = employees.value.filter(employee => employee.id !== id);
    };

    return {
      selectedCompany,
      showViewEmployeeModal,
      showEditEmployeeModal,
      selectedEmployee,
      editEmployeeData,
      employees, // Expose the employees array to the template
      filteredEmployees,
      viewEmployee,
      editEmployee,
      updateEmployee,
      cancelEditEmployee,
      deleteEmployee
    };
  }
}
</script>

<style scoped>
.fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style> -->


<template>
  <div class="p-10">
    <div class="container mx-auto" :class="{ 'blurred': deleteDialogVisible }">
      <!-- Filter Buttons -->
      <div class="filter-buttons flex justify-center space-x-4 mb-6">
        <button @click="selectedCompany = 'Institution A'" :class="{'bg-blue-500 text-white': selectedCompany === 'Institution A', 'bg-gray-300': selectedCompany !== 'Institution A'}" class="px-4 py-2 rounded-lg">Institution A</button>
        <button @click="selectedCompany = 'CyberOne'" :class="{'bg-blue-500 text-white': selectedCompany === 'CyberOne', 'bg-gray-300': selectedCompany !== 'CyberOne'}" class="px-4 py-2 rounded-lg">CyberOne</button>
        <button @click="selectedCompany = 'eDev'" :class="{'bg-blue-500 text-white': selectedCompany === 'eDev', 'bg-gray-300': selectedCompany !== 'eDev'}" class="px-4 py-2 rounded-lg">eDev</button>
        <button @click="selectedCompany = 'All'" :class="{'bg-blue-500 text-white': selectedCompany === 'All', 'bg-gray-300': selectedCompany !== 'All'}" class="px-4 py-2 rounded-lg">All</button>
      </div>
      
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-3xl font-semibold">All Employees</h2>
        <router-link to="/Employee/NewEmployee">
          <button class="bg-blue-500 text-white px-4 py-2 rounded-lg">New Employee</button>
        </router-link>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300 rounded-lg">
          <thead>
            <tr class="bg-sky-600">
              <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
              <th class="px-4 py-4  w-1/8 text-left">First Name</th>
              <th class="px-4 py-4  w-1/8 text-left">Last Name</th>
              <th class="px-4 py-4  w-1/8 text-left">Company</th>
              <th class="px-4 py-4  w-1/8 text-left">Position</th>
              <th class="px-4 py-4  w-1/8 text-left">Position</th>
              <th class="px-4 py-4  w-1/8 text-left">Position</th>
              <th class="px-4 py-4  w-1/8 text-left">Position</th>
              <th class="px-4 py-4  w-1/8 text-left">Position</th>

              <th class="px-4 py-4  w-1/8 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(employee, index) in displayedEmployees" :key="employee.id"
                :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
                class="border-b border-gray-300 hover:bg-blue-100">
              <td class="px-4 py-4 text-left border-r border-black-900">{{ index + 1 }}</td>
              <td class="px-4 py-4 text-left">{{ employee.name }}</td>
              <td class="px-4 py-4 text-left">{{ employee.last_name }}</td>
              <td class="px-4 py-4 text-left">{{ getInstitutionName(employee.institucion_id) }}</td>
              <td class="px-4 py-4 text-left">{{ employee.job_position_id }}</td>
              <td class="px-4 py-4 text-left">{{ employee.job_position_id }}</td>
              <td class="px-4 py-4 text-left">{{ employee.job_position_id }}</td>
              <td class="px-4 py-4 text-left">{{ employee.job_position_id }}</td>
              <td class="px-4 py-4 text-left">{{ employee.job_position_id }}</td>


              <td class="px-4 py-4 text-left">
                <router-link :to="'/Employee/ViewEmployee/' + employee.id">
                  <i @click="viewCompany(company.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>

                  <!-- <button class="bg-green-500 text-white px-2 py-1 rounded-lg">View</button> -->
                </router-link>
                <router-link :to="'/Employee/EditEmployee/' + employee.id">
                  <i @click="editCompany(employee.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>

                  <!-- <button class="bg-yellow-500 text-white px-2 py-1 rounded-lg ml-2">Edit</button> -->
                </router-link>
                <i @click="confirmDelete(employee.id, employee.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>

                <!-- <button @click="deleteEmployee(employee.id)" class="bg-red-500 text-white px-2 py-1 rounded-lg ml-2">Delete</button> -->
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api'; // Assuming you have an API module

export default {
  setup() {
    const selectedCompany = ref('All');
    const employees = ref([]);
    const institutions = ref({}); // Object to store institution names by ID

    const router = useRouter();

    const fetchAllEmployees = async () => {
      try {
        const employeesResponse = await api.get('/employees/');
        employees.value = employeesResponse.data;
        
        const institutionsResponse = await api.get('/institutions/');
        institutionsResponse.data.forEach(institution => {
          institutions.value[institution.id] = institution.name;
        });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const displayedEmployees = computed(() => {
      if (selectedCompany.value === 'All') {
        return employees.value;
      } else {
        return employees.value.filter(employee => getInstitutionName(employee.institucion_id) === selectedCompany.value);
      }
    });

    const getInstitutionName = (institutionId) => {
      return institutions.value[institutionId] || '';
    };

    const deleteEmployee = (employeeId) => {
      // Logic to handle deleting an employee
    };

    onMounted(() => {
      fetchAllEmployees();
    });

    return {
      selectedCompany,
      displayedEmployees,
      getInstitutionName,
      deleteEmployee
    };
  }
}
</script>

