<template>
  <div>
    <div class="p-10">
      <div class="container mx-auto p-6 bg-white shadow-xl rounded-lg border-yellow-800" :class="{ 'blurred': deleteDialogVisible }">
        <!-- Breadcrumbs -->
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
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 160" class=" w-6 h-7 mr-2 mb-[-8px]  text-black-500" fill="black" >
            <path d="M31.17,58.6V54.26a2,2,0,0,0-2.91-1.78l-14,7.15a2,2,0,0,0-1.09,1.78v5.76l4-1.9V62.64l10-5.11v3Z"/>
            <path d="M59.17,45.28v-4a2,2,0,0,0-2.91-1.78l-14,7.15a2,2,0,0,0-1.09,1.78v5.45l4-1.9V49.61l10-5.11v2.68Z"/>
            <path d="M84.05,71.42a2,2,0,0,0-1.95-.09l-14,7A2,2,0,0,0,67,80.13v20.2l-2.59-2.59a2,2,0,0,0-2.83,2.83l6,6a2.05,2.05,0,0,0,2.32.37l4.78-2.44v4l-3.22,1.64a2,2,0,0,0,1.82,3.57l9.83-5a2,2,0,0,0-1.82-3.57l-2.61,1.34v-4l5.22-2.67A2,2,0,0,0,85,98V73.12A2,2,0,0,0,84.05,71.42ZM81,96.79,71,101.9V81.37l10-5Z"/>
            <path d="M44,75v4.45l13.65-6.6A6,6,0,0,1,57,70.11V68.69Z"/>
            <path d="M33,89.15a2,2,0,0,0,2-2V84.7L38.83,83A2,2,0,0,0,40,81.13v-9a2,2,0,0,0-2.83-1.82l-11,5A2,2,0,0,0,25,77.13v9a2,2,0,0,0,.92,1.68,2.06,2.06,0,0,0,1.91.14L31,86.52v.62A2,2,0,0,0,33,89.15ZM29,83V78.42l7-3.19v4.61Z"/>
            <path d="M69,73.12a2,2,0,0,0,2-2V68.67l3.83-1.74A2,2,0,0,0,76,65.11v-9a2,2,0,0,0-2.83-1.82l-11,5A2,2,0,0,0,61,61.1v9a2,2,0,0,0,.92,1.68,2,2,0,0,0,1.91.14L67,70.49v.62A2,2,0,0,0,69,73.12ZM65,67V62.39l7-3.19v4.61Z"/>
            <path d="M52.11,85.35l-14,7A2.06,2.06,0,0,0,37,94.15v20.2l-2.59-2.59a2,2,0,0,0-2.83,2.83l6,6a2.05,2.05,0,0,0,2.32.37l4.78-2.44v4l-3.22,1.64a2,2,0,1,0,1.82,3.57l9.83-5a2,2,0,0,0-1.82-3.57l-2.61,1.34v-4l5.22-2.67A2,2,0,0,0,55,112V87.14a1.87,1.87,0,0,0-.12-.67A2.06,2.06,0,0,0,52.11,85.35ZM51,110.82l-10,5.11V103.34l10-5.16Zm0-17.14L41,98.83V95.39l10-5Z"/>
            <path d="M95,65.22a2,2,0,0,0-1.07-1.79L84,58.18V41.07a2,2,0,0,0-2.86-1.81l-80,38.06A2,2,0,0,0,0,79.13V121.2a2,2,0,0,0,1,1.71,2.07,2.07,0,0,0,2,.07l25-12.87A5.84,5.84,0,0,1,33,107.18V103l-29,15V101.35l7.81,5.47a2,2,0,0,0,2,.15L33,97.4V94.15a6.06,6.06,0,0,1,.16-1.31l-20,10-7.18-5L22.33,89.9A6,6,0,0,1,21,86.14v0L4,94.31V80.4L80,44.24V62l1.4-.68,7.21,3.81-4.28,2.14a5.89,5.89,0,0,1,1.81.72,6,6,0,0,1,1.91,1.9L93.89,67A2,2,0,0,0,95,65.22Z"/>
            <polygon points="63 87.48 59 89.55 59 94.05 63 91.99 63 87.48"/>
            <path d="M63,80.13a6,6,0,0,1,.52-2.45l-8,4a5.75,5.75,0,0,1,.65.35,6,6,0,0,1,2.31,2.65L63,82.42Z"/>
            <path d="M127.16.37a2,2,0,0,0-1.82-.26L44,28.41,2.53,17.1A2,2,0,0,0,0,19V56.92a2,2,0,0,0,1.43,1.92l7.75,2.33a6,6,0,0,1,1.49-3.74L4,55.43V21.65L70.61,39.83l5.55-2.64L50.81,30.28,124,4.82V37l-20.93,7.55L88,40.42a6.09,6.09,0,0,1,0,.65v3.51l36,9.83V91.46L89,81v4.18l36.43,10.94A2,2,0,0,0,128,94.15V52.88a2,2,0,0,0-1.47-1.93l-16.74-4.57,16.89-6.09A2,2,0,0,0,128,38.4V2A2,2,0,0,0,127.16.37Z"/>
          </svg>
            <span class="font-semibold">{{ $t('departments') }}</span>
          </nav>
        </div>

        <!-- Search and Filter Box -->
        <div class="mt-10 bg-gray-100 p-10 shadow-2xl border border-blue-100 mb-8 flex items-center">
          <!-- Search Input -->
          <div class="relative flex-grow mr-4 max-w-xs"> <!-- Adjusted width here -->
            <input
              type="text"
              v-model="searchQuery"
              :placeholder="$t('search')"
              class="border border-gray-300 rounded-lg px-4 py-2 pl-10 shadow-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
          </div>
          
          <!-- Dropdown -->
          <div class="relative flex-shrink-0 w-64"> <!-- Adjust width as needed -->
            <select 
              v-model="selectedCompany" 
              @change="filterDepartments" 
              class="block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-md bg-white text-gray-700 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 appearance-none transition duration-150 ease-in-out">
                <option value="" class="py-2 px-4 hover:bg-blue-100">{{ $t('all_companies') }}</option>
                <option v-for="company in companies" :key="company.id" :value="company.id" class="py-2 px-4 hover:bg-blue-100">
                  {{ company.name }}
                </option>
            </select>
            <i class="fas fa-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
          </div>
        </div>

        <!-- Dynamic Header and Button -->
        <div class="flex justify-between items-center mb-4 mt-8">
          <h2 class="text-3xl font-semibold">
            {{ selectedCompany ? `${$t('all_departments_of')} ${getCompanyName(selectedCompany)}` : $t('all_departments') }}
          </h2>
          <router-link :to="`/Departments/NewDepartment?companyId=${selectedCompany}`">
            <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
              <i class="fas fa-plus-circle fa-lg mr-2"></i>{{ $t('new_department') }}
            </button>
          </router-link>
        </div>

        <!-- Departments Tables by Company -->
        <div v-if="filteredDepartments.length === 0 && selectedCompany" class="p-4 text-center text-gray-500">
          {{ $t('no_records_found') }}
        </div>
        <div v-else>
          <div v-for="(departments, companyId) in filteredDepartments" :key="companyId" class="mb-8">
            <div v-if="departments.length === 0" class="p-4 text-center text-gray-500">
              {{ $t('no_records_found') }}
            </div>
            <div  v-else>
              <h3 class="text-2xl font-semibold mb-4">{{ getCompanyName(companyId) }}</h3>      
              <div class="overflow-x-auto shadow-2xl drop-shadow-2xl border border-blue-200 rounded-lg border border-blue-500 shadow-3xl rounded-lg border-2 border-blue-300">
                <table class="min-w-full border-collapse">
                  <thead>
                    <tr class="bg-sky-600 text-white">
                      <th class="w-16 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('no') }}</th>
                      <th class="w-32 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('name') }}</th>
                      <th class="w-48 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('descriptions') }}</th>
                      <th class="w-32 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('company') }}</th>
                      <th class="w-20 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('active') }}</th>
                      <th class="w-40 px-4 py-4 text-base text-center font-semibold">{{ $t('actions') }}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(department, index) in departments" :key="department.id"
                        :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
                        class="border-b border-gray-300 hover:bg-blue-100 transition duration-200">
                      <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ index + 1 }}</td>
                      <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ department.name }}</td>
                      <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ department.slug }}</td>
                      <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ getCompanyName(department.institution_id) }}</td>
                      <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">
                        <div class="flex items-center justify-center h-full">
                          <span v-if="department.active" class="text-green-500">
                            <i class="fas fa-check-circle fa-lg"></i>
                          </span>
                          <span v-else class="text-red-500">
                            <i class="fas fa-times-circle fa-lg"></i>
                          </span>
                        </div>
                      </td>
                      <td class="rounded-lg px-4 py-4 text-center">
                        <div class="flex items-center justify-center h-full space-x-6">
                          <i v-tooltip="$t('view')" @click="viewDepartment(department.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer hover:text-green-600 transition duration-300"></i>
                          <i v-tooltip="$t('edit')" @click="editDepartment(department.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer hover:text-yellow-600 transition duration-300"></i>
                          <i v-tooltip="$t('delete')" @click="confirmDelete(department.id, department.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer hover:text-red-600 transition duration-300"></i>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- Delete Confirmation Dialog -->
        <Dialog v-model:visible="deleteDialogVisible" :header="$t('confirm')" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete', { name: 'department', nameToDelete: DepartmentToDeleteName }) }}</p>
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
import { ref, onMounted, computed,watch } from 'vue';
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

const searchQuery = ref('');
const selectedCompany = ref('');

const getAllDepartments = () => {
  api.get('/departments/active_departments')
    .then(response => {
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
      companiesLoaded.value = true;
    })
    .catch(error => {
      console.error('Error fetching companies:', error);
    });
};


const getCompanyName = (companyId) => {
  const idToFind = Number(companyId);
  const company = companies.value.find(c => Number(c.id) === idToFind);

  return company ? company.name : 'Unknown Company';
};



const filteredDepartments = computed(() => {
  if (!departmentsByCompany.value || typeof departmentsByCompany.value !== 'object') {
    return {};
  }

  const query = searchQuery.value.toLowerCase();
  const filtered = {};

  // If a company is selected, filter for that company only
  if (selectedCompany.value) {
    const companyDepartments = departmentsByCompany.value[selectedCompany.value];

    if (Array.isArray(companyDepartments)) {
      const filteredDepartments = companyDepartments.filter(department => {
        const nameMatch = department.name.toLowerCase().includes(query);
        const slugMatch = department.slug.toLowerCase().includes(query);
        const companyMatch = getCompanyName(department.institution_id).toLowerCase().includes(query);

        return nameMatch || slugMatch || companyMatch;
      });

      if (filteredDepartments.length > 0) {
        filtered[selectedCompany.value] = filteredDepartments;
      } else {
        // If no departments found for the selected company, show "No records found"
        filtered[selectedCompany.value] = [];
      }
    } else {
      // If no departments array exists for the selected company, show "No records found"
      filtered[selectedCompany.value] = [];
    }
  } else {
    // If no company is selected, show departments for all companies
    Object.keys(departmentsByCompany.value).forEach(companyId => {
      const departments = departmentsByCompany.value[companyId];

      if (Array.isArray(departments)) {
        const filteredDepartments = departments.filter(department => {
          const nameMatch = department.name.toLowerCase().includes(query);
          const slugMatch = department.slug.toLowerCase().includes(query);
          const companyMatch = getCompanyName(department.institution_id).toLowerCase().includes(query);

          return nameMatch || slugMatch || companyMatch;
        });

        if (filteredDepartments.length > 0) {
          filtered[companyId] = filteredDepartments;
        }
      }
    });
  }

  return filtered;
});





const filterDepartments = () => {
  // Triggered by dropdown change, handled by computed properties
};

const viewDepartment = (DepartmentId) => {
  router.push(`/Departments/${DepartmentId}`);
};

const editDepartment = (DepartmentId) => {
  router.push(`/Departments/Edit/${DepartmentId}`);
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
</script>

<style scoped>
.blurred {
  filter: blur(4px);
}
</style>
