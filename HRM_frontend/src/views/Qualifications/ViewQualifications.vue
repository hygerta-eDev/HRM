
 <template>
  <div class="container mx-auto p-6">
    <div class="edit-Qualification p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">

      <h1 class="text-2xl font-bold mb-6">View Qualification</h1>
      <div v-if="Qualification" class="Qualification-details flex flex-wrap">
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Qualification Name</label>
          <div class="input-container">
            <div class="input-content">{{ Qualification.name }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <div class="input-container">
            <div class="input-content">{{ Qualification.slug }}</div>
          </div>
        </div>
      </div>
      <div v-else class="loading text-center mt-4">
        <p>Loading...</p>
      </div>
      <div class="text-right mt-4">
        <router-link v-if="Qualification" :to="`/Companies/Edit/${Qualification.id}`">
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
const Qualification = ref(null);

const getQualification = () => {
  const QualificationId = Number(route.params.id);
  api.get(`/qualification/${QualificationId}`)
    .then(response => {
      Qualification.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching Qualification:', error);
    });
};

onMounted(getQualification);
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
