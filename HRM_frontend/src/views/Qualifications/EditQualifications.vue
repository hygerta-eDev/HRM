
<template>
    <div class="container mx-auto p-6">
      <div class="edit-Qualification p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
  
      <h1 class="text-2xl font-bold mb-6">Edit Qualification</h1>
      <div v-if="Qualification" class="Qualification-details flex flex-wrap">
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Qualification Name</label>
          <input v-model="Qualification.name" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="Qualification.slug" type="text" class="w-full px-3 py-2 border border-blue-200 rounded-md shadow">
        </div>

        <div class="w-full text-right mt-4 px-2">
          <button @click="updateQualification" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow">Save</button>
          <router-link :to="`/Qualifications`">
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
  
  const updateQualification = () => {
  if (Qualification.value) {
    api.put(`/qualification/update_qualifications/${Qualification.value.id}`, Qualification.value)
      .then(response => {
        console.log('Qualification updated successfully:', response.data);
        router.push('/Qualifications');  
        setTimeout(() => {
          toast.success("Qualification edited successfully!", {
            autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });   
        }, 250);

      })
      .catch(error => {
        console.error('Error updating Qualification:', error);
      });
  }
};

  const cancelEdit = () => {
    // Redirect back to Qualification list or view page
  };
  
  onMounted(getQualification);
  </script>
  
  <style scoped>
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  