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
            <span class="font-semibold">{{ $t('job_positions') }}</span>
          </nav>
        </div>

        <!-- Search and Filter Box -->
        <div class="mt-10 bg-gray-100 p-10 shadow-2xl border border-blue-100 mb-8 flex items-center space-x-4">
          <!-- Search Input -->
          <div class="relative flex-grow mr-4 max-w-xs">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="{{ $t('search') }}"
              @input="filterJobPositions"
              class="border border-gray-300 rounded-lg px-4 py-2 pl-10 shadow-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <i class="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
          </div>
          
          <!-- Company Dropdown -->
          <div class="relative flex-shrink-0 w-64">
            <select 
              v-model="selectedCompany" 
              @change="onCompanyChange" 
              class="block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-md bg-white text-gray-700 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 appearance-none transition duration-150 ease-in-out">
              <option value="" class="py-2 px-4 hover:bg-blue-100">{{ $t('all_companies') }}</option>
              <option v-for="company in companies" :key="company.id" :value="company.id" class="py-2 px-4 hover:bg-blue-100">
                {{ company.name }}
              </option>
            </select>
            <i class="fas fa-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
          </div>

          <!-- Department Dropdown -->
          <div class="relative flex-shrink-0 w-64">
            <select 
              v-model="selectedDepartment" 
              @change="filterJobPositions" 
              class="block w-full px-4 py-2 border border-gray-300 rounded-lg shadow-md bg-white text-gray-700 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 appearance-none transition duration-150 ease-in-out">
              <option value="" class="py-2 px-4 hover:bg-blue-100">{{ $t('all_departments') }}</option>
              <option v-for="department in filteredDepartments" :key="department.id" :value="department.id" class="py-2 px-4 hover:bg-blue-100">
                {{ department.name }}
              </option>
            </select>
            <i class="fas fa-chevron-down absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 pointer-events-none"></i>
          </div>
        </div>

        <!-- New Job Position Button Aligned to the Right -->
        <div class="flex justify-end items-center mb-8">
          <router-link :to="`/JobPositions/NewJobPosition`">
            <button class="bg-sky-600 text-white px-4 py-2 rounded-lg hover:bg-sky-700 transition duration-300 flex items-center shadow-md">
              <i class="fas fa-plus-circle fa-lg mr-2"></i>{{ $t('new_job_position') }}
            </button>
          </router-link>
        </div>

        <!-- Dynamic Header and Button -->
        <div class="flex justify-between items-center mb-4 mt-8">
          <h2 class="text-3xl font-semibold">
            {{ selectedCompany ? `${$t('all_job_positions_of')} ${getCompanyName(selectedCompany)}` : $t('all_job_positions') }}
          </h2>
        </div>

        <!-- Job Positions Table by Company -->
        <div v-if="Object.keys(filteredJobPositions).length === 0" class="p-4 text-center text-gray-500">
          {{ $t('no_records_found') }}
        </div>
        <div v-else>
          <div v-for="(jobPositions, companyId) in filteredJobPositions" :key="companyId" class="mb-8">
            <h3 class="text-2xl font-semibold mb-4">{{ getCompanyName(companyId) }}</h3>
            <div v-if="jobPositions.length === 0" class="p-4 text-center text-gray-500">
              {{ $t('no_records_found') }}
            </div>
            <div v-else class="overflow-x-auto shadow-2xl drop-shadow-2xl border border-blue-200 rounded-lg">
              <table class="min-w-full border-collapse">
                <thead>
                  <tr class="bg-sky-600 text-white">
                    <th class="w-16 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('no') }}</th>
                    <th class="w-32 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('title') }}</th>
                    <th class="w-48 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('description') }}</th>
                    <th class="w-32 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('department') }}</th>
                    <th class="w-20 px-4 py-4 text-base border-r border-gray-200 text-center font-semibold">{{ $t('active') }}</th>
                    <th class="w-40 px-4 py-4 text-base text-center font-semibold">{{ $t('actions') }}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(job, index) in jobPositions" :key="job.id"
                      :class="{ 'bg-white': index % 2 === 0, 'bg-gray-100': index % 2 !== 0 }"
                      class="border-b border-gray-300 hover:bg-blue-100 transition duration-200">
                    <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ index + 1 }}</td>
                    <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ job.name }}</td>
                    <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ job.slug }}</td>
                    <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">{{ getDepartmentName(job.department_id) }}</td>
                    <td class="rounded-lg px-4 py-4 text-base border-r border-gray-200 text-center">
                      <div class="flex items-center justify-center h-full">
                        <span v-if="job.active" class="text-green-500">
                          <i class="fas fa-check-circle fa-lg"></i>
                        </span>
                        <span v-else class="text-red-500">
                          <i class="fas fa-times-circle fa-lg"></i>
                        </span>
                      </div>
                    </td>
                    <td class="rounded-lg px-4 py-4 text-center">
                      <div class="flex items-center justify-center h-full space-x-6">
                        <router-link :to="`/JobPositions/${job.id}`" @click="onViewJob(job.id)">
                          <i class="fas fa-eye fa-lg text-green-500 cursor-pointer hover:text-green-600 transition duration-300"></i>
                        </router-link>
                        <router-link :to="`/JobPositions/Edit/${job.id}`">
                          <i class="fas fa-edit fa-lg text-yellow-500 cursor-pointer hover:text-yellow-600 transition duration-300"></i>
                        </router-link>
                        <i @click="confirmDeleteJob(job.id, job.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer hover:text-red-600 transition duration-300"></i>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px] bg-white"
              :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
        <p>Are you sure you want to delete the Job Position "{{ getJobPositionName(JobToDelete) }}"?</p>
        <div class="flex justify-center mt-6">
          <Button label="Delete" @click="performDelete" class="bg-red-500 border-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition duration-300 ml-5 shadow-md" />
          <Button label="Cancel" @click="cancelDelete" class="bg-slate-400 border-gray-500 text-white py-2 px-4 rounded-lg hover:bg-gray-900 transition duration-300 mr-3 ml-5 shadow-md" />
        </div>
      </Dialog>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();
const router = useRouter();

const companies = ref([]);
const departments = ref([]);
const selectedCompany = ref('');
const selectedDepartment = ref('');
const jobPositions = ref([]);
const searchQuery = ref('');
const filteredJobPositions = ref({});
const filteredDepartments = ref([]);
const deleteDialogVisible = ref(false);
const JobToDelete = ref(null);

onMounted(async () => {
  await fetchCompanies();
  await fetchDepartments();
  await fetchJobPositions();
});

const fetchCompanies = async () => {
  try {
    const response = await api.get('/institutions/active_institutions');
    companies.value = response.data;
  } catch (error) {
    console.error('Failed to fetch companies:', error);
  }
};

const fetchDepartments = async () => {
  try {
    const response = await api.get('/departments/active_departments');
    departments.value = response.data;
  } catch (error) {
    console.error('Failed to fetch departments:', error);
  }
};

const fetchJobPositions = async () => {
  try {
    const response = await api.get('/jobPosition/active_jobPosition');
    jobPositions.value = response.data;
    filterJobPositions();
  } catch (error) {
    console.error('Failed to fetch job positions:', error);
  }
};

const onCompanyChange = () => {
  filterDepartments();
  filterJobPositions();
};

const filterDepartments = () => {
  if (selectedCompany.value) {
    filteredDepartments.value = departments.value.filter(dept => dept.company_id === selectedCompany.value);
  } else {
    filteredDepartments.value = [];
  }
};

const filterJobPositions = () => {
  const query = searchQuery.value.toLowerCase();
  const companyFilter = selectedCompany.value ? job => job.company_id === selectedCompany.value : () => true;
  const departmentFilter = selectedDepartment.value ? job => job.department_id === selectedDepartment.value : () => true;

  filteredJobPositions.value = groupJobPositionsByCompany(
    jobPositions.value
      .filter(job => companyFilter(job) && departmentFilter(job))
      .filter(job => job.name.toLowerCase().includes(query))
  );
};

const groupJobPositionsByCompany = (jobPositions) => {
  return jobPositions.reduce((acc, job) => {
    if (!acc[job.company_id]) {
      acc[job.company_id] = [];
    }
    acc[job.company_id].push(job);
    return acc;
  }, {});
};

const getCompanyName = (companyId) => {
  const company = companies.value.find(company => company.id === companyId);
  return company ? company.name : '';
};

const getDepartmentName = (departmentId) => {
  const department = departments.value.find(dept => dept.id === departmentId);
  return department ? department.name : '';
};

const onViewJob = (jobId) => {
  // Handle the view job action
};

const confirmDeleteJob = (jobId, jobName) => {
  JobToDelete.value = { id: jobId, name: jobName };
  deleteDialogVisible.value = true;
};

const performDelete = async () => {
  try {
    await api.delete(`/jobPositions/delete_jobPosition/${JobToDelete.value.id}`);
    deleteDialogVisible.value = false;
    await fetchJobPositions();
  } catch (error) {
    console.error('Failed to delete job position:', error);
  }
};

const cancelDelete = () => {
  deleteDialogVisible.value = false;
  JobToDelete.value = null;
};

const getJobPositionName = (job) => job ? job.name : '';
</script>

<style scoped>
.blurried {
  filter: blur(5px);
}
</style>
