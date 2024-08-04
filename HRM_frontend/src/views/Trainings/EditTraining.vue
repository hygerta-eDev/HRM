<template>
    <div class="container mx-auto p-6">
      <div v-if="Training" class="edit-Training p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">Edit Training</h1>
        <div class="Training-details flex flex-wrap">
          <div class="w-full  mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Training Title</label>
            <input v-model="Training.title" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
            <VueDatePicker  :placeholder="$t('select_a_date')" v-model="Training.start_date" type="date" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md"></VueDatePicker>
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
            <VueDatePicker  :placeholder="$t('select_a_date')" v-model="Training.end_date" type="date" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md"></VueDatePicker>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Description</label>
            <textarea v-model="Training.description" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md"></textarea>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Outcome</label>
            <input v-model="Training.outcome" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md">
          </div>
          <div class="w-full flex">
            <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Completed At</label>
            <VueDatePicker   :placeholder="$t('select_a_date')" v-model="Training.completed_at" type="date" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow-md"></VueDatePicker>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
            <div class="flex items-center mt-3 ml-48">
              <InputSwitch v-model="Training.active" disabled />
            </div>
          </div>

          </div>
          <div class="w-full text-right mt-4 px-2">
            <button @click="updateTraining" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Save</button>
            <router-link :to="`/Trainings`">
              <button @click="cancelEdit" class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
            </router-link>
          </div>
        </div>
      </div>
      <div v-else class="loading">
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  import InputSwitch from 'primevue/inputswitch';
  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'
  const route = useRoute();
  const router = useRouter();
  const Training = ref(null);
  
  const getTraining = () => {
    const TrainingId = Number(route.params.id);
    api.get(`/training/${TrainingId}`)
      .then(response => {
        Training.value = response.data;
        // Convert dates to ISO string for input fields
        Training.value.start_date = new Date(Training.value.start_date).toISOString().split('T')[0];
        Training.value.end_date = new Date(Training.value.end_date).toISOString().split('T')[0];
        Training.value.completed_at = Training.value.completed_at ? new Date(Training.value.completed_at).toISOString().split('T')[0] : null;
      })
      .catch(error => {
        console.error('Error fetching Training:', error);
      });
  };
  
  const updateTraining = () => {
    if (Training.value) {
      // Determine active status based on completed_at field
      Training.value.active = !Training.value.completed_at;
  
      api.put(`/training/update_trainings/${Training.value.id}`, Training.value)
        .then(response => {
          console.log('Training updated successfully:', response.data);
          router.push('/Trainings');
          setTimeout(() => {
            toast.success("Training edited successfully!", {
              autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });
          }, 250);
        })
        .catch(error => {
          console.error('Error updating Training:', error);
          toast.error("Failed to update Training!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        });
    }
  };
  
  const cancelEdit = () => {
    router.push('/Trainings'); // Redirect back to Training list or view page
  };
  
  onMounted(getTraining);
  
  // Watch for changes to completed_at and update active status accordingly
  watch(() => Training.value ? Training.value.completed_at : null, (newVal) => {
    if (Training.value) {
      if (newVal) {
        Training.value.active = false;
      } else {
        Training.value.active = true;
      }
    }
  });
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  