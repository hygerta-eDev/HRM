<template>
    <div class="create-training-container flex justify-center items-center mt-10">
      <div class="create-training p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 w-full md:w-3/4">
        <h1 class="text-2xl font-bold mb-6">{{ $t('create_new_training') }}</h1>
        <div class="training-details flex flex-wrap">
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('training_title') }}</label>
            <input v-model="newTraining.title" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('start_date') }}</label>
            <VueDatePicker :placeholder="$t('select_a_date')" v-model="newTraining.start_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">Select a date</VueDatePicker>
          </div>
          <div class="w-full md:w-1/2 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('end_date') }}</label>
            <VueDatePicker  :placeholder="$t('select_a_date')" v-model="newTraining.end_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
          </div>
          <input v-model="newTraining.completed_at" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" hidden>
          <div class="w-full h-36 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">{{ $t('description') }}</label>
            <textarea v-model="newTraining.description" class="w-full h-24 px-3 py-2 border border-blue-500 rounded-md shadow-md"></textarea>
          </div>
          <div class="w-full text-right mt-4 px-2">
            <button @click="validateAndCreateTraining" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">{{ $t('create') }}</button>
            <router-link :to="`/Trainings`">
              <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">{{ $t('cancel') }}</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref,watch } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'
  const router = useRouter();
  const newTraining = ref({
    title: '',
    start_date: '',
    end_date: '',
    description: '',
    user_id: 1,
    active: true,
    completed_at: null,
    created_at: new Date().toISOString(),
  });

  watch(
      () => [newTraining.value.title, newTraining.value.description],
      ([newTitle, newDescription]) => {
        if (newTitle) {
          newTraining.value.title = newTitle.charAt(0).toUpperCase() + newTitle.slice(1);
        }
        if (newDescription) {
          newTraining.value.description = newDescription.charAt(0).toUpperCase() + newDescription.slice(1);
        }
      }
    );

  const validateAndCreateTraining = () => {
    if (!newTraining.value.title || !newTraining.value.start_date || !newTraining.value.end_date || !newTraining.value.description) {
      toast.error(this.$t('fill_required_fields'), {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
      return;
    }
  
    newTraining.value.active = !newTraining.value.completed_at;
  
    api.post('/training/create_training', newTraining.value)
      .then(response => {
        console.log('Training created successfully:', response.data);
  
        router.push('/Trainings');
        setTimeout(() => {
          toast.success(this.$t('training_created_successfully'), {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }, 250);
      })
      .catch(error => {
        console.error('Error creating Training:', error);
        toast.error(this.$t('failed_to_create_training'), {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };
  </script>
  
  <style scoped>
  .create-training {
    margin-top: 20px;
  }

  </style>
  