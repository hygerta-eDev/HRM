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

<!-- 

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


 -->
<!-- 
 <template>
  <div>
    <h1>Download Generated Document</h1>
    <form @submit.prevent="generateDocument">
      <label for="name">Employee Name:</label>
      <input type="text" id="name" v-model="employee.name" required>
      <br><br>
      <label for="personal_number">Personal Number:</label>
      <input type="text" id="personal_number" v-model="employee.personal_number" required>
      <br><br>
      <button type="submit">Generate and Download Document</button>
    </form>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  data() {
    return {
      employee: {
        name: '',
        personal_number: ''
      }
    };
  },
  methods: {
    async generateDocument() {
      try {
        const response = await api.post('/employees/generate-document', this.employee, {
          responseType: 'blob', // Ensure responseType is set to blob to handle binary responses
          headers: {
            'Content-Type': 'application/json' // Set Content-Type header appropriately
          }
        });

        // Create a Blob object from the response data
        const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });

        // let filename = 'document.docx';
        let filename = this.employee.name ? `${this.employee.name}_contract.docx` : 'document.docx';

        const contentDisposition = response.headers['content-disposition'];
        if (contentDisposition) {
          const filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
          const matches = filenameRegex.exec(contentDisposition);
          if (matches && matches.length > 1) {
            filename = matches[1].replace(/['"]/g, '');
          }
        }

        // Create a link element to trigger the download
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        // Clean up by revoking the object URL
        window.URL.revokeObjectURL(url);

        alert('Document downloaded successfully!');
      } catch (error) {
        console.error('Error generating document:', error);
        alert('Failed to generate document');
      }
    }
  }
};
</script> -->
<!-- 
<template>
  <div>
    <h1>Download Generated Document</h1>
    <form @submit.prevent="generateDocument">
      <label for="name">Employee Name:</label>
      <input type="text" id="name" v-model="employee.name" required>
      <br><br>
      <label for="personal_number">Personal Number:</label>
      <input type="text" id="personal_number" v-model="employee.personal_number" required>
      <br><br>
      <label for="date_of_birth">Date of Birth:</label>
      <input type="date" id="date_of_birth" v-model="employee.date_of_birth" required>
      <br><br>
      <label for="city">Place of Birth:</label>
      <input type="text" id="city" v-model="employee.city" required>
      <br><br>
      <label for="street">Address:</label>
      <input type="text" id="street" v-model="employee.street" required>
      <br><br>
      <label for="job_position_id">Job Position:</label>
      <input type="text" id="job_position_id" v-model="employee.job_position_id" required>
      <br><br>
      <label for="date_hired">Date Hired:</label>
      <input type="date" id="date_hired" v-model="employee.date_hired" required>
      <br><br>
      <label for="contract_end_date">Contract End Date:</label>
      <input type="date" id="contract_end_date" v-model="employee.contract_end_date">
      <br><br>
      <label for="today">Today's Date:</label>
      <input type="date" id="today" v-model="employee.today" required>
      <br><br>
      <label for="salary">Salary:</label>
      <input type="text" id="salary" v-model="employee.salary" required>
      <br><br>
      <button type="submit">Generate and Download Document</button>
    </form>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  data() {
    return {
      employee: {
        name: '',
        personal_number: '',
        date_of_birth: '',
        city: '',
        street: '',
        job_position_id: '',
        date_hired: '',
        contract_end_date: '',
        today: '',
        salary: ''
      }
    };
  },
  methods: {
    async generateDocument() {
      try {
        const response = await api.post('/employees/generate-document', this.employee, {
          responseType: 'blob',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });

        let filename = this.employee.name ? `${this.employee.name}_contract.docx` : 'document.docx';

        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        window.URL.revokeObjectURL(url);

        alert('Document downloaded successfully!');
      } catch (error) {
        console.error('Error generating document:', error);
        alert('Failed to generate document');
      }
    }
  }
};
</script> -->


<!-- <template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        this.error = null;
        const response = await api.post('/user/login', {
          username: this.username,
          password: this.password,
        });
        const { access_token, user_id, role, name } = response.data;
        localStorage.setItem('token', access_token);
        localStorage.setItem('user_id', user_id);
        localStorage.setItem('role', role);
        localStorage.setItem('name', name);
        this.$router.push('/dashboard'); // Redirect to the dashboard
      } catch (error) {
        this.error = error.response ? error.response.data.detail : 'An error occurred';
      }
    },
  },
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.form-group {
  margin-bottom: 1em;
}
label {
  display: block;
  margin-bottom: 0.5em;
}
input {
  width: 100%;
  padding: 0.5em;
  box-sizing: border-box;
}
button {
  padding: 0.5em 1em;
}
.error {
  color: red;
  margin-top: 1em;
}
</style> -->



<!-- 
<template>
  <div class="max-w-md mx-auto p-4">
    <form @submit.prevent="createLeave">
      <div class="mb-4">
        <label for="employee_id" class="block text-gray-700">Employee ID</label>
        <input v-model="leaveData.employee_id" id="employee_id" type="number" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="leave_type_id" class="block text-gray-700">Leave Type ID</label>
        <input v-model="leaveData.leave_type_id" id="leave_type_id" type="number" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="start_date" class="block text-gray-700">Start Date</label>
        <input v-model="leaveData.start_date" id="start_date" type="date" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="end_date" class="block text-gray-700">End Date</label>
        <input v-model="leaveData.end_date" id="end_date" type="date" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="days" class="block text-gray-700">Days</label>
        <input v-model="leaveData.days" id="days" type="number" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="user_id" class="block text-gray-700">User ID</label>
        <input v-model="leaveData.user_id" id="user_id" type="number" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50" />
      </div>

      <div class="mb-4">
        <label for="status" class="block text-gray-700">Status</label>
        <select v-model="leaveData.status" id="status" required class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring focus:ring-opacity-50">
          <option value="Pending">Pending</option>
          <option value="Approved">Approved</option>
          <option value="Rejected">Rejected</option>
        </select>
      </div>

      <button type="submit" class="w-full bg-blue-600 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300">Create Leave</button>
    </form>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  data() {
    return {
      leaveData: {
        employee_id: '',
        leave_type_id: '',
        start_date: '',
        end_date: '',
        days: '',
        user_id: '',
        status: 'Pending',
        created_at: new Date().toISOString(),
      },
    };
  },
  methods: {
    async createLeave() {
      try {
        const response = await api.post('/leaves/create_leaves', this.leaveData);
        alert('Leave created successfully');
        // Reset form
        this.leaveData = {
          employee_id: '',
          leave_type_id: '',
          start_date: '',
          end_date: '',
          days: '',
          user_id: '',
          status: 'Pending',
          created_at: new Date().toISOString(),

        };
      } catch (error) {
        alert('An error occurred while creating the leave');
      }
    },
  },
};
</script>

<style scoped>
/* Add any scoped styles if necessary */
</style> -->

<!-- 
<template>
  <div class="max-w-2xl mx-auto p-4">
    <h2 class="text-2xl font-bold mb-4">Pending Leave Requests</h2>
    <div v-if="loading" class="text-center">Loading...</div>
    <div v-else>
      <div v-if="pendingLeaves && pendingLeaves.length === 0" class="text-center text-gray-600">No pending leave requests found.</div>
      <div v-for="leave in pendingLeaves" :key="leave.id" class="mb-4 p-4 border rounded-md shadow-sm">
        <p><strong>Employee ID:</strong> {{ leave.employee_id }}</p>
        <p><strong>Leave Type ID:</strong> {{ leave.leave_type_id }}</p>
        <p><strong>Start Date:</strong> {{ leave.start_date }}</p>
        <p><strong>End Date:</strong> {{ leave.end_date }}</p>
        <p><strong>Days:</strong> {{ leave.days }}</p>
        <p><strong>User ID:</strong> {{ leave.user_id }}</p>
        <p><strong>Status:</strong> {{ leave.status }}</p>
        <div class="mt-2 flex gap-2">
          <button @click="approveLeave(leave)" class="bg-green-500 text-white py-1 px-3 rounded-md hover:bg-green-600">Approve</button>
          <button @click="openRejectModal(leave)" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
        </div>
      </div>
    </div>

    <div v-if="showRejectModal" class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
      <div class="bg-white p-4 rounded-md shadow-md">
        <h3 class="text-xl font-bold mb-2">Reject Leave Request</h3>
        <p><strong>Employee ID:</strong> {{ rejectLeave.employee_id }}</p>
        <p><strong>Leave Type ID:</strong> {{ rejectLeave.leave_type_id }}</p>
        <p><strong>Start Date:</strong> {{ rejectLeave.start_date }}</p>
        <p><strong>End Date:</strong> {{ rejectLeave.end_date }}</p>
        <p><strong>Days:</strong> {{ rejectLeave.days }}</p>
        <textarea v-model="rejectedComment" class="w-full p-2 border rounded-md" placeholder="Enter rejection comment"></textarea>
        <div class="mt-4 flex gap-2">
          <button @click="rejectLeaveRequest" class="bg-red-500 text-white py-1 px-3 rounded-md hover:bg-red-600">Reject</button>
          <button @click="closeRejectModal" class="bg-gray-500 text-white py-1 px-3 rounded-md hover:bg-gray-600">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { api } from '@/api';

export default {
  data() {
    return {
      pendingLeaves: [],
      loading: false,
      showRejectModal: false,
      rejectLeave: null,
      rejectedComment: '',
      errors: {}
    };
  },
  created() {
    this.fetchPendingLeaves();
  },
  methods: {
    async fetchPendingLeaves() {
      this.loading = true;
      try {
        const response = await api.get('/leaves/leave/pending');
        this.pendingLeaves = response.data;
      } catch (error) {
        alert('An error occurred while fetching pending leave requests');
      } finally {
        this.loading = false;
      }
    },
    async approveLeave(leave) {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leaves/leave/${leave.id}/status`, {
          ...leave,
          status: 'Approved',
          approved_by_id: userId,
          approved_at: new Date().toISOString(),
          updated_at: new Date().toISOString()

        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== leave.id);
        alert('Leave request has been approved successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, leave.id, error.response.data);
        } else {
          alert('An error occurred while approving the leave request');
        }
      }
    },
    openRejectModal(leave) {
      this.rejectLeave = leave;
      this.showRejectModal = true;
    },
    async rejectLeaveRequest() {
      try {
        const userId = localStorage.getItem('user_id');
        await api.patch(`/leave/${this.rejectLeave.id}/status`, {
          ...this.rejectLeave,
          status: 'Rejected',
          rejected_by_id: userId,
          rejected_at: new Date().toISOString(),
          rejected_comment: this.rejectedComment
        });
        this.pendingLeaves = this.pendingLeaves.filter(l => l.id !== this.rejectLeave.id);
        this.closeRejectModal();
        alert('Leave request has been rejected successfully');
      } catch (error) {
        if (error.response && error.response.data && Array.isArray(error.response.data)) {
          this.$set(this.errors, this.rejectLeave.id, error.response.data);
        } else {
          alert('An error occurred while rejecting the leave request');
        }
      }
    },
    closeRejectModal() {
      this.showRejectModal = false;
      this.rejectLeave = null;
      this.rejectedComment = '';
    }
  }
};

</script>

<style scoped>
/* Add any scoped styles if necessary */
</style> -->
<template>
  <div>
    <vue-cal
      v-model="selectedDate"
      :events="holidayEvents"
      :mode="'month'"
      :month="currentMonth"
      @change-month="handleMonthChange"
    />
  </div>
</template>

<script>
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css'; // Import default styles

export default {
  components: {
    VueCal,
  },
  data() {
    return {
      selectedDate: new Date(), // Initial selected date
      currentMonth: new Date(), // Initial month to display
      holidayEvents: [
        // Example holiday events (replace with your data)
        {
          start: new Date('2024-07-01'),
          end: new Date('2024-07-01'),
          title: 'Independence Day',
          desc: 'National holiday',
        },
        {
          start: new Date('2024-07-04'),
          end: new Date('2024-07-04'),
          title: 'Labor Day',
          desc: 'Public holiday',
        },
        // Add more holidays as needed
      ],
    };
  },
  methods: {
    handleMonthChange(month) {
      // Handle month change event if needed
      console.log('Month changed to:', month);
    },
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
