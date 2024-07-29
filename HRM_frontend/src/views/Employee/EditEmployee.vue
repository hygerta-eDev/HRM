<template>
    <div class="container mx-auto p-6">
      <div  class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
        <h1 class="text-2xl font-bold mb-6">Edit New Employee</h1>
        <div class="employee-details mb-6">
        <div class="flex items-center mb-4 mt-10">
          <hr class="flex-grow border-gray-400">
          <h2 class="mx-4 text-xl font-semibold text-center">Personal Information</h2>
          <hr class="flex-grow border-gray-400">
        </div>
        <div class="flex flex-wrap -mx-2 bg-gray-200">
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Number</label>
            <input v-model="editEmployee.number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" disabled>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
            <input v-model="editEmployee.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
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
            <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
            <input v-model="editEmployee.username" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Personal Number</label>
            <input v-model="editEmployee.personal_number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
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
          <label class="block text-gray-700 text-sm font-bold mb-2">Gender</label>
          <select v-model="editEmployee.gender" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Gender</option>
            <option v-for="genders in genderOptions" :key="genders" :value="genders">
              {{ genders }}
            </option>
          </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Marital Status</label>
            <select v-model="editEmployee.marital_status" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select maritalStatus</option>
              <option v-for="maritalStatus in maritalStatusOptions" :key="maritalStatus" :value="maritalStatus">
                {{ maritalStatus}}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Date of Birth</label>
            <input v-model="editEmployee.date_of_birth" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        </div>
        <div  class="employee-details mb-6">      
  <div class="flex items-center mb-4 mt-10">
          <hr class="flex-grow border-gray-400">
          <h2 class="mx-4 text-xl font-semibold text-center">Contact Details</h2>
          <hr class="flex-grow border-gray-400">
        </div>
        <div  class="flex flex-wrap -mx-2 bg-gray-200">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Street</label>
            <input v-model="editEmployee.street" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">City</label>
            <select v-model="editEmployee.selectedCity" @change="onCityChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select City</option>
              <option v-for="city in cities" :key="city.city_name" :value="city.city_name">
                {{ city.city_name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
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
          </div>

<div class="container mx-auto p-6">
      <div class="flex items-center mb-4 mt-10">
        <hr class="flex-grow border-gray-400">
        <h2 class="mx-4 text-xl font-semibold text-center">Employeement Details</h2>
        <hr class="flex-grow border-gray-400">
      </div>
      <div class="flex flex-wrap -mx-2 bg-gray-200">
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
          
        </div>
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
          <div class="flex items-center mb-4 mt-10">
            <hr class="flex-grow border-gray-400">
            <h2 class="mx-4 text-xl font-semibold text-center">Upload Documents</h2>
            <hr class="flex-grow border-gray-400">
          </div>

          <div class="flex flex-wrap -mx-2 bg-gray-200">
            <div class="w-full mb-4 px-2">
              <form @submit.prevent="submitForm">
                <div v-if="showDocumentFields">
                  <div v-for="(doc, index) in metadata" :key="index" class="flex flex-wrap">
                    <!-- Select Category -->
                    <div class="w-full md:w-1/4 mb-4 px-2">
                      <label :for="'category-' + index" class="block text-gray-700 text-sm font-bold mb-2">Select Category:</label>
                      <select
                        :id="'category-' + index"
                        v-model.number="doc.selectedCategory"
                        @change="fetchTitles(index)"
                        class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                      >
                        <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
                          {{ category.category_name }}
                        </option>
                      </select>
                    </div>
                    <!-- Select Title -->
                    <div class="w-full md:w-1/4 mb-4 px-2">
                      <label :for="'title-' + index" class="block text-gray-700 text-sm font-bold mb-2">Select Title:</label>
                      <select
                        :id="'title-' + index"
                        v-model="doc.selectedTitle"
                        class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                      >
                        <option v-for="title in doc.titles" :key="title.title_id" :value="title.title">
                          {{ title.title }}
                        </option>
                      </select>
                    </div>
                    <!-- Description -->
                    <div class="w-full md:w-1/4 mb-4 px-2">
                      <label class="block text-gray-700 text-sm font-bold mb-2">Description:</label>
                      <input v-model="doc.description" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    </div>
                    <!-- Select Files -->
                    <div class="w-full md:w-1/4 mb-4 px-2">
                      <label class="block text-gray-700 text-sm font-bold mb-2">Select Files:</label>
                      <input type="file" multiple @change="handleFileChange(index, $event)" class="block w-full text-sm text-gray-900 border border-blue-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400">
                    </div>
                  </div>
                </div>
                <button type="button" @click="addDocument" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Document</button>
              </form>
            </div>
          </div>
        </div>
        <div class="container mx-auto p-6">
            <div class="create-company p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
              <h1 class="text-2xl font-bold mb-6">Work Experience</h1>
              <form @submit.prevent="submitForm">
                <div class="flex flex-wrap">
                <div v-for="(workExperience, index) in workExperienceList" :key="index" class="w-full sm:w-1/4 md:w-1/3 p-2">
                  <div class="edit-company p-8 rounded-lg shadow-xl border border-blue-200 bg-gray-100">
                    <div class="mb-4">
                      <label :for="'title-' + index" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
                      <input type="text" v-model="workExperience.name" :id="'title-' + index" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    </div>
                    <div class="mb-4">
                      <label :for="'type-' + index" class="block text-gray-700 text-sm font-bold mb-2">Type:</label>
                      <select v-model="workExperience.type" :id="'type-' + index" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                        <option value="">Select Type</option>
                        <option v-for="work_experience_type in workExperienceOptions" :key="work_experience_type" :value="work_experience_type">
                          {{ work_experience_type }}
                        </option>
                      </select>
                    </div>
                    <div class="w-full mb-4 px-2">
                      <label :for="'start-' + index" class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
                      <input :id="'start-' + index" v-model="workExperience.start" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    </div>
                    <div class="w-full mb-4 px-2">
                      <label :for="'end-' + index" class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
                      <input :id="'end-' + index" v-model="workExperience.end" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
                    </div>
                    <div class="mb-4">
                      <!-- <label :for="'days-' + index" class="block text-gray-700 text-sm font-bold mb-2">Days:</label> -->
                      <input type="number" :id="'days-' + index" v-model="workExperience.days" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" readonly hidden>
                    </div>
                  </div>
                </div>
              </div>
              </form>
              <!-- <button type="button" @click="addWorkExperience" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Work Experience</button> -->
            </div>
        </div>
        <div class="w-full text-right mt-4 px-2">
          <button @click="validateAndRegisterEmployee(); " type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Edit</button>
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
