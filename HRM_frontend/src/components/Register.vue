<script setup>
import { ref, onMounted, watch } from 'vue';
import { api } from '@/api';

const user = ref({
  name: '',
  username: '',
  email: '',
  password: '',
  password_confirmation: '',
  active: true,
  language: '',
  banned_until: null // Initialize banned_until as null
});

const users = ref([]);

const getAllUsers = () => {
  api.get('/user/')
    .then(response => {
      console.log('All users:', response.data);
      users.value = response.data;
    })
    .catch(error => {
      console.error('There was a problem fetching users:', error);
    });
};

const createUser = () => {
  user.value.email_verified_at = getCurrentDateTime();

  api.post('/user/create_user', user.value)
    .then(response => {
      console.log('User created successfully:', response.data);
    })
    .catch(error => {
      console.error('There was a problem creating the user:', error);
    });
};

const getCurrentDateTime = () => {
  const now = new Date();
  return now.toISOString();
};

onMounted(getAllUsers);

// Watch for changes in banned_until date
watch(() => user.value.banned_until, (newValue) => {
  if (newValue && new Date(newValue) < new Date()) {
    user.value.active = true; // Set active to true if banned_until date has passed
  }
});
</script>



<template>
    <section class="bg-gray-50 dark:bg-gray-900">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
                <img class="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo">
                Flowbite    
            </a>
            <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                        Create an account
                    </h1>
                    <form class="space-y-4 md:space-y-6" @submit.prevent="createUser">
                        <div>
                            <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                            <input type="text" name="name" id="name"v-model="user.name" required class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Name LastName">
                        </div>
                        <div>
                            <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Username</label>
                            <input type="text" id="username" v-model="user.username" required class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="username" >
                        </div>
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                            <input type="email" id="email" v-model="user.email" required class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" >
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input type="password" name="password" id="password" v-model="user.password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                        </div>
                        <div>
                            <label for="confirm-password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>
                            <input type="confirm-password" id="password_confirmation" v-model="user.password_confirmation" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                        </div>
                        <div class="flex items-start">
                            <div class="mr-3 text-sm">
                                <label for="active" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Active</label>
                            </div>
                            <div class="flex items-center h-5">
                              <input id="active" aria-describedby="active" v-model="user.active" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" >
                            </div>

                        </div>
                        <!-- <div>
                            <label for="active" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Active</label>
                            <input type="checkbox" id="active" v-model="user.active" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" >
                        </div> -->
                        <div>
                            <label for="language" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Language</label>
                            <input type="text" id="language" v-model="user.language" required class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" >
                        </div>
                        <input type="hidden" id="email_verified_at" ref="emailConfirmation">
                        <input type="hidden" id="banned_until" ref="bannedUntil">

                        <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Create</button>
                        <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                            Already have an account? <a href="#" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
      </section>
    </template>
<!-- <template>
    <div>
      <h2>Create User</h2>
      <form @submit.prevent="createUser">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="user.name" required>
        </div>
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="user.username" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="user.email" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="user.password" required>
        </div>
        <div>
          <label for="password_confirmation">Confirm Password:</label>
          <input type="password" id="password_confirmation" v-model="user.password_confirmation" required>
        </div>
        <div>
          <label for="active">Active:</label>
          <input type="checkbox" id="active" v-model="user.active">
        </div>
        <input type="hidden" id="email_verified_at" ref="emailConfirmation">
        <input type="hidden" id="banned_until" ref="bannedUntil">
         <div>
  <label for="user_id">User ID:</label>
  <input type="text" id="user_id" v-model="user.user_id">
</div> 
    
            <div>
          <label for="language">Language:</label>
          <input type="text" id="language" v-model="user.language">
        </div>
        <button type="submit">Create</button>
      </form>
    </div>
    <button type="submit" >Createall</button>
  </template> -->

<!-- <template>
    <div>
      <h2>Create User</h2>
      <form @submit.prevent="createUser">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="user.name" required>
        </div>
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="user.username" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="user.email" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="user.password" required>
        </div>
        <div>
          <label for="password_confirmation">Confirm Password:</label>
          <input type="password" id="password_confirmation" v-model="user.password_confirmation" required>
        </div>
        <div>
          <label for="active">Active:</label>
          <input type="checkbox" id="active" v-model="user.active">
        </div>
        <input type="hidden" id="email_verified_at" ref="emailConfirmation">
        <input type="hidden" id="banned_until" ref="bannedUntil">
         <div>
  <label for="user_id">User ID:</label>
  <input type="text" id="user_id" v-model="user.user_id">
</div> 
    
            <div>
          <label for="language">Language:</label>
          <input type="text" id="language" v-model="user.language">
        </div>
        <button type="submit">Create</button>
      </form>
    </div>
    <button type="submit" >Createall</button>
  </template>
  
  <script>
import axios from 'axios'; // Import Axios
import { api } from '@/api'; 
export default {
  data() {
    return {
      user: {
        name: '',
        username: '',
        email: '',
        password: '',
        password_confirmation: '',
        active: true,
        language: '',
        // user_id: 8 
      },
      users:[]
    };
  },
  methods: {

    getAllUsers() {
        
      // Use your custom Axios instance (api) to make the request
      api.get('/user/') // Assuming '/' is your endpoint to fetch all users
        .then(response => {
          console.log('All users:', response.data);
          this.users = response.data; // Update the users array with fetched data
        })
        .catch(error => {
          console.error('There was a problem fetching users:', error);
          // Optionally, display an error message to the user
        });
    },

    createUser() {
        
      // Set email_confirmation and banned_until to the current date and time
      this.user.email_verified_at = this.getCurrentDateTime();
      this.user.banned_until = this.getCurrentDateTime();
    //   this.user.user_id=this.user_id
      // Use your custom Axios instance (api) to make the request
      api.post('/user/create_user', this.user) // Assuming '/create_user' is your endpoint
        .then(response => {
          console.log('User created successfully:', response.data);
          // Optionally, perform any additional actions here
        })
        .catch(error => {
          console.error('There was a problem creating the user:', error);
          // Optionally, display an error message to the user
        });
    },
    getCurrentDateTime() {
      // Function to get the current date and time in a suitable format
      const now = new Date();
      return now.toISOString(); // Adjust format as per your requirement
    }
  },
  mounted() {
    // Fetch all users when the component is mounted
    this.getAllUsers();
  }
};
</script>

<style>
/* Add your component-specific styles here */
</style> -->
