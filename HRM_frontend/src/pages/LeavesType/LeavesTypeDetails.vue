<!-- <script setup>
import { push } from 'notivue'
import { ref } from 'vue';

const notive = ref({
  isRunning: true
});
</script>

<template>
  <div class="p-4 sm:ml-64">
    <h1>LeaveType Details</h1>
    <button @click="push.success('Hi! I am your first notification!')">Push</button>

    <Notivue :item="notive.value">
      Render your notifications or use isRunning as needed 
      <Notification v-if="notive.value.isRunning" :item="item" />
    </Notivue>
  </div>
</template> -->

<template>
  <div>
    <button @click="notify">Notify!</button>
  </div>
</template>

<script setup>
import { toast } from 'vue3-toastify';

const notify = () => {
  toast("Wow, so easy!", {
    autoClose: 5000,
    position: toast.POSITION.TOP_RIGHT,
  });
};
</script>
