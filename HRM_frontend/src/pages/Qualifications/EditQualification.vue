<template>
    <Navbar/>
    <Sidebar />
    <main class="flex-1 p-8 sm:ml-64">
        <div class="mt-10 p-12 text-black">
            <div class="flex justify-between items-center mb-4">
                    <h2 class="text-2xl font-bold">Edit Qualification</h2>
                    <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
            </div>
            <form @submit.prevent="submitForm" class="space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center sm:space-x-4">                
                    <div class="flex-1">
                        <label for="name" class="block mb-2  text-sm font-medium text-black dark:text-black">Name:</label>
                        <input type="text" id="name" v-model="editedQualification.name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    </div>
                    <div class="flex-1">
                        <label for="slug" class="block mb-2 text-sm font-medium text-black dark:text-black">Description:</label>
                        <textarea id="slug" v-model="editedQualification.slug" class="bg-gray-50  border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
                    </div>
                    <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Save Changes</button>
                </div>
            </form>
        </div>
    </main>
</template>
  
  <script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { api } from '@/api';
    import Sidebar from '../../components/Sidebar.vue'
    import Navbar from '../../components/Navbar.vue';
    
    const router = useRouter();
    const editedQualification = ref({});
    const qualificationId = router.currentRoute.value.params.id;
    
    const backToIndex = () => {
    router.push({ name: 'Qualifications' });
  };

    onMounted(async () => {
        try {
        const response = await api.get(`/qualification/${qualificationId}`);
        editedQualification.value = response.data;
        console.log(response.data);
        } catch (error) {
        console.error('Error fetching qualification:', error);
        }
    });
    
    const submitForm = async () => {
        try {
        await api.put(`/qualification/update_qualifications/${qualificationId}`, editedQualification.value);
        router.push('/qualifications'); // Redirect to qualifications list after editing
        // router.emit('qualificationUpdated', editedQualification.value);

        } catch (error) {
        console.error('Error editing qualification:', error);
        }
    };
  </script>
  