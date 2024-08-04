<template>
    <div class="container mx-auto p-6">
      <div class="create-employee grid grid-cols-1 md:grid-cols-3 gap-6 p-8 rounded-lg shadow-lg border border-gray-300 bg-white">
        <!-- Left Sidebar -->
        <div class="md:col-span-1">
          <div class="flex flex-col items-center">
            <div class="w-32 h-32 mb-4">
              <img src="#" alt="Profile Picture" class="rounded-full w-full h-full object-cover">
            </div>
            <button class="bg-blue-500 text-white px-4 py-2 rounded shadow mb-4">Upload Photo</button>
            <ul class="text-gray-700">
              <li class="mb-2"><a href="#" @click.prevent="selectSection('personal')" class="hover:underline">Personal Details</a></li>
              <li class="mb-2"><a href="#" @click.prevent="selectSection('job')" class="hover:underline">Job Details</a></li>
              <li class="mb-2"><a href="#" @click.prevent="selectSection('documents')" class="hover:underline">Documents</a></li>
              <li class="mb-2"><a href="#" @click.prevent="selectSection('work_experience')" class="hover:underline">Work Experience</a></li>
            </ul>
          </div>
        </div>
        <!-- Form Section -->
        <div class="md:col-span-2">
          <div v-if="selectedSection === 'personal'">
            <!-- Personal Information Section -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="flex items-center mb-4 mt-10">
                <hr class="flex-grow border-gray-400">
                <h2 class="mx-4 text-xl font-semibold text-center">Personal Information</h2>
                <hr class="flex-grow border-gray-400">
              </div>
              <!-- Personal Information Fields -->
              <div class="mb-4" v-for="(field, index) in personalFields" :key="index">
                <label class="block text-gray-700 text-sm font-bold mb-2">{{ field.label }}</label>
                <div class="input-container">
                  <div class="input-content">{{ field.value }}</div>
                </div>
              </div>
            </div>
          </div>
  
          <div v-if="selectedSection === 'job'">
            <!-- Employment Details Section -->
            <div class="container mx-auto p-6">
              <div class="flex items-center mb-4 mt-10">
                <hr class="flex-grow border-gray-400">
                <h2 class="mx-4 text-xl font-semibold text-center">Employment Details</h2>
                <hr class="flex-grow border-gray-400">
              </div>
              <div class="flex flex-wrap -mx-2 bg-gray-200">
                <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2" v-for="(field, index) in jobFields" :key="index">
                  <label class="block text-gray-700 text-sm font-bold mb-2">{{ field.label }}</label>
                  <div class="input-container">
                    <div class="input-content">{{ field.value }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
  
          <div v-if="selectedSection === 'documents'">
            <!-- Documents Section -->
            <div class="container mx-auto p-6">
              <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
                <h1 class="text-2xl font-bold mb-6">Documents</h1>
                <div v-if="documents.length">
                  <div v-for="(doc, index) in documents" :key="index" class="mb-4">
                    <div class="flex justify-between items-center">
                      <div>
                        <h3 class="text-lg font-semibold">{{ doc.title }}</h3>
                        <p>{{ doc.description }}</p>
                      </div>
                      <div>
                        <button @click="downloadDocument(doc)" class="bg-green-500 text-white px-4 py-2 rounded-lg ml-2 shadow-md">Download</button>
                      </div>
                    </div>
                  </div>
                  <button @click="downloadDocuments" class="bg-green-500 text-white px-4 py-2 rounded-lg ml-2 shadow-md">Download All Documents</button>
                </div>
                <div v-else>
                  <p>No documents available.</p>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Work Experience -->
          <div v-if="selectedSection === 'work_experience'">
            <div class="container mx-auto p-6">
              <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
                <h1 class="text-2xl font-bold mb-6">Work Experience</h1>
                <form @submit.prevent="submitForm">
                  <div class="flex flex-wrap">
                    <div v-for="(workExperience, index) in workExperienceList" :key="index" class="w-full sm:w-1/4 md:w-1/3 p-2">
                      <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2"> Name</label>
                        <input v-model="workExperience.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                      </div>
                      <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2">Type</label>
                        <input v-model="workExperience.type" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                      </div>
                      <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
                        <input v-model="workExperience.start" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                      </div>
                      <div class="mb-4">
                        <label class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
                        <input v-model="workExperience.end" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
  
          <div class="mt-6">
            <button @click="saveEmployee" class="bg-green-500 text-white px-4 py-2 rounded shadow">Save</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, watch, computed } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  
  export default {
    setup() {
      const selectedSection = ref('personal');
      const showDocumentFields = ref(false);
      const workExperiences = ref([]);
      const router = useRouter();
      const route = useRoute();
      const documentUpload = ref(null);
      const institutions = ref([]);
      const departments = ref([]);
      const jobPositions = ref([]);
      const ethnicities = ref([]);
      const maritalStatusOptions = ref([]);
      const workExperienceOptions = ref([]);
      const genderOptions = ref([]);
      const cityOptions = ref([]);
      const zipCodeOptions = ref([]);
      const cities = ref([]);
      const zipCodes = ref([]);
      const selectedZipCode = ref('');
      const selectedCategory = ref('');
      const categories = ref([]);
      const generatedNumber = ref([]);
      const documents = ref([]);
      const documents_id = ref('');
      const titles = ref([]);
      const selectedTitle = ref('');
      const files = ref([]);
      const metadata = ref([{ selectedTitle: '', description: '', category_id: selectedCategory.value }]);
  
      const editEmployee = ref({
        selectedInstitution: null,
        selectedDepartment: null,
        selectedJobPosition: null,
        selectedCity: '',
        selectedZipCode: '',
        name: '',
        number: '',
        username: '',
        middle_name: '',
        last_name: '',
        gender: '',
        ethnicity_id: 0,
        marital_status: '',
        date_of_birth: '',
        date_hired: '',
        contract_end_date: '',
        personal_number: '',
        salary: '0',
        addition: 0,
        street: ' ',
        city: '',
        zipcode: '',
        country: '',
        phone_number: '',
        phone_number_2: '',
        email: '',
        email_2: '',
        days_off: '',
        transferred_days_off: '',
        earned_days_off: '',
        next_year_earned_days_off: '',
        active: true,
        qualification_id: 0,
        documents_id: 0,
      });
  
      const workExperienceList = ref([{ name: '', type: '', start: '', end: '' }]);
  
      const personalFields = computed(() => [
        { label: 'First Name', value: editEmployee.value.name },
        { label: 'Middle Name', value: editEmployee.value.middle_name },
        { label: 'Last Name', value: editEmployee.value.last_name },
        { label: 'Date of Birth', value: editEmployee.value.date_of_birth },
        { label: 'Street', value: editEmployee.value.street },
        { label: 'City', value: editEmployee.value.city },
        { label: 'Zip Code', value: editEmployee.value.zipcode },
        { label: 'Country', value: editEmployee.value.country },
        { label: 'Phone Number', value: editEmployee.value.phone_number },
        { label: 'Phone Number 2', value: editEmployee.value.phone_number_2 },
        { label: 'Email', value: editEmployee.value.email },
        { label: 'Email 2', value: editEmployee.value.email_2 },
        { label: 'Gender', value: editEmployee.value.gender },
        { label: 'Marital Status', value: editEmployee.value.marital_status },
        { label: 'Ethnicity', value: editEmployee.value.ethnicity_id },
        { label: 'Qualification', value: editEmployee.value.qualification_id },
      ]);
  
      const jobFields = computed(() => [
        { label: 'Date Hired', value: editEmployee.value.date_hired },
        { label: 'Contract End Date', value: editEmployee.value.contract_end_date },
        { label: 'Personal Number', value: editEmployee.value.personal_number },
        { label: 'Salary', value: editEmployee.value.salary },
        { label: 'Addition', value: editEmployee.value.addition },
        { label: 'Days Off', value: editEmployee.value.days_off },
        { label: 'Transferred Days Off', value: editEmployee.value.transferred_days_off },
        { label: 'Earned Days Off', value: editEmployee.value.earned_days_off },
        { label: 'Next Year Earned Days Off', value: editEmployee.value.next_year_earned_days_off },
        { label: 'Active', value: editEmployee.value.active },
      ]);
  
    //   const employeeId = route.params.employeeId;
      const employeeId= localStorage.getItem('employee_id') || ''; // Get user's name from local storage

      const fetchEmployeeData = async () => {
  if (employeeId) {
    try {
      const response = await api.get(`/employees/employees/${employeeId}`);
      console.log("API Response:", response);

      const employeeData = response.data; // Access the data directly since it's not an array

      if (employeeData) {
        // Ensure the employeeData has all necessary fields initialized
        editEmployee.value = {
          ...editEmployee.value, // Spread existing properties to retain default values
          ...employeeData,
          country: employeeData.country || 'Kosovo', // Default to 'Kosovo' if country is not defined
        };

        console.log("Employee Data:", editEmployee.value);
      } else {
        console.error("Employee data is undefined");
      }
    } catch (error) {
      console.error("Error fetching employee data:", error);
    }
  }
};



  
      onMounted(async () => {
        await fetchEmployeeData();
        await fetchEmployeeDocuments();
      });
  
      watch(editEmployee, () => {
        if (editEmployee.value.selectedZipCode && !zipCodes.value.includes(editEmployee.value.selectedZipCode)) {
          editEmployee.value.selectedZipCode = '';
        }
      });
  
      const saveEmployee = async () => {
        try {
          await api.put(`employees/${employeeId}`, editEmployee.value);
          toast.success('Employee updated successfully!');
          router.push('/employees');
        } catch (error) {
          toast.error('Error updating employee.');
        }
      };
  

      const downloadDocuments = async () => {
        // const employeeId = route.params.id;
        try {
          const response = await api.get(`/download_all/${employeeId}`, {
            responseType: 'blob'
          });
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `employee_${employeeId}_documents.zip`);
          document.body.appendChild(link);
          link.click();
        } catch (error) {
          console.error('Error downloading documents:', error);
          toast.error('Failed to download documents!', {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }
      };
      const fetchEmployeeDocuments = async (employeeId) => {
        try {
        const employeeId= localStorage.getItem('employee_id') || ''; 

          const response = await api.get(`/api/employees/${employeeId}/documents`);
          documents.value = response.data;
          console.log(documents.value); // Debugging to see the fetched documents
        } catch (error) {
          console.error('Error fetching employee documents:', error);
        }
      };


      const downloadDocument = async (doc) => {
        try {
          const response = await api.get(`/download_file/${doc.document_id}`, {
            responseType: 'blob',
          });

          // Extracting the file extension from the mime type
          const mimeType = response.headers['content-type'];
          const extension = mimeType.split('/')[1];

          // Creating a Blob from the response data
          const blob = new Blob([response.data], { type: mimeType });

          // Creating a URL for the Blob
          const url = window.URL.createObjectURL(blob);

          // Creating a link element to trigger the download
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `${doc.title}.${extension}`); // Appending the correct extension to the filename
          document.body.appendChild(link);

          // Triggering the download
          link.click();

          // Cleaning up
          document.body.removeChild(link);
          window.URL.revokeObjectURL(url);
        } catch (error) {
          console.error('Error downloading document:', error);
        }
      };
      const deleteDocument = async (doc) => {
            try {
              const response = await api.delete(`/delete_document/${doc.document_id}`);
              if (response.status === 200) {
                documents.value = documents.value.filter(d => d.document_id !== doc.document_id);
                toast.success('Document deleted successfully!', {
                  autoClose: 3000,
                  position: toast.POSITION.TOP_RIGHT,
                });
              }
            } catch (error) {
              console.error('Error deleting document:', error);
              toast.error('Failed to delete document!', {
                  autoClose: 3000,
                position: toast.POSITION.TOP_RIGHT,
              });
            }
          };
      const selectSection = (section) => {
        selectedSection.value = section;
      };
      const selectedInstitutionName = computed(() => {
      const institution = institutions.value.find(inst => inst.id === editEmployee.value.selectedInstitution);
          return institution ? institution.name : 'Unknown Institution';
        });
        const selectedDepartmentName = computed(() => {
          const department = departments.value.find(inst => inst.id === editEmployee.value.selectedDepartment);
          return department ? department.name : 'Unknown Department';
        });
            const selectedJobPositionName = computed(() => {
        const jobPosition = jobPositions.value.find(job => job.id === editEmployee.value.selectedJobPosition);
        return jobPosition ? jobPosition.name : 'Unknown Job Position';
        });

        const selectedEthnicityName = computed(() => {
        const ethnicity = ethnicities.value.find(eth => eth.id === editEmployee.value.ethnicity_id);
        return ethnicity ? ethnicity.name : 'Unknown Ethnicity';
        });
      return {
        selectedInstitutionName,
        selectedDepartmentName,
        selectedJobPositionName,
        selectedEthnicityName,
        selectedSection,
        editEmployee,
        personalFields,
        jobFields,
        documents,
        workExperienceList,
        fetchEmployeeData,
        saveEmployee,
        downloadDocument,
        downloadDocuments,
        fetchEmployeeDocuments,
        selectSection,
      };
    },
  };
  </script>
  
  <style scoped>
  .input-container {
    display: flex;
    align-items: center;
    border: 1px solid #cbd5e0;
    border-radius: 0.375rem;
    padding: 0.5rem 1rem;
    background-color: #f7fafc;
  }
  .input-content {
    flex-grow: 1;
    color: #2d3748;
  }
  </style>
  