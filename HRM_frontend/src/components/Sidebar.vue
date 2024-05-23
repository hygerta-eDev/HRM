<template>
    <div class="h-screen bg-gray-800" id="side-bar" :class="dataOpenSideBar ? 'side-bar-visible' : 'side-bar-close'">
      <div class="bg-gray-700 h-[50px] flex justify-center items-center">
        <div class="text-xl font-bold text-center flex items-center justify-center text-white h-full" v-show="dataOpenSideBar">
          eTech - CyberOne - eDev
        </div>
        <img src="../assets/img/logo-etech.png" v-show="!dataOpenSideBar" class="p-1 w-9 h-9 rounded-full ring-2 ring-gray-100 dark:ring-gray-500" alt="Avatar" />
      </div>
      <div class="flex flex-col justify-between h-[calc(100vh-3rem)] bg-gray-900">
        <div class="menu-man text-left px-2 whitespace-nowrap">
          <div class="profile flex justify-center items-center text-center p-5">
            <div class="text-center text-white" v-show="dataOpenSideBar">
              <img src="../assets/img/logo-etech.png" class="p-1 w-24 h-24 rounded-full ring-2 ring-gray-300 dark:ring-gray-500 mb-4" alt="Avatar" />
              <h5 class="text-xl font-medium leading-tight mb-2"> User Logged </h5>
              <p class="text-gray-500">(Role)</p>
            </div>
          </div>
          <div class="py-3 rounded-sm cursor-pointer text-gray-300 hover:text-white">
            <router-link to="/dashboard" class="px-2 flex space-x-2">
              <span class="pi pi-home" v-tooltip="'Dashboard'"></span> 
              <span v-show="dataOpenSideBar">Dashboard</span>
            </router-link>
          </div>
          <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
            <router-link to="/Employee" class="px-2 flex space-x-2">
              <span class="pi pi-user" v-tooltip="'Employee'"></span> 
              <span v-show="dataOpenSideBar">Employee</span>
            </router-link>
          </div>
          <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
            <router-link to="/Trainings" class="px-2 flex space-x-2">
              <span class="pi pi-graduation-cap" v-tooltip="'Trainings'"></span>
              <span v-show="dataOpenSideBar">Trainings</span>
            </router-link>
          </div>
          <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
            <router-link to="/Leaves" class="px-2 flex space-x-2">
              <span class="pi pi-calendar" v-tooltip="'Leaves'"></span>
              <span v-show="dataOpenSideBar">Leaves</span>
            </router-link>
          </div>
          <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white" id="admin-dropdown" @click="toggleAdminDropdown">
            <div class="px-2 flex space-x-2 justify-between items-center">
              <div class="flex space-x-2">
                <span class="pi pi-shield" v-tooltip="'Administrator'"></span>
                <span v-show="dataOpenSideBar">Administrator</span>
              </div>
              <span class="pi pi-chevron-down" v-if="dataOpenSideBar"></span>
            </div>
            <div v-if="adminDropdownOpen" class="pl-6 mt-2 space-y-6" id="dropdown-menu"> <!-- Changed space-y-2 to space-y-4 -->
              <router-link to="/Companies" class="block text-gray-300 hover:text-white">Companies</router-link>
              <router-link to="/Departments" class="block text-gray-300 hover:text-white">Departments</router-link>
              <router-link to="/Jobs" class="block text-gray-300 hover:text-white">Jobs</router-link>
              <router-link to="/Qualifications" class="block text-gray-300 hover:text-white">Qualifications</router-link>
              <router-link to="/Ethnicity" class="block text-gray-300 hover:text-white">Ethnicity</router-link>
              <router-link to="/LeaveTypes" class="block text-gray-300 hover:text-white">LeaveTypes</router-link>
            </div>
          </div>
        </div>
        <div class="menu-man text-left px-2 justify-self-end whitespace-nowrap">
          <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
            <a href="#Settings" target="_blank" class="px-12 flex space-x-2 pi pi-cog"><span></span><span>Settings</span></a>
          </div>
        </div>
      </div>
    </div>
  </template>
  

  <script setup>
  import { ref, watch } from 'vue';
  
  const props = defineProps({
    dataOpenSideBar: Boolean,
    clickHamburger: Function
  });
  
  const adminDropdownOpen = ref(false);
  
  const toggleAdminDropdown = () => {
    adminDropdownOpen.value = !adminDropdownOpen.value;
  };
  
  // Watch for sidebar state change and close admin dropdown if sidebar is closed
  watch(() => props.dataOpenSideBar, (newValue) => {
    if (!newValue) {
      adminDropdownOpen.value = false;
    }
  });
  </script>
  
  <style scoped>
  #side-bar {
    overflow: hidden;
    transition: width 0.3s;
  }
  .side-bar-visible {
    width: 250px;
  }
  .side-bar-close {
    width: 50px;
  }
  .menu-man {
    transition: all 0.3s ease-in-out;
  }
  
  /* Responsive design */
  @media (max-width: 768px) {
    #side-bar {
      width: 100%;
      height: auto;
      position: absolute;
      z-index: 50;
    }
    .side-bar-visible {
      width: 100%;
      height: 100%;
    }
    .side-bar-close {
      width: 0;
    }
  }
  
  #dropdown-menu {
    padding-top: 10px;
  }
  </style>