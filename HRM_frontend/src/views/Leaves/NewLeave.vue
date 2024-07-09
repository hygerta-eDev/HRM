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
    <div class="max-w-md mx-auto p-4">
      <form @submit.prevent="createLeave" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
    
        <div class="mb-4">
          <label for="leave_type_id" class="block text-gray-700">Leave Type</label>
          <select v-model="selectedLeaveType" id="leave_type_id" required 
                  class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300">
            <option value="" disabled>Select Leave Type</option>
            <option v-for="type in leaveTypes" :key="type.id" :value="type.id">{{ type.slug }}</option>
          </select>
        </div>
    
        <div v-if="selectedLeaveType && leaveTypeInfo[selectedLeaveType]">
          <p class="text-sm text-gray-500 mb-2">
            Total Days: {{ leaveTypeInfo[selectedLeaveType].amount }}
            | Taken: {{ leaveTypeInfo[selectedLeaveType].taken }}
            | Available: {{ leaveTypeInfo[selectedLeaveType].available }}
          </p>
        </div>
    
        <div class="mb-4">
          <label for="start_date" class="block text-gray-700">Start Date</label>
          <input v-model="leaveData.start_date" id="start_date" type="date" @change="calculateWorkdays" required 
                 class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300" />
        </div>
    
        <div class="mb-4">
          <label for="end_date" class="block text-gray-700">End Date</label>
          <input v-model="leaveData.end_date" id="end_date" type="date" @change="calculateWorkdays" required 
                 class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-blue-300" />
        </div>
    
        <input v-model.number="leaveData.days" id="days" type="hidden" />
    
        <button type="submit" class="w-full bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300 mt-4">
          Create Leave
        </button>
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
          status: 'Pending',
          created_at: new Date().toISOString(),
        },
        leaveTypes: [],
        leaveTypeInfo: {},
        selectedLeaveType: '',
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
          this.leaveData.user_id = userId;
          this.leaveData.employee_id = userId;
  
          const response = await api.post('/leaves/create_leaves', this.leaveData);
          alert('Leave created successfully');
          this.resetForm();
  
        } catch (error) {
          alert('An error occurred while creating the leave');
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
          const userId = localStorage.getItem('user_id');
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
  
          this.leaveData.days = workdays;
        }
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
      }
    },
    watch: {
      selectedLeaveType: 'fetchLeaveTypeInfo' // Watch for changes in selectedLeaveType and fetch leave type info
    },
    created() {
      this.fetchLeaveTypes(); // Fetch leave types when component is created
    }
  };
  </script>
  