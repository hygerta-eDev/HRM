<template>
  <div :class="['sidebar', { 'sidebar-open': isOpen, 'sidebar-closed': !isOpen }]">
    <nav class="bg-gray-900 text-white p-4 shadow-lg flex justify-between items-center fixed top-0 inset-x-0 z-50">
      <button @click="toggleSidebar" class="flex items-center focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
      <div class="relative flex items-center">
        <button @click="toggleDropdown" class="flex items-center focus:outline-none mr-4">
          <span class="mr-2">MyProfile</span>
          <i class="pi pi-user" style="color: #fff"></i>
        </button>
        <transition name="fade">
          <div v-if="isDropdownOpen" class="absolute right-0 mt-60 w-48 bg-white rounded-md shadow-lg py-2 z-20">
            <!-- Profile Dropdown Content -->
            <div class="block px-4 py-2 text-gray-800">Profile Options</div>
            <a href="#" @click.prevent="viewProfile" class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out">View Profile</a>
            <a href="#" class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out">Settings</a>
            <a href="#" class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out">Logout</a>
          </div>
        </transition>
        <div class="relative">
          <button @click="toggleLanguageModal" class="flex items-center focus:outline-none mr-4">
            <img :src="flagIcon" alt="Language Flag" class="w-6 h-6 rounded-full">
          </button>
          <transition name="fade">
            <div v-if="isLanguageModalOpen" class="absolute right-0 mt-5 w-48 bg-white rounded-md shadow-lg py-2 z-20">
              <div class="block px-4 py-2 text-gray-800">{{$t('language')}}</div>
              <a href="#" @click.prevent="changeLanguage('en')" class="flex items-center px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out">
                <img src="../assets/img/england_flag.png" alt="English" class="w-6 h-6 mr-2 rounded-full" />
                {{$t('english')}}
              </a>
              <a href="#" @click.prevent="changeLanguage('al')" class="flex items-center px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out">
                <img src="../assets/img/albanian_flag1.png" alt="Albanian" class="w-6 h-6 mr-2 rounded-full" />
                {{$t('albanian')}}
              </a>
            </div>
          </transition>
        </div>
        <div class="relative">
          <button @click="toggleNotifications" class="flex items-center focus:outline-none mr-4">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-5-5.917V4a1 1 0 10-2 0v1.083A6.002 6.002 0 006 11v3.159c0 .417-.151.822-.405 1.136L4 17h5m0 0v1a3 3 0 006 0v-1m-6 0h6"></path>
            </svg>
          </button>
          <transition name="fade">
            <div v-if="isNotificationsOpen" class="absolute right-0 mt-5 w-48 bg-white rounded-md shadow-lg py-2 z-20">
              <div class="block px-4 py-2 text-gray-800">Notifications</div>
              <!-- Add your notification items here -->
              <div class="block px-4 py-2 text-gray-800">No new notifications</div>
            </div>
          </transition>
        </div>
        <div class="relative">
          <button @click="toggleDarkMode" class="flex items-center focus:outline-none">
            <svg v-if="!darkMode" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m8.66-10.66l-.707-.707M5.64 5.64l-.707-.707M21 12h-1M4 12H3m15.66 4.66l-.707-.707M5.64 18.36l-.707-.707M16 9a4 4 0 10-8 0 4 4 0 008 0z"></path>
            </svg>
            <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.293 17.293A8 8 0 1112 4a8.001 8.001 0 015.293 13.293z"></path>
            </svg>
          </button>
        </div>
      </div>
    </nav>


    <!-- Sidebar -->
    <transition name="slide">
      <div
        v-if="isSidebarOpen"
       class="fixed inset-y-0 left-0 z-40 w-64 bg-gray-900 text-white shadow-lg"
      >
        <div
          class="relative flex-1 flex flex-col max-w-xs w-full bg-gray-900 text-white shadow-lg"
        >
          <div class="absolute top-0 right-0 -mr-12 pt-2">
            <button
              @click="toggleSidebar"
              class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:bg-gray-600"
            >
              <span class="sr-only">Close sidebar</span>
              <svg
                class="h-6 w-6 text-white"
                stroke="currentColor"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                ></path>
              </svg>
            </button>
          </div>
          <div class="mt-16 flex-1 h-10">
            <div class="w-6/12 mb-16 ml-14">
              <img src="../assets/img/logo-etech.png" alt="" />
            </div>
            <nav class="px-2 space-y-2">
              <RouterLink
                to="/Dashboard"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-home mr-4"></i>
                Dashboard
              </RouterLink>
              <RouterLink
                to="/Employee"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-users mr-4"></i>
                Employee
              </RouterLink>
              <RouterLink
                to="/Assessments"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-th-large mr-4"></i>
                Assessments
              </RouterLink>
              <RouterLink
                to="/Trainings"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-book mr-4"></i>
                Trainings
              </RouterLink>
              <RouterLink
                to="/Leaves"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-calendar-minus mr-4"></i>
                Leaves
              </RouterLink>
              <RouterLink
                to="/Documents"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
              >
                <i class="pi pi-file mr-4"></i>
                Documents
              </RouterLink>
              <!-- Administrator Dropdown -->
              <div
                @click="toggleAdminDropdown"
                class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150 cursor-pointer"
              >
                <i class="pi pi-id-card mr-4"></i>
                Administrator
                <i
                  :class="{
                    'pi pi-chevron-down': isAdminDropdownOpen,
                    'pi pi-chevron-up': !isAdminDropdownOpen,
                  }"
                  class="ml-auto"
                ></i>
              </div>
              <transition name="fade">
                <div v-show="isAdminDropdownOpen" class="pl-8 space-y-2">
                  <RouterLink
                    to="/Companies"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                  <i class="fa-regular fa-building mr-4"></i>
                    Companies
                  </RouterLink>
                  <router-link
                    to="/Departments"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-briefcase mr-4"></i>
                    Departments
                  </router-link>
                  <RouterLink
                    to="/JobPositions"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-briefcase mr-4"></i>
                    Jobs
                  </RouterLink>
                  <RouterLink
                    to="/Qualifications"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-id-card mr-4"></i>
                    Qualifications
                  </RouterLink>
                  <RouterLink
                    to="/Ethnicities"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-users mr-4"></i>
                    Ethnicity
                  </RouterLink>
                  <RouterLink
                    to="/LeaveTypes"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-calendar-minus mr-4"></i>
                    Leave Types
                  </RouterLink>
                  <RouterLink
                    to="/Holidays"
                    class="group flex items-center px-2 py-2 text-xl leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
                  >
                    <i class="pi pi-calendar-minus mr-4"></i>
                    Holidays
                  </RouterLink>
                </div>
              </transition>
            </nav>
          </div>
        </div>
      </div>
    </transition>

    <!-- Sidebar Icons -->
    <transition name="slide">
      <div
        v-show="!isSidebarOpen"
         class="fixed inset-y-0 left-0 z-40 w-14 bg-gray-900 text-white shadow-lg mt-14"
      >
        <div class="relative flex-1 flex flex-col items-center py-4">
          <RouterLink
            to="/Dashboard"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Dashboard'"
          >
            <i class="pi pi-home mr-1 text-2xl"></i>
          </RouterLink>
          <RouterLink
            to="/Employee"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Employee'"
          >
            <i class="pi pi-users mr-1 text-2xl"></i>
          </RouterLink>
          <RouterLink
            to="/Assessments"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Assessments'"
          >
            <i class="pi pi-th-large mr-1 text-2xl"></i>
          </RouterLink>
          <RouterLink
            to="/Trainings"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Trainings'"
          >
            <i class="pi pi-book mr-1 text-2xl"></i>
          </RouterLink>
          <RouterLink
            to="/Leaves"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Leaves'"
          >
            <i class="pi pi-calendar-minus mr-1 text-2xl"></i>
          </RouterLink>
          <RouterLink
            to="/Documents"
            class="group flex items-center px-2 py-2 text-base leading-6 font-medium rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700 transition ease-in-out duration-150"
            v-tooltip="'Documents'"
          >
            <i class="pi pi-file mr-1 text-2xl"></i>
          </RouterLink>
        </div>
      </div>
    </transition>
    <!-- <div :class="{'ml-64': isSidebarOpen, 'ml-8': !isSidebarOpen}">
      <RouterView />
    </div> -->
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import axios from 'axios';

// Import images for flag icons
import englandFlag from '@/assets/img/england_flag.png';
import albanianFlag from '@/assets/img/albanian_flag1.png';

export default {
  setup() {
    const { locale } = useI18n();
    const isSidebarOpen = ref(true);
    const isAdminDropdownOpen = ref(false);
    const isDropdownOpen = ref(false);
    const isLanguageModalOpen = ref(false);
    const isNotificationsOpen = ref(false);
    const showProfile = ref(false); // Track if profile is being shown
    const employee = ref({}); // Employee profile data

    // Handle role if needed
    const userRole = ref(JSON.parse(localStorage.getItem('roles') || '[]'));

    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value;
      if (isDropdownOpen.value) {
        isLanguageModalOpen.value = false; 
        isNotificationsOpen.value = false; 
      }
    };

    const toggleSidebar = () => {
      isSidebarOpen.value = !isSidebarOpen.value;
    };

    const toggleAdminDropdown = () => {
      isAdminDropdownOpen.value = !isAdminDropdownOpen.value;
    };

    const toggleNotifications = () => {
      isNotificationsOpen.value = !isNotificationsOpen.value;
      if (isNotificationsOpen.value) {
        isDropdownOpen.value = false;
        isLanguageModalOpen.value = false; 
      }
    };

    const toggleLanguageModal = () => {
      isLanguageModalOpen.value = !isLanguageModalOpen.value;
      if (isLanguageModalOpen.value) {
        isDropdownOpen.value = false;
        isNotificationsOpen.value = false; 
 
      }
    };

    const viewProfile = async () => {
      try {
        const response = await axios.get('/api/employee/profile'); // Adjust URL as necessary
        employee.value = response.data;
        showProfile.value = true; // Show the profile view
        isLanguageModalOpen.value = false; // Ensure language modal is hidden when profile is opened
      } catch (error) {
        console.error('Error fetching profile data:', error);
      }
    };

    const changeLanguage = (lang) => {
      locale.value = lang;
      toggleLanguageModal();
    };

    const flagIcon = computed(() =>
      locale.value === 'en' ? englandFlag : albanianFlag
    );

    return {
      isDropdownOpen,
      isLanguageModalOpen,
      isNotificationsOpen,
      isAdminDropdownOpen,
      isSidebarOpen,
      showProfile,
      employee,
      toggleDropdown,
      toggleLanguageModal,
      viewProfile,
      changeLanguage,
      toggleSidebar,
      toggleAdminDropdown,
      toggleNotifications,
      flagIcon
    };
  }
};

</script>

<!-- <script>
import { useI18n } from "vue-i18n";
import usFlagIcon from '../assets/img/england_flag.png'; // Adjust the path as necessary
import alFlagIcon from '../assets/img/albanian_flag1.png';

export default {
  data() {
    return {
      isSidebarOpen: true,
      isAdminDropdownOpen: false,
      isDropdownOpen: false,
      isLanguageModalOpen: false,
      currentLanguage: 'en', // Default language

      userRole: JSON.parse(localStorage.getItem('roles') || '[]'), // Ensure role is an array
    };
  },
  computed: {
    isAdmin() {
      console.log(this.userRole);
      return this.userRole.includes(1); 
    },
    isUser() {
      return this.userRole.includes(3); 
    },
    flagIcon() {
      return this.currentLanguage === 'en' ? usFlagIcon : alFlagIcon;
    }
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    toggleAdminDropdown() {
      this.isAdminDropdownOpen = !this.isAdminDropdownOpen;
    },
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    changeLanguage(lang) {
      // Update the language using i18n instance from Vue
      this.$i18n.locale = lang;
    },
    toggleLanguageModal() {
      this.isLanguageModalOpen = !this.isLanguageModalOpen;
    },
    changeLanguage(lang) {
      // Update the language using i18n instance from Vue
      this.$i18n.locale = lang;
      this.currentLanguage = lang; // Update the current language
      this.toggleLanguageModal()
    },
    
  },
};
</script> -->

<style scoped>
/* Fade transition for dropdown */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease-in-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Slide transition for sidebar */
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease-in-out;
}
.slide-enter-from {
  transform: translateX(-100%);
}
.slide-leave-to {
  transform: translateX(-100%);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
.slide-enter-active {
  transition: transform 0.5s;
}
.slide-enter, .slide-leave-to {
  transform: translateX(-100%);
}
.ml-64 {
  margin-left: 0rem; /* Sidebar width */
}

.ml-8 {
  margin-left: -10rem; /* Negative margin to move left when sidebar is closed */
}


</style>
