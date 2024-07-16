<template>
  <div class="container mx-auto p-6">
    <div class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
      <h1 class="text-2xl font-bold mb-6">Register New Employee</h1>
      <div class="flex justify-center mb-6">
        <div v-for="(step, index) in steps" :key="index" class="flex items-center">
          <div class="relative">
            <!-- Step Circle -->
            <div class="flex items-center justify-center w-12 h-12 rounded-full"
                :class="{'bg-blue-500': currentStep >= index, 'bg-gray-200': currentStep < index}">
              <span class="text-lg font-bold text-white">{{ index + 1 }}</span>
            </div>
            <!-- Step Name -->
            <div class="mt-2 flex items-center justify-center wrap">
              <span class="block text-center w-12"
                    :class="{'font-bold': currentStep >= index, 'text-gray-400': currentStep < index}">
                {{ step }}
              </span>
            </div>
          </div>
          <!-- Connector -->
          <div v-if="index !== steps.length - 1"
              class="w-24 mb-16 h-1"
              :class="{'bg-blue-500': currentStep > index, 'bg-gray-200': currentStep <= index}"></div>
        </div>
      </div>
      <!-- Personal Information Section -->
      <div v-show="currentStep === 0" class="employee-details mb-6">
        <div class="flex items-center  mt-10 mb-10">
          <hr class="flex-grow border-gray-400">
          <h2 class="mx-4 text-xl font-semibold text-center">Personal Information</h2>
          <hr class="flex-grow border-gray-400">
        </div>  
        <div class="flex flex-wrap -mx-2 p-10 bg-gray-200">
          <div class="w-full md:w-1/3 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Number</label>
            <input v-model="newEmployee.number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" disabled>
          </div>
          <div class="w-full md:w-1/3 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
            <input v-model="newEmployee.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Middle Name</label>
            <input v-model="newEmployee.middle_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
            <input v-model="newEmployee.last_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
            <input v-model="newEmployee.username" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Personal Number</label>
            <input v-model="newEmployee.personal_number" type="text"  pattern="^\d{10}$" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" maxlength="10">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Ethnicity</label>
            <select v-model="newEmployee.ethnicity_id" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Ethnicity</option>
              <option v-for="ethnicity in ethnicities" :key="ethnicity.id" :value="ethnicity.id">
                {{ ethnicity.name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Gender</label>
            <select v-model="newEmployee.gender" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Gender</option>
              <option v-for="gender in genderOptions" :key="gender" :value="gender">
                {{ gender }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Marital Status</label>
            <select v-model="newEmployee.marital_status" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Marital Status</option>
              <option v-for="status in maritalStatusOptions" :key="status" :value="status">
                {{ status }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Date of Birth</label>
            <VueDatePicker placeholder="Select a date"  v-model="newEmployee.date_of_birth" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
          </div>
        </div>
      </div>
      
      <div v-show="currentStep === 1" class="employee-details mb-6">
        <div class="flex items-center mb-10 mt-10">
          <hr class="flex-grow border-gray-400">
          <h2 class="mx-4 text-xl font-semibold text-center">Contact Details</h2>
          <hr class="flex-grow border-gray-400">
        </div>
        <div class="flex flex-wrap -mx-2 p-10 bg-gray-200">
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Street</label>
            <input v-model="newEmployee.street" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">City</label>
            <select v-model="newEmployee.selectedCity" @change="onCityChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select City</option>
              <option v-for="city in cities" :key="city.city_name" :value="city.city_name">
                {{ city.city_name }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Zip Code</label>
            <select v-model="newEmployee.selectedZipCode" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Zip Code</option>
              <option v-for="zip in zipCodes" :key="zip" :value="zip">
                {{ zip }}
              </option>
            </select>
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Country</label>
            <input v-model="newEmployee.country" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number</label>
            <input v-model="newEmployee.phone_number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Phone Number 2</label>
            <input v-model="newEmployee.phone_number_2" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Email</label>
            <input v-model="newEmployee.email" type="email" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
          <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">Email 2</label>
            <input v-model="newEmployee.email_2" type="email" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        </div>
      </div>

      <div v-show="currentStep === 2" class="employee-details mb-6">
        <div class="flex items-center mb-10 mt-10 ">
          <hr class="flex-grow border-gray-400">
          <h2 class="mx-4 text-xl font-semibold text-center">Employeement Details</h2>
          <hr class="flex-grow border-gray-400">
        </div>
        <div class="flex flex-wrap -mx-2 p-10">
          
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Date Hired</label>
          <VueDatePicker placeholder="Select a date" v-model="newEmployee.date_hired" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Contract End Date</label>
          <VueDatePicker placeholder="Select a date" v-model="newEmployee.contract_end_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
            <label class="block text-gray-700 text-sm font-bold mb-2">The Workouts Selection</label>
            <input v-model="newEmployee.the_workouts_selection" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Institution</label>
          <select v-model="newEmployee.selectedInstitution" @change="onInstitutionChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Institution</option>
            <option v-for="institution in institutions" :key="institution.id" :value="institution.id">
              {{ institution.name }}
            </option>
          </select>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Department</label>
          <select v-model="newEmployee.selectedDepartment" @change="onDepartmentChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Department</option>
            <option v-for="department in departments" :key="department.id" :value="department.id">
              {{ department.name }}
            </option>
          </select>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Job Position</label>
          <select v-model="newEmployee.selectedJobPosition" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              <option value="">Select Job Position</option>
              <option v-for="position in jobPositions" :key="position.id" :value="position">
                  {{ position.name }}
              </option>
          </select>
      </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Salary</label>
          <input v-model="newEmployee.salary" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Addition</label>
          <input v-model="newEmployee.addition" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>




        <!-- <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Days Off</label> -->
          <input v-model="newEmployee.days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" hidden>
        <!-- </div> -->
        <!-- <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Transferred Days Off</label> -->
          <input v-model="newEmployee.transferred_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" hidden>
        <!-- </div> -->
        <!-- <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Earned Days Off</label> -->
          <input v-model="newEmployee.earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" hidden>
        <!-- </div> -->
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Next Year Earned Days Off</label>
          <input v-model="newEmployee.next_year_earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" >
        </div>
        <!-- <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">CV</label> -->
          <input v-model="newEmployee.cv" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" hidden>
        <!-- </div> -->

        </div>
      </div>

      <div v-show="currentStep === 3" class="container mx-auto p-6">
      <div class="flex items-center mb-10 mt-10">
        <hr class="flex-grow border-gray-400">
        <h2 class="mx-4 text-xl font-semibold text-center">Upload Documents</h2>
        <hr class="flex-grow border-gray-400">
      </div>
      <div class="flex flex-wrap -mx-2 ">
        <!-- Document Fields -->
        <div class="w-full  mb-4 px-2">
          <form @submit.prevent="submitForm">
            <div v-for="(doc, index) in metadata" :key="index" class="flex mb-4">
              <div class="w-full md:w-1/2 mb-4 px-2">
                <label :for="'category-' + index" class="block text-gray-700 text-sm font-bold mb-2">Select Category:</label>
                <select
                  class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"
                  :id="'category-' + index"
                  v-model.number="doc.selectedCategory"
                  @change="fetchTitles(index)"
                >
                  <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
                    {{ category.category_name }}
                  </option>
                </select>
              </div>
              <div class="w-full md:w-1/2 mb-4 px-2">
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
              <div class="w-full md:w-1/2 mb-4 px-2">
                <label class="block text-gray-700 text-sm font-bold mb-2">Description:</label>
                <input v-model="doc.description" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
              </div>
              <div class="w-full md:w-1/2 mb-4 px-2">
                <label class="block text-gray-700 text-sm font-bold mb-2">Select Files:</label>
                <input type="file" multiple @change="handleFileChange(index, $event)" class="block w-full text-sm text-gray-900 border border-blue-500 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400">
              </div>
            </div>
            <button type="button" @click="addDocument" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add Another Document</button>
          </form>
        </div>
      </div>
      </div>

      <div v-show="currentStep === 4" class="container mx-auto p-6">
  <div class="flex items-center mb-10 mt-10">
    <hr class="flex-grow border-gray-400">
    <h2 class="mx-4 text-xl font-semibold text-center">Work Experience</h2>
    <hr class="flex-grow border-gray-400">
  </div>
  <div class="flex flex-wrap -mx-2 justify-center items-center">
    <form @submit.prevent="submitForm">
      <div v-for="(workExperience, index) in workExperienceList" :key="index" class="flex bg-gray-200 flex-wrap mb-6 border border-blue-500 rounded-md shadow-md p-4 relative">
        <h6 class="absolute top-0 left-0 bg-blue-500 text-white px-2 py-1 rounded-br-md">Work Experience {{ index + 1 }}</h6>
        <div class="w-full md:w-1/2 px-2 mb-4 mt-8">
          <label :for="'title-' + index" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
          <input type="text" v-model="workExperience.name" :id="'title-' + index" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/2 px-2 mb-4 mt-8">
          <label :for="'type-' + index" class="block text-gray-700 text-sm font-bold mb-2">Type:</label>
          <select v-model="workExperience.type" :id="'type-' + index" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Type</option>
            <option v-for="work_experience_type in workExperienceOptions" :key="work_experience_type" :value="work_experience_type">
              {{ work_experience_type }}
            </option>
          </select>
        </div>
        <div class="w-full md:w-1/2 mb-4 px-2">
          <label :for="'start-' + index" class="block text-gray-700 text-sm font-bold mb-2">Start Date</label>
          <VueDatePicker :id="'start-' + index" v-model="workExperience.start" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
        </div>
        <div class="w-full md:w-1/2 mb-4 px-2">
          <label :for="'end-' + index" class="block text-gray-700 text-sm font-bold mb-2">End Date</label>
          <VueDatePicker :id="'end-' + index" v-model="workExperience.end" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md"></VueDatePicker>
        </div>
        <input type="number" :id="'days-' + index" v-model="workExperience.days" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md" readonly hidden>
      </div>
      <button type="button" @click="addWorkExperience" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md mr-2">Add  Work Experience</button>
    </form>
  </div>
</div>


      <div class="w-full text-right mt-4 px-2">
        <!-- Previous Button -->
        <button v-if="currentStep > 0" @click="currentStep--" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Previous</button>
        
        <!-- Next Button -->
        <button v-if="currentStep < steps.length - 1" @click="currentStep++" class="bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md">Next</button>
        
        <!-- Register Button -->
        <button v-if="currentStep === steps.length - 1" @click="validateAndRegisterEmployee" type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Register</button>
        
        <!-- Cancel Button -->
        <router-link :to="`/Employee`">
          <button class="ml-2 bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import { ref, onMounted,watch } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';
  import VueDatePicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'


  export default {
    setup() {

      const currentStep =ref(0);
      const router = useRouter();
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
      const selectedCategory = ref(null);
      const categories = ref([]);
      const generatedNumber = ref([]);

      const titles = ref([]);
      const selectedTitle = ref('');
      const files = ref([])
      const metadata = ref([{ selectedCategory: null, selectedTitle: '', description: '', titles: [] }]);

      // const metadata = ref([{ selectedTitle: '', description: '', category_id: selectedCategory.value }]);
      const newEmployee = ref({
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
        street: 'Hulaj',
        city: '',
        zipcode: '',
        country: 'Kosova',
        phone_number: '044364211',
        phone_number_2: '044364211',
        email: 'hulajhygerta@gmail.com',
        email_2: 'hulajhygerta@gmail.com',
        days_off: 0,
        transferred_days_off: 0,
        earned_days_off: 0,
        next_year_earned_days_off: 2028,
        active: true,
        qualification_id: 1,
        user_id: 0,
        the_workouts_selection: 'primar',
        created_at: new Date().toISOString(),
      });
      const workExperienceList = ref([]);

      const addWorkExperience = () => {
        workExperienceList.value.push({
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
const newEmployeeContract = ref({
  name:'',
  personal_number:'',
  date_of_birth:'',
  city:'',

  street:'',
  job_position_id:'',
  date_hired:'',
  contract_end_date:'',
  created_at:'',
  salary:'',
  
  
});
      watch(
        [() => newEmployee.value.name, () => newEmployee.value.last_name],
        () => {
          if (newEmployee.value.name && newEmployee.value.last_name) {
            newEmployee.value.username = `${newEmployee.value.name.toLowerCase().replace(/\s+/g, '')}.${newEmployee.value.last_name.toLowerCase().replace(/\s+/g, '')}`;
          }
        }
      );

      const fetchNumber = async () => {
        try {
          const response = await api.get('/employees/generate_unique_number');
          generatedNumber.value = response.data;
          newEmployee.value.number = generatedNumber.value.number; 
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
      const selectedCategory = metadata.value[index].selectedCategory;
      if (selectedCategory) {
        try {
          const response = await api.get(`/api/titles?category_id=${selectedCategory}`);
          metadata.value[index].titles = response.data;
        } catch (error) {
          console.error("Error fetching titles:", error);
        }
      }
    };

    const handleFileChange = (index, event) => {
      const selectedFiles = event.target.files;
      if (selectedFiles && selectedFiles.length > 0) {
        files.value[index] = selectedFiles;
      }
    };

    const addDocument = () => {
      metadata.value.push({ selectedCategory: null, selectedTitle: '', description: '', titles: [] });
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

    const submitWorkExperience = async () => {
      try {
        const responseEmployeeId = await api.get('/employees/last_employee_id');
        const lastEmployeeId = responseEmployeeId.data;

        workExperienceList.value.forEach(workExperience => {
          workExperience.employee_id = lastEmployeeId;
        });

        const response = await api.post('/workExperience/create_WorkExperience', workExperienceList.value);
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


  // Define handleFileChange function
  // const handleFileChange = (index, event) => {
  //   const selectedFiles = event.target.files;
  //   if (selectedFiles && selectedFiles.length > 0) {
  //     files.value[index] = selectedFiles[0];
  //   }
  // };
      // const handleFileChange = (index, event) => {
      //   const selectedFiles = event.target.files;
      //   if (selectedFiles && selectedFiles.length > 0) {
      //     files.value[index] = selectedFiles;
      //   }
      // };

      // const addDocument = () => {
      //   metadata.value.push({ selectedTitle: '', description: '', category_id: null });
      // };

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
              newEmployee.value.selectedZipCode = zipCodesData[0];
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
        //   const response = await api.get('/employees/marital_status'); // Adjust endpoint based on your API structure
        // maritalStatusOptions.value = response.data.map(maritalStatus => ({ id: maritalStatus.id, name: maritalStatus.name }));
        // console.log(maritalStatusOptions)
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
    //   const fetchGenderOptions = async () => {
    //   try {
    //     // Example API call
    //     const response = await api.get('/employees/genders'); // Adjust endpoint based on your API structure
    //     genderOptions.value = response.data.map(gender => ({ id: gender.id, name: gender.name }));
    //     console.log(genderOptions)
    //   } catch (error) {
    //     console.error('Error fetching genders:', error);
    //   }
    // };

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
        const institutionId = newEmployee.value.selectedInstitution;
        if (institutionId) {
          fetchDepartments(institutionId);
          jobPositions.value = [];
          const departmentId = newEmployee.value.selectedDepartment;
          if (departmentId) {
            fetchJobPositions(institutionId, departmentId);
          }
        }
      };

      const onDepartmentChange = () => {
        const institutionId = newEmployee.value.selectedInstitution;
        const departmentId = newEmployee.value.selectedDepartment;
        // const jobPositionId=newEmployee.value.selectedJobPosition
        if (institutionId && departmentId ) {
          fetchJobPositions(institutionId, departmentId);
        } else {
          console.error('Either institutionId or departmentId is null.');
        }
      };
      const generate_contract = async() => {
        try {
          newEmployeeContract.value.name = newEmployee.value.name;
        newEmployeeContract.value.personal_number = newEmployee.value.personal_number;
        newEmployeeContract.value.date_of_birth = newEmployee.value.date_of_birth;
        newEmployeeContract.value.city=newEmployee.value.selectedCity
        newEmployeeContract.value.street = newEmployee.value.street;
        newEmployeeContract.value.job_position_id = newEmployee.value.selectedJobPosition.name;
        console.log(newEmployeeContract.value.job_position_id)
        newEmployeeContract.value.date_hired = newEmployee.value.date_hired;
        newEmployeeContract.value.contract_end_date = newEmployee.value.contract_end_date;
        newEmployeeContract.value.created_at = newEmployee.value.created_at.split('T')[0];
        newEmployeeContract.value.salary = newEmployee.value.salary;

        const responseEmployeeId = await api.get('/employees/last_employee_id');
        const employee_id = responseEmployeeId.data;
        const response = await api.post(`/employees/generate_and_attach_document/${employee_id}`,newEmployeeContract.value);
          // print("test test",newEmployeeContract)
        } catch (error) {
          handleApiError(error, 'job positions');
        }
      };
      const validateAndRegisterEmployee = async (documentUpload) => {
        newEmployee.value.institucion_id = newEmployee.value.selectedInstitution;
        newEmployee.value.department_id = newEmployee.value.selectedDepartment;
        newEmployee.value.job_position_id = newEmployee.value.selectedJobPosition.id;
        newEmployee.value.city=newEmployee.value.selectedCity
        newEmployee.value.date_hired = new Date(newEmployee.value.date_hired).toISOString().split('T')[0];
        newEmployee.value.date_of_birth = new Date(newEmployee.value.date_of_birth).toISOString().split('T')[0];
        newEmployee.value.contract_end_date = new Date(newEmployee.value.contract_end_date).toISOString().split('T')[0];
  
        newEmployee.value.zipcode=newEmployee.value.selectedZipCode

        newEmployee.value.user_id = 1;

        try {
          const response = await api.post('/employees/create_employee', newEmployee.value);
          console.log('Employee created successfully:', response.data);
          await submitForm();     
          await submitWorkExperience();
          await generate_contract();

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
        fetchCategories();
        fetchNumber();
        // fetchUsername();
        fetchInstitutions();
        fetchEthnicities();
        fetchMaritalStatusOptions();
        fetchGenderOptions();
        fetchCitiesAndZipCodes();
        fetchWorkExperienceType();
      });

      return {
        currentStep,
      steps: ['Personal Information', 'Contact Details', 'Employment Details', 'Upload Documents', 'Work Experience'],
   
        workExperienceList,
      addWorkExperience,
        institutions,
        departments,
        jobPositions,
        newEmployee,
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
        addWorkExperience,
        files,
        selectedCategory,
        categories,
        titles,
        selectedTitle,
        newEmployee,
        // workExperienceData,
        fetchTitles,
        fetchCategories,
        fetchNumber,
        generatedNumber,
        selectedTitle,
        // workExperienceData,
        submitWorkExperience,
        generate_contract,
      };
    },
  };
</script>

<style scoped>
  .container {
    max-width: 1200px;
  }


</style> 
