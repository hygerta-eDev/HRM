<template>
    <div class="flex flex-wrap justify-center gap-4">
      <!-- Display each document type as a clickable box -->
      <div
        v-for="documentType in documentTypes"
        :key="documentType.id"
        @click="fetchEmployees(documentType.id)"
        class="cursor-pointer border border-gray-300 rounded-lg p-4 shadow-md transition duration-300 ease-in-out hover:bg-gray-100"
      >
        <h3 class="text-lg font-semibold">{{ documentType.name }}</h3>
        <p class="text-sm text-gray-600">{{ documentType.description }}</p>
      </div>
  
      <!-- Display employees for selected document type -->
      <div v-if="selectedDocumentType">
        <h2 class="text-xl font-semibold mt-4">Employees with {{ selectedDocumentType.name }}:</h2>
        <ul>
          <li v-for="employee in employees" :key="employee.id" class="mt-2">
            {{ employee.name }}
          </li>
          <p v-if="employees.length === 0">No employees found.</p>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        documentTypes: [
          { id: 1, name: 'Passport', description: 'International passport document' },
          { id: 2, name: 'ID Card', description: 'Government-issued identification card' },
          { id: 3, name: 'Driver\'s License', description: 'Official driving permit' },
          { id: 4, name: 'Visa', description: 'Travel visa document' },
        ],
        selectedDocumentType: null,
        employees: [],
      };
    },
    methods: {
      async fetchEmployees(documentTypeId) {
        // Simulate fetching employees from API based on document type
        try {
          // Replace with actual API call to fetch employees
          // For demo, just simulate fetching employees
          this.selectedDocumentType = this.documentTypes.find(doc => doc.id === documentTypeId);
          this.employees = await this.getEmployeesByDocumentType(documentTypeId);
        } catch (error) {
          console.error('Error fetching employees:', error);
        }
      },
      async getEmployeesByDocumentType(documentTypeId) {
        // Simulate API call to fetch employees by document type
        // Replace with actual API call
        return new Promise(resolve => {
          setTimeout(() => {
            // Simulated data
            const employees = [
              { id: 1, name: 'John Doe' },
              { id: 2, name: 'Jane Smith' },
              { id: 3, name: 'Michael Brown' },
            ];
            resolve(employees);
          }, 1000); // Simulate delay for API call
        });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your component styles here */
  </style>
  