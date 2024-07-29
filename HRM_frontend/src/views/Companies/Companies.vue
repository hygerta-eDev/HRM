<template >
  <div>
  <div class="p-10" >
    <div class="container mx-auto " :class="{ 'blurred': deleteDialogVisible }">
      <div class="flex justify-between items-center mb-4" >
        <h2 class="text-3xl font-semibold">Companies</h2>
        <router-link to="/Companies/NewCompany">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">{{ $t('new_company') }}</button>
        </router-link>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300 rounded-lg">
          <thead>
            <tr class="bg-sky-600">
              <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
              <th class="px-4 py-4 text-left w-1/4 text-base">{{ $t('name') }}</th>
              <th class="px-4 py-4 text-left w-1/4 text-base">Descriptions</th>
              <th class="px-4 py-4 text-left w-1/4 text-base">Active</th>
              <th class="px-4 py-4 text-left w-1/4 text-base">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(company, index) in paginatedCompanies" :key="company.id"
                :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
                class="border-b border-gray-300 hover:bg-blue-100">
              <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
              <td class="px-4 py-4 text-left text-base">{{ company.name }}</td>
              <td class="px-4 py-4 text-left text-base">{{ company.slug }}</td>
              <td class="px-4 py-4 text-left">
                <span v-if="company.active" class="text-green-500">
                  <i class="fas fa-check-circle fa-lg"></i>
                </span>
                <span v-else class="text-red-500">
                  <i class="fas fa-times-circle fa-lg"></i>
                </span>
              </td>
              <td class="px-4 py-4 actions text-left">
                <router-link :to="`/Companies/${company.id}`">
                  <i @click="viewCompany(company.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                </router-link>
                <router-link :to="`/Companies/Edit/${company.id}`">
                  <i @click="editCompany(company.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                </router-link>
                <i @click="confirmDelete(company.id, company.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- <Paginator :totalRecords="totalRecords" :rows="rowsPerPage" @onPageChange="onPageChange"></Paginator> -->
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"  :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the company "{{ companyToDeleteName }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class=" bg-red-500 border-red-500 ml-5" />
        <!-- <button @click="performDelete" class="bg-red-500 text-white py-2 px-4 rounded-lg">Delete</button> -->

        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
        <!-- <button @click="cancelDelete" class="mr-3 bg-gray-400 text-white py-2 px-4 rounded-lg ml-5">Cancel</button> -->

      </div>
    </Dialog>
  </div>
</div>
</template>

<script setup>
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import Paginator from 'primevue/paginator';
import { toast } from 'vue3-toastify';

const router = useRouter();
const companies = ref([]);
const totalRecords = ref(0);
const currentPage = ref(0);
const rowsPerPage = ref(10); // Adjust based on your preference
const deleteDialogVisible = ref(false);
const companyToDeleteName = ref('');
let companyToDelete = null;

const getUserIdFromLocalStorage = () => {
  const user = localStorage.getItem('user_id');
  return user; // Adjust according to your local storage structure
};

const getAllCompanies = () => {
  const userId = getUserIdFromLocalStorage();
  // const yourAuthToken = 'your-auth-token'; // Replace with your actual token

  api.get('/institutions/active_institutions', {
    // headers: {
    //   // 'Authorization': `Bearer ${yourAuthToken}`,
    //   'x-user-id': userId // Custom header to pass user_id
    // }
  })
  .then(response => {
    console.log('All companies:', response.data);
    companies.value = response.data;
    totalRecords.value = response.data.length;
  })
  .catch(error => {
    console.error('Error fetching companies:', error);
  });
};

onMounted(getAllCompanies);

const onPageChange = (event) => {
  currentPage.value = event.page;
};

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
  deleteDialogVisible.value = true;
};

const cancelDelete = () => {
  companyToDelete = null;
  companyToDeleteName.value = '';
  deleteDialogVisible.value = false;
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