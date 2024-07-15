<!-- <template>
  <div class="container w-full mx-auto p-6">
    <h2 class="text-2xl font-bold mb-4">Pending Leave Requests</h2>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else>
      <div v-if="pendingLeaves && pendingLeaves.length === 0" class="text-center text-gray-600">No pending leave requests found.</div>
      <div v-else>
        <table class="table-auto w-full shadow-md mt-5 rounded border-separate border-spacing-y-2">
          <thead class="bg-sky-600">
            <tr>
              <th class="px-4 py-4 border-b w-1/8">Employee</th>
              <th class="px-4 py-4 border-b w-1/8">Leave Type</th>
              <th class="px-4 py-4 border-b w-1/8">Start Date</th>
              <th class="px-4 py-4 border-b w-1/8">End Date</th>
              <th class="px-4 py-4 border-b w-1/8">Days</th>
              <th class="px-4 py-4 border-b w-1/8">Status</th>
              <th class="px-4 py-4 border-b w-1/8">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="leave in pendingLeaves" :key="leave.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2 w-1/8">{{ getEmployeesName( leave.employee_id )}}</td>
              <td class="border px-4 py-2 w-1/8">{{ getLeaveTypeName(leave.leave_type_id) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ formatISODate(leave.start_date) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ formatISODate(leave.end_date) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ leave.days }}</td>
              <td class="border px-4 py-2 w-1/8">
                <span :class="statusClass(leave.status)">
                  {{ leave.status }}
                </span>
              </td>
              <td class="border px-4 py-2 w-1/8">
                <div class="flex gap-2">
                  <button @click="approveLeave(leave)" class="bg-green-500 text-white py-1 px-3 rounded-md hover:bg-green-600">Approve</button>
                  <button @click="openRejectModal(leave)" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        
      </div>
    </div>
<div v-if="showRejectModal" class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
  <div class="bg-white p-2 rounded-md shadow-md w-1/2 h-1/2 overflow-auto">
    <h3 class="text-3xl font-bold mb-10 mt-10">Reject Leave Request</h3>
    <div class="flex flex-wrap mb-4  gap-3">
      <div class="flex items-center mb-3 ml-5">
      <p class=" w-[6rem]"><strong>Employee:</strong></p>
      <p class="flex-auto">{{ getEmployeesName(rejectLeave.employee_id) }}</p>
    </div>
    <div class="flex items-center mb-3">
      <p class=" w-[6rem]"><strong>Leave Type:</strong></p>
      <p class="flex-auto">{{ getLeaveTypeName(rejectLeave.leave_type_id) }}</p>
    </div>
    <div class="flex items-center mb-3">
      <p class=" w-[6rem]"><strong>Start Date:</strong></p>
      <p class="flex-auto">{{ formatISODate(rejectLeave.start_date) }}</p>
    </div>
    <div class="flex items-center mb-3">
      <p class=" w-[6rem]"><strong>End Date:</strong></p>
      <p class="flex-auto">{{ formatISODate(rejectLeave.end_date) }}</p>
    </div>
    <div class="flex items-center mb-3">
      <p class=" w-[6rem]"><strong>Days:</strong></p>
      <p class="flex-auto">{{ rejectLeave.days }}</p>
    </div>
    </div>
    <textarea v-model="rejectedComment" class="w-full p-2 h-24 border rounded-md mb-4" placeholder="Enter rejection comment"></textarea>
    <div class="mt-4 flex gap-2 place-content-center">
      <button @click="rejectLeaveRequest" class="bg-red-500 text-white py-2 px-4 rounded-md hover:bg-red-600 mr-0">Reject</button>
      <button @click="closeRejectModal" class="bg-gray-500 text-white py-2 px-4 rounded-md hover:bg-gray-600">Cancel</button>
    </div>
  </div>
</div>


  </div>
</template>


<script>
import { api } from '@/api';
import { ref } from "vue";

import Dialog from 'primevue/dialog';

export default {
  data() {
    return {
      visible: false,
      pendingLeaves: [],
      loading: false,
      showRejectModal: false,
      rejectLeave: null,
      rejectedComment: '',
      leaveTypes: [],
      allEmployees: [],

      errors: {}
    };
  },
  created() {
    this.fetchPendingLeaves();
    this.fetchLeaveTypes();
    this.fetchEmployees();

  },
  methods: {
    async fetchPendingLeaves() {
      this.loading = true;
      try {
        const response = await api.get('/leaves/leave/pending');
        this.pendingLeaves = response.data;
      } catch (error) {
        alert('An error occurred while fetching pending leave requests');
      } finally {
        this.loading = false;
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
    getLeaveTypeName(id) {
      const type = this.leaveTypes.find(type => type.id === id);
      return type ? type.slug : 'Unknown';
    },
    async fetchEmployees() {
      try {
        const response = await api.get('/employees/');
        this.allEmployees = response.data;
      } catch (error) {
        alert('An error occurred while fetching employees types');
      }
    },
    getEmployeesName(id) {
      const name = this.allEmployees.find(name => name.id === id);
      return name ? name.name : 'Unknown';
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
        'bg-green-400 text-green-800 px-2 py-1 rounded-full': status === 'Approved',
        'bg-red-400 text-red-800 px-2 py-1 rounded-full': status === 'Rejected',
        'bg-blue-400 text-blue-800 px-2 py-1 rounded-full': status === 'Pending',
      };
    },
    async approveLeave(leave) {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leaves/leave/${leave.id}/status`, {
          ...leave,
          status: 'Approved',
          approved_by_id: userId,
          approved_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== leave.id);
        alert('Leave request has been approved successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, leave.id, error.response.data);
        } else {
          alert('An error occurred while approving the leave request');
        }
      }
    },
    openRejectModal(leave) {
      this.rejectLeave = leave;
      this.showRejectModal = true;
    },
    async rejectLeaveRequest() {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leaves/leave/${this.rejectLeave.id}/status`, {
          ...this.rejectLeave,
                    status: 'Rejected',
          rejected_by_id: userId,
          rejected_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
          rejected_comment: this.rejectedComment
        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== this.rejectLeave.id);
        this.closeRejectModal();
        alert('Leave request has been rejected successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, this.rejectLeave.id, error.response.data);
        } else {
          alert('An error occurred while rejecting the leave request');
        }
      }
    },
    closeRejectModal() {
      this.showRejectModal = false;
      this.rejectLeave = null;
      this.rejectedComment = '';
    }
  }
};
</script>

<style scoped>

thead th {
  height: 3rem; /* Adjust this value to increase/decrease header height */
}

th, td {
  width: 12.5%; /* Each column takes up 1/8 of the total width */
}
</style> -->

<template>
  <div class="container w-full mx-auto p-6">
    <h2 class="text-2xl font-bold mb-4">Pending Leave Requests</h2>
        <div class="mt-2 w-full flex justify-end">
          <router-link to="/Leaves/AllLeaves">
            <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">All Leaaves</button>
          </router-link>
        </div>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else>
      <div v-if="pendingLeaves && pendingLeaves.length === 0" class="text-center text-gray-600">No pending leave requests found.</div>
      <div v-else>
        <table class="m-6 table-auto w-full shadow-md mt-5 rounded border-separate border-spacing-y-2">
          <thead class="bg-sky-600">
            <tr>
              <th class="px-4 py-4 border-b w-1/8">Employee</th>
              <th class="px-4 py-4 border-b w-1/8">Leave Type</th>
              <th class="px-4 py-4 border-b w-1/8">Start Date</th>
              <th class="px-4 py-4 border-b w-1/8">End Date</th>
              <th class="px-4 py-4 border-b w-1/8">Days</th>
              <th class="px-4 py-4 border-b w-1/8">Status</th>
              <th class="px-4 py-4 border-b w-1/8">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="leave in pendingLeaves" :key="leave.id" class="hover:bg-gray-100">
              <td class="border px-4 py-2 w-1/8">{{ getEmployeesName(leave.employee_id) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ getLeaveTypeName(leave.leave_type_id) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ formatISODate(leave.start_date) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ formatISODate(leave.end_date) }}</td>
              <td class="border px-4 py-2 w-1/8">{{ leave.days }}</td>
              <td class="border px-4 py-2 w-1/8">
                <span :class="statusClass(leave.status)">
                  {{ leave.status }}
                </span>
              </td>
              <td class="border px-4 py-2 w-1/8">
                <div class="flex gap-2 items-center justify-center">
                  <button @click="approveLeave(leave)" class="bg-green-500 text-white py-1 px-3 rounded-md hover:bg-green-600">Approve</button>
                  <button @click="openRejectModal(leave)" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Reject Modal -->
    <div v-if="showRejectModal" class="fixed inset-0 z-50 bg-gray-500 bg-opacity-75 flex items-center justify-center">
      <div class="bg-white p-2 rounded-md shadow-md w-1/2 h-1/2 overflow-auto">
        <h3 class="text-3xl font-bold mb-10 mt-10">Reject Leave Request</h3>
        <div class="flex flex-wrap mb-4 gap-3">
          <div class="flex items-center mb-3 ml-5">
            <p class="w-[6rem]"><strong>Employee:</strong></p>
            <p class="flex-auto">{{ getEmployeesName(rejectLeave.employee_id) }}</p>
          </div>
          <div class="flex items-center mb-3">
            <p class="w-[6rem]"><strong>Leave Type:</strong></p>
            <p class="flex-auto">{{ getLeaveTypeName(rejectLeave.leave_type_id) }}</p>
          </div>
          <div class="flex items-center mb-3">
            <p class="w-[6rem]"><strong>Start Date:</strong></p>
            <p class="flex-auto">{{ formatISODate(rejectLeave.start_date) }}</p>
          </div>
          <div class="flex items-center mb-3">
            <p class="w-[6rem]"><strong>End Date:</strong></p>
            <p class="flex-auto">{{ formatISODate(rejectLeave.end_date) }}</p>
          </div>
          <div class="flex items-center mb-3">
            <p class="w-[6rem]"><strong>Days:</strong></p>
            <p class="flex-auto">{{ rejectLeave.days }}</p>
          </div>
        </div>
        <textarea v-model="rejectedComment" class="w-full p-2 h-24 border rounded-md mb-4" placeholder="Enter rejection comment"></textarea>
        <div class="mt-4 flex gap-2 place-content-center">
          <button @click="rejectLeaveRequest" class="bg-red-500 text-white py-2 px-4 rounded-md hover:bg-red-600 mr-0">Reject</button>
          <button @click="closeRejectModal" class="bg-gray-500 text-white py-2 px-4 rounded-md hover:bg-gray-600">Cancel</button>
        </div>
      </div>
    </div>

    <!-- Calendar Component -->
    <div class="z-0 ml-10 p-10 h-[1100px] is-light-mode calendar-container">
      <Qalendar 
        :events="events"
        :config="config"
      />
    </div>
  </div>
</template>

<script>
import { api } from '@/api';
import { ref } from "vue";
import { Qalendar } from "qalendar";

export default {
  components: {
    Qalendar,
  },
  data() {
    return {
      config: {
        week: {
          startsOn: 'monday', // Start the week on Monday
          nDays: 7,           // Show 7 days in a week view
          scrollToHour: 5,    // Scroll to 5 AM by default
        },
        style: {
          backgroundColor: "#F0F0F0", // Set background color for the calendar
          colorSchemes: {
            red: {
              backgroundColor: "#FF5733", // Example red color scheme
            },
            blue: {
              backgroundColor: "#337DFF", // Example blue color scheme
            },
            green: {
              backgroundColor: "#33FF57", // Example green color scheme
            },
            yellow: {
              backgroundColor: "#FFFF33", // Example yellow color scheme
            },
            orange: {
              backgroundColor: "#FFA533", // Example orange color scheme
            },
            purple: {
              backgroundColor: "#9333FF", // Example purple color scheme
            },
          },
        },
        dayStyle: {
          // Customize styles for individual days
          isWeekend: {
            backgroundColor: "#FF5733", // Red color for weekends
          },
          isToday: {
            backgroundColor: "#337DFF", // Blue color for today
          },
          // Customize weekdays color
          isWeekday: {
            backgroundColor: "#33FF57", // Green color for weekdays
          },
        },
        defaultMode: 'month',

      },
      pendingLeaves: [],
      loading: false,
      showRejectModal: false,
      rejectLeave: null,
      rejectedComment: '',
      leaveTypes: [],
      allEmployees: [],
      events: [], // Array to hold calendar events
      errors: {}
    };
  },
  created() {
    this.fetchPendingLeaves();
    this.fetchLeaveTypes();
    this.fetchEmployees();
    this.fetchApprovedLeaves(); // Fetch approved leaves when component is created
  },
  methods: {
    async fetchPendingLeaves() {
      this.loading = true;
      try {
        const response = await api.get('/leaves/leave/pending');
        this.pendingLeaves = response.data;
      } catch (error) {
        alert('An error occurred while fetching pending leave requests');
      } finally {
        this.loading = false;
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
    async fetchEmployees() {
      try {
        const response = await api.get('/employees/');
        this.allEmployees = response.data;
      } catch (error) {
        alert('An error occurred while fetching employees types');
      }
    },
    getEmployeesName(id) {
      const name = this.allEmployees.find(emp => emp.id === id);
      return name ? name.name : 'Unknown';
    },
    getLeaveTypeName(id) {
      const type = this.leaveTypes.find(type => type.id === id);
      return type ? type.slug : 'Unknown';
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
        'bg-green-400 text-green-800 px-2 py-1 rounded-full': status === 'Approved',
        'bg-red-400 text-red-800 px-2 py-1 rounded-full': status === 'Rejected',
        'bg-blue-400 text-blue-800 px-2 py-1 rounded-full': status === 'Pending',
      };
    },
    async approveLeave(leave) {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leaves/leave/${leave.id}/status`, {
          ...leave,
          status: 'Approved',
          approved_by_id: userId,
          approved_at: new Date().toISOString(),
          updated_at: new Date().toISOString()
        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== leave.id);
        this.addEventToCalendar(leave); // Add approved leave to calendar
        alert('Leave request has been approved successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, leave.id, error.response.data);
        } else {
          alert('An error occurred while approving the leave request');
        }
      }
    },
    async fetchApprovedLeaves() {
      this.loading = true;
      try {
        const response = await api.get('/leaves/active_leaves/aproved');
        this.approvedLeaves = response.data;
        console.log(this.approvedLeaves)
        this.updateApprovedEvents();
      } catch (error) {
        alert('An error occurred while fetching approved leaves');
      } finally {
        this.loading = false;
      }
    },
    updateApprovedEvents() {
      this.events = this.approvedLeaves.map((leave, index) => ({
        id: leave.id,
        title: `${this.getEmployeesName(leave.employee_id)} in leave`,
        time: {
          start:this.formatISODate(leave.start_date),
          end: this.formatISODate(leave.end_date),
        },
        with: this.getEmployeesName(leave.employee_id),
        colorSchemes: 'red',
        color: this.getEventColor(index),
      }));
      console.log('Fetched events:', this.events);

    },
    getEventColor(index) {
        // Example function to return different colors based on index or event properties
        const colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple','rgb(101 163 13)']; // Define your color palette
        return colors[index % colors.length]; // Cycle through colors based on index
      },
    openRejectModal(leave) {
      this.rejectLeave = leave;
      this.showRejectModal = true;
    },
    async rejectLeaveRequest() {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leaves/leave/${this.rejectLeave.id}/status`, {
          ...this.rejectLeave,
          status: 'Rejected',
          rejected_by_id: userId,
          rejected_at: new Date().toISOString(),
          updated_at: new Date().toISOString(),
          rejected_comment: this.rejectedComment
        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== this.rejectLeave.id);
        this.closeRejectModal();
        alert('Leave request has been rejected successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, this.rejectLeave.id, error.response.data);
        } else {
          alert('An error occurred while rejecting the leave request');
        }
      }
    },
    closeRejectModal() {
      this.showRejectModal = false;
      this.rejectLeave = null;
      this.rejectedComment = '';
    }
  }
};
</script>

<style>
@import "qalendar/dist/style.css";

.calendar-container {
  background-color:rgb(243, 244, 246) !important;
  margin-left: 50px;
  /* border-color: black; Set background color for the entire calendar */
}
/* .calendar-month .calendar-month__week-day-names, */
/* .calendar-month__day-date, */
.calendar-month__weekday:nth-child(6),
.calendar-month__weekday:nth-child(7){
  background-color: #ffffffb6;
  color: #FF5733 ;
  
}
/* .calendar-month__day-date, */
.calendar-month__day-name:nth-child(6),
.calendar-month__day-name:nth-child(7) {
  color: #FF5733 !important; /* Red color for Saturday (6th day in a week starting from Monday) */
}
/* class="calendar-month__day-name calendar-month__week-day-name" */
.calendar-month__weekday:nth-child(6) .calendar-month__day-date { /* Saturday */
    color: #FF5733; /* Red text color for Saturdays */
}

.calendar-month__weekday:nth-child(7) .calendar-month__day-date { /* Sunday */
    color: #FF5733; /* Red text color for Sundays */
}


/* .calendar-week__day:nth-child(6),

.calendar-week__day:nth-child(5), */
/* .week-timeline__day-name:nth-child(6) .week-timeline__day-name, */
.week-timeline__day:nth-child(6),
.week-timeline__day:nth-child(7){
  /* background-color: #ffffff; */
  color: #FF5733 ;
}
/* .week-timeline,
.calendar-root-wrapper .calendar-root, 
.week-timeline {
  border-color: black !important;
}
.day-timeline:not(:last-child),
.calendar-week__day:not(:last-child) {
    border-right: 1px dashed rgb(2, 2, 2) !important;

}
.day-timeline:not(:last-child) {
    border-right: 1px dashed rgb(2, 2, 2) !important;
    border-top: 1px dashed rgb(2, 2, 2) !important;

} */



</style>