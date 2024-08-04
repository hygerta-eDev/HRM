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
            <span class="font-semibold">{{ $t('companies') }}</span>
          </nav>
        </div>
        <div class="flex justify-between items-center mb-4 mt-16">
          <h2 class="text-3xl font-semibold">{{ $t('all_companies') }}</h2>
          <div class="flex items-center">
            <div class="relative mr-4">
              <input
                type="text"
                v-model="searchQuery"
                placeholder="Search companies"
                class="border border-gray-300 rounded-lg px-4 py-2 pl-10 shadow-inner"
              />
              <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
            </div>
            <router-link to="/Companies/NewCompany">
              <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
                <i class="fas fa-plus-circle fa-lg mr-2"></i>{{ $t('new_company') }}
              </button>
            </router-link>
          </div>
        </div>
        <div class="overflow-x-auto shadow-3xl rounded-lg border-2 border-blue-300">
          <table class="min-w-full border-collapse">
            <thead>
              <tr class="bg-sky-600 text-white">
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('no') }}</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('name') }}</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('descriptions') }}</th>
                <th class="px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('active') }}</th>
                <th class="px-4 py-4 text-base text-center font-semibold">{{ $t('actions') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(company, index) in filteredCompanies" :key="company.id"
                  :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
                  class="border-b border-gray-300 hover:bg-blue-100 transition duration-200">
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ company.name }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ company.slug }}</td>
                <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">
                  <div class="flex items-center justify-center h-full">
                    <span v-if="company.active" class="text-green-500">
                      <i class="fas fa-check-circle fa-lg"></i>
                    </span>
                    <span v-else class="text-red-500">
                      <i class="fas fa-times-circle fa-lg"></i>
                    </span>
                  </div>
                </td>
                <td class="rounded-lg px-4 py-4 text-center">
                  <div class="flex items-center justify-center h-full space-x-6">
                    <i v-tooltip="$t('view')" @click="viewCompany(company.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer hover:text-green-600 transition duration-300"></i>
                    <i v-tooltip="$t('edit')" @click="editCompany(company.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer hover:text-yellow-600 transition duration-300"></i>
                    <i v-tooltip="$t('delete')" @click="confirmDelete(company.id, company.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer hover:text-red-600 transition duration-300"></i>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <Dialog v-model:visible="deleteDialogVisible" :header="$t('confirm')" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete', { companyName: companyToDeleteName }) }}</p>
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
// import 'primevue/resources/themes/aura-light-indigo/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

const router = useRouter();
const companies = ref([]);
const totalRecords = ref(0);
const currentPage = ref(0);
const rowsPerPage = ref(10);
const deleteDialogVisible = ref(false);
const companyToDeleteName = ref('');
const searchQuery = ref('');
let companyToDelete = null;

const getUserIdFromLocalStorage = () => {
  const user = localStorage.getItem('user_id');
  return user; 
};

const getAllCompanies = () => {
  // const userId = getUserIdFromLocalStorage();
  const userId = 1;

  api.get('/institutions/active_institutions', {})
    .then(response => {
      console.log('All companies:', response.data);
      companies.value = response.data;
      totalRecords.value = response.data.length;
    })
    .catch(error => {
      console.error('Error fetching companies:', error);
    });
};

onMounted(() => {
  getAllCompanies();
});

const onPageChange = (event) => {
  currentPage.value = event.page;
};

const filteredCompanies = computed(() => {
  if (searchQuery.value) {
    return companies.value.filter(company => 
      company.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      company.slug.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  }
  return paginatedCompanies.value;
});

const paginatedCompanies = computed(() => {
  const startIndex = currentPage.value * rowsPerPage.value;
  const endIndex = Math.min(startIndex + rowsPerPage.value, companies.value.length);
  return companies.value.slice(startIndex, endIndex);
});

const viewCompany = (companyId) => {
  router.push(`/Companies/${companyId}`);
};

const editCompany = (companyId) => {
  router.push(`/Companies/Edit/${companyId}`);
};

const confirmDelete = (companyId, companyName) => {
  companyToDelete = companyId;
  companyToDeleteName.value = companyName;
  deleteDialogVisible.value = true; // Show the dialog
};

const cancelDelete = () => {
  companyToDelete = null;
  companyToDeleteName.value = '';
  deleteDialogVisible.value = false; // Hide the dialog
};

const performDelete = () => {
  if (companyToDelete) {
    api.delete(`/institutions/delete_institution/${companyToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        getAllCompanies();
        toast.success("Company deleted successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      })
      .catch(error => {
        console.error('Error deleting company:', error);
        toast.error("Failed to delete company!", {
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
