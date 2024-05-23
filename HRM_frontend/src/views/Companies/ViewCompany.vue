<template>
    <div class="view-company">
      <h1>View Company</h1>
      <div v-if="company" class="company-details">
        <h2>{{ company.name }}</h2>
        <table>
          <tr>
            <th>ID:</th>
            <td>{{ company.id }}</td>
          </tr>
          <tr>
            <th>Name:</th>
            <td>{{ company.name }}</td>
          </tr>
          <tr>
            <th>Manager:</th>
            <td>{{ company.menager }}</td>
          </tr>
        </table>
      </div>
      <div v-else class="loading">
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  export default {
    setup() {
      const route = useRoute();
      const company = ref(null);
  
      onMounted(() => {
        const companyId = Number(route.params.id);
        const companies = [
          { id: 1, name: 'eTech', menager: 'MenagersName' },
          { id: 2, name: 'CyberOne', menager: 'MenagersName' },
          { id: 3, name: 'eDev', menager: 'MenagersName' }
        ];
        company.value = companies.find(c => c.id === companyId);
      });
  
      return {
        company
      };
    }
  };
  </script>
  
  <style scoped>
  .view-company {
    max-width: 600px;
    margin: 0 auto;
  }
  
  .company-details {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .company-details h2 {
    margin-top: 0;
  }
  
  .loading {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #666;
  }
  </style>
  