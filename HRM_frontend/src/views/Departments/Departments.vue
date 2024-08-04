<!-- <template>
  <div>
    <div class="p-10">
      <div class="container mx-auto p-6 bg-white shadow-xl rounded-lg border-blue-800" :class="{ 'blurred': deleteDialogVisible }">
        
        <div class="relative mb-6">
          <nav class="flex items-center text-sm text-gray-700">
            <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
              <i class="fas fa-home text-lg mr-2"></i>
              {{ $t('home') }}
            </router-link>
            <span class="mx-2">></span>
            <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
              <i class="fas fa-user-cog text-lg mr-2"></i>
              {{ $t('administrator') }}
            </router-link>
            <span class="mx-2">></span>
            <span class="font-semibold">{{ $t('departments') }}</span>
          </nav>
        </div>

        <div class="flex justify-between items-center mb-4 mt-16">
          <h2 class="text-3xl font-semibold">{{ $t('all_departments') }}</h2>
          <router-link to="/Departments/NewDepartment">
            <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
              <i class="fas fa-plus-circle fa-lg mr-2"></i>{{ $t('new_department') }}
            </button>
          </router-link>
        </div>

        <div v-for="(departments, companyId) in departmentsByCompany" :key="companyId" class="mb-8">
          <h3 class="text-2xl font-semibold mb-4">{{ getCompanyName(companyId) }}</h3>
          <div class="overflow-x-auto shadow-3xl rounded-lg border-2 border-blue-300">
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

        <Dialog v-model:visible="deleteDialogVisible" :header="$t('confirm')" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete', { departmentName: DepartmentToDeleteName }) }}</p>
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
import { ref, onMounted } from 'vue';
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
</script>

<style scoped>
.blurred {
  filter: blur(5px);
  pointer-events: none;
}
</style> -->
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
              placeholder="{{ $t('search') }}"
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
        <div v-if="Object.keys(filteredDepartments).length === 0" class="p-4 text-center text-gray-500">
          {{ $t('no_records_found') }}
        </div>
        <div v-else>
          <div v-for="(departments, companyId) in filteredDepartments" :key="companyId" class="mb-8">
            <h3 class="text-2xl font-semibold mb-4">{{ getCompanyName(companyId) }}</h3>
            <div v-if="departments.length === 0" class="p-4 text-center text-gray-500">
              {{ $t('no_records_found') }}
            </div>
            <div v-else class="overflow-x-auto shadow-2xl drop-shadow-2xl border border-blue-200 rounded-lg border border-blue-500 shadow-3xl rounded-lg border-2 border-blue-300">
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

        <!-- Delete Confirmation Dialog -->
        <Dialog v-model:visible="deleteDialogVisible" :header="$t('confirm')" @hide="cancelDelete" class="w-[575px] bg-white" :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
          <p>{{ $t('confirm_delete', { departmentName: DepartmentToDeleteName }) }}</p>
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
  if (!departmentsByCompany.value || !Array.isArray(companies.value)) {
    return {};
  }

  const query = searchQuery.value.toLowerCase(); 
  const filtered = {};

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

  return selectedCompany.value && filtered[selectedCompany.value] ? { [selectedCompany.value]: filtered[selectedCompany.value] } : filtered;
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
