<template>
    <div class="container mx-auto p-6">
      <div class="create-Training p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
        <h1 class="text-2xl font-bold mb-6">Create New Training</h1>
        <div class="Training-details flex flex-wrap">
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Training Title</label>
            <input v-model="newTraining.title" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
            <input v-model="newTraining.start_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
            <input v-model="newTraining.end_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Description</label>
            <textarea v-model="newTraining.description" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></textarea>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Outcome</label>
            <input v-model="newTraining.outcome" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Active</label>
            <div class="flex items-center mt-3 ml-48">
              <InputSwitch v-model="newTraining.active" />
            </div>
          </div>
          <div class="w-full text-right mt-4 px-2">
            <button @click="validateAndCreateTraining" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
            <router-link :to="`/Trainings`">
              <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import InputSwitch from 'primevue/inputswitch';
  import { toast } from 'vue3-toastify';
  
  const router = useRouter();
  const newTraining = ref({
    title: '',
    start_date: '',
    end_date: '',
    description: '',
    outcome: '',
    user_id: 1,
    active: true,
    completed_at: new Date().toISOString(), // Set to current timestamp
    created_at: new Date().toISOString(), // Set to current timestamp
  });
  
  const validateAndCreateTraining = () => {
    if (!newTraining.value.title || !newTraining.value.start_date || !newTraining.value.end_date || !newTraining.value.description || !newTraining.value.outcome) {
      toast.error("Please fill in all required fields.", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
      return;
    }
  
    api.post('/training/create_training', newTraining.value)
      .then(response => {
        console.log('Training created successfully:', response.data);
  
        router.push('/Trainings');
        setTimeout(() => {
          toast.success("Training created successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }, 250);
      })
      .catch(error => {
        console.error('Error creating Training:', error);
        toast.error("Failed to create Training!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };
  </script>
  
  <style scoped>
  .create-Training {
    margin-top: 20px;
  }
  </style>
  