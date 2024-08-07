<template>
  <div class="container mx-auto p-6">
    <!-- Breadcrumbs -->
    <div class="relative mb-6">
      <nav class="flex items-center text-sm text-gray-700">
        <router-link to="/Dashboard" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-home text-lg mr-2"></i> Home
        </router-link>
        <span class="mx-2">/</span>
        <router-link to="/Administrator" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-user-cog text-lg mr-2"></i> Administrator
        </router-link>
        <span class="mx-2">/</span>
        <router-link to="/Departments" class="text-blue-500 hover:underline flex items-center">
          <i class="fas fa-building text-lg mr-2"></i> Departments
        </router-link>
        <span class="mx-2">/</span>
        <span class="font-semibold">Edit Department</span>
      </nav>
    </div>

    <div class="shadow-2xl rounded-lg border border-blue-500 relative mt-12 bg-white">
      <div class="absolute inset-x-0 -top-5 flex justify-center">
        <h1 class="text-3xl font-bold text-gray-800 bg-white px-4 relative z-10">
          Edit Department
        </h1>
      </div>
      <div class="pt-12 px-8 pb-8">
        <div v-if="Department" class="grid grid-cols-1 md:grid-cols-2 gap-8 p-10">
          <!-- Department Name -->
          <div class="w-full">
            <label for="departmentName" class="block text-sm font-semibold mb-2 text-gray-700">Department Name</label>
            <div class="input-container">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 160" class="absolute left-3 w-5 h-5" fill="gray" stroke="currentColor" stroke-width="4">
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
              <input v-model="Department.name" type="text" id="departmentName" class="w-full py-3 pl-10 px-3 bg-gray-100 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
          </div>

          <!-- Slug -->
          <div class="w-full">
            <label for="slug" class="block text-sm font-semibold mb-2 text-gray-700">Slug</label>
            <div class="input-container">
              <i class="fas fa-tag input-icon"></i>
              <input v-model="Department.slug" type="text" id="slug" class="w-full  pl-10 px-3 bg-gray-100 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
          </div>

          <!-- Company -->
          <div class="w-full">
            <label for="company" class="block text-sm font-semibold mb-2 text-gray-700">Company</label>
            <div class="input-container">
              <i class="fas fa-building input-icon"></i>
              <select v-model="Department.institution_id" id="company" class="w-full pl-10 px-3 py-2 bg-gray-100 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                <option value="" disabled>Select a Company</option>
                <option v-for="company in activeCompanies" :key="company.id" :value="company.id">{{ company.name }}</option>
              </select>
            </div>
          </div>

          <!-- Active -->
          <div class="w-full">
            <label for="active" class="block text-sm font-semibold mb-2 text-gray-700">Active</label>
            <div class="flex items-center justify-center mt-2">
              <InputSwitch v-model="Department.active" />
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-else class="text-center mt-4">
          <p>Loading...</p>
        </div>

        <!-- Action Buttons -->
        <div class="mt-6 flex justify-end gap-4">
          <button @click="updateDepartment" class="bg-blue-600 text-white px-6 py-2 rounded-lg shadow-md font-bold hover:bg-blue-700 transition duration-300">Save</button>
          <router-link to="/Departments">
            <button @click="cancelEdit" class="bg-gray-500 text-white px-6 py-2 rounded-lg shadow-md hover:bg-gray-600 transition font-bold duration-300">Cancel</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { api } from '@/api';
import InputSwitch from 'primevue/inputswitch';
import { toast } from 'vue3-toastify';

const route = useRoute();
const router = useRouter();
const Department = ref(null);
const activeCompanies = ref([]);

const getActiveCompanies = () => {
  api.get('institutions/active_institutions')
    .then(response => {
      activeCompanies.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching active companies:', error);
    });
};

const getDepartment = () => {
  const DepartmentId = Number(route.params.id);
  api.get(`/departments/${DepartmentId}`)
    .then(response => {
      Department.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Department:', error);
    });
};

const updateDepartment = () => {
  if (Department.value) {
    api.put(`/departments/update_department/${Department.value.id}`, Department.value)
      .then(response => {
        console.log('Department updated successfully:', response.data);
        router.push('/Departments');  
        toast.success("Department edited successfully!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });   
      })
      .catch(error => {
        console.error('Error updating Department:', error);
      });
  }
};

const cancelEdit = () => {
  // Redirect back to Department list or view page
};

onMounted(() => {
  getActiveCompanies();
  getDepartment();
});
</script>

<style scoped>
.input-container {
  position: relative;
  display: flex;
  align-items: center;
  background-color: #fff;
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-icon {
  position: absolute;
  left: 0.75rem;
  color: #4a5568;
  
}
.input-content {
  padding: 0.5rem;
  flex: 1;
  margin-right: 20px;
}
.relative {
  position: relative;
}

.text-gray-700 {
  color: #4a5568;
}

.shadow-lg {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.border-blue-500 {
  border-color: #3b82f6;
}

.absolute {
  position: absolute;
}
</style>
