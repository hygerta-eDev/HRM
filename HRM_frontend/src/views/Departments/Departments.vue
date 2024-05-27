<template>
  <div class="p-10">
    <div class="container mx-auto" :class="{ 'blurred': deleteDialogVisible }">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-3xl font-semibold">Departments</h2>
        <router-link to="/Departments/NewDepartment">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Department</button>
        </router-link>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300 rounded-lg">
          <thead>
            <tr class="bg-sky-600">
              <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
              <th class="px-4 py-4 text-left w-1/5 text-base">Name</th>
              <th class="px-4 py-4 text-left w-1/5 text-base">Descriptions</th>
              <th class="px-4 py-4 text-left w-1/5 text-base">Companies</th>
              <th class="px-4 py-4 text-left w-1/5 text-base">Active</th>
              <th class="px-4 py-4 text-left w-1/5 text-base">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(department, index) in paginatedDepartments" :key="department.id"
            :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
            class="border-b border-gray-300 hover:bg-blue-100">
              <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ index + 1 }}</td>
              <td class="px-4 py-4 text-left text-base">{{ department.name }}</td>
              <td class="px-4 py-4 text-left text-base">{{ department.slug }}</td>
              <td class="px-4 py-4 text-left text-base">{{ getCompanyName(department.institution_id) }}</td>
              <td class="px-4 py-4 text-left">
                <span v-if="department.active" class="text-green-500">
                  <i class="fas fa-check-circle fa-lg"></i>
                </span>
                <span v-else class="text-red-500">
                  <i class="fas fa-times-circle fa-lg"></i>
                </span>
              </td>
              <td class="px-4 py-4 actions text-left">
                <router-link :to="`/Departments/${department.id}`">
                  <i @click="viewDepartment(department.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                </router-link>
                <router-link :to="`/Departments/Edit/${department.id}`">
                  <i @click="editDepartment(department.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                </router-link>
                <i @click="confirmDelete(department.id, department.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- <Paginator :totalRecords="totalRecords" :rows="rowsPerPage" @onPageChange="onPageChange"></Paginator> -->
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"  :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Department "{{ DepartmentToDeleteName }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class=" bg-red-500 border-red-500 ml-5" />
        <!-- <button @click="performDelete" class="bg-red-500 text-white py-2 px-4 rounded-lg">Delete</button> -->

        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
        <!-- <button @click="cancelDelete" class="mr-3 bg-gray-400 text-white py-2 px-4 rounded-lg ml-5">Cancel</button> -->

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
import Paginator from 'primevue/paginator';
import { toast } from 'vue3-toastify';

const router = useRouter();
const departments = ref([]);
const companies = ref([]);
const totalRecords = ref(0);
const currentPage = ref(0);
const rowsPerPage = ref(100);
const deleteDialogVisible = ref(false);
const DepartmentToDeleteName = ref('');
let DepartmentToDelete = null;

const getAllDepartments = () => {
  api.get('/departments/active_departments')
    .then(response => {
      console.log('All departments:', response.data);
      departments.value = response.data;
      totalRecords.value = response.data.length;
    })
    .catch(error => {
      console.error('Error fetching departments:', error);
    });
};

const getAllCompanies = () => {
  api.get('/institutions/active_institutions')
    .then(response => {
      companies.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching companies:', error);
    });
};

onMounted(() => {
  getAllDepartments();
  getAllCompanies();
});

const getCompanyName = (companyId) => {
  const company = companies.value.find(company => company.id === companyId);
  return company ? company.name : 'Unknown';
};

const onPageChange = (event) => {
  currentPage.value = event.page;
};

const paginatedDepartments = computed(() => {
  const startIndex = currentPage.value * rowsPerPage.value;
  const endIndex = Math.min(startIndex + rowsPerPage.value, departments.value.length);
  return departments.value.slice(startIndex, endIndex);
});

const viewDepartment = (departmentId) => {
  router.push(`/Companies/${departmentId}`);
};

const editDepartment = (departmentId) => {
  router.push(`/Companies/Edit/${departmentId}`);
};

const confirmDelete = (departmentId, departmentName) => {
  DepartmentToDelete = departmentId;
  DepartmentToDeleteName.value = departmentName;
  deleteDialogVisible.value = true;
};

const cancelDelete = () => {
  DepartmentToDelete = null;
  DepartmentToDeleteName.value = '';
  deleteDialogVisible.value = false;
};

const performDelete = () => {
  if (DepartmentToDelete) {
    api.delete(`/departments/delete_department/${DepartmentToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        getAllDepartments();
        toast.success("Department deleted successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      })
      .catch(error => {
        console.error('Error deleting department:', error);
        toast.error("Failed to delete department!", {
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
