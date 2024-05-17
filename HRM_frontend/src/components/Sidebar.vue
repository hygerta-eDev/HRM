<template>
    <div class="h-screen bg-gray-800" id="side-bar" :class="dataOpenSideBar==true? 'side-bar-visible':'side-bar-close'">
        <div class="bg-gray-700 h-[50px]">
            <div class="text-xl font-bold text-center flex items-center justify-center text-white h-full">
                eTech - CyberOne - eDev
            </div>
        </div>
        <div class="flex flex-col justify-between h-[calc(100vh-3rem)] bg-gray-900">
            <div class="menu-man text-left px-2 whitespace-nowrap">
                <div class="profile flex justify-center items-center text-center p-5">
                    <div class="text-center text-white" v-show="dataOpenSideBar">
                        <img src="https://avatars.githubusercontent.com/u/97021587?v=4" class="p-1 w-24 h-24 rounded-full ring-2 ring-gray-300 dark:ring-gray-500 mb-4" alt="Avatar" />
                        <h5 class="text-xl font-medium leading-tight mb-2"> Arti Shala </h5>
                        <p class="text-gray-500">Admin (Role)</p>
                        {{dataOpenSideBar}}
                    </div>
                </div>
                <div class="py-3 rounded-sm cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/dashboard" class="px-2 flex space-x-2"><span class="pi pi-microsoft" v-tooltip.right="Dashboard"></span> <span v-show="dataOpenSideBar"> Dashboard</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/user" class="px-2 flex space-x-2"><span class="pi pi-user" v-tooltip.right="Dashboard"></span> <span v-show="dataOpenSideBar"> Dashboard</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/product" class="px-2 flex space-x-2"><span class="pi pi-cart-plus"></span><span>Trainings</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/contact" class="px-2 flex space-x-2"><span class="pi pi-whatsapp"></span><span>Leaves</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/customer" class="px-2 flex space-x-2"><span class="pi pi-shield"></span><span>Administrator</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/activation" class="px-2 flex space-x-2"><span class="pi pi-check-circle"></span><span>Activation</span></router-link>
                </div>
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <div class="px-2 flex space-x-2"><span class="pi pi-slack" v-tooltip.right="Setting"></span><span>Setting</span></div>
                </div>
            </div>
            <div class="menu-man text-left px-2 justify-self-end whitespace-nowrap">
                <div class="py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <a href="https://website-nuxt-front.vercel.app/" target="_blank" class="px-2 flex space-x-2"><span class="pi pi-question"></span><span>"About Me"</span></a>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import Tooltip from 'primevue/tooltip';
    import Dropdown from 'primevue/dropdown';


const props = defineProps({
  dataOpenSideBar: Boolean,
  clickHamburger: Function
});
</script>

<style>
    #sidebar{
        overflow: hidden;
        transition: 300ms;
    }
    .side-bar-visible{
        width: 250px !important;
    }
    .side-bar-close{
        width: 50px !important;
    }
</style>