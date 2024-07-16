<template>
    <div>
      <div class="p-10">
        <div class="container mx-auto" :class="{ 'blurred': deleteDialogVisible }">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-3xl font-semibold">{{ $t('trainings') }}</h2>
            <router-link to="/Trainings/Newtraining">
              <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">{{ $t('new_training') }}</button>
            </router-link>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full border-collapse border border-gray-300 rounded-lg">
              <thead>
                <tr class="bg-sky-600 text-white">
                  <th class="px-4 py-4 text-left text-base border-r border-black-900">{{ $t('no') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('title') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('end_date') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('outcome') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('completed_at') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('description') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('start_date') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('active') }}</th>
                  <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('actions') }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(training, index) in Trainings" :key="training.id"
                    :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
                    class="border-b border-gray-300 hover:bg-blue-100">
                  <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ index + 1 }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ training.title }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ formatDate(training.end_date) }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ training.outcome }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ formatDate(training.completed_at) }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ training.description }}</td>
                  <td class="px-4 py-4 text-left text-base">{{ formatDate(training.start_date) }}</td>
  
                  <td class="px-4 py-4 text-left">
                    <span v-if="training.active" class="text-green-500">
                      <i class="fas fa-check-circle fa-lg"></i>
                    </span>
                    <span v-else class="text-red-500">
                      <i class="fas fa-times-circle fa-lg"></i>
                    </span>
                  </td>
                  <td class="px-4 py-4 actions text-left">
                    <router-link :to="`/Trainings/${training.id}`">
                      <i @click="viewTraining(training.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                    </router-link>
                    <router-link :to="`/Trainings/Edit/${training.id}`">
                      <i @click="editTraining(training.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                    </router-link>
                    <i @click="confirmDelete(training.id, training.title)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
                  </td>
                </tr>
              </tbody>
            </table>
            <!-- <Paginator :totalRecords="totalRecords" :rows="rowsPerPage" @onPageChange="onPageChange"></Paginator> -->
          </div>
        </div>
  
        <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete_training') }} "{{ trainingToDeleteName }}"?</p>
          <div class="flex justify-center mt-6">
            <Button label="{{ $t('delete') }}" @click="performDelete" class="bg-red-500 border-red-500 ml-5" />
            <Button label="{{ $t('cancel') }}" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
          </div>
        </Dialog>
      </div>
    </div>
  </template>
  
  <script setup>
    import Dialog from 'primevue/dialog';
    import Button from 'primevue/button';
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { api } from '@/api';

  
    const Trainings = ref([]);
    const totalRecords = ref(0);
    const currentPage = ref(0);
    const rowsPerPage = ref(100);
    const deleteDialogVisible = ref(false);
    const trainingToDeleteName = ref('');
    let trainingToDelete = null;
  
    const getAllTrainings = () => {
      api.get('/training/active_trainings')
        .then(response => {
          console.log('All Trainings:', response.data);
          Trainings.value = response.data;
          totalRecords.value = response.data.length;
        })
        .catch(error => {
          console.error('Error fetching Trainings:', error);
        });
    };
  
    const viewTraining = (trainingId) => {
      router.push(`/Trainings/${trainingId}`);
    };
  
    const editTraining = (trainingId) => {
      router.push(`/Trainings/Edit/${trainingId}`);
    };
  
    const confirmDelete = (trainingId, trainingName) => {
      trainingToDelete = trainingId;
      trainingToDeleteName.value = trainingName;
      deleteDialogVisible.value = true;
    };
  
    const cancelDelete = () => {
      deleteDialogVisible.value = false;
    };
  
    const performDelete = () => {
      if (trainingToDelete) {
        api.delete(`/trainings/${trainingToDelete}`)
          .then(() => {
            toast.success(t('delete_success'));
            deleteDialogVisible.value = false;
            getAllTrainings(); // Refresh trainings after deletion
          })
          .catch(error => {
            console.error('Error deleting training:', error);
            toast.error(t('delete_error'));
          });
      }
    };
  
    onMounted(getAllTrainings);
  
    // Format date as per your requirements
    const formatDate = (dateString) => {
      return dateString ? new Date(dateString).toLocaleDateString() : '';
    };
  
  </script>
  
  <style scoped>
    /* Add scoped styles as needed */
  </style>
  