<script setup>
import Sidebar from '../../components/Sidebar.vue'
import Navbar from '../../components/Navbar.vue';
import { ref, onMounted, watch } from 'vue';
import { api } from '@/api';
import { useRouter } from 'vue-router';

const router = useRouter();

const department = ref({
  name: '',
  slug: '',

});
const backToIndex = () => {
    router.push({ name: 'Departments' });
  };


// const createDepartment = () => {

//   api.post('/departments/create_department', department.value)
//     .then(response => {
//       console.log('Department created successfully:', response.data);
//       router.push('/departments');
//     })
//     .catch(error => {
//       console.error('There was a problem creating the user:', error);
//     });
// };

const createDepartment = async () => {
        try {
        await api.post('/departments/create_department', department.value)
        router.push('/departments'); // Redirect to departments list after editing
        console.log('Department created successfully:', response.data);

        } catch (error) {
            console.error('There was a problem creating the user:', error);
        }
    };
</script>

<template>
<Navbar/>
<Sidebar />
<!-- <div class="mt-14 p-4 sm:ml-64 text-black">

<div class="flex justify-between items-center mb-4 mt-5">
            <h2 class="mt-10 text-2xl font-bold">Create Department</h2>
            <button @click="backToIndex" class=" mt-10 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
      </div>
<form class="mt-10  sm:ml-64" @submit.prevent="createDepartment"> 
    <div class="grid gap-6 mb-6 md:grid-cols-2">
        <div>
            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>
            <input type="text" id="name" v-model="department.name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required />
        </div>
        <div>
            <label for="slug" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>
            <input type="text" id="slug"v-model="department.slug" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required />
        </div>
    </div>
    <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
</form>
</div> -->
<main class="flex-1 p-8 sm:ml-64">
        <div class="mt-10 p-12 text-black">
            <div class="flex justify-between items-center mb-4">
                    <h2 class="text-2xl font-bold">Create Department</h2>
                    <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
            </div>
            <form @submit.prevent="createDepartment" class="space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center sm:space-x-4">                
                    <div class="flex-1">
                        <label for="name" class="block mb-2  text-sm font-medium text-black dark:text-black">Name:</label>
                        <input type="text" id="name" v-model="department.name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    </div>
                    <div class="flex-1">
                        <label for="slug" class="block mb-2 text-sm font-medium text-black dark:text-black">Description:</label>
                        <textarea id="slug" v-model="department.slug" class="bg-gray-50  border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
                    </div>
                    <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Create</button>
                </div>
            </form>
        </div>
    </main>
</template>