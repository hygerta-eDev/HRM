<template>
    <div class="w-full bg-gray-100">
      <div class="flex justify-between items-center h-[50px] px-4 md:px-8">
        <div class="p-4 cursor-pointer hover:bg-gray-50" @click="clickHamburger">
          <i class="pi pi-bars"></i>
        </div>
        <div class="flex-1 flex justify-center py-2 md:max-w-lg">
          <InputText type="text" v-model="value" class="w-full md:w-auto" placeholder="Search..." />
        </div>
        <div class="flex space-x-3 items-center justify-center px-3">
          <div class="text-md">Admin</div>
          <Avatar
            icon="pi pi-bell"
            style="background-color: #dee9fc; color: #1a2551"
            @click="toggleNotifications"
            aria-haspopup="true"
            aria-controls="notifications_menu"
          />
          <Menu ref="notificationsMenu" id="notifications_menu" :model="notificationItems" :popup="true" />
          <Avatar
            icon="pi pi-user"
            style="background-color: #dee9fc; color: #1a2551"
            @click="toggleProfileMenu"
            aria-haspopup="true"
            aria-controls="profile_menu"
          />
          <Menu ref="profileMenu" id="profile_menu" :model="profileItems" :popup="true" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Avatar from 'primevue/avatar';
  import InputText from 'primevue/inputtext';
  import Menu from 'primevue/menu';
  
  // Define props
  const props = defineProps({
    dataOpenSideBar: Boolean,
    clickHamburger: Function
  });
  
  const profileMenu = ref();
  const notificationsMenu = ref();
  
  const profileItems = ref([
    {
      label: 'Options',
      items: [
        {
          label: 'Profile',
          icon: 'pi pi-user'
        },
        {
          label: 'Logout',
          icon: 'pi pi-sign-out'
        }
      ]
    }
  ]);
  
  const notificationItems = ref([
    {
      label: 'Notifications',
      items: [
        {
          label: 'Notification 1',
          icon: 'pi pi-bell'
        },
        {
          label: 'Notification 2',
          icon: 'pi pi-bell'
        },
        // Add more notifications as needed
      ]
    }
  ]);
  
  const toggleProfileMenu = (event) => {
    profileMenu.value.toggle(event);
  };
  
  const toggleNotifications = (event) => {
    notificationsMenu.value.toggle(event);
  };
  </script>
  
  <style scoped>
  /* Add responsive styles for the navbar */
  @media (max-width: 768px) {
    .pi-bars {
      font-size: 1.5rem; /* Adjust icon size for smaller screens */
    }
  
    .w-full {
      padding-left: 1rem;
      padding-right: 1rem;
    }
  
    .px-4 {
      padding-left: 1rem;
      padding-right: 1rem;
    }
  
    .md\:max-w-lg {
      max-width: 100%;
    }
  }
  </style>
  