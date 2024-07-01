
 <template>
  <div class="container mx-auto p-6">
    <div class="edit-leaveType p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">

      <h1 class="text-2xl font-bold mb-6">View leaveType</h1>
      <div v-if="leaveType" class="leaveType-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">leaveType Name</label>
          <div class="input-container">
            <div class="input-content">{{ leaveType.slug }}</div>
          </div>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <div class="input-container">
            <div class="input-content">{{ leaveType.limit }}</div>
          </div>
        </div>
      </div>
      <div v-else class="loading text-center mt-4">
        <p>Loading...</p>
      </div>
      <div class="text-right mt-4">
        <router-link v-if="leaveType" :to="`/LeaveTypes/Edit/${leaveType.id}`">
          <button class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow">Edit</button>
        </router-link>
        <router-link :to="`/LeaveTypes`">
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
const leaveType = ref(null);

const getleaveType = () => {
  const leaveTypeId = Number(route.params.id);
  api.get(`/leaveType/${leaveTypeId}`)
    .then(response => {
      leaveType.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching leaveType:', error);
    });
};

onMounted(getleaveType);
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
