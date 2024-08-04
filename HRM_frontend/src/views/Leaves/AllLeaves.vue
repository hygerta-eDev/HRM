<template>
    <div class="container mx-auto p-6">
      <div class="p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">All Leaves</h1>
        <div class=" w-full flex justify-end">
          <router-link to="/Leaves/EditLeaves">
            <button class="mb-2 bg-gray-500 text-white px-4 py-2 rounded-lg">Back</button>
          </router-link>
        </div>
        <table class="table-auto bg-white w-full shadow-md rounded border-separate border-spacing-y-2">
          <thead class="bg-sky-600">
            <tr>
              <th class="px-4 py-2 border-b w-1/6">Employee</th>
              <th class="px-4 py-2 border-b w-1/6">Leave Type</th>
              <th class="px-4 py-2 border-b w-1/6">Start Date</th>
              <th class="px-4 py-2 border-b w-1/6">End Date</th>
              <th class="px-4 py-2 border-b w-1/6">Days</th>
              <th class="px-4 py-2 border-b w-1/6">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(leave, index) in leaves"
              :key="leave.id"
              class="border-b border-gray-300 hover:bg-blue-100 cursor-pointer"
              :class="{ 'bg-white': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
              @click="showLeaveDetails(leave)"
            >
              <td class="border px-4 py-2">{{ getEmployeesName(leave.employee_id) }}</td>
              <td class="border px-4 py-2">{{ getLeaveTypeName(leave.leave_type_id) }}</td>
              <td class="border px-4 py-2">{{ formatISODate(leave.start_date) }}</td>
              <td class="border px-4 py-2">{{ formatISODate(leave.end_date) }}</td>
              <td class="border px-4 py-2">{{ leave.days }}</td>
              <!-- <td class="border px-4 py-2">
                <span :class="statusClass(leave.status)">
                  {{ leave.status }}
                </span>
              </td> -->
              <td class="border px-4 py-2 flex items-center ">
                <span v-if="leave.status === 'Approved'" class="ml-3 mr-6">
                    <i class="fas  fa-lg fa-check-circle text-green-400"></i>
                </span>
                <span v-if="leave.status === 'Pending'" class="ml-3 mr-6">
                    <i class="fas  fa-lg fa-clock text-yellow-400"></i>
                </span>
                <span v-if="leave.status === 'Rejected'" class="ml-3 mr-6">
                    <i class="fas  fa-lg fa-times-circle text-red-500"></i>
                </span>
                <span>{{ leave.status }}</span>
               </td>


            </tr>
          </tbody>
        </table>
  
        <!-- Details Section -->
        <div v-if="selectedLeave" class="fixed inset-0 z-50 bg-gray-500 bg-opacity-75 flex items-center justify-center">
    <div class="bg-blue-100 p-4 rounded-lg shadow-lg max-w-3xl w-full overflow-hidden relative">
      <!-- Close button with adjusted position -->
      <button class="absolute top-2 right-2 text-gray-600" @click="closeLeaveDetails">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <h2 class="text-3xl font-bold mb-6">Leave Details of {{ getEmployeesName(selectedLeave.employee_id) }}</h2>
      <!-- Display leave quota details -->
      <div class="divide-y divide-gray-200">
        <div class="py-4">
          <!-- <h3 class="text-xl font-bold mb-2">Leave Quota Details</h3> -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
            <div v-for="(quota, index) in leaveQuotas" :key="index" class="bg-gray-100 p-4 rounded-lg shadow-md">
              <p class="text-lg font-semibold mb-2">{{ getLeaveTypeName(quota.leave_type_id) }}</p>
              <ul>
                <li><span class="font-semibold">Amount:</span> {{ quota.amount }}</li>
                <li><span class="font-semibold">Taken:</span> {{ quota.taken }}</li>
                <li><span class="font-semibold">Available:</span> {{ quota.available }}</li>
              </ul>
            </div>
            <div class="bg-gray-100 p-4 rounded-lg shadow-md">
                <p class="mt-4 text-xl font-semibold mb-2">Total Leaves: </p>
                <p class="text-2xl font-semibold mb-2">{{ TotalLeaves }}</p>
            </div>
          </div>
        </div>
        <!-- Additional sections can be added here -->
      </div>
    </div>
  </div>
      </div>
    </div>
  </template>
  
  <script>
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  
  export default {
    data() {
      return {
        leaves: [], // Array to store all leave details
        leaveTypes: [], // Array to store leave types
        allEmployees: [], // Array to store all employee details
        selectedLeave: null, // Selected leave to show details
        leaveDaysByType: {}, // Days for each leave type for the selected employee
        leaveQuotas: [], // Array to store leave quotas for selected employee
        TotalLeaves:'',
      };
    },
    computed: {
      localStorageUserId() {
        return localStorage.getItem('userId') || '';
      }
    },
    methods: {
      async fetchLeaves() {
        try {
          const response = await api.get('/leaves/'); // Adjust the API endpoint as needed
          this.leaves = response.data;
        } catch (error) {
          toast.error('An error occurred while fetching leaves');
        }
      },
      async fetchLeaveTypes() {
        try {
          const response = await api.get('/leaveType/active_leaveTypes');
          this.leaveTypes = response.data;
        } catch (error) {
          alert('An error occurred while fetching leave types');
        }
      },
      async fetchAllLeaves(employee_id) {
        try {
          const response = await api.get(`/leaves/count_leaves/${employee_id}`);
          this.TotalLeaves = response.data;
        } catch (error) {
          alert('An error occurred while fetching leaves total');
        }
      },
      async fetchEmployees() {
        try {
          const response = await api.get('/employees/');
          this.allEmployees = response.data;
        } catch (error) {
          toast.error('An error occurred while fetching employees');
        }
      },
      async fetchEmployeeLeaveQuotes(employeeId) {
        try {
          const response = await api.get(`/leaveQuota/employee_leave_quotes/${employeeId}`);
          this.leaveQuotas = response.data;
        } catch (error) {
          toast.error('An error occurred while fetching employee leave quotes');
        }
      },
      getLeaveTypeName(id) {
        const type = this.leaveTypes.find(type => type.id === id);
        return type ? type.slug : 'Unknown';
      },
      getEmployeesName(id) {
        const employee = this.allEmployees.find(emp => emp.id === id);
        return employee ? employee.name : 'Unknown';
      },
      formatISODate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
      },
      statusClass(status) {
        return {
          'bg-green-500 text-black-900 px-2 py-1 rounded-full': status === 'Approved',
          'bg-red-600 text-black-900 px-2 py-1 rounded-full': status === 'Rejected',
          'bg-blue-600 text-black-900 px-2 py-1 rounded-full': status === 'Pending',
        };
      },
      showLeaveDetails(leave) {
        this.selectedLeave = leave;
        this.leaveDaysByType = this.leaves
          .filter(l => l.employee_id === leave.employee_id)
          .reduce((acc, l) => {
            if (acc[l.leave_type_id]) {
              acc[l.leave_type_id] += l.days;
            } else {
              acc[l.leave_type_id] = l.days;
            }
            return acc;
          }, {});
        // Fetch employee leave quotes for the selected employee
        this.fetchEmployeeLeaveQuotes(leave.employee_id);
        this.fetchAllLeaves(leave.employee_id)
      },
      closeLeaveDetails() {
        this.selectedLeave = null; // Reset selectedLeave to close the modal
      },
    },
    created() {
      this.fetchLeaves(); // Fetch all leaves when component is created
      this.fetchLeaveTypes(); // Fetch leave types when component is created
      this.fetchEmployees();
       // Fetch all employees when component is created
    }
  };
  </script>
  
  <style scoped>

  </style>
  