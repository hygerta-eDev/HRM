<template>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->
    <div class="relative mb-6">
      <nav class="flex items-center text-sm text-gray-700">
        <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-home text-lg mr-2"></i> <!-- Home icon -->
          Home
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-user-cog text-lg mr-2"></i> <!-- Administrator icon -->
          Administrator
        </router-link>
        <span class="mx-2">></span>
        <router-link to="/Holidays" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-calendar-alt text-lg mr-2"></i> <!-- Holidays icon -->
          Holidays
        </router-link>
        <span class="mx-2">></span>
        <span class="font-semibold">Edit Holiday</span>
      </nav>
    </div>

    <!-- Main Content -->
    <div class="p-10 shadow-lg rounded-lg border border-yellow-500 bg-white relative mt-12">
      <div v-if="Holiday" class="absolute inset-x-0 -top-10 flex justify-center">
        <h1 class="text-4xl font-bold text-yellow-800 bg-white px-6 py-4 relative z-10">
          Edit {{Holiday.description}}
        </h1>
      </div>
      <div v-if="Holiday" class="pt-16 px-8 pb-8">
        <div class="flex flex-col md:flex-row gap-6">
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday description</label>
            <i class="absolute left-3 mt-5 transform -translate-y-1/2 text-gray-500 fas fa-info-circle"></i>
            <input v-model="Holiday.description" type="text" class="w-full pl-10 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday date</label>
            <i class="absolute left-3 mt-5 transform -translate-y-1/2 text-gray-500 fas fa-calendar-alt"></i>
            <input v-model="Holiday.date" type="text" class="w-full pl-10 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
          <div class="flex-1 relative">
            <label class="block text-sm font-semibold mb-2 text-gray-700">Holiday recurring</label>
            <i class="absolute left-3 mt-5 transform -translate-y-1/2 text-gray-500 fas fa-sync-alt"></i>
            <input v-model="Holiday.recurring" type="text" class="w-full pl-10 py-2 border border-gray-300 rounded-md shadow-sm">
          </div>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <button @click="updateHoliday" class="bg-yellow-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-600 transition duration-300">Save</button>
          <router-link to="/Holidays">
            <button @click="cancelEdit" class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-gray-600 transition duration-300">Cancel</button>
          </router-link>
        </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>Loading...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';

const route = useRoute();
const router = useRouter();
const Holiday = ref(null);

const getHoliday = () => {
  const HolidayId = Number(route.params.id);
  api.get(`/holidays/${HolidayId}`)
    .then(response => {
      Holiday.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Holiday:', error);
    });
};

const updateHoliday = () => {
  if (Holiday.value) {
    api.put(`/holidays/update_holiday/${Holiday.value.id}`, Holiday.value)
      .then(response => {
        console.log('Holiday updated successfully:', response.data);
        router.push('/Holidays');
        setTimeout(() => {
          toast.success("Holiday edited successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }, 250);
      })
      .catch(error => {
        console.error('Error updating Holiday:', error);
      });
  }
};

const cancelEdit = () => {
  router.push('/Holidays');
};

onMounted(getHoliday);
</script>

<style scoped>
.relative {
  position: relative;
}
.absolute {
  position: absolute;
}
.top-0 {
  top: 0;
}
.left-0 {
  left: 0;
}
.mb-4 {
  margin-bottom: 1rem;
}
</style>
