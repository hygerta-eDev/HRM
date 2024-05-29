<template >
  <div class="p-10" >
    <div class="container mx-auto " :class="{ 'blurred': deleteDialogVisible }">
      <div class="flex justify-between items-center mb-4" >
        <h2 class="text-3xl font-semibold">Ethnicities</h2>
        <router-link to="/Ethnicities/NewEthnicity">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Ethnicity</button>
        </router-link>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300 rounded-lg">
          <thead>
            <tr class="bg-sky-600">
              <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
              <th class="px-4 py-4 text-left w-1/2 text-base">Name</th>
              <th class="px-4 py-4 text-left w-1/2 text-base">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(Ethnicity, index) in paginatedEthnicities" :key="Ethnicity.id"
                :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
                class="border-b border-gray-300 hover:bg-blue-100">
              <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
              <td class="px-4 py-4 text-left text-base">{{ Ethnicity.name }}</td>

              <td class="px-4 py-4 actions text-left">
                <router-link :to="`/Ethnicities/${Ethnicity.id}`">
                  <i @click="viewEthnicity(Ethnicity.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                </router-link>
                <router-link :to="`/Ethnicities/Edit/${Ethnicity.id}`">
                  <i @click="editEthnicity(Ethnicity.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                </router-link>
                <i @click="confirmDelete(Ethnicity.id, Ethnicity.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- <Paginator :totalRecords="totalRecords" :rows="rowsPerPage" @onPageChange="onPageChange"></Paginator> -->
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"  :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Ethnicity "{{ EthnicityToDeleteName }}"?</p>
      <div class="flex justify-center mt-6">
        <Button label="Delete" @click="performDelete" class=" bg-red-500 border-red-500 ml-5" />
        <!-- <button @click="performDelete" class="bg-red-500 text-white py-2 px-4 rounded-lg">Delete</button> -->

        <Button label="Cancel" @click="cancelDelete" class="mr-3 ml-5" :style="{ backgroundColor: '#6B7280', borderColor: '#6B7280' }" />
        <!-- <button @click="cancelDelete" class="mr-3 bg-gray-400 text-white py-2 px-4 rounded-lg ml-5">Cancel</button> -->

      </div>
    </Dialog>
  </div>
</template>

<script setup>
  import Dialog from 'primevue/dialog';
  import Button from 'primevue/button';
  import { ref, onMounted, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import Paginator from 'primevue/paginator';
  import { toast } from 'vue3-toastify';

  const router = useRouter();
  const Ethnicities = ref([]);
  const totalRecords = ref(0);
  const currentPage = ref(0);
  const rowsPerPage = ref(100);
  const deleteDialogVisible = ref(false);
  const EthnicityToDeleteName = ref('');
  let EthnicityToDelete = null;

  const getAllEthnicities = () => {
    api.get('/ethnicities/active_ethnicities')
      .then(response => {
        console.log('All Ethnicities:', response.data);
        Ethnicities.value = response.data;
        totalRecords.value = response.data.length;
      })
      .catch(error => {
        console.error('Error fetching Ethnicities:', error);
      });
  };
  onMounted(getAllEthnicities);

  const onPageChange = (event) => {
    currentPage.value = event.page;
  };

  const paginatedEthnicities = computed(() => {
    const startIndex = currentPage.value * rowsPerPage.value;
    const endIndex = Math.min(startIndex + rowsPerPage.value, Ethnicities.value.length);
    return Ethnicities.value.slice(startIndex, endIndex);
  });

  const viewEthnicity = (EthnicityId) => {
    router.push(`/Ethnicities/${EthnicityId}`);
  };

  const editEthnicity = (EthnicityId) => {
    router.push(`/Ethnicities/Edit/${EthnicityId}`);
  };

  const confirmDelete = (EthnicityId, EthnicityName) => {
    EthnicityToDelete = EthnicityId;
    EthnicityToDeleteName.value = EthnicityName;
    deleteDialogVisible.value = true;
  };

  const cancelDelete = () => {
    EthnicityToDelete = null;
    EthnicityToDeleteName.value = '';
    deleteDialogVisible.value = false;
  };
  const performDelete = () => {
    if (EthnicityToDelete) {
      api.delete(`/ethnicities/delete_ethnicity/${EthnicityToDelete}`)
        .then(() => {
          deleteDialogVisible.value = false;
          getAllEthnicities();
          toast.success("Ethnicity deleted successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        })
        .catch(error => {
          console.error('Error deleting Ethnicity:', error);
          toast.error("Failed to delete Ethnicity!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        });
    }
  };


</script>

<style scoped>
.blurred {
  filter: blur(5px);
  pointer-events: none;
}

</style>
