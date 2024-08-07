<template>
  <div>
    <div class="p-10">
      <div class="container mx-auto p-6 bg-white shadow-xl rounded-lg border-blue-800" :class="{ 'blurred': deleteDialogVisible }">
        <div class="relative mb-6">
          <nav class="flex items-center text-sm text-gray-700">
            <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
              <i class="fas fa-home text-lg mr-2"></i> <!-- Home icon -->
              {{ $t('home') }}
            </router-link>
            <span class="mx-2">></span>
            <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
              <i class="fas fa-user-cog text-lg mr-2"></i> <!-- Administrator icon -->
              {{ $t('administrator') }}
            </router-link>
            <span class="mx-2">></span>
            
            <span class="font-semibold"><i class="fa-solid fa-graduation-cap"></i>{{ $t('qualifications') }}</span>
          </nav>
        </div>
        <div class="flex justify-between items-center mb-4 mt-16">
          <h2 class="text-3xl font-semibold">{{ $t('all_qualifications') }}</h2>
          <div class="flex items-center">
            <div class="relative mr-4">
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search qualifications"
                class="border border-gray-300 rounded-lg px-4 py-2 pl-10 shadow-inner"
              />
              <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
            </div>
            <router-link to="/Qualifications/NewQualifications">
              <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
                <i class="fas fa-plus-circle fa-lg mr-2"></i>{{ $t('new_qualification') }}
              </button>
            </router-link>
          </div>
        </div>
        <div class="overflow-x-auto shadow-2xl drop-shadow-2xl border border-blue-200 rounded-lg">
          <table class="min-w-full border-collapse">
            <thead>
              <tr class="bg-sky-600 text-white">
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('no') }}</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('name') }}</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('descriptions') }}</th>
                <th class="px-4 py-4 text-base text-center font-semibold">{{ $t('actions') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(qualification, index) in filteredQualifications" :key="qualification.id"
                  :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
                  class="border-b border-gray-300 hover:bg-blue-100 transition duration-200">
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ qualification.name }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ qualification.slug }}</td>
                <td class="rounded-lg px-4 py-4 text-center">
                  <div class="flex items-center justify-center h-full space-x-6">
                    <i v-tooltip="$t('view')" @click="viewQualification(qualification.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer hover:text-green-600 transition duration-300"></i>
                    <i v-tooltip="$t('edit')" @click="editQualification(qualification.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer hover:text-yellow-600 transition duration-300"></i>
                    <i v-tooltip="$t('delete')" @click="confirmDelete(qualification.id, qualification.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer hover:text-red-600 transition duration-300"></i>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <Dialog v-model:visible="deleteDialogVisible" :header="$t('confirm')" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete', { qualificationName: qualificationToDeleteName }) }}</p>
          <div class="flex justify-center mt-6">
            <Button :label="$t('delete')" @click="performDelete" class="bg-red-500 border-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition duration-300 ml-5 shadow-md" />
            <Button :label="$t('cancel')" @click="cancelDelete" class="bg-slate-400 border-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-900 transition duration-300 mr-3 ml-5 shadow-md" />
          </div>
        </Dialog>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const router = useRouter();
const qualifications = ref([]);
const totalRecords = ref(0);
const currentPage = ref(0);
const rowsPerPage = ref(10);
const deleteDialogVisible = ref(false);
const qualificationToDeleteName = ref('');
const searchQuery = ref('');
let qualificationToDelete = null;

const getAllQualifications = () => {
  api.get('/qualification/active_qualifications')
    .then(response => {
      qualifications.value = response.data;
      totalRecords.value = response.data.length;
    })
    .catch(error => {
      console.error('Error fetching qualifications:', error);
    });
};

onMounted(getAllQualifications);

const onPageChange = (event) => {
  currentPage.value = event.page;
};

const filteredQualifications = computed(() => {
  if (searchQuery.value) {
    return qualifications.value.filter(qualification => 
      qualification.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      qualification.slug.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }
  return paginatedQualifications.value;
});

const paginatedQualifications = computed(() => {
  const startIndex = currentPage.value * rowsPerPage.value;
  const endIndex = Math.min(startIndex + rowsPerPage.value, qualifications.value.length);
  return qualifications.value.slice(startIndex, endIndex);
});

const viewQualification = (qualificationId) => {
  router.push(`/Qualifications/${qualificationId}`);
};

const editQualification = (qualificationId) => {
  router.push(`/Qualifications/Edit/${qualificationId}`);
};

const confirmDelete = (qualificationId, qualificationName) => {
  qualificationToDelete = qualificationId;
  qualificationToDeleteName.value = qualificationName;
  deleteDialogVisible.value = true;
};

const cancelDelete = () => {
  qualificationToDelete = null;
  qualificationToDeleteName.value = '';
  deleteDialogVisible.value = false;
};

const performDelete = () => {
  if (qualificationToDelete) {
    api.delete(`/qualification/delete_qualification/${qualificationToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        getAllQualifications();
        toast.success("Qualification deleted successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      })
      .catch(error => {
        toast.error("Failed to delete qualification!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  }
};
</script>

<style scoped>
.blurred {
  filter: blur(5px);
  pointer-events: none;
}
</style>
