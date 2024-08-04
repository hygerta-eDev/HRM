<template>
  <div>
    <div class="p-10">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8" :class="{ 'blurred': deleteDialogVisible }">
        <h2 class="bg-gray-100 p-5 text-3xl font-semibold">{{ $t('trainings') }}</h2>
        <hr>
        <div class="p-10">
          <h3 class="text-xl font-semibold mb-2">{{ $t('ongoing_trainings') }}</h3>
          <div v-if="ongoingTrainings.length === 0">
            <p>{{ $t('no_ongoing_trainings') }}</p>
          </div>
          <div v-else>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
              <div v-for="(training, index) in ongoingTrainings" :key="index" class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                <div class="p-4">
                  <h4 class="text-lg font-semibold mb-2">{{ training.title }}</h4>
                  <p class="text-sm text-gray-600 mb-2">{{ formatDate(training.start_date) }} - {{ formatDate(training.end_date) }}</p>
                  <router-link :to="`/Trainings/${training.id}`" class="text-blue-500 hover:underline">{{ $t('view_details') }}</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex justify-end mb-4">
          <router-link to="/Trainings/Newtraining">
            <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">
              <i class="fa-solid fa-circle-plus"></i> {{ $t('new_training') }}
            </button>
          </router-link>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full border-collapse border border-gray-300 rounded-lg">
            <thead>
              <tr class="bg-sky-600 text-white">
                <th class="px-4 py-4 text-left text-base border-r border-black-900">{{ $t('no') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('title') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('end_date') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('description') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('start_date') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('active') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('completed_at') }}</th>
                <th class="px-4 py-4 text-left w-1/8 text-base">{{ $t('outcome') }}</th>
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
                <td class="px-4 py-4 text-left text-base">{{ formatDate(training.completed_at) }}</td>
                <td class="px-4 py-4 text-left text-base">{{ training.outcome }}</td>
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
import { toast } from 'vue3-toastify';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const router = useRouter();
const Trainings = ref([]);
const deleteDialogVisible = ref(false);
const trainingToDeleteName = ref('');
let trainingToDelete = null;

const getAllTrainings = () => {
  api.get('/training/active_trainings')
    .then(response => {
      console.log('All Trainings:', response.data);
      Trainings.value = response.data;
      computeOngoingTrainings(); // Compute ongoing trainings after fetching
    })
    .catch(error => {
      console.error('Error fetching Trainings:', error);
    });
};

const ongoingTrainings = ref([]);

const computeOngoingTrainings = () => {
  const currentDate = new Date();
  ongoingTrainings.value = Trainings.value.filter(training => {
    const startDate = new Date(training.start_date);
    const endDate = new Date(training.end_date);
    // Adjust to include time component for precise comparison
    startDate.setHours(0, 0, 0, 0);
    endDate.setHours(23, 59, 59, 999);
    currentDate.setHours(0, 0, 0, 0);
    return training.active && startDate <= currentDate && currentDate <= endDate;
  });
  console.log(ongoingTrainings);
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
    api.delete(`/training/delete_training/${trainingToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        toast.success(t('delete_success'));
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
.container {
  margin: auto;
  max-width: 1400px; /* Adjust max-width as per your design */
  padding: 0 1rem;
}

/* Adjust other scoped styles as needed */
</style>
