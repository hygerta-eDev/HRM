<!-- <template>
    <div class="max-w-md mx-auto p-4">
      <form @submit.prevent="createLeave">
  
        <div class="mb-4">
          <label for="leave_type_id" class="block text-gray-700">Leave Type ID</label>
          <input v-model.number="leaveData.leave_type_id" id="leave_type_id" type="number" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
        </div>
  
        <div class="mb-4">
          <label for="start_date" class="block text-gray-700">Start Date</label>
          <input v-model="leaveData.start_date" id="start_date" type="date" @change="calculateWorkdays" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
        </div>
  
        <div class="mb-4">
          <label for="end_date" class="block text-gray-700">End Date</label>
          <input v-model="leaveData.end_date" id="end_date" type="date" @change="calculateWorkdays" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
        </div>
          <input v-model.number="leaveData.days" id="days" type="hidden" />
  
  
  
        <button type="submit" class="w-full bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300">Create Leave</button>
      </form>
    </div>
  </template>
  
 <script>
 import { api } from '@/api';
 
 export default {
   data() {
     return {
       leaveData: {
         employee_id: '',
         leave_type_id: '',
         start_date: '',
         end_date: '',
         days: '',
         user_id: '',
         status: 'Pending', // Automatically set to Pending
         created_at: new Date().toISOString(),
       },
     };
   },
   computed: {
     localStorageUserId() {
       return localStorage.getItem('userId') || ''; // Fetch user id from localStorage
     }
   },
   methods: {
     async createLeave() {
       try {
        const userId = localStorage.getItem('user_id');
        this.leaveData.user_id= userId
        this.leaveData.employee_id= userId

         const response = await api.post('/leaves/create_leaves', this.leaveData);
         alert('Leave created successfully');
         // Reset form
         this.leaveData = {
           employee_id: '',
           leave_type_id: '',
           start_date: '',
           end_date: '',
           days: '',
           user_id: '',
           status: 'Pending',
           created_at: new Date().toISOString(),
         };
       } catch (error) {
         alert('An error occurred while creating the leave');
       }
     },
     calculateWorkdays() {
       if (this.leaveData.start_date && this.leaveData.end_date) {
         const start = new Date(this.leaveData.start_date);
         const end = new Date(this.leaveData.end_date);
         let workdays = 0;
         const currentDate = new Date(start);
 
         while (currentDate <= end) {
           const dayOfWeek = currentDate.getDay();
           if (dayOfWeek !== 0 && dayOfWeek !== 6) { // Exclude weekends (0 = Sunday, 6 = Saturday)
             workdays++;
           }
           currentDate.setDate(currentDate.getDate() + 1);
         }
 
         this.leaveData.days = workdays;
       }
     }
   },
 };
 </script>
  -->
  
  <template>
    <div class="container w-full mx-auto p-6">
      <div class="p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">Create Leave</h1>
        <form @submit.prevent="createLeave" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-wrap">
          <div class="w-full lg:w-1/4 mb-4 lg:mb-0 px-2">
            <label for="leave_type_id" class="block text-gray-700">Leave Type</label>
            <select v-model="selectedLeaveType" id="leave_type_id" required
                    class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300">
              <option value="" disabled>Select Leave Type</option>
              <option v-for="type in leaveTypes" :key="type.id" :value="type.id">{{ type.slug }}</option>
            </select>
            <div v-if="selectedLeaveType && leaveTypeInfo[selectedLeaveType]" class=" px-2">
              <p class="text-sm text-gray-500 mb-2">
                Total Days: {{ leaveTypeInfo[selectedLeaveType].amount }}
                | Taken: {{ leaveTypeInfo[selectedLeaveType].taken }}
                | Available: {{ leaveTypeInfo[selectedLeaveType].available }}
              </p>
            </div>
          </div>
  
          <div class="w-full lg:w-1/4 mb-4 lg:mb-0 px-2">
            <label for="start_date" class="block text-gray-700">Start Date</label>
            <input v-model="leaveData.start_date" id="start_date" type="date" @change="calculateWorkdays" required
                   class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300" />
          </div>
  
          <div class="w-full lg:w-1/4 mb-4 lg:mb-0 px-2">
            <label for="end_date" class="block text-gray-700">End Date</label>
            <input v-model="leaveData.end_date" id="end_date" type="date" @change="calculateWorkdays" required
                   class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300" />
          </div>
  
          <input v-model.number="leaveData.days" id="days" type="hidden" />
  
          <div>
            <div class="w-full lg:w-auto lg:w-1/4 px-2  flex items-center justify-center mt-7">
                <button type="submit" class="flex items-center justify-center bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300">
              Create Leave
            </button>
            <router-link to="/Leaves">
                <button class="ml-3 flex items-center justify-center bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300">Back</button>
            </router-link>
            </div>

          </div>
        </form>
  
        <!-- Display leave details for logged-in user -->
        
      </div>
      <div class="p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 mt-5">
        <div class="bg-white w-full shadow-md mt-5 rounded border-separate border-spacing-y-2 h-20 flex items-center justify-center">
            <h2 class="text-2xl font-bold">Your Leave Details</h2>
        </div>
        <table class="table-auto bg-white w-full shadow-md mt-5 rounded border-separate border-spacing-y-2">
          <thead class="bg-sky-600">
            <tr >
              <th class="px-4 py-2 border-b w-1/5">Leave Type</th>
              <th class="px-4 py-2 border-b w-1/5">Start Date</th>
              <th class="px-4 py-2 border-b w-1/5">End Date</th>
              <th class="px-4 py-2 border-b w-1/5">Days</th>
              <th class="px-4 py-2 border-b w-1/5">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr
                v-for="(leave, index) in leaveDetails"
                :key="leave.id"
                class="border-b border-gray-300 hover:bg-blue-100"
                :class="{ 'bg-white': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
            >
                <td class="border px-4 py-2">{{ getLeaveTypeName(leave.leave_type_id) }}</td>
                <td class="border px-4 py-2">{{ formatISODate(leave.start_date) }}</td>
                <td class="border px-4 py-2">{{ formatISODate(leave.end_date) }}</td>
                <td class="border px-4 py-2">{{ leave.days }}</td>
                <!-- <td class="border px-4 py-2"> -->
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
                <!-- </td> -->
            </tr>
            </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';

  export default {
    data() {
      return {
        
        leaveData: {
          employee_id: '',
          leave_type_id: '',
          start_date: '',
          end_date: '',
          days: '',
          user_id: '',
          status: 'Pending',
          created_at: new Date().toISOString(),
        },
        leaveTypes: [],
        leaveTypeInfo: {},
        selectedLeaveType: '',
        leaveDetails: [], // Array to store leave details for logged-in user
      };
    },
    computed: {
      localStorageUserId() {
        return localStorage.getItem('userId') || '';
      }
    },
    methods: {
      async createLeave() {
        try {
          const userId = localStorage.getItem('user_id');
          const employeeId = localStorage.getItem('employee_id');

          this.leaveData.user_id = userId;
          this.leaveData.employee_id = employeeId;
          this.leaveData.leave_type_id = this.selectedLeaveType;
          const response = await api.post('/leaves/create_leaves', this.leaveData);
          alert('Leave created successfully');
          this.resetForm();
          this.fetchUserLeaveDetails(); // Refresh leave details after creating new leave
        } catch (error) {
        if (error.response && error.response.data && error.response.data.detail) {
          if (error.response.data.detail === "There is already a pending leave request for this leave type.") {
            toast.error("There is already a pending leave request for this leave type.");
          } else {
            toast.error( error.response.data.detail);
          }
        } else {
          toast.error('An error occurred while creating the leave');
        }
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
      async fetchLeaveTypeInfo() {
        try {
          const userId = localStorage.getItem('employee_id');
          const response = await api.get(`/leaveQuota/leaveType/leaveTypeInfo/${userId}/${this.selectedLeaveType}`);
          this.leaveTypeInfo[this.selectedLeaveType] = response.data; // Update leaveTypeInfo for the selected type
          console.log(this.leaveTypeInfo[this.selectedLeaveType].amount); // Check the amount after updating
        } catch (error) {
          alert('An error occurred while fetching leave type information', error);
        }
      },
      calculateWorkdays() {
        if (this.leaveData.start_date && this.leaveData.end_date) {
          const start = new Date(this.leaveData.start_date);
          const end = new Date(this.leaveData.end_date);
          let workdays = 0;
          const currentDate = new Date(start);
  
          while (currentDate <= end) {
            const dayOfWeek = currentDate.getDay();
            if (dayOfWeek !== 0 && dayOfWeek !== 6) {
              workdays++;
            }
            currentDate.setDate(currentDate.getDate() + 1);
          }
          this.leaveData.days = workdays > 0 ? workdays : 1;
        //   this.leaveData.days = workdays;
        }
      },
      formatISODate(dateString) {
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0'); // Add 1 since months are zero-based
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    },
      resetForm() {
        this.leaveData = {
          employee_id: '',
          leave_type_id: '',
          start_date: '',
          end_date: '',
          days: '',
          user_id: '',
          status: 'Pending',
          created_at: new Date().toISOString(),
        };
        this.selectedLeaveType = '';
      },
      getLeaveTypeName(id) {
      const type = this.leaveTypes.find(type => type.id === id);
      return type ? type.slug : 'Unknown';
    },
    statusClass(status) {
      return {
        'bg-green-400 text-green-900 px-2 py-1 rounded-full': status === 'Approved',
        'bg-red-400 text-red-900 px-2 py-1 rounded-full': status === 'Rejected',
        'bg-blue-400 text-blue-900 px-2 py-1 rounded-full': status === 'Pending',
      };
    },

      async fetchUserLeaveDetails() {
        try {
          const userId = localStorage.getItem('employee_id');
          const response = await api.get(`/leaves/leaves/user/${userId}`);
          this.leaveDetails = response.data;
        } catch (error) {
          console.error('Error fetching user leave details:', error);
        }
      },
    },

    watch: {
      selectedLeaveType: 'fetchLeaveTypeInfo' // Watch for changes in selectedLeaveType and fetch leave type info
    },
    created() {
      this.fetchLeaveTypes(); // Fetch leave types when component is created
      this.fetchUserLeaveDetails(); // Fetch initial user leave details
    }
  };
  </script>
  