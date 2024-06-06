<template >
  <div class="p-10" >
    <div class="container mx-auto " :class="{ 'blurred': deleteDialogVisible }">
      <div class="flex justify-between items-center mb-4" >
        <h2 class="text-3xl font-semibold">Qualifications</h2>
        <router-link to="/Qualifications/NewQualifications">
          <button class="bg-sky-600 text-white px-4 py-2 rounded-lg">New Qualification</button>
        </router-link>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse border border-gray-300 rounded-lg">
          <thead>
            <tr class="bg-sky-600">
              <th class="px-4 py-4 text-left text-base border-r border-black-900">No</th>
              <th class="px-4 py-4 text-left w-1/3 text-base">Name</th>
              <th class="px-4 py-4 text-left w-1/3 text-base">Descriptions</th>
              <th class="px-4 py-4 text-left w-1/3 text-base">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(Qualification, index) in paginatedQualifications" :key="Qualification.id"
                :class="{ 'bg-white-100': index % 2 === 0, 'bg-gray-300': index % 2 !== 0 }"
                class="border-b border-gray-300 hover:bg-blue-100">
              <td class="px-4 py-4 text-left text-base border-r border-black-900">{{ (currentPage * rowsPerPage) + index + 1 }}</td>
              <td class="px-4 py-4 text-left text-base">{{ Qualification.name }}</td>
              <td class="px-4 py-4 text-left text-base">{{ Qualification.slug }}</td>

              <td class="px-4 py-4 actions text-left">
                <router-link :to="`/Qualifications/${Qualification.id}`">
                  <i @click="viewQualification(Qualification.id)" class="fas fa-eye fa-lg text-green-500 cursor-pointer"></i>
                </router-link>
                <router-link :to="`/Qualifications/Edit/${Qualification.id}`">
                  <i @click="editQualification(Qualification.id)" class="fas fa-edit fa-lg text-yellow-500 cursor-pointer ml-6"></i>
                </router-link>
                <i @click="confirmDelete(Qualification.id, Qualification.name)" class="fas fa-trash-alt fa-lg text-red-500 cursor-pointer ml-6"></i>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- <Paginator :totalRecords="totalRecords" :rows="rowsPerPage" @onPageChange="onPageChange"></Paginator> -->
      </div>
    </div>

    <Dialog v-model:visible="deleteDialogVisible" header="Confirm" @hide="cancelDelete" class="w-[575px]"  :breakpoints="{ '1199px': '75vw', '575px': '90vw' }">
      <p>Are you sure you want to delete the Qualification "{{ QualificationToDeleteName }}"?</p>
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
  const Qualifications = ref([]);
  const totalRecords = ref(0);
  const currentPage = ref(0);
  const rowsPerPage = ref(100);
  const deleteDialogVisible = ref(false);
  const QualificationToDeleteName = ref('');
  let QualificationToDelete = null;

  const getAllQualifications = () => {
    api.get('/qualification/active_qualifications')
      .then(response => {
        console.log('All Qualifications:', response.data);
        Qualifications.value = response.data;
        totalRecords.value = response.data.length;
      })
      .catch(error => {
        console.error('Error fetching Qualifications:', error);
      });
  };
  onMounted(getAllQualifications);

  const onPageChange = (event) => {
    currentPage.value = event.page;
  };

  const paginatedQualifications = computed(() => {
    const startIndex = currentPage.value * rowsPerPage.value;
    const endIndex = Math.min(startIndex + rowsPerPage.value, Qualifications.value.length);
    return Qualifications.value.slice(startIndex, endIndex);
  });

  const viewQualification = (QualificationId) => {
    router.push(`/Qualifications/${QualificationId}`);
  };

  const editQualification = (QualificationId) => {
    router.push(`/Qualifications/Edit/${QualificationId}`);
  };

  const confirmDelete = (QualificationId, QualificationName) => {
    QualificationToDelete = QualificationId;
    QualificationToDeleteName.value = QualificationName;
    deleteDialogVisible.value = true;
  };

  const cancelDelete = () => {
    QualificationToDelete = null;
    QualificationToDeleteName.value = '';
    deleteDialogVisible.value = false;
  };
  const performDelete = () => {
    if (QualificationToDelete) {
      api.delete(`/qualification/delete_qualification/${QualificationToDelete}`)
        .then(() => {
          deleteDialogVisible.value = false;
          getAllQualifications();
          toast.success("Qualification deleted successfully!", {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        })
        .catch(error => {
          console.error('Error deleting Qualification:', error);
          toast.error("Failed to delete Qualification!", {
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
