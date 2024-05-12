<script setup>
import { toast } from 'vue3-toastify';
import { ref } from 'vue';
import { api } from '@/api';
import { useRouter } from 'vue-router';
import Sidebar from '../../components/Sidebar.vue';
import Navbar from '../../components/Navbar.vue';

const router = useRouter();

const leaveType = ref({
  slug: '',
  limit: ''
});

const backToIndex = () => {
  router.push({ name: 'LeaveTypes' });
};

const getCurrentDateTime = () => {
  const now = new Date();
  return now.toISOString();
};

const createLeaveType = async () => {
  try {
    leaveType.value.created_at = getCurrentDateTime();
    await api.post('/leaveType/create_leaveType', leaveType.value);
 // Redirect to leave types list after creation
    router.push('/leaveTypes');

    toast("Leave type created successfully!", {
     autoClose: 3000,
      position: toast.POSITION.TOP_RIGHT,
    });
  } catch (error) {
    console.error('There was a problem creating the leave type:', error);
  }
};
</script>

<template>
<Navbar/>
<Sidebar />
<main class="flex-1 p-8 sm:ml-64">
        <div class="mt-10 p-12 text-black">
            <div class="flex justify-between items-center mb-4">
                    <h2 class="text-2xl font-bold">Create leaveType</h2>
                    <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
            </div>
            <form @submit.prevent="createLeaveType" class="space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center sm:space-x-4">                
                    <div class="flex-1">
                        <label for="name" class="block mb-2  text-sm font-medium text-black dark:text-black">Name:</label>
                        <input type="slug" id="slug" v-model="leaveType.slug" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    </div>
                    <div class="flex-1">
                        <label for="limit" class="block mb-2 text-sm font-medium text-black dark:text-black">Days:</label>
                        <textarea id="limit" v-model="leaveType.limit" class="bg-gray-50  border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
                    </div>
                    <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Create</button>
                </div>
            </form>
        </div>
    </main>
</template>