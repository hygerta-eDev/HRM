<script setup>
import { ref, onMounted, watch } from 'vue';
import { api } from '@/api';
const sidebarOpen = ref(false);
const userMenuOpen = ref(false);


const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value;
};

const toggleUserMenu = () => {
    userMenuOpen.value = !userMenuOpen.value;
};
</script>
<template>
    <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
        <div class="px-4 py-4 lg:px-5 lg:pl-3">
            <div class="flex items-center justify-between">
                <div class="flex items-center justify-start rtl:justify-end">
                <!-- <button @click="toggleSidebar" aria-controls="logo-sidebar" type="button" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                    <span class="sr-only">Toggle Sidebar</span>
                    <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M4 6h16V5H4v1zm0 6h16v-1H4v1zm0 6h16v-1H4v1z"></path>
                    </svg>
                </button> -->
                    <a href="https://etech-rks.com" class="flex ms-2 md:me-24">
                        <img src="../assets/logo.jpeg" class="h-8 me-3" alt="eTech-CyberOne-eDev Logo" />
                        <span class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white">eTech-CyberOne-eDev</span>
                    </a>
                </div>
                <div class="relative"> <!-- This container is positioned relative to the viewport -->
                    <button @click="toggleUserMenu" type="button" class="flex items-center mr-5 bg-gray-800 rounded-full focus:outline-none focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" aria-expanded="false" data-dropdown-toggle="dropdown-user">
                        <span class="sr-only">Open user menu</span>
                        <img class="w-8 h-8 rounded-full lg:w-10 lg:h-10" src="https://flowbite.com/docs/images/people/profile-picture-5.jpg" alt="user photo">
                    </button>
                    <div :class="{ 'block': userMenuOpen, 'hidden':userMenuOpen }" class="absolute top-6 right-12 mt-2 w-48 bg-white shadow-lg rounded-md dark:bg-gray-700 lg:w-auto">
                        <div class="px-4 py-3" role="none">
                            <p class="text-sm text-gray-900 dark:text-white" role="none">
                                Neil Sims
                            </p>
                            <a href="#" class="text-sm font-medium text-gray-900 truncate dark:text-gray-300" role="none">
                                neil.sims@flowbite.com
                            </a>
                        </div>
                        <ul class="py-1" role="none">
                            <!-- <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Dashboard</a>
                            </li>
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Settings</a>
                            </li>
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Earnings</a>
                            </li> -->
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Sign out</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>