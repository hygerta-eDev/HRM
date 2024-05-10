<template>
 <aside :style="{ transform: sidebarOpen ? 'translateX(-80%)' :'translateX(0)' }" id="logo-sidebar" class="fixed top-0 left-0 z-40 w-64 h-screen pt-20 transition-transform bg-white border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700" aria-label="Sidebar">
    <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
        <button @click="toggleSidebar" class="absolute  right-0 mt-2 mr-2 block text-gray-900 dark:text-white focus:outline-none focus:text-white">
        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path v-if="sidebarOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/>
          <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
        <ul class="space-y-2 font-medium">
            <li>
                <a href="#" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
            
                    <span class="ms-3 text-left rtl:text-right whitespace-nowrap">{{$t('dashboard')}}</span>
          </a>
            </li>
            <li>
                <a href="/employees" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
                    <!-- <div  class=" block text-gray-900 dark:text-white focus:outline-none focus:text-white"> -->

                    <svg :style="{ transform: sidebarOpen ? 'translateX(-80%)' :'translateX(-1100%)' }" class="fixed right-0 ml-4 flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                    <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                </svg>
                <!-- </div> -->
                    <span class="flex-1 ms-3 ml-9 whitespace-nowrap">{{$t('employee')}}</span>
                </a>
            </li>
            <li>
                <a href="#" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
                    <img src="../assets/list.png" class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" alt="assessment Logo" />
                    <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">{{$t('assessment')}}</span>
                </a>
            </li>

            <li>
                <a href="#" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">

                <span class="flex-1 ms-3 whitespace-nowrap">{{$t('trainings')}}</span>
                </a>
            </li>
            <li>
                <a href="#" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">

                <span class="flex-1 ms-3 whitespace-nowrap">{{$t('leaves')}}</span>
                </a>
            </li>
            <li>
                <div>
                    <button @click="toggleDropdown" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700" aria-controls="dropdown-example" :aria-expanded="isDropdownOpen.toString()">
                        <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">{{$t('administrator')}}</span>
                        <svg v-if="!isDropdownOpen" class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                        </svg>
                        <svg v-else class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l-4-4-4 4"/>
                        </svg>
                    </button>
                    <ul v-if="isDropdownOpen" id="dropdown-example" class="py-2 space-y-2">
                        <li>
                            <a href="/departments" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('departments')}}</a>
                        </li>
                        <li>
                            <a href="/jobPositions" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('jobs')}}</a>
                        </li>
                        <li>
                            <a href="/qualifications" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('qualifications')}}</a>
                        </li>
                        <li>
                            <a href="/ethnicities" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('ethnicity')}}</a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('leaves')}}</a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{$t('Assessment_question')}}</a>
                        </li>
                    </ul>
                </div>
         </li>
            <!-- <li>
                <a href="#" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">
                <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                    <path d="M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z"/>
                </svg>
                <span class="flex-1 ms-3 whitespace-nowrap">{{$t('Attendance')}}</span>
                </a>
            </li> -->
        </ul>
    </div>
    </aside>
   
</template>
<script>
import { ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import DepartmentsView from '../views/DepartmentsView.vue'

export default {
  setup() {
    const sidebarOpen = ref(false);
    const isDropdownOpen = ref(false);
    const { t } = useI18n();

    const toggleSidebar = () => {
      sidebarOpen.value = !sidebarOpen.value;
    };

    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value;
    };

    const sidebarClass = computed(() => {
      return sidebarOpen.value ? 'translate-x-0' : '-translate-x-full';
    });

    return {
      sidebarOpen,
      isDropdownOpen,
      toggleSidebar,
      toggleDropdown,
      sidebarClass,
      t
    };
  }
};
</script>