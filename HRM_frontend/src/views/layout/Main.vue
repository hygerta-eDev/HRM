<template>
    <div class="w-full h-full flex">
        <Sidebar :dataOpenSideBar="openSidebar" />
        <div class="w-full h-full">
            <Navbar :dataOpenSideBar="openSidebar" :clickHamburger="toggleSidebar" />
            <div class="w-full h-[calc(100vh-50px)]">
                <router-view></router-view>
            </div>    
        </div>
    </div>

</template>

<script>
    import Navbar from '../../components/Navbar.vue'
    import Sidebar from '../../components/Sidebar.vue'
    export default {
    components: { Navbar, Sidebar },
    data() {
        return {
            openSidebar: true
        };
    },
    methods: {
        toggleSidebar() {
            this.openSidebar = !this.openSidebar;
        }
    }
};
</script>

<style>

</style>
