<template>
    <div class="container mx-auto p-6">
      <div  class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
        <h1 class="text-2xl font-bold mb-6">Edit New Employee</h1>
        <div class="employee-details flex flex-wrap">
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
            <input v-model="editEmployee.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Number</label>
            <input v-model="editEmployee.number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" disabled>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
            <input v-model="editEmployee.username" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Middle Name</label>
            <input v-model="editEmployee.middle_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
            <input v-model="editEmployee.last_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Gender</label>
          <select v-model="editEmployee.gender" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Gender</option>
            <option v-for="genders in genderOptions" :key="genders.id" :value="genders.id">
              {{ genders }}
            </option>
          </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity</label>
            <select v-model="editEmployee.ethnicity_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Ethnicity</option>
              <option v-for="ethnicity in ethnicities" :key="ethnicity.id" :value="ethnicity.id">
                {{ ethnicity.name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Marital Status</label>
            <select v-model="editEmployee.marital_status" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select maritalStatus</option>
              <option v-for="maritalStatus in maritalStatusOptions" :key="maritalStatus.id" :value="maritalStatus.id">
                {{ maritalStatus}}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Date of Birth</label>
            <input v-model="editEmployee.date_of_birth" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Date Hired</label>
            <input v-model="editEmployee.date_hired" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Contract End Date</label>
            <input v-model="editEmployee.contract_end_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Institution</label>
            <select v-model="editEmployee.selectedInstitution" @change="onInstitutionChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Institution</option>
              <option v-for="institution in institutions" :key="institution.id" :value="institution.id">
                {{ institution.name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>
            <select v-model="editEmployee.selectedDepartment" @change="onDepartmentChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Department</option>
              <option v-for="department in departments" :key="department.id" :value="department.id">
                {{ department.name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Personal Number</label>
            <input v-model="editEmployee.personal_number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Salary</label>
            <input v-model="editEmployee.salary" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Addition</label>
            <input v-model="editEmployee.addition" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Job Position</label>
            <select v-model="editEmployee.selectedJobPosition" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Job Position</option>
              <option v-for="position in jobPositions" :key="position.id" :value="position.id">
                {{ position.name }}
              </option>
            </select>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Street</label>
            <input v-model="editEmployee.street" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">City</label>
            <select v-model="editEmployee.selectedCity" @change="onCityChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select City</option>
              <option v-for="city in cities" :key="city.city_name" :value="city.city_name">
                {{ city.city_name }}
              </option>
            </select>
          </div>
          <div class="w-full mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Zip Code</label>
            <select v-model="editEmployee.selectedZipCode" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Zip Code</option>
              <option v-for="zip in zipCodes" :key="zip" :value="zip">
                {{ zip }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Country</label>
            <input v-model="editEmployee.country" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number</label>
            <input v-model="editEmployee.phone_number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number 2</label>
            <input v-model="editEmployee.phone_number_2" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Email</label>
            <input v-model="editEmployee.email" type="email" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Email 2</label>
            <input v-model="editEmployee.email_2" type="email" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Days Off</label>
            <input v-model="editEmployee.days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Transferred Days Off</label>
            <input v-model="editEmployee.transferred_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Earned Days Off</label>
            <input v-model="editEmployee.earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Next Year Earned Days Off</label>
            <input v-model="editEmployee.next_year_earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">CV</label>
            <input v-model="editEmployee.cv" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">The Workouts Selection</label>
            <input v-model="editEmployee.the_workouts_selection" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        </div>
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
                        <button @click="deleteDocument(doc)" class="bg-red-500 text-white px-4 py-2 rounded-lg ml-2 shadow-md">Delete</button>
                        </div>
                        
                    </div>
                </div>
                <button @click="downloadDocuments" class="bg-green-500 text-white px-4 py-2 rounded-lg ml-2 shadow-md">Download AllDocuments</button>
            </div>
            <div v-else>
                <p>No documents available.</p>
            </div>
            </div>
        </div>
        <div class="container mx-auto p-6">
    <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
      <h1 class="text-2xl font-bold mb-6">Upload Documents</h1>
      <form>
        <div v-for="(doc, index) in metadata" :key="index">
          <div class="w-full mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="category">Select Category:</label>
            <select class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" :id="'category-' + index" v-model="doc.selectedCategory" @change="fetchTitles(index)">
              <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
                {{ category.category_name }}
              </option>
            </select>
          </div>
          <div class="w-full mb-4">
            <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Select Title:</label>
            <select :id="'title-' + index" v-model="doc.selectedTitle" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option v-for="title in doc.titles" :key="title.title_id" :value="title.title">
                {{ title.title }}
              </option>
            </select>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Description:</label>
            <input v-model="doc.description" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">Select Files:</label>
            <input type="file" multiple @change="handleFileChange(index, $event)" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        </div>
        <button type="button" @click="addDocument" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Document</button>
      </form>
    </div>
  </div>
        <!-- <div class="container mx-auto p-6">
          <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
            <h1 class="text-2xl font-bold mb-6">Upload Documents</h1>
            <form >
              <div v-for="(doc, index) in metadata" :key="index">
                <div class="w-full mb-4 ">
                  <label class="block text-gray-700 text-sm font-bold mb-2" for="category">Select Category:</label>
                  <select  class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" id="category" v-model="selectedCategory" @change="fetchTitles">
                    <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
                      {{ category.category_name }}
                    </option>
                  </select>
                </div>
                <div class="w-full mb-4 ">
                  <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Select Title:</label>
                  <select id="title" v-model="doc.selectedTitle" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    <option v-for="title in titles" :key="title.title_id" :value="title.title">
                      {{ title.title }}
                    </option>
                  </select>
                </div>
                <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2">Description:</label>
                  <input v-model="doc.description" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                </div>
                <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2">Select Files:</label>
                  <input type="file" multiple @change="handleFileChange(index, $event)" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                </div>
              </div>
              <button type="button" @click="addDocument" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Document</button>
            </form>
          </div>
        </div> -->
        <div class="container mx-auto p-6">
          <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
            <h1 class="text-2xl font-bold mb-6">workExperience</h1>
            <form @submit.prevent="submitForm">
              <div>
                <div class="mb-4">
                  <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
                  <input type="text" id="name" v-model="workExperienceData.name" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                </div>
                <div class="mb-4">
                  <label for="type" class="block text-gray-700 text-sm font-bold mb-2">Type:</label>
                  <select v-model="workExperienceData.type" id="type" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    <option value="">Select Type</option>
                    <option v-for="work_experience_type in workExperienceOptions" :key="work_experience_type" :value="work_experience_type">
                      {{ work_experience_type }}
                    </option>
                  </select>
                </div>
                <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
                  <label for="start" class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
                  <input id="start" v-model="workExperienceData.start" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                </div>
                <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
                  <label for="end" class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
                  <input id="end" v-model="workExperienceData.end" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                </div>
                <div class="mb-4">
                  <label for="days" class="block text-gray-700 text-sm font-bold mb-2">Days:</label>
                  <input type="number" id="days" v-model="workExperienceData.days" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" readonly>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndRegisterEmployee(); " type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Register</button>
          <router-link :to="`/Employee`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
          </router-link>
        </div>
      </div>
    </div>
  </template>

  <script>
  import { ref, onMounted,watch } from 'vue';
  import { useRouter,useRoute } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';

  export default {
    setup() {
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
      const files = ref([])
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
        qualification_id: '',
        user_id: '',
        the_workouts_selection: '',
        created_at: new Date().toISOString(),
      });
      const workExperienceData = ref({
        name: '',
        start: '',
        type: '',
        end: '',
        days: 0,
        employee_id: 0,
        created_at: new Date().toISOString(),
        user_id: 1, 
      });

    
      watch([() => editEmployee.value.name, () => editEmployee.value.last_name], () => {
      if (editEmployee.value.name && editEmployee.value.last_name) {
        editEmployee.value.username = `${editEmployee.value.name}.${editEmployee.value.last_name}`;
      }
    });

      const fetchNumber = async () => {
        try {
          const response = await api.get('/employees/generate_unique_number');
          generatedNumber.value = response.data;
          editEmployee.value.number = generatedNumber.value.number; 
          // console.log(generatedNumber.value);
          // console.log(generatedNumber)
        } catch (error) {
          console.error("Error fetching categories:", error);
        }
      };

      const fetchCategories = async () => {
      try {
        const response = await api.get('/api/categories');
        categories.value = response.data;
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    };

    const fetchTitles = async (index) => {
      const category = metadata.value[index].selectedCategory;
      if (category) {
        try {
          const response = await api.get(`/api/titles?category_id=${category}`);
          metadata.value[index].titles = response.data;
        } catch (error) {
          console.error("Error fetching titles:", error);
        }
      }
    };

    // const handleFileChange = (index, event) => {
    //   const selectedFiles = event.target.files;
    //   if (selectedFiles && selectedFiles.length > 0) {
    //     files.value[index] = selectedFiles;
    //   }
    // };

    // const addDocument = () => {
    //   metadata.value.push({ selectedCategory: '', selectedTitle: '', description: '', titles: [] });
    // };

      const fetchWorkExperienceType = async () => {
        try {
          const response = await api.get('/workExperience/work_experience/type');
          workExperienceOptions.value = response.data;
        } catch (error) {
          handleApiError(error, 'marital status options');
        }
      };
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

      const submitWorkExperience = async () => {
        try {
          const responseEmployeeId = await api.get('/employees/last_employee_id');
          const lastEmployeeId = responseEmployeeId.data;

          workExperienceData.value.employee_id = lastEmployeeId;

          const response = await api.post('/workExperience/create_WorkExperience', workExperienceData.value);
          console.log('Success:', response.data);
        } catch (error) {
          console.error('Error:', error);
        }
      };
      const submitForm = async () => {
        try {
          const response = await api.get('/employees/last_employee_id');

          const lastEmployeeId = response.data;

          for (let i = 0; i < metadata.value.length; i++) {

            const doc = metadata.value[i];

            const formData = new FormData();

            const metadataObject = {
              title: doc.selectedTitle,
              description: doc.description,
              category_id: selectedCategory.value,
              created_at: new Date().toISOString(),
              updated_at: new Date().toISOString(),
              employee_id: lastEmployeeId 
            };

            formData.append('metadata_json', JSON.stringify([metadataObject]));

            for (const file of files.value[i]) {
              formData.append('files', file);
            }

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
  // const handleFileChange = (index, event) => {
  //   const selectedFiles = event.target.files;
  //   if (selectedFiles && selectedFiles.length > 0) {
  //     files.value[index] = selectedFiles[0];
  //   }
  // };
      const handleFileChange = (index, event) => {
        const selectedFiles = event.target.files;
        if (selectedFiles && selectedFiles.length > 0) {
          files.value[index] = selectedFiles;
        }
      };

      const addDocument = () => {
        metadata.value.push({ selectedTitle: '', description: '', category_id: null });
      };

      const fetchCitiesAndZipCodes = async () => {
        try {
            const response = await api.get('/employees/cities');
            // console.log("response", response);
            cities.value = response.data;
            // console.log(cities.value);
          } catch (error) {
            console.error('Error fetching cities:', error);
          }
      };

      const fetchZipCodes = async (cityName) => {
        try {
          const response = await api.get('/employees/zipcodes', {
            params: {
              city_name: cityName
            },
            headers: {
              'Accept': 'application/json'
            }
          });
          // console.log(response.data);
          const zipCodesData = response.data.zip_codes;
          if (Array.isArray(zipCodesData)) {
            zipCodes.value = zipCodesData;
            if (zipCodesData.length === 1) {
              editEmployee.value.selectedZipCode = zipCodesData[0];
            }
          }
        } catch (error) {
          console.error('Error fetching zip codes:', error);
          handleApiError(error, 'zipcodes');
        }
      };

      const onCityChange = (event) => {
        const cityName = event.target.value;
        fetchZipCodes(cityName);
      };

      const fetchEthnicities = async () => {
        try {
          const response = await api.get('/ethnicities/active_ethnicities');
          ethnicities.value = response.data;
        } catch (error) {
          handleApiError(error, 'ethnicities');
        }
      };

      const fetchInstitutions = async () => {
        try {
          const response = await api.get('/institutions/active_institutions');
          institutions.value = response.data;
        } catch (error) {
          handleApiError(error, 'institutions');
        }
      };

      const fetchMaritalStatusOptions = async () => {
        try {
          const response = await api.get('/employees/marital_status');
          maritalStatusOptions.value = response.data;
        } catch (error) {
          handleApiError(error, 'marital status options');
        }
      };

      const fetchGenderOptions = async () => {
        try {
          const response = await api.get('/employees/genders');
          genderOptions.value = response.data;
        } catch (error) {
          handleApiError(error, 'gender options');
        }
      };

      const fetchDepartments = async (institutionId) => {
        try {
          const response = await api.get(`/departments/institutions/${institutionId}/departments`);
          departments.value = response.data;
        } catch (error) {
          handleApiError(error, 'departments');
        }
      };

      const fetchJobPositions = async (institutionId, departmentId) => {
        try {
          const response = await api.get(`/institutions/job_positions/${institutionId}/${departmentId}?institutions_id=${institutionId}`);
          jobPositions.value = response.data;
        } catch (error) {
          handleApiError(error, 'job positions');
        }
      };

      const onInstitutionChange = () => {
        const institutionId = editEmployee.value.selectedInstitution;
        if (institutionId) {
          fetchDepartments(institutionId);
          jobPositions.value = [];
          const departmentId = editEmployee.value.selectedDepartment;
          if (departmentId) {
            fetchJobPositions(institutionId, departmentId);
          }
        }
      };

      const onDepartmentChange = () => {
        const institutionId = editEmployee.value.selectedInstitution;
        const departmentId = editEmployee.value.selectedDepartment;
        // const jobPositionId=editEmployee.value.selectedJobPosition
        if (institutionId && departmentId ) {
          fetchJobPositions(institutionId, departmentId);
        } else {
          console.error('Either institutionId or departmentId is null.');
        }
      };
            watch(() => editEmployee.value.selectedCity, (newCity) => {
                if (newCity) {
                    fetchZipCodes(newCity);
                } else {
                    zipCodes.value = [];
                }
                });
      const fetchEmployeeData = async () => {
        try {
            const id = Number(route.params.id);
            const response = await api.get(`/employees/employees/${id}`);
            const employeeData = response.data;

            editEmployee.value.user_id = 1;

            // editEmployee.value.gender = employeeData.genders;

            // editEmployee.value.marital_status = employeeData.maritalStatus;
            editEmployee.value.genders = employeeData.gender;
            editEmployee.value.maritalStatus = employeeData.marital_status;
            editEmployee.value.selectedInstitution = employeeData.institucion_id;
            editEmployee.value.selectedDepartment = employeeData.department_id;
            editEmployee.value.selectedJobPosition = employeeData.job_position_id;
            editEmployee.value.selectedCity=employeeData.city
            editEmployee.value.selectedZipCode =employeeData.zipcode
            onInstitutionChange();
            // onCityChange();
            for (const key in employeeData) {
            if (Object.prototype.hasOwnProperty.call(employeeData, key)) {
                // if (key !== 'gender' && key !== 'marital_status' ) {
                editEmployee.value[key] = employeeData[key];
                // }
            }
            }
        } catch (error) {
            console.error("Error fetching employee data:", error);
        }
    };


    const downloadDocuments = async () => {
      const employeeId = route.params.id;
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
        const employeeId = route.params.id;

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

//     const fetchEmployeeDocuments = async (employeeId) => {

// try {
//   const employeeId = route.params.id;

//   const response = await api.get(`/api/employees/${employeeId}/documents`);
//   documents.value = response.data;
//   documents_id =documents.value.document_id
//   console.log(documents_id)
// } catch (error) {
//   console.error('Error fetching employee documents:', error);
// }
// };

//     const downloadDocument = async (doc) => {
//       try {
//         const response = await api.get(`/download_file/${doc.id}`, {
//           responseType: 'blob',
//         });
//         const url = window.URL.createObjectURL(new Blob([response.data]));
//         const link = document.createElement('a');
//         link.href = url;
//         link.setAttribute('download', doc.title);
//         document.body.appendChild(link);
//         link.click();
//         document.body.removeChild(link);
//       } catch (error) {
//         console.error('Error downloading document:', error);
//       }
//     };
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
      const validateAndRegisterEmployee = async (documentUpload) => {
        console.log(editEmployee.value); // Log the editEmployee.value object
        editEmployee.value.gender = editEmployee.value.genders; // Corrected assignment
        console.log(editEmployee.value.genders)
        editEmployee.value.marital_status = editEmployee.value.maritalStatus;
        console.log(editEmployee.value.marital_status)

        editEmployee.value.institucion_id = editEmployee.value.selectedInstitution;
        editEmployee.value.department_id = editEmployee.value.selectedDepartment;
        editEmployee.value.job_position_id = editEmployee.value.selectedJobPosition;
        editEmployee.value.city=editEmployee.value.selectedCity

        editEmployee.value.zipcode=editEmployee.value.selectedZipCode

        editEmployee.value.user_id = 1;

        try {
            const employeeId = route.params.id;

          const response = await api.put(`/employees/update_employee/${employeeId}`, editEmployee.value);
          // console.log('Employee created successfully:', response.data);
          await submitForm();     
          await submitWorkExperience();
          router.push('/Employee');
          setTimeout(() => {
            toast.success('Employee created successfully!', {
              autoClose: 3000,
              position: toast.POSITION.TOP_RIGHT,
            });
          }, 250);
        } catch (error) {
          console.error('Error creating employee:', error);
          toast.error('Failed to create employee!', {
            autoClose: 3000,
            position: toast.POSITION.TOP_RIGHT,
          });
        }
      };
      const handleApiError = (error, resourceName) => {
        console.error(`Error fetching ${resourceName}:`, error);
        toast.error(`Failed to fetch ${resourceName}!`, {
          autoClose: 3000,
          position: toast.POSITION.TOP_RIGHT,
        });
      };



      onMounted(() => {
        const employeeId = route.params.id;
      fetchEmployeeDocuments(employeeId);
        fetchEmployeeDocuments();
        fetchEmployeeData();
        fetchCategories();
        // fetchUploadDocuments();
        fetchNumber();
        // downloadDocuments();
        // fetchUsername();
        fetchInstitutions();
        fetchEthnicities();
        fetchMaritalStatusOptions();
        fetchGenderOptions();
        fetchCitiesAndZipCodes();
        fetchWorkExperienceType();
      });

      return {
        institutions,
        departments,
        jobPositions,
        editEmployee,
        validateAndRegisterEmployee,
        onInstitutionChange,
        onDepartmentChange,
        ethnicities,
        maritalStatusOptions,
        workExperienceOptions,
        genderOptions,
        cityOptions,
        zipCodeOptions,
        cities,
        zipCodes,
        onCityChange,
        selectedZipCode,
        documentUpload,
        metadata,
        submitForm,
        handleFileChange,
        addDocument,
        files,
        selectedCategory,
        categories,
        titles,
        selectedTitle,
        editEmployee,
        workExperienceData,
        fetchTitles,
        fetchCategories,
        downloadDocuments,
        downloadDocument,
        documents_id,
        deleteDocument,
        // fetchUploadDocuments,
        documents,
        fetchEmployeeDocuments,
        fetchNumber,
        generatedNumber,
        selectedTitle,
        workExperienceData,
        submitWorkExperience,
      };
    },
  };
</script>


<!-- 
<template>
    <div class="container mx-auto p-6">
      <div class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">Edit Employee</h1>
        <div class="employee-details flex flex-wrap">
          <div
            class="w-full md:w-1/3 mb-4 md:mb-0 px-2"
            v-for="(field, index) in employeeFields"
            :key="index"
          >
            <label class="block text-gray-700 text-sm font-bold mb-2">
              {{ field.label }}
            </label>
            <component
              :is="field.component"
              v-model="editEmployee[field.model]"
              :type="field.type"
              :disabled="field.disabled"
              :class="field.class"
            >
              <option
                v-if="field.options"
                v-for="option in field.options"
                :key="option.value"
                :value="option.value"
              >
                {{ option.text }}
              </option>
            </component>
          </div>
        </div>
        <div class="container mx-auto p-6">
          <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
            <h1 class="text-2xl font-bold mb-6">Upload Documents</h1>
            <form>
              <div v-for="(doc, index) in metadata" :key="index">
                <div class="w-full mb-4">
                  <label
                    class="block text-gray-700 text-sm font-bold mb-2"
                    for="category"
                  >
                    Select Category:
                  </label>
                  <select
                    class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                    id="category"
                    v-model="doc.category_id"
                    @change="fetchTitles"
                  >
                    <option
                      v-for="category in categories"
                      :key="category.category_id"
                      :value="category.category_id"
                    >
                      {{ category.category_name }}
                    </option>
                  </select>
                </div>
                <div class="w-full mb-4">
                  <label
                    for="title"
                    class="block text-gray-700 text-sm font-bold mb-2"
                  >
                    Select Title:
                  </label>
                  <select
                    id="title"
                    v-model="doc.selectedTitle"
                    class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                  >
                    <option
                      v-for="title in titles"
                      :key="title.title_id"
                      :value="title.title"
                    >
                      {{ title.title }}
                    </option>
                  </select>
                </div>
                <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2">
                    Description:
                  </label>
                  <input
                    v-model="doc.description"
                    type="text"
                    class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                  />
                </div>
                <div class="mb-4">
                  <label class="block text-gray-700 text-sm font-bold mb-2">
                    Select Files:
                  </label>
                  <input
                    type="file"
                    multiple
                    @change="handleFileChange(index, $event)"
                    class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                  />
                </div>
              </div>
              <button
                type="button"
                @click="addDocument"
                class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2"
              >
                Add Another Document
              </button>
            </form>
          </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button
            @click="validateAndRegisterEmployee"
            type="submit"
            class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md"
          >
            Register
          </button>
          <router-link :to="`/Employee`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">
              Cancel
            </button>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  import { useRouter, useRoute } from "vue-router";
  import { api } from "@/api";
  import { toast } from "vue3-toastify";
  
  export default {
    setup() {
      const router = useRouter();
      const route = useRoute();
      const institutions = ref([]);
      const departments = ref([]);
      const jobPositions = ref([]);
      const ethnicities = ref([]);
      const maritalStatusOptions = ref([]);
      const genderOptions = ref([]);
      const cityOptions = ref([]);
      const zipCodeOptions = ref([]);
      const categories = ref([]);
      const titles = ref([]);
      const selectedCategory = ref("");
      const metadata = ref([
        { selectedTitle: "", description: "", category_id: selectedCategory.value },
      ]);
  
      const editEmployee = ref({
        selectedInstitution: null,
        selectedDepartment: null,
        selectedJobPosition: null,
        selectedCity: "",
        selectedZipCode: "",
        name: "",
        number: "",
        username: "",
        middle_name: "",
        last_name: "",
        gender: "",
        ethnicity_id: 0,
        marital_status: "",
        date_of_birth: "",
        date_hired: "",
        contract_end_date: "",
        personal_number: "",
        salary: "",
        addition: 0,
        street: "",
        city: "",
        zipcode: "",
        country: "",
        phone_number: "",
        phone_number_2: "",
        email: "",
        email_2: "",
        days_off: 0,
        transferred_days_off: 0,
        earned_days_off: 0,
        next_year_earned_days_off: 0,
        active: true,
        qualification_id: 0,
        user_id: 0,
        the_workouts_selection: "",
        created_at: new Date().toISOString(),
      });
  
      const employeeFields = [
        { label: "Name", component: "input", type: "text", model: "name", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Number", component: "input", type: "text", model: "number", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", disabled: true },
        { label: "Username", component: "input", type: "text", model: "username", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Middle Name", component: "input", type: "text", model: "middle_name", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Last Name", component: "input", type: "text", model: "last_name", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Gender", component: "select", model: "gender", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", options: genderOptions.value },
        { label: "Ethnicity", component: "select", model: "ethnicity_id", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", options: ethnicities.value },
        { label: "Marital Status", component: "select", model: "marital_status", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", options: maritalStatusOptions.value },
        { label: "Date of Birth", component: "input", type: "date", model: "date_of_birth", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Date Hired", component: "input", type: "date", model: "date_hired", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Contract End Date", component: "input", type: "date", model: "contract_end_date", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Personal Number", component: "input", type: "text", model: "personal_number", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Salary", component: "input", type: "number", model: "salary", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
        { label: "Addition", component: "input", type: "number", model: "addition", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Street", component: "input", type: "text", model: "street", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "City", component: "select", model: "selectedCity", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", options: cityOptions.value },
      { label: "Zip Code", component: "select", model: "selectedZipCode", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md", options: zipCodeOptions.value },
      { label: "Country", component: "input", type: "text", model: "country", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Phone Number", component: "input", type: "text", model: "phone_number", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Secondary Phone Number", component: "input", type: "text", model: "phone_number_2", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Email", component: "input", type: "email", model: "email", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Secondary Email", component: "input", type: "email", model: "email_2", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Days Off", component: "input", type: "number", model: "days_off", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Transferred Days Off", component: "input", type: "number", model: "transferred_days_off", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Earned Days Off", component: "input", type: "number", model: "earned_days_off", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Next Year Earned Days Off", component: "input", type: "number", model: "next_year_earned_days_off", class: "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" },
      { label: "Active", component: "input", type: "checkbox", model: "active", class: "mr-2 leading-tight" },
    ];

    const fetchData = async () => {
      try {
        const [
          institutionsResponse,
          departmentsResponse,
          jobPositionsResponse,
          ethnicitiesResponse,
          maritalStatusResponse,
          genderResponse,
          cityResponse,
          zipCodeResponse,
          categoriesResponse,
        ] = await Promise.all([
          api.get("/institutions"),
          api.get("/departments"),
          api.get("/job_positions"),
          api.get("/ethnicities"),
          api.get("/marital_status"),
          api.get("/genders"),
          api.get("/cities"),
          api.get("/zip_codes"),
          api.get("/categories"),
        ]);

        institutions.value = institutionsResponse.data;
        departments.value = departmentsResponse.data;
        jobPositions.value = jobPositionsResponse.data;
        ethnicities.value = ethnicitiesResponse.data;
        maritalStatusOptions.value = maritalStatusResponse.data;
        genderOptions.value = genderResponse.data;
        cityOptions.value = cityResponse.data;
        zipCodeOptions.value = zipCodeResponse.data;
        categories.value = categoriesResponse.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    const fetchEmployeeData = async (id) => {
      try {
        const response = await api.get(`/employees/employees/${id}`);
        const employeeData = response.data;

        // Map fetched data to editEmployee object
        for (const key in employeeData) {
          if (editEmployee.value.hasOwnProperty(key)) {
            editEmployee.value[key] = employeeData[key];
          }
        }
      } catch (error) {
        console.error("Error fetching employee data:", error);
      }
    };

    const fetchTitles = async () => {
      try {
        const response = await api.get(`/api/titles?category_id=${selectedCategory.value}`);
        titles.value = response.data;
      } catch (error) {
        console.error("Error fetching titles:", error);
      }
    };

    const addDocument = () => {
      metadata.value.push({ selectedTitle: "", description: "", category_id: selectedCategory.value });
    };

    const handleFileChange = (index, event) => {
      const files = event.target.files;
      metadata.value[index].files = files;
    };

    const validateAndRegisterEmployee = async () => {
      try {
        const employeeData = {
          ...editEmployee.value,
          selectedInstitution: editEmployee.value.selectedInstitution,
          selectedDepartment: editEmployee.value.selectedDepartment,
          selectedJobPosition: editEmployee.value.selectedJobPosition,
          selectedCity: editEmployee.value.selectedCity,
          selectedZipCode: editEmployee.value.selectedZipCode,
        };

        const employeeResponse = await api.put(`/employees/employees/${route.params.id}`, employeeData);

        if (metadata.value.length) {
          const formData = new FormData();
          metadata.value.forEach((doc, index) => {
            formData.append(`metadata[${index}][title]`, doc.selectedTitle);
            formData.append(`metadata[${index}][description]`, doc.description);
            Array.from(doc.files).forEach((file, fileIndex) => {
              formData.append(`files[${index}][${fileIndex}]`, file);
            });
          });

          const documentResponse = await api.post(`/api/documents/upload`, formData);
        }

        toast.success("Employee updated successfully");
        router.push("/Employee");
      } catch (error) {
        toast.error("Failed to update employee");
        console.error("Error updating employee:", error);
      }
    };

    onMounted(() => {
      fetchData();
      const id = route.params.id;
      fetchEmployeeData(id);
    });

    return {
      editEmployee,
      employeeFields,
      institutions,
      departments,
      jobPositions,
      ethnicities,
      maritalStatusOptions,
      genderOptions,
      cityOptions,
      zipCodeOptions,
      categories,
      titles,
      selectedCategory,
      metadata,
      addDocument,
      handleFileChange,
      validateAndRegisterEmployee,
    };
  },
};
</script> -->
