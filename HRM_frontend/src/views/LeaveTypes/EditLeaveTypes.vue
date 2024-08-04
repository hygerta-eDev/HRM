
<template>
    <div class="container mx-auto p-6">
      <div class="edit-leaveType p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
  
      <h1 class="text-2xl font-bold mb-6">Edit leaveType</h1>
      <div v-if="leaveType" class="leaveType-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">leaveType Name</label>
          <input v-model="leaveType.slug" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="leaveType.limit" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="updateleaveType" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/LeaveTypes`">
            <button @click="cancelEdit" class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="loading">
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
  import InputSwitch from 'primevue/inputswitch';

  
  const route = useRoute();
  const router = useRouter();
  const leaveType = ref(null);

  
  const getleaveType = () => {
    const leaveTypeId = Number(route.params.id);
    api.get(`/leaveType/${leaveTypeId}`)
      .then(response => {
        leaveType.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching leaveType:', error);
      });
  };
  
  const updateleaveType = () => {
  if (leaveType.value) {
    api.put(`/leaveType/update_leaveType/${leaveType.value.id}`, leaveType.value)
      .then(response => {
        console.log('leaveType updated successfully:', response.data);
        router.push('/LeaveTypes');  
        setTimeout(() => {
          toast.success("leaveType edited successfully!", {
            autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });   
        }, 250);

      })
      .catch(error => {
        console.error('Error updating leaveType:', error);
      });
  }
};

  const cancelEdit = () => {
    // Redirect back to leaveType list or view page
  };
  
  onMounted(getleaveType);
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  