 <template>
  <div class="container mx-auto p-6">
    <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Create New Company</h1>
      <div class="company-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Company Name</label>
          <input v-model="newCompany.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Slug</label>
          <input v-model="newCompany.slug" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0  px-2">
          <label class="mr-5 block text-gray-700 text-sm font-bold items-center">Active</label>
          <div class="flex items-center mt-3 ml-48">
            <InputSwitch class="" v-model="newCompany.active"  />
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndCreateCompany" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Create</button>
          <router-link :to="`/Companies`">
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
  const newCompany = ref({
    name: '',
    slug: '',
    active: false
  });

  const validateAndCreateCompany = () => {
    if (!newCompany.value.name || !newCompany.value.slug) {
      toast.error("Please fill in all required fields.", {
        autoClose: 3000,
        position: toast.POSITION.TOP_RIGHT,
      });
      return; 
    }

    newCompany.value.user_id = 1;
    api.post('/institutions/create_institution', newCompany.value)
      .then(response => {
        console.log('Company created successfully:', response.data);

        router.push('/Companies'); 
        setTimeout(() => {
            toast.success("Company created successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });      
        }, 250);
      })
      .catch(error => {
        console.error('Error creating company:', error);
        toast.error("Failed to created company!", {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };
</script>

<style scoped>
.create-company {
  margin-top: 20px;
}
</style>