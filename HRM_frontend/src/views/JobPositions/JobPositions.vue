<template>
  <div class="p-10">
    <div class="container mx-auto" :class="{ 'blurred': deleteDialogVisible }">

      <!-- New Job Position Button Aligned to the Right -->
      <div class="flex justify-end items-center mb-8">
        <router-link :to="`/JobPositions/NewJobPosition`">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Job Position</button>
        </router-link>
      </div>

      <!-- Departments and Job Positions Table -->
      <div v-for="(companyDepartments, companyId) in departmentsByCompany" :key="companyId" class="mb-8">
        <h2 class="text-3xl font-semibold mb-4 bg-blue-100 p-6 border border-gray-300">Departments of Company {{ getCompanyName(Number(companyId)) }}</h2>
        
        <div v-for="department in companyDepartments" :key="department.id" class="mb-8">
          <h3 class="text-2xl font-semibold mb-2 bg-blue-200 p-4 border border-gray-300 m-4">Job Positions in {{ department.name }}</h3>
          <template v-if="getJobPositionsByDepartment(department.id).length === 0">
            <div class="text-gray-500">
              No job positions for this department.
            </div>
          </template>
          <template v-else>
            <div class="overflow-x-auto">
              <table class="w-[1450px] border-collapse border border-gray-300 rounded-lg m-10">
                <thead>
                  <tr class="bg-sky-600 text-white">
                    <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
                    <th class="px-4 py-4 text-left w-1/5 text-base">Title</th>
                    <th class="px-4 py-4 text-left w-1/5 text-base">Description</th>
                    <th class="px-4 py-4 text-left w-1/5 text-base">Department</th>
                    <th class="px-4 py-4 text-left w-1/5 text-base">Active</th>
                    <th class="px-4 py-4 text-left w-1/5 text-base">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(job, index) in getJobPositionsByDepartment(department.id)" :key="job.id"
                    :class="{ 'bg-white': index % 2 === 0, 'bg-gray-200': index % 2 !== 0 }"
                    class="border-b border-gray-300 hover:bg-blue-100">
                    <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ index + 1 }}</td>
                    <td class="px-4 py-4 text-left text-base">{{ job.name }}</td>
                    <td class="px-4 py-4 text-left text-base">{{ job.slug }}</td>
                    <td class="px-4 py-4 text-left text-base">{{ getDepartmentName(job.department_id) }}</td>
                    <td class="px-4 py-4 text-left">
                      <span v-if="job.active" class="text-green-500">
                        <i class="fas fa-check-circle fa-lg"></i>
                      </span>
                      <span v-else class="text-red-500">
                        <i class="fas fa-times-circle fa-lg"></i>
                      </span>
                    </td>
                    <td class="px-4 py-4 actions text-left">
                      <router-link :to="`/JobPositions/${job.id}`" @click="onViewJob(job.id)">
  <i class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
</router-link>

                      <router-link :to="`/JobPositions/Edit/${job.id}`">
                        <i class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                      </router-link>
                      <i @click="confirmDeleteJob(job.id, job.title)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </template>
        </div>
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Job Position "{{ getJobPositionName(JobToDelete) }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class="bg-red-500 border-red-500 ml-5" />
        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
      </div>
    </Dialog>
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
const jobPositionsByDepartment = ref({});
const companies = ref([]);
const data = ref([]);
const deleteDialogVisible = ref(false);
const JobToDeleteTitle = ref('');
let JobToDelete = null;
const onViewJob = (jobId) => {
  console.log('Job ID:', jobId);
};

const getAllDepartments = () => {
  api.get('/departments/active_departments')
    .then(response => {
      const departmentsData = response.data; // Store the department data
      data.value = departmentsData; // Set the department data in the 'data' ref

      const groupedDepartments = {};
      departmentsData.forEach(department => {
        if (!groupedDepartments[department.institution_id]) {
          groupedDepartments[department.institution_id] = [];
        }
        groupedDepartments[department.institution_id].push(department);
      });
      departmentsByCompany.value = groupedDepartments;

      // Fetch job positions for each department
      getAllJobPositions();

      // Assuming you have a separate API to get company names
      getCompanies();
    })
    .catch(error => {
      console.error('Error fetching departments:', error);
    });
};

const getAllJobPositions = () => {
  api.get('/jobPosition/active_jobPosition')
    .then(response => {
      const data = response.data;
      const groupedJobPositions = {};
      data.forEach(job => {
        if (!groupedJobPositions[job.department_id]) {
          groupedJobPositions[job.department_id] = [];
        }
        groupedJobPositions[job.department_id].push(job);
      });
      jobPositionsByDepartment.value = groupedJobPositions;
    })
    .catch(error => {
      console.error('Error fetching job positions:', error);
    });
};

const getCompanies = () => {
  api.get('/institutions/active_institutions')
    .then(response => {
      companies.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching companies:', error);
    });
};

const getCompanyName = (companyId) => {
  const company = companies.value.find(company => company.id === companyId);
  return company ? company.name : 'Unknown Company';
};

const getDepartmentName = (departmentId) => {
  const department = data.value.find(department => department.id === departmentId);
  return department ? department.name : 'Unknown DEPARTMENT';
  // Implement a function to get department name by id from your data
};
const getJobPositionName = (jobId) => {
  const jobPositions = Object.values(jobPositionsByDepartment.value).flat();
  const job = jobPositions.find(job => job.id === jobId);
  return job ? job.name : 'Unknown Job Position';
};


const getJobPositionsByDepartment = (departmentId) => {
  return jobPositionsByDepartment.value[departmentId] || [];
};

onMounted(() => {
  getAllDepartments();
});

const confirmDeleteJob = (jobId, jobTitle) => {
  JobToDelete = jobId;
  JobToDeleteTitle.value = jobTitle;
  deleteDialogVisible.value = true;
};

const cancelDelete = () => {
  JobToDelete = null;
  JobToDeleteTitle.value = '';
  deleteDialogVisible.value = false;
};

const performDelete = () => {
  if (JobToDelete) {
    api.delete(`/jobPosition/delete_jobPosition/${JobToDelete}`)
      .then(() => {
        deleteDialogVisible.value = false;
        getAllJobPositions();
        toast.success("Job Position deleted successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      })
      .catch(error => {
        console.error('Error deleting job position:', error);
        toast.error("Failed to delete job position!", {
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
