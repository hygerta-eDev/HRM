<template>
  <div class="p-10">
    <div class="container mx-auto p-6 bg-white shadow-xl rounded-lg border-blue-800" :class="{ 'blurred': deleteDialogVisible }">
      <div class="relative mb-6">
        <nav class="flex items-center text-sm text-gray-700">
          <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
            <i class="fas fa-home text-lg mr-2"></i>
            Home
          </router-link>
          <span class="mx-2">></span>
          <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
            <i class="fas fa-user-cog text-lg mr-2"></i>
            Administrator
          </router-link>
          <span class="mx-2">></span>
          <span class="font-semibold">Holidays</span>
        </nav>
      </div>
      <div class="flex justify-between items-center mb-4 mt-16">
        <h2 class="text-3xl font-semibold">Holidays</h2>
        <div class="flex items-center">
          <div class="relative mr-4">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Search Holidays"
              class="border border-gray-300 rounded-lg px-4 py-2 pl-10 shadow-inner"
            />
            <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
          </div>
          <div class="flex items-center">
            <router-link to="/Holidays/NewHoliday">
              <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
                <i class="fas fa-plus-circle fa-lg mr-2"></i>New Holiday
              </button>
            </router-link>
          </div>
        </div>
      </div>
      <div v-if="filteredHolidays.length === 0" class="p-4 text-center text-gray-500">
        No data
      </div>
      <div v-else>
        <div class="overflow-x-auto shadow-2xl drop-shadow-2xl border border-blue-200 rounded-lg">
          <table class="min-w-full border-collapse">
            <thead>
              <tr class="bg-sky-600 text-white">
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">No</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">Date</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">Description</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">Recurring</th>
                <th class="px-4 py-4 text-base text-center font-semibold">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(Holiday, index) in filteredHolidays" :key="Holiday.id"
                  :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
                  class="border-b border-gray-300 hover:bg-blue-100 transition duration-200">
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ formatDate(Holiday.date) }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ Holiday.description }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ Holiday.recurring ? 'Yes' : 'No' }}</td>
                <td class="rounded-lg px-4 py-4 text-center">
                  <div class="flex items-center justify-center h-full space-x-6">
                    <router-link :to="`/Holidays/${Holiday.id}`">
                      <i class="fas fa-eye fa-lg text-green-500 cursor-pointer hover:text-green-600 transition duration-300"></i>
                    </router-link>
                    <router-link :to="`/Holidays/Edit/${Holiday.id}`">
                      <i class="fas fa-edit fa-lg text-yellow-500 cursor-pointer hover:text-yellow-600 transition duration-300"></i>
                    </router-link>
                    <i @click="confirmDelete(Holiday.id, Holiday.description)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer hover:text-red-600 transition duration-300"></i>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Holiday "{{ HolidayToDeleteName }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class="bg-red-500 border-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition duration-300 ml-5 shadow-md" />
        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5 bg-gray-500 border-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-600 transition duration-300 shadow-md" />
      </div>
    </Dialog>
  </div>
</template>

<script setup>
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';
import { format } from 'date-fns';

const router = useRouter();
const Holidays = ref([]);
const totalRecords = ref(0);
const currentPage = ref(0);
const rowsPerPage = ref(100);
const deleteDialogVisible = ref(false);
const HolidayToDeleteName = ref('');
let HolidayToDelete = null;
const searchQuery = ref('');

const getAllHolidays = () => {
  api.get('/holidays/active_holidays')
    .then(response => {
      Holidays.value = response.data;
      totalRecords.value = response.data.length;
    })
    .catch(error => {
      console.error('Error fetching Holidays:', error);
    });
};
onMounted(getAllHolidays);

const onPageChange = (event) => {
  currentPage.value = event.page;
};

const filteredHolidays = computed(() => {
  if (searchQuery.value) {
    return Holidays.value.filter(Holiday => 
      Holiday.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      Holiday.date.toLowerCase().includes(searchQuery.value.toLowerCase())

    );
  }
  return paginatedHolidays.value;
});

const paginatedHolidays = computed(() => {
  const startIndex = currentPage.value * rowsPerPage.value;
  const endIndex = Math.min(startIndex + rowsPerPage.value, Holidays.value.length);
  return Holidays.value.slice(startIndex, endIndex);
});

const formatDate = (date) => {
  return format(new Date(date), 'dd MMM yyyy');
};

const confirmDelete = (HolidayId, HolidayName) => {
  HolidayToDelete = HolidayId;
  HolidayToDeleteName.value = HolidayName;
  deleteDialogVisible.value = true;
};

const cancelDelete = () => {
  HolidayToDelete = null;
  HolidayToDeleteName.value = '';
  deleteDialogVisible.value = false;
};

const performDelete = () => {
  if (HolidayToDelete) {
    api.delete(`/holidays/delete_holiday/${HolidayToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        getAllHolidays();
        toast.success("Holiday deleted successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      })
      .catch(error => {
        console.error('Error deleting Holiday:', error);
        toast.error("Failed to delete Holiday!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  }
};
</script>
