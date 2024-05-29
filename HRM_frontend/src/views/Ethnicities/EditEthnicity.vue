
<template>
    <div class="container mx-auto p-6">
      <div class="edit-Ethnicity p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
  
      <h1 class="text-2xl font-bold mb-6">Edit Ethnicity</h1>
      <div v-if="Ethnicity" class="Ethnicity-details flex flex-wrap">
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity Name</label>
          <input v-model="Ethnicity.name" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2 mt-6">

          <button @click="updateEthnicity" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/Ethnicities`">
            <button @click="cancelEdit" class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow">Cancel</button>
          </router-link>
        </div>


      </div>
      <div v-else class="loading">
        <p>Loading...</p>
      </div>
    </div>
  </div>
</template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  import InputSwitch from 'primevue/inputswitch';

  
  const route = useRoute();
  const router = useRouter();
  const Ethnicity = ref(null);

  
  const getEthnicity = () => {
    const EthnicityId = Number(route.params.id);
    api.get(`/ethnicities/${EthnicityId}`)
      .then(response => {
        Ethnicity.value = response.data;
      })
      .catch(error => {
        console.error('Error fetching Ethnicity:', error);
      });
  };
  
  const updateEthnicity = () => {
  if (Ethnicity.value) {
    api.put(`/ethnicities/update_ethnicity/${Ethnicity.value.id}`, Ethnicity.value)
      .then(response => {
        console.log('Ethnicity updated successfully:', response.data);
        router.push('/Ethnicities');  
        setTimeout(() => {
          toast.success("Ethnicity edited successfully!", {
            autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });   
        }, 250);

      })
      .catch(error => {
        console.error('Error updating Ethnicity:', error);
      });
  }
};

  const cancelEdit = () => {
    // Redirect back to Ethnicity list or view page
  };
  
  onMounted(getEthnicity);
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  