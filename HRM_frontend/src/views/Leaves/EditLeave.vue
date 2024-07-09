
<template>
    <div class="max-w-2xl mx-auto p-4">
      <h2 class="text-2xl font-bold mb-4">Pending Leave Requests</h2>
      <div v-if="loading" class="text-center">Loading...</div>
      <div v-else>
        <div v-if="pendingLeaves && pendingLeaves.length === 0" class="text-center text-gray-600">No pending leave requests found.</div>
        <div v-for="leave in pendingLeaves" :key="leave.id" class="mb-4 p-4 border rounded-md shadow-sm">
          <p><strong>Employee ID:</strong> {{ leave.employee_id }}</p>
          <p><strong>Leave Type ID:</strong> {{ leave.leave_type_id }}</p>
          <p><strong>Start Date:</strong> {{ leave.start_date }}</p>
          <p><strong>End Date:</strong> {{ leave.end_date }}</p>
          <p><strong>Days:</strong> {{ leave.days }}</p>
          <p><strong>User ID:</strong> {{ leave.user_id }}</p>
          <p><strong>Status:</strong> {{ leave.status }}</p>
          <div class="mt-2 flex gap-2">
            <button @click="approveLeave(leave)" class="bg-green-500 text-white py-1 px-3 rounded-md hover:bg-green-600">Approve</button>
            <button @click="openRejectModal(leave)" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
          </div>
        </div>
      </div>
  
      <!-- Reject Modal -->
      <div v-if="showRejectModal" class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
        <div class="bg-white p-4 rounded-md shadow-md">
          <h3 class="text-xl font-bold mb-2">Reject Leave Request</h3>
          <p><strong>Employee ID:</strong> {{ rejectLeave.employee_id }}</p>
          <p><strong>Leave Type ID:</strong> {{ rejectLeave.leave_type_id }}</p>
          <p><strong>Start Date:</strong> {{ rejectLeave.start_date }}</p>
          <p><strong>End Date:</strong> {{ rejectLeave.end_date }}</p>
          <p><strong>Days:</strong> {{ rejectLeave.days }}</p>
          <textarea v-model="rejectedComment" class="w-full p-2 border rounded-md" placeholder="Enter rejection comment"></textarea>
          <div class="mt-4 flex gap-2">
            <button @click="rejectLeaveRequest" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
            <button @click="closeRejectModal" class="bg-gray-500 text-white py-1 px-3 rounded-md hover:bg-gray-600">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  <script>
  import { api } from '@/api';
  
  export default {
    data() {
      return {
        pendingLeaves: [],
        loading: false,
        showRejectModal: false,
        rejectLeave: null,
        rejectedComment: '',
        errors: {}
      };
    },
    created() {
      this.fetchPendingLeaves();
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
  /* Add any scoped styles if necessary */
  </style>
  