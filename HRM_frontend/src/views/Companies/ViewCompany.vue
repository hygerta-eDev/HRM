<!-- <template>
  <div class="view-company bg-gray-100 p-8 max-w-md mx-auto">
    <h1 class="text-2xl font-bold mb-4">View Company</h1>
    <div v-if="institution" class="company-details bg-white rounded-lg shadow-md p-6">
      <h2 class="text-lg font-semibold mb-4">{{ institution.name }}</h2>
      <div class="overflow-x-auto">
        <table class="w-full table-auto">
          <tr>
            <th class="px-4 py-2">ID:</th>
            <td class="px-4 py-2">{{ institution.id }}</td>
          </tr>
          <tr>
            <th class="px-4 py-2">Name:</th>
            <td class="px-4 py-2">{{ institution.name }}</td>
          </tr>
          <tr>
            <th class="px-4 py-2">Slug:</th>
            <td class="px-4 py-2">{{ institution.slug }}</td>
          </tr>
          <tr>
            <th class="px-4 py-2">Active:</th>
            <td class="px-4 py-2">{{ institution.active ? 'Yes' : 'No' }}</td>
          </tr>
        </table>
      </div>
    </div>
    <div v-else class="loading text-center mt-4">
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';

export default {
  setup() {
    const route = useRoute();
    const institution = ref(null);

    onMounted(() => {
      const institution_id = Number(route.params.id);
      api.get(`/institutions/${institution_id}`)
        .then(response => {
          institution.value = response.data;
        })
        .catch(error => {
          console.error('Error fetching company:', error);
        });
    });

    return {
      institution
    };
  }
};
</script>

<style scoped>
.view-company {
  max-width: 600px;
}

.company-details {
  max-height: 400px; /* Limit the height to enable scrolling if necessary */
}

.loading {
  font-style: italic;
  color: #666;
}
</style>

 -->


 <template>
  <div class="container mx-auto p-6">
    <div class="edit-company p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">

      <h1 class="text-2xl font-bold mb-6">View Company</h1>
      <div v-if="company" class="company-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company Name</label>
          <div class="input-container">
            <div class="input-content">{{ company.name }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <div class="input-container">
            <div class="input-content">{{ company.slug }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-48">
            <InputSwitch class="" v-model="company.active" disabled />
          </div>
        </div>

      </div>
      <div v-else class="loading text-center mt-4">
        <p>Loading...</p>
      </div>
      <div class="text-right mt-4">
        <router-link v-if="company" :to="`/Companies/Edit/${company.id}`">
          <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">Edit</button>
        </router-link>
        <router-link :to="`/Companies`">
          <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow ml-2">Back</button>
        </router-link>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';
import InputSwitch from 'primevue/inputswitch';

const route = useRoute();
const company = ref(null);

const getCompany = () => {
  const companyId = Number(route.params.id);
  api.get(`/institutions/${companyId}`)
    .then(response => {
      company.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching company:', error);
    });
};

onMounted(getCompany);
</script>

<style scoped>
.input-container {
  width: 100%;
  background-color: #fff;
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-content {
  padding: 0.5rem;
}
</style>
