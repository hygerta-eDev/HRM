<template>
  <div class="p-6 container">
    <!-- Company List -->
    <div>
      <h2 class="text-lg font-semibold mb-4">Companies</h2>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300">
          <thead>
            <tr class="bg-gray-200">
              <th class="px-4 py-2">Company Name</th>
              <th class="px-4 py-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="company in companies" :key="company.id" class="hover:bg-gray-100">
              <td class="px-4 py-2">{{ company.name }}</td>
              <td class="px-4 py-2 actions">
                <router-link :to="`/Companies/${company.id}`">
                  <button @click="viewCompany(company.id)" class="bg-green-500 text-white px-2 py-1 rounded-lg">View</button>
                </router-link>
                <router-link :to="`/Companies/EditCompany/${company.id}`">
                  <button @click="editCompany(company.id)" class="bg-yellow-500 text-white px-2 py-1 rounded-lg ml-2">Edit</button>
                </router-link>
                <button @click="deleteCompany(company.id)" class="bg-red-500 text-white px-2 py-1 rounded-lg ml-2">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- New Company Button -->
    <router-link to="/Companies/NewCompany">
      <button class="bg-blue-500 text-white px-4 py-2 mt-4 rounded-lg">New Company</button>
    </router-link>
    
    <!-- View Company Popup -->
    <div v-if="showViewCompanyModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 backdrop-blur-md flex justify-center items-center">
      <div class="bg-white rounded-lg p-6 w-full max-w-lg">
        <h3 class="text-xl font-semibold mb-4">Company Details</h3>
        <p><strong>Company Name:</strong> {{ selectedCompany?.name }}</p>
        <p><strong>Manager:</strong> {{ selectedCompany?.menager }}</p>
        <div class="text-right mt-4">
          <button @click="showViewCompanyModal = false" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Close</button>
        </div>
      </div>
    </div>
    
    <!-- Edit Company Popup -->
    <div v-if="showEditCompanyModal" class="fixed inset-0 bg-gray-800 bg-opacity-50 backdrop-blur-md flex justify-center items-center">
      <div class="bg-white rounded-lg p-6 w-full max-w-lg">
        <h3 class="text-xl font-semibold mb-4">Edit Company</h3>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company Name</label>
          <input v-model="editCompanyData.name" type="text" class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">Manager</label>
          <input v-model="editCompanyData.menager" type="text" class="w-full px-3 py-2 border rounded-md">
        </div>
        <div class="text-right">
          <button @click="updateCompany" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Save</button>
          <button @click="cancelEditCompany" class="bg-gray-400 text-white px-4 py-2 ml-2 rounded-lg">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

interface Company {
  id: number;
  name: string;
  menager: string;
}

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const showViewCompanyModal = ref<boolean>(false);
    const showEditCompanyModal = ref<boolean>(false);
    const selectedCompany = ref<Company | null>(null); // Company selected for viewing
    const editCompanyData = ref<Company>({ id: 0, name: '', menager: '' });

    // Dummy data for companies (replace this with your actual data)
    const companies = ref<Company[]>([
      { id: 1, name: 'eTech', menager: 'MenagersName' },
      { id: 2, name: 'CyberOne', menager: 'MenagersName' },
      { id: 3, name: 'eDev', menager: 'MenagersName' }
    ]);

    const getCompanyById = (id: number) => {
      return companies.value.find(company => company.id === id) || null;
    };

    const viewCompany = (id: number) => {
      selectedCompany.value = getCompanyById(id);
      showViewCompanyModal.value = true;
    };

    const editCompany = (id: number) => {
      const company = getCompanyById(id);
      if (company) {
        editCompanyData.value = { ...company };
        showEditCompanyModal.value = true;
      }
    };

    const updateCompany = () => {
      const index = companies.value.findIndex(c => c.id === editCompanyData.value.id);
      if (index !== -1) {
        companies.value[index] = { ...editCompanyData.value };
      }
      showEditCompanyModal.value = false;
    };

    const cancelEditCompany = () => {
      showEditCompanyModal.value = false;
    };

    const deleteCompany = (id: number) => {
      companies.value = companies.value.filter(company => company.id !== id);
    };

    onMounted(() => {
      const id = Number(route.params.id);
      if (route.path.includes('ViewCompany') && id) {
        viewCompany(id);
      }
      if (route.path.includes('EditCompany') && id) {
        editCompany(id);
      }
    });

    return {
      companies,
      showViewCompanyModal,
      showEditCompanyModal,
      selectedCompany,
      editCompanyData,
      viewCompany,
      editCompany,
      updateCompany,
      cancelEditCompany,
      deleteCompany
    };
  }
}
</script>

<style scoped>
.fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
