<template>
  <div>
    <!-- Navbar -->
    <nav
      class="bg-gray-900 text-white p-4 shadow-lg flex justify-between items-center fixed top-0 inset-x-0 z-50"
    >
      <button
        @click="toggleSidebar"
        class="flex items-center focus:outline-none"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16M4 18h16"
          ></path>
        </svg>
      </button>
      <div class="relative">
        <button
          @click="toggleDropdown"
          class="flex items-center focus:outline-none"
        >
          <span class="mr-2">MyProfile</span>
          <i class="pi pi-user" style="color: #fff"></i>
        </button>
        <transition name="fade">
          <div
            v-if="isDropdownOpen"
            class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-2 z-20"
          >
            <a
              href="#"
              class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out"
              >Profile</a
            >
            <a
              href="#"
              class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out"
              >Logout</a
            >
            <div class="block px-4 py-2 text-gray-800">Language</div>
            <a
              href="#"
              @click.prevent="changeLanguage('en')"
              class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out"
              >English</a
            >
            <a
              href="#"
              @click.prevent="changeLanguage('al')"
              class="block px-4 py-2 text-gray-800 hover:bg-gray-200 transition duration-150 ease-in-out"
              >Albanian</a
            >
          </div>
        </transition>
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
                v-if="isAdmin"
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
                    <i class="pi pi-briefcase mr-4"></i>
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
  </div>
</template>

<script>
import { useI18n } from "vue-i18n";

export default {
  data() {
    return {
      isSidebarOpen: true,
      isAdminDropdownOpen: false,
      isDropdownOpen: false,
      userRole: JSON.parse(localStorage.getItem('roles') || '[]'), // Ensure role is an array
    };
  },
  computed: {
    isAdmin() {
      console.log(this.userRole);
      return this.userRole.includes(1); // Ensure role ID is correctly compared
    },
    isUser() {
      return this.userRole.includes(3); // Ensure role ID is correctly compared
    },
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
    }
    
  },
};
</script>

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
</style>
