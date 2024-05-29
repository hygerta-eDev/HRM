 <template>
  <div class="container mx-auto p-6">
    <div class="create-Qualification p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Create New Qualification</h1>
      <div class="Qualification-details flex flex-wrap">
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Qualification Name</label>
          <input v-model="newQualification.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/2 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Description</label>
          <input v-model="newQualification.slug" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>

        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndCreateQualification" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
          <router-link :to="`/Qualifications`">
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
  const newQualification = ref({
    name: '',
    slug: '',
    active: false
  });

  const validateAndCreateQualification = () => {
    if (!newQualification.value.name || !newQualification.value.slug) {
      toast.error("Please fill in all required fields.", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
      return; 
    }

    newQualification.value.user_id = 1;
    api.post('/qualification/create_qualifications', newQualification.value)
      .then(response => {
        console.log('Qualification created successfully:', response.data);

        router.push('/Qualifications'); 
        setTimeout(() => {
            toast.success("Qualification created successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });      
        }, 250);
      })
      .catch(error => {
        console.error('Error creating Qualification:', error);
        toast.error("Failed to created Qualification!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };
</script>

<style scoped>
.create-Qualification {
  margin-top: 20px;
}
</style>