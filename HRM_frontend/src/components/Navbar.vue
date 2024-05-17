<template>
    <div class="w-full bg-gray-100">
        <div class="flex justify-between items-center h-[50px]">
            <div class="p-4 cursor-pointer hover:bg-gray-50" @click="clickHamburger">
                <i class="pi pi-bars"></i>
            </div>
            <div class="py-2">
                {{ dataOpenSideBar }}
                <InputText type="text" v-model="value" class="40px" placeholder="Search..."/>
            </div>
            <div class="flex space-x-3 items-center justify-center px-3">
                <div class="text-md">Admin</div>
                <Avatar icon="pi pi-user" style="background-color: #dee9fc; color: #1a2551" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu" />
                <Menu ref="menu" id="overlay_menu" :model="items" :popup="true"  />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";

import Avatar from 'primevue/avatar';
import InputText from 'primevue/inputtext';
import Menu from 'primevue/menu';

// Define props
const props = defineProps({
  dataOpenSideBar: Boolean,
  clickHamburger:Function
});

const menu = ref();
const items = ref([
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
const toggle = (event) => {
    menu.value.toggle(event);
};


</script>