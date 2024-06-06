<template>
  <div>
  <div class="p-10">
    <div class="container mx-auto" :class="{ 'blurred': deleteDialogVisible }">

      <!-- New Department Button -->
      <div class="flex justify-end items-center mb-8">
        <router-link :to="`/Departments/NewDepartment`">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Department</button>
        </router-link>
      </div>

      <!-- Departments Table -->
      <div v-for="(companyDepartments, companyId) in departmentsByCompany" :key="companyId" class="mb-8">
        <h2 class="text-3xl font-semibold mb-4">Departments of Company {{ getCompanyName(Number(companyId)) }}</h2>
        <div class="overflow-x-auto">
          <table class="w-full border-collapse border border-gray-300 rounded-lg">
            <thead>
              <tr class="bg-sky-600 text-white">
                <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
                <th class="px-4 py-4 text-left w-1/5 text-base">Name</th>
                <th class="px-4 py-4 text-left w-1/5 text-base">Descriptions</th>
                <th class="px-4 py-4 text-left w-1/5 text-base">Company</th>
                <th class="px-4 py-4 text-left w-1/5 text-base">Active</th>
                <th class="px-4 py-4 text-left w-1/5 text-base">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(department, index) in companyDepartments" :key="department.id"
                :class="{ 'bg-white': index % 2 === 0, 'bg-gray-200': index % 2 !== 0 }"
                class="border-b border-gray-300 hover:bg-blue-100">
                <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ index + 1 }}</td>
                <td class="px-4 py-4 text-left text-base">{{ department.name }}</td>
                <td class="px-4 py-4 text-left text-base">{{ department.slug }}</td>
                <td class="px-4 py-4 text-left text-base">{{ getCompanyName(department.institution_id) }}</td> <!-- Display company name -->
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
                    <i class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                  </router-link>
                  <router-link :to="`/Departments/Edit/${department.id}`">
                    <i class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                  </router-link>
                  <i @click="confirmDelete(department.id, department.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Department "{{ DepartmentToDeleteName }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class="bg-red-500 border-red-500 ml-5" />
        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
      </div>
    </Dialog>
  </div>
  </div>
</template>



<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import { toast } from 'vue3-toastify';

const router = useRouter();
const departmentsByCompany = ref({});
const companies = ref([]);
const companiesLoaded = ref(false);
const deleteDialogVisible = ref(false);
const DepartmentToDeleteName = ref('');
let DepartmentToDelete = null;

const getAllDepartments = () => {
  api.get('/departments/active_departments')
    .then(response => {
      console.log('API response:', response.data);
      const data = response.data;
      const groupedDepartments = {};
      data.forEach(department => {
        if (!groupedDepartments[department.institution_id]) {
          groupedDepartments[department.institution_id] = [];
        }
        groupedDepartments[department.institution_id].push(department);
      });
      departmentsByCompany.value = groupedDepartments;
    })
    .catch(error => {
      console.error('Error fetching departments:', error);
    });
};

const getCompanies = () => {
  api.get('/institutions/active_institutions')
    .then(response => {
      companies.value = response.data;
      companiesLoaded.value = true;  // Set the loaded state to true
    })
    .catch(error => {
      console.error('Error fetching companies:', error);
    });
};

const getCompanyName = (companyId) => {
  const company = companies.value.find(company => company.id === companyId);
  return company ? company.name : 'Unknown Company';
};

onMounted(() => {
  getAllDepartments();
  getCompanies();
});

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

// Watch for changes in departmentsByCompany and companies data
watch([departmentsByCompany, companiesLoaded], () => {
  if (companiesLoaded.value) {
    Object.keys(departmentsByCompany.value).forEach(companyId => {
      const companyName = getCompanyName(Number(companyId));
      if (companyName === 'Unknown Company') {
        console.warn(`Company with ID ${companyId} not found in companies list.`);
      }
    });
  }
});
</script>
