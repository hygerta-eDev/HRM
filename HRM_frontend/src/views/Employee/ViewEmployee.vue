<template>
    <div class="container mx-auto p-6">
      <div class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
        <h1 class="text-2xl font-bold mb-6">View Employee {{ editEmployee.name }}</h1>
        
        <!-- Personal Information -->
        <div class="employee-details mb-6">
          <div class="flex items-center mb-4 mt-10">
            <hr class="flex-grow border-gray-400">
            <h2 class="mx-4 text-xl font-semibold text-center">Personal Information</h2>
            <hr class="flex-grow border-gray-400">
          </div>
          <div class="flex flex-wrap -mx-2 bg-gray-200">
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
                <label class="block text-gray-700 text-sm font-bold mb-2">Number</label>
                <div class="input-container">
                    <div class="input-content">{{ editEmployee.number }}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
              <div class="input-container">
                    <div class="input-content">{{ editEmployee.name }}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Middle Name</label>
              <div class="input-container">
                    <div class="input-content">{{editEmployee.middle_name }}</div>
                </div>
              <!-- <input v-model="editEmployee.middle_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" disabled> -->
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.last_name }}</div>
                </div>

              
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.username }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Personal Number</label>
              <div class="input-container">
                    <div class="input-content">{{editEmployee.personal_number }}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity</label>              
              <div class="input-container" >
                    <div class="input-content">                  
                        {{ selectedEthnicityName}}
                    </div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Gender</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.gender}}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Marital Status</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.marital_status}}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Date of Birth</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.date_of_birth }}</div>
                </div>
            </div>
          </div>
        </div>
        
        <!-- Contact Details -->
        <div class="employee-details mb-6">
          <div class="flex items-center mb-4 mt-10">
            <hr class="flex-grow border-gray-400">
            <h2 class="mx-4 text-xl font-semibold text-center">Contact Details</h2>
            <hr class="flex-grow border-gray-400">
          </div>
          <div class="flex flex-wrap -mx-2 bg-gray-200">
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Street</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.street }}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">City</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.selectedCity}}</div>
                </div>
            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Zip Code</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.selectedZipCode }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Country</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.country }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.phone_number }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number 2</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.phone_number_2 }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Email</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.email }}</div>
                </div>

            </div>
            <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
              <label class="block text-gray-700 text-sm font-bold mb-2">Email 2</label>              
              <div class="input-container">
                    <div class="input-content">{{editEmployee.email_2 }}</div>
                </div>

            </div>
          </div>
        </div>
        
        <!-- Employment Details -->
        <div class="container mx-auto p-6">
      <div class="flex items-center mb-4 mt-10">
        <hr class="flex-grow border-gray-400">
        <h2 class="mx-4 text-xl font-semibold text-center">Employeement Details</h2>
        <hr class="flex-grow border-gray-400">
      </div>
      <div class="flex flex-wrap -mx-2 bg-gray-200">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Date Hired</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.date_hired }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Contract End Date</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.contract_end_date }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Institution</label>              
            <div class="input-container">
                    <div class="input-content">{{selectedInstitutionName  }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>              
            <div class="input-container">
                    <div class="input-content">{{selectedDepartmentName }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Salary</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.salary }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Addition</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.addition }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Job Position</label>              
            <div class="input-container">
                    <div class="input-content">{{selectedJobPositionName }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Days Off</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.days_off }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Transferred Days Off</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.transferred_days_off }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Earned Days Off</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.earned_days_off }}</div>
                </div>

          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Next Year Earned Days Off</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.next_year_earned_days_off }}</div>
                </div>

          </div>

          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">The Workouts Selection</label>              
            <div class="input-container">
                    <div class="input-content">{{editEmployee.the_workouts_selection }}</div>
                </div>

          </div>
</div>
          
        </div>
        
        <!-- Documents -->
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
                  <button @click="downloadDocuments" class="bg-green-500 text-white px-4 py-2 rounded-lg ml-2 shadow-md">Download AllDocuments</button>
              </div>
              <div v-else>
                  <p>No documents available.</p>
              </div>
            </div>
        </div>
        
        <!-- Work Experience -->
        <div class="container mx-auto p-6">
          <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 ">
            <h1 class="text-2xl font-bold mb-6">Work Experience</h1>
            <form v-if="workExperienceList.length"  @submit.prevent="submitForm">
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
            <div v-else>
                  <p>No work_experience available.</p>
              </div>
          </div>
        </div>
        
        <!-- Buttons -->
        <div class="w-full text-right mt-4 px-2">
          <router-link :to="`/Employee`">
            <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
          </router-link>
        </div>
      </div>
    </div>
  </template>
<script>
import { ref, onMounted,watch,computed } from 'vue';
import { useRouter,useRoute } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';

export default {
  setup() {
    const showDocumentFields= ref(false);
    const  workExperiences= ref([]);
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
    const workExperienceList = ref([]);

    const addWorkExperience = () => {
        workExperienceList.value.push({
          id:'',
          name: '',
          start: '',
          type: '',
          end: '',
          days: 0,
          employee_id: 0,
          created_at: new Date().toISOString(),
          user_id: 1,
        });
      };
      watch(
        [() => editEmployee.value.name, () => editEmployee.value.last_name],
        () => {
          if (editEmployee.value.name && editEmployee.value.last_name) {
            editEmployee.value.username = `${editEmployee.value.name.toLowerCase()}.${editEmployee.value.last_name.toLowerCase()}`;
          }
        }
      );

      const editExperienceId = ref(null); // Track which experience is being edited
      const editExperience = ref({
        name: '',
        type: '',
        start: '',
        end: '',
        days: 0,
      });

      const fetchWorkExperiences = async () => {
        try {
          const employeeId = route.params.id;
          const response = await api.get(`/workExperience/employees/${employeeId}/work_experiences`);
          workExperienceList.value = response.data.map((experience) => ({
            ...experience,
            start: experience.start ? new Date(experience.start).toISOString().split('T')[0] : '',
            end: experience.end ? new Date(experience.end).toISOString().split('T')[0] : '',
          }));
          console.log('work', workExperienceList.value);
        } catch (error) {
          console.error('Error fetching work experiences:', error);
        }
      };

      const startEditing = (experience) => {
        editExperienceId.value = experience.id;
        editExperience.value = {
          name: experience.name,
          type: experience.type,
          start: experience.start,
          end: experience.end,
          days: experience.days,
        };
      };

      const cancelEditing = () => {
        editExperienceId.value = null;
        editExperience.value = {
          name: '',
          type: '',
          start: '',
          end: '',
          days: 0,
        };
      };

      const saveEdit = async () => {
        try {
          const employeeId = route.params.id;
          const currentTime = new Date().toISOString();
          const updatedExperiences = workExperienceList.value.map(experience => ({
            ...experience,
            updated_at: currentTime 
          }));

          const response = await api.put(`/workExperience/employees/${employeeId}/work_experiences`, updatedExperiences);

          console.log('Work experiences updated successfully:', response.data);
          cancelEditing();
        } catch (error) {
          console.error('Error saving work experiences:', error);
        }
      };


      const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toISOString().split('T')[0]; // Format as YYYY-MM-DD
      };

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
      const fetchWorkExperienceType = async () => {
        try {
          const response = await api.get('/workExperience/work_experience/type');
          workExperienceOptions.value = response.data;
        } catch (error) {
          handleApiError(error, 'marital status options');
        }
      };
      const calculateDays = (workExperience) => {
        if (workExperience.start && workExperience.end) {
          const startDate = new Date(workExperience.start);
          const endDate = new Date(workExperience.end);
          const timeDifference = endDate - startDate;
          const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));
          workExperience.days = daysDifference;
        } else {
          workExperience.days = 0;
        }
      };

      watch(() => workExperienceList.value, (newVal) => {
        newVal.forEach(workExperience => calculateDays(workExperience));
      }, { deep: true });

      const submitForm = async () => {
          try {
            const lastEmployeeId = route.params.id;

            for (let i = 0; i < metadata.value.length; i++) {

              const doc = metadata.value[i];

              const formData = new FormData();

              const metadataObject = {
                  title: doc.selectedTitle,
                  description: doc.description,
                  category_id: doc.selectedCategory,
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


      const handleFileChange = (index, event) => {
        const selectedFiles = event.target.files;
        if (selectedFiles && selectedFiles.length > 0) {
          files.value[index] = selectedFiles;
        }
      };

      const addDocument = () => {
        metadata.value.push({ selectedTitle: '', description: '', category_id: null ,}) ;if (!showDocumentFields.value) {
          showDocumentFields.value = true;
        }
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
          console.log(ethnicities)
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
            console.log(employeeData);

            // editEmployee.value.gender = employeeData.genders;

            // editEmployee.value.marital_status = employeeData.maritalStatus;
            editEmployee.value.genders = employeeData.gender;
            editEmployee.value.maritalStatus = employeeData.marital_status;
            editEmployee.value.selectedInstitution = employeeData.institucion_id;
            console.log("editemployee",editEmployee.value.selectedInstitution)
            console.log("employeeData",employeeData.institucion_id)

            editEmployee.value.selectedDepartment = employeeData.department_id;
            editEmployee.value.selectedJobPosition = employeeData.job_position_id;
            editEmployee.value.selectedCity=employeeData.city;
            editEmployee.value.selectedZipCode =employeeData.zipcode;
            onInstitutionChange();
            // onCityChange();
            for (const key in employeeData) {
            if (Object.prototype.hasOwnProperty.call(employeeData, key)) {
                editEmployee.value[key] = employeeData[key];
                
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
            console.log(editEmployee)
            try {
                const employeeId = route.params.id;

              const response = await api.put(`/employees/update_employee/${employeeId}`, editEmployee.value);
              // console.log('Employee created successfully:', response.data);
              await submitForm();     
              await saveEdit();
              router.push('/Employee');
              setTimeout(() => {
                toast.success('Employee updated successfully!', {
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
      fetchWorkExperiences();

    });

    return {
      selectedInstitutionName,
      selectedDepartmentName,
      selectedJobPositionName,
      selectedEthnicityName,
      showDocumentFields,
      workExperienceList,
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
      // workExperienceData,
      addWorkExperience,
      fetchWorkExperiences,
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
      // workExperienceData,
      addWorkExperience,
      workExperiences,
      formatDate,
      // submitWorkExperience,
      startEditing,
    cancelEditing,
    saveEdit,
    editExperience
    };
  },
};
</script>
<style scoped>
.input-container {
  width: 100%;
  background-color: #fff;
  border: 1px solid #a0aec0;
  border-radius: 0.25rem;
}

.input-content {
  padding: 0.5rem;
}
</style>