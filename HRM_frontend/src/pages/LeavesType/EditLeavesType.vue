<template>
    <Navbar/>
    <Sidebar />
    <main class="flex-1 p-8 sm:ml-64">
        <div class="mt-10 p-12 text-black">
            <div class="flex justify-between items-center mb-4">
                    <h2 class="text-2xl font-bold">Edit LeaveType</h2>
                    <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
            </div>
            <form @submit.prevent="submitForm" class="space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center sm:space-x-4">                

                    <div class="flex-1">
                        <label for="slug" class="block mb-2 text-sm font-medium text-black dark:text-black">Description:</label>
                        <textarea id="slug" v-model="editedLeaveType.slug" class="bg-gray-50  border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
                    </div>
                    <div class="flex-1">
                        <label for="limit" class="block mb-2  text-sm font-medium text-black dark:text-black">limit:</label>
                        <input type="text" id="limit" v-model="editedLeaveType.limit" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    </div>
                    <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Save Changes</button>
                </div>
            </form>
        </div>
    </main>
</template>
  
  <script setup>
  import { toast } from 'vue3-toastify';

    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { api } from '@/api';
    import Sidebar from '../../components/Sidebar.vue'
    import Navbar from '../../components/Navbar.vue';
    
    const router = useRouter();
    const editedLeaveType = ref({});
    const leaveTypeId = router.currentRoute.value.params.id;

    const backToIndex = () => {
    router.push({ name: 'LeaveTypes' });
  };
  const getCurrentDateTime = () => {
        const now = new Date();
        return now.toISOString();
    };

    onMounted(async () => {
        try {
        const response = await api.get(`/leaveType/${leaveTypeId}`);
        editedLeaveType.value = response.data;
        console.log(response.data);
        } catch (error) {
        console.error('Error fetching leaveType:', error);
        }
    });
    
    const submitForm = async () => {
        try {
        editedLeaveType.value.updated_at = getCurrentDateTime(); 
        editedLeaveType.value.deleted_at = getCurrentDateTime(); 

        await api.put(`/leaveType/update_leaveType/${leaveTypeId}`, editedLeaveType.value);
        router.push('/leaveTypes'); 
        // router.emit('leaveTypeUpdated', editedleaveType.value);
        toast("Leave type edited successfully!", {
     autoClose: 3000,
      position: toast.POSITION.TOP_RIGHT,
    });
        } catch (error) {
        console.error('Error editing department:', error);
        }
    };
  </script>
  