<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white p-8 rounded-lg shadow-md">
      <h3 class="text-lg font-semibold mb-4">Confirm Deletion</h3>
      <p class="mb-4">Are you sure you want to delete this {{ itemType }}?</p>
      <div class="flex justify-end">
        <button @click="cancelDelete" class="mr-4 px-4 py-2 bg-gray-200 text-gray-800 rounded-md">Cancel</button>
        <button @click="confirmDelete" class="px-4 py-2 bg-red-600 text-white rounded-md">Delete</button>
      </div>
    </div>
  </div>
</template>

  
  <script setup>
  // import { defineProps, defineEmits } from 'vue';
  
//   const props = defineProps();
import { ref, onMounted } from 'vue';

  const { departmentId } = defineProps();
  const itemType = ref('');
  const emit = defineEmits();
  
  const cancelDelete = () => {
    emit('cancel');
  };
  const confirmDelete = () => {
  // Perform the deletion based on the type of item (department or qualification)
  if (itemType.value === 'department') {
    emit('confirmDelete', departmentId);
    // Delete department logic
  } else if (itemType.value === 'qualification') {
    emit('confirmDelete', departmentId);
    // Delete qualification logic
  }
};
  // const confirmDelete = () => {
  //   emit('confirmDelete', departmentId);
  // };
  </script>
  