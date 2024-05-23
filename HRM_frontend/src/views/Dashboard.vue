<template>
  <div class="h-full w-full relative ">
    <div class="absolute inset-0 bg-cover bg-center" style="background-image: url('https://etech-rks.com/wp-content/uploads/2020/12/slider-bg-1-1-1.jpg')"></div>
    <div class="relative z-10 flex flex-col items-center justify-center h-full">
      <h1 class="text-3xl font-semibold text-white">Dashboard Main Content</h1>
      <p class="mt-4 text-white">This is the main content area of the dashboard.</p>

      <!-- Dashboard Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mt-10 w-full px-6">
        <div class="p-6 bg-white rounded-lg shadow-lg">
          <div class="flex items-center">
            <i class="pi pi-users text-4xl text-blue-500"></i>
            <div class="ml-4">
              <p class="text-gray-600">Employees</p>
              <p class="text-2xl font-semibold">120</p>
            </div>
          </div>
        </div>
        <div class="p-6 bg-white rounded-lg shadow-lg">
          <div class="flex items-center">
            <i class="pi pi-calendar text-4xl text-green-500"></i>
            <div class="ml-4">
              <p class="text-gray-600">Upcoming Trainings</p>
              <p class="text-2xl font-semibold">5</p>
            </div>
          </div>
        </div>
        <div class="p-6 bg-white rounded-lg shadow-lg">
          <div class="flex items-center">
            <i class="pi pi-briefcase text-4xl text-yellow-500"></i>
            <div class="ml-4">
              <p class="text-gray-600">Open Positions</p>
              <p class="text-2xl font-semibold">8</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Progress Bars -->
      <div class="w-full px-6 mt-10">
        <div class="p-6 bg-white rounded-lg shadow-lg mb-6">
          <p class="text-gray-600 mb-2">Project Completion</p>
          <div class="relative pt-1">
            <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-blue-200">
              <div style="width:70%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500"></div>
            </div>
            <p class="text-right text-sm text-gray-600">70%</p>
          </div>
        </div>
        <div class="p-6 bg-white rounded-lg shadow-lg">
          <p class="text-gray-600 mb-2">Employee Satisfaction</p>
          <div class="relative pt-1">
            <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-green-200">
              <div style="width:85%" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500"></div>
            </div>
            <p class="text-right text-sm text-gray-600">85%</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
};
</script>

<style scoped>
.absolute {
  background-attachment: fixed;
}
</style>
