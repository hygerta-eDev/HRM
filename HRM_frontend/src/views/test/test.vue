<!-- 
<template>
  <div class="container mx-auto p-6">
    <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
      <h1 class="text-2xl font-bold mb-6">Upload Documents</h1>
      <form @submit.prevent="submitForm">
        <div v-for="(doc, index) in metadata" :key="index">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
            <input v-model="doc.title" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Description:</label>
            <input v-model="doc.description" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Category ID:</label>
            <input v-model="doc.category_id" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Select Files:</label>
            <input type="file" multiple @change="handleFileChange(index, $event)" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        </div>
        <button type="button" @click="addDocument" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Document</button>
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md">Upload</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { api } from '@/api';
const files = ref([])
// Define metadata as a ref
const metadata = ref([{ title: '', description: '', category_id: null }]);

// Define submitForm function
const submitForm = async () => {
  try {
    // Make an API call to fetch the last employee ID
    const response = await api.get('/employees/last_employee_id');
    const lastEmployeeId = response.data;

    // Iterate over each document and upload it separately
    for (let i = 0; i < metadata.value.length; i++) {
      const doc = metadata.value[i];
      const formData = new FormData();

      // Create metadata object for the current document
      const metadataObject = {
        title: doc.title,
        description: doc.description,
        category_id: doc.category_id,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        created_by: lastEmployeeId // Use the last employee ID
      };

      // Append metadata object to formData
      formData.append('metadata_json', JSON.stringify([metadataObject]));

      // Append file to formData
      formData.append('files', files.value[i]);

      // Delay upload by 100 milliseconds for each document
      await new Promise(resolve => setTimeout(resolve, i * 100));

      // Upload the current document
      const uploadResponse = await api.post(`/attach_documents/${lastEmployeeId}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Document uploaded:', uploadResponse.data);
    }
  } catch (error) {
    console.error('Error uploading documents:', error);
  }
};

// Define handleFileChange function
const handleFileChange = (index, event) => {
  const selectedFiles = event.target.files;
  if (selectedFiles && selectedFiles.length > 0) {
    files.value[index] = selectedFiles[0];
  }
};

// Define addDocument function
const addDocument = () => {
  metadata.value.push({ title: '', description: '', category_id: null });
};

export default {
  setup() {
    // Return metadata and other functions from setup()
    return { metadata, submitForm, handleFileChange, addDocument };
  }
};
</script> -->


<!-- <template>
  <div>
    <h2>Post Form</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="workExperienceData.name" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="start">Start Date:</label>
        <input type="datetime-local" id="start" v-model="workExperienceData.start" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="type">Type:</label>
        <input type="text" id="type" v-model="workExperienceData.type" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="end">End Date:</label>
        <input type="datetime-local" id="end" v-model="workExperienceData.end" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="days">Days:</label>
        <input type="number" id="days" v-model="workExperienceData.days" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="employee_id">Employee ID:</label>
        <input type="number" id="employee_id" v-model="workExperienceData.employee_id" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import {api} from '@/api';

export default {
  data() {
    return {
      formData: {
        workExperience_name: '',
        workExperience_start: '',
        workExperience_type: '',
        workExperience_end: '',
        workExperience_days: 0,
        workExperience_employee_id: 0,
        workExperience_created_at: new Date().toISOString(),
        workExperience_user_id: 1 // Assigning user_id here
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        const responseEmployeeId = await api.get('/employees/last_employee_id');
        const lastEmployeeId = response.responseEmployeeId;
        newEmployee.value.institucion_id = newEmployee.value.selectedInstitution;

        workExperienceData.value.name = workExperienceData.value.workExperience_name
        workExperienceData.value.start = workExperienceData.value.workExperience_start
        workExperienceData.value.type = workExperienceData.value.workExperience_type
        workExperienceData.value.end = workExperienceData.value.workExperience_end
        workExperienceData.value.days = workExperienceData.value.workExperience_days
        workExperienceData.value.employee_id = workExperienceData.value.workExperience_employee_id
        workExperienceData.value.created_at = lastEmployeeId

        const response = await api.post('/workExperience/create_WorkExperience', this.workExperienceData);
        console.log('Success:', response.data);
        // Optionally, you can redirect or show a success message here
      } catch (error) {
        console.error('Error:', error);
        // Handle error here
      }
    }
  }
};
</script>

<style scoped>
.form-group {
  margin-bottom: 15px;
}
</style>
 -->

 <!-- workExperience -->

<!-- 
 <template>
  <div>
    <h2>Post Form</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="workExperienceData.name" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="start">Start Date:</label>
        <input type="datetime-local" id="start" v-model="workExperienceData.start" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="type">Type:</label>
        <input type="text" id="type" v-model="workExperienceData.type" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="end">End Date:</label>
        <input type="datetime-local" id="end" v-model="workExperienceData.end" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="days">Days:</label>
        <input type="number" id="days" v-model="workExperienceData.days" class="form-control" readonly>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import {api} from '@/api';

export default {
  setup() {
    const workExperienceData = ref({
      name: '',
      start: '',
      type: '',
      end: '',
      days: 0,
      employee_id: 0,
      created_at: new Date().toISOString(),
      user_id: 1, // Assigning user_id here
    });

    const calculateDays = () => {
      if (workExperienceData.value.start && workExperienceData.value.end) {
        const startDate = new Date(workExperienceData.value.start);
        const endDate = new Date(workExperienceData.value.end);
        const timeDifference = endDate - startDate;
        const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));
        workExperienceData.value.days = daysDifference;
      } else {
        workExperienceData.value.days = 0;
      }
    };

    watch(() => [workExperienceData.value.start, workExperienceData.value.end], calculateDays);

    const submitForm = async () => {
      try {
        const responseEmployeeId = await api.get('/employees/last_employee_id');
        const lastEmployeeId = responseEmployeeId.data;

        workExperienceData.value.employee_id = lastEmployeeId;

        const response = await api.post('/workExperience/create_WorkExperience', workExperienceData.value);
        console.log('Success:', response.data);
        // Optionally, you can redirect or show a success message here
      } catch (error) {
        console.error('Error:', error);
        // Handle error here
      }
    };

    return {
      workExperienceData,
      submitForm,
    };
  },
};
</script>

<style scoped>
.form-group {
  margin-bottom: 15px;
}
</style> -->



<template>
  <div>
    <div>
      <label for="category">Select Category:</label>
      <select id="category" v-model="selectedCategory" @change="fetchTitles">
        <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
          {{ category.category_name }}
        </option>
      </select>
    </div>

    <div>
      <label for="title">Select Title:</label>
      <select id="title" v-model="selectedTitle">
        <option v-for="title in titles" :key="title.title">{{ title.title }}</option>
      </select>
    </div>
  </div>
</template>

<script>
import {api} from '@/api';

export default {
  data() {
    return {
      categories: [],
      titles: [],
      selectedCategory: null,
      selectedTitle: null
    };
  },
  mounted() {
    this.fetchCategories();
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await api.get('/api/categories');
        this.categories = response.data;
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    },
    async fetchTitles() {
      if (this.selectedCategory) {
        try {
          const response = await api.get(`/api/titles?category_id=${this.selectedCategory}`);
          this.titles = response.data;
        } catch (error) {
          console.error("Error fetching titles:", error);
        }
      }
    }
  }
};
</script>