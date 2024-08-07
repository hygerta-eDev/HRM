<template>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->
    <div class="relative mb-6">
      <nav class="flex items-center text-sm text-gray-700">
        <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-home text-lg mr-2"></i> <!-- Home icon -->
          Home
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-user-cog text-lg mr-2"></i> <!-- Administrator icon -->
          Administrator
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/LeaveTypes" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-clipboard-list text-lg mr-2"></i> <!-- LeaveTypes icon -->
          Leave Types
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">Edit Leave Type</span>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="p-10 shadow-lg rounded-lg border border-blue-500 bg-white relative mt-12">
      <div v-if="leaveType" class="absolute inset-x-0 -top-10 flex justify-center">
        <h1 class="text-4xl font-bold text-gray-800 bg-white px-6 py-4 relative z-10">
        Edit {{leaveType.slug}}
        </h1>
      </div>
      <div v-if="leaveType" class="pt-16 px-8 pb-8">
        <div class="flex flex-col md:flex-row gap-6">
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Leave Type Name</label>
            <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-clipboard"></i>
            <input v-model="leaveType.slug" type="text" class="pl-10 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm"> 
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Limit</label>
            <i class="absolute left-3 top-1/2 mt-3 transform -translate-y-1/2 text-gray-500 fas fa-sliders-h"></i>
            <input v-model="leaveType.limit" type="number" class="w-full pl-10 px-3 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <button @click="updateLeaveType" class="bg-blue-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-600 transition duration-300">Save</button>
          <router-link to="/LeaveTypes">
            <button @click="cancelEdit" class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-gray-600 transition duration-300">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>Loading...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';

const route = useRoute();
const router = useRouter();
const leaveType = ref(null);

const getLeaveType = () => {
  const leaveTypeId = Number(route.params.id);
  api.get(`/leaveType/${leaveTypeId}`)
    .then(response => {
      leaveType.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Leave Type:', error);
    });
};

const updateLeaveType = () => {
  if (leaveType.value) {
    api.put(`/leaveType/update_leaveType/${leaveType.value.id}`, leaveType.value)
      .then(response => {
        console.log('Leave Type updated successfully:', response.data);
        router.push('/LeaveTypes');
        setTimeout(() => {
          toast.success("Leave Type edited successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }, 250);
      })
      .catch(error => {
        console.error('Error updating Leave Type:', error);
      });
  }
};

const cancelEdit = () => {
  router.push('/LeaveTypes');
};

onMounted(getLeaveType);
</script>

<style scoped>
.loading {
  text-align: center;
  margin-top: 20px;
  font-style: italic;
  color: #666;
}
</style>
