 <template>
  <div class="container mx-auto p-6">
    <div class="create-Ethnicity p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Create New Ethnicity</h1>
      <div class="Ethnicity-details flex flex-wrap">
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity Name</label>
          <input v-model="newEthnicity.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2 mt-6">
          <button @click="validateAndCreateEthnicity" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
          <router-link :to="`/Ethnicities`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
          </router-link>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import InputSwitch from 'primevue/inputswitch';
  import { toast } from 'vue3-toastify';

  const router = useRouter();
  const newEthnicity = ref({
    name: '',
  });

  const validateAndCreateEthnicity = () => {
    if (!newEthnicity.value.name ) {
      toast.error("Please fill in all required fields.", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
      return; 
    }

    newEthnicity.value.user_id = 1;
    api.post('/ethnicities/create_ethnicity', newEthnicity.value)
      .then(response => {
        console.log('Ethnicity created successfully:', response.data);

        router.push('/Ethnicities'); 
        setTimeout(() => {
            toast.success("Ethnicity created successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });      
        }, 250);
      })
      .catch(error => {
        console.error('Error creating Ethnicity:', error);
        toast.error("Failed to created Ethnicity!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };
</script>

<style scoped>
.create-Ethnicity {
  margin-top: 20px;
}
</style>