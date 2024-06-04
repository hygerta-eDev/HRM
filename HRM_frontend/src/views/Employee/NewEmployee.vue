<template>
  <div class="container mx-auto p-6">
    <div  class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100 ">
      <h1 class="text-2xl font-bold mb-6">Register New Employee</h1>
      <div class="employee-details flex flex-wrap">
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Name</label>
          <input v-model="newEmployee.name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Number</label>
          <input v-model="newEmployee.number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Username</label>
          <input v-model="newEmployee.username" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Middle Name</label>
          <input v-model="newEmployee.middle_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Last Name</label>
          <input v-model="newEmployee.last_name" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
        <label class="block text-gray-700 text-sm font-bold mb-2">Gender</label>
        <select v-model="newEmployee.gender" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
          <option value="">Select Gender</option>
          <option v-for="genders in genderOptions" :key="genders.id" :value="genders.id">
            {{ genders }}
          </option>
        </select>
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
          <label class="block text-gray-700 text-sm font-bold mb-2">Marital Status</label>
          <select v-model="newEmployee.marital_status" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select maritalStatus</option>
            <option v-for="maritalStatus in maritalStatusOptions" :key="maritalStatus.id" :value="maritalStatus.id">
              {{ maritalStatus }}
            </option>
          </select>
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Date of Birth</label>
          <input v-model="newEmployee.date_of_birth" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Date Hired</label>
          <input v-model="newEmployee.date_hired" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Contract End Date</label>
          <input v-model="newEmployee.contract_end_date" type="date" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
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
          <label class="block text-gray-700 text-sm font-bold mb-2">Personal Number</label>
          <input v-model="newEmployee.personal_number" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Salary</label>
          <input v-model="newEmployee.salary" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Addition</label>
          <input v-model="newEmployee.addition" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Job Position</label>
          <select v-model="newEmployee.selectedJobPosition" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select Job Position</option>
            <option v-for="position in jobPositions" :key="position.id" :value="position.id">
              {{ position.name }}
            </option>
          </select>
        </div>
        <div class="w-full mb-4 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Street</label>
          <input v-model="newEmployee.street" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full mb-4 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">City</label>
          <select v-model="newEmployee.selectedCity" @change="onCityChange" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
            <option value="">Select City</option>
            <option v-for="city in cities" :key="city.city_name" :value="city.city_name">
              {{ city.city_name }}
            </option>
          </select>
        </div>
        <div class="w-full mb-4 px-2">
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
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Days Off</label>
          <input v-model="newEmployee.days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Transferred Days Off</label>
          <input v-model="newEmployee.transferred_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Earned Days Off</label>
          <input v-model="newEmployee.earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">Next Year Earned Days Off</label>
          <input v-model="newEmployee.next_year_earned_days_off" type="number" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">CV</label>
          <input v-model="newEmployee.cv" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
        <div class="w-full md:w-1/3 mb-4 md:mb-0 px-2">
          <label class="block text-gray-700 text-sm font-bold mb-2">The Workouts Selection</label>
          <input v-model="newEmployee.the_workouts_selection" type="text" class="w-full px-3 py-2 border border-blue-500 rounded-md shadow-md">
        </div>
      </div>
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
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { api } from '@/api';
  import { toast } from 'vue3-toastify';

  export default {
    setup() {
      const router = useRouter();
      const documentUpload = ref(null); 
      const institutions = ref([]);
      const departments = ref([]);
      const jobPositions = ref([]);
      const ethnicities = ref([]);
      const maritalStatusOptions = ref([]);
      const genderOptions = ref([]);
      const cityOptions = ref([]);
      const zipCodeOptions = ref([]);
      const cities = ref([]);
      const zipCodes = ref([]);
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
        gender: 'N/A',
        ethnicity_id: 0,
        marital_status: 'Single',
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
        cv: 'test',
        the_workouts_selection: 'primar',
        created_at: new Date().toISOString(),
      });
      const files = ref([])
      const metadata = ref([{ title: '', description: '', category_id: null }]);

      const submitForm = async () => {
        try {
          const response = await api.get('/employees/last_employee_id');
          const lastEmployeeId = response.data;

          for (let i = 0; i < metadata.value.length; i++) {
            const doc = metadata.value[i];
            const formData = new FormData();

            const metadataObject = {
              title: doc.title,
              description: doc.description,
              category_id: doc.category_id,
              created_at: new Date().toISOString(),
              updated_at: new Date().toISOString(),
              created_by: lastEmployeeId 
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
            // Store all selected files for the current document
            files.value[index] = selectedFiles;
          }
        };

        const addDocument = () => {
          metadata.value.push({ title: '', description: '', category_id: null });
        };

        const fetchCitiesAndZipCodes = async () => {
            try {
              const response = await api.get('/employees/cities');
              console.log("response", response);
              cities.value = response.data;
              console.log(cities.value);
            } catch (error) {
              console.error('Error fetching cities:', error);
            }
        };
        const selectedZipCode = ref('');

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
            console.log(response.data);
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

        const validateAndRegisterEmployee = async (documentUpload) => {
          newEmployee.value.institucion_id = newEmployee.value.selectedInstitution;
          newEmployee.value.department_id = newEmployee.value.selectedDepartment;
          newEmployee.value.job_position_id = newEmployee.value.selectedJobPosition;
          newEmployee.value.city=newEmployee.value.selectedCity

          newEmployee.value.zipcode=newEmployee.value.selectedZipCode

          newEmployee.value.user_id = 1;

          try {
            const response = await api.post('/employees/create_employee', newEmployee.value);
            console.log('Employee created successfully:', response.data);

            await submitForm();     

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
          fetchInstitutions();
          fetchEthnicities();
          fetchMaritalStatusOptions();
          fetchGenderOptions();
          fetchCitiesAndZipCodes();
            });

        return {
          institutions,
          departments,
          jobPositions,
          newEmployee,
          validateAndRegisterEmployee,
          onInstitutionChange,
          onDepartmentChange,
          ethnicities,
          maritalStatusOptions,
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

      };
    },
};
</script>

<style scoped>
.container {
  max-width: 1200px;
}
</style> 







<!-- 



<template>
  <div class="container mx-auto p-6">
    <div class="create-employee p-8 rounded-lg shadow-lg border border-blue-500 bg-gray-100">
      <h1 class="text-2xl font-bold mb-6">Register New Employee</h1>
      <div class="employee-details flex flex-wrap">
        <div v-for="(field, index) in formFields" :key="index" class="w-full md:w-1/3 mb-4 px-2">
          <label :class="labelClass">{{ field.label }}</label>
          <input v-if="field.type === 'input'" v-model="newEmployee[field.model]" :type="field.inputType" :class="inputClass" />
          <select v-else-if="field.type === 'select'" v-model="newEmployee[field.model]" :class="inputClass" @change="field.onChange">
            <option value="">{{ field.placeholder }}</option>
            <option v-for="option in field.options" :key="option.value" :value="option.value">
              {{ option.text }}
            </option>
          </select>
        </div>
      </div>
      <DocumentUploadComponent />
      <div class="w-full text-right mt-4 px-2">
        <button @click="validateAndRegisterEmployee" type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 shadow-md">Register</button>
        <router-link :to="`/Employee`">
          <button class="bg-gray-400 text-white px-4 py-2 rounded-lg shadow-md">Cancel</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '@/api';
import { toast } from 'vue3-toastify';
import DocumentUploadComponent from '../test/test.vue';

export default {
  components: { DocumentUploadComponent },

  setup() {
    const router = useRouter();
    const documentUpload = ref(null);

    const institutions = ref([]);
    const departments = ref([]);
    const jobPositions = ref([]);
    const ethnicities = ref([]);
    const maritalStatusOptions = ref([]);
    const genderOptions = ref([]);
    const cities = ref([]);
    const zipCodes = ref([]);
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
      gender: 'N/A',
      ethnicity_id: 0,
      marital_status: 'Single',
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
      cv: 'test',
      the_workouts_selection: 'primar',
      created_at: new Date().toISOString(),
    });
    const files = ref([[]]);
    const metadata = ref([{ title: '', description: '', category_id: null }]);

    const submitForm = async () => {
      try {
        const response = await api.get('/employees/last_employee_id');
        const lastEmployeeId = response.data;

        for (let i = 0; i < metadata.value.length; i++) {
          const doc = metadata.value[i];
          const formData = new FormData();

          const metadataObject = {
            title: doc.title,
            description: doc.description,
            category_id: doc.category_id,
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString(),
            created_by: lastEmployeeId,
          };

          formData.append('metadata_json', JSON.stringify([metadataObject]));

          for (let j = 0; j < files.value[i].length; j++) {
            formData.append(`files[${j}]`, files.value[i][j]);
          }

          await new Promise((resolve) => setTimeout(resolve, i * 100));

          const uploadResponse = await api.post(`/attach_documents/${lastEmployeeId}`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
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
        files.value[index] = Array.from(selectedFiles);
      }
    };

    const addDocument = () => {
      metadata.value.push({ title: '', description: '', category_id: null });
      files.value.push([]);
    };

    const fetchCitiesAndZipCodes = async () => {
      try {
        const response = await api.get('/employees/cities');
        cities.value = response.data;
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
    console.log(response.data);
    const zipCodesData = response.data.zip_codes;
    if (Array.isArray(zipCodesData)) {
      // Assign all zip codes to the zipCodes array
      zipCodes.value = zipCodesData;
      // If there's only one zip code, automatically select it
      if (zipCodesData.length === 1) {
        newEmployee.value.selectedZipCode = zipCodesData[0];
      }
    }
  } catch (error) {
    console.error('Error fetching zip codes:', error);
    // Handle errors here
  }
};


    const onCityChange = () => {
      const cityName = newEmployee.value.selectedCity;
      fetchZipCodes(cityName);
    };

    const fetchEthnicities = async () => {
      try {
        const response = await api.get('/ethnicities/active_ethnicities');
        ethnicities.value = response.data.map(ethnicity => ({ value: ethnicity.id, text: ethnicity.name }));
      } catch (error) {
        handleApiError(error, 'ethnicities');
      }
    };

    const fetchInstitutions = async () => {
      try {
        const response = await api.get('/institutions/active_institutions');
        institutions.value = response.data.map(institution => ({ value: institution.id, text: institution.name }));
      } catch (error) {
        handleApiError(error, 'institutions');
      }
    };

    const fetchMaritalStatusOptions = async () => {
      try {
        const response = await api.get('/employees/marital_status');
        maritalStatusOptions.value = response.data.map(status => ({ value: status.id, text: status.status }));
      } catch (error) {
        handleApiError(error, 'marital status options');
      }
    };

    const fetchGenderOptions = async () => {
      try {
        const response = await api.get('/employees/genders');
        genderOptions.value = response.data.map(gender => ({ value: gender.id, text: gender.gender }));
      } catch (error) {
        handleApiError(error, 'gender options');
      }
    };

    const fetchDepartments = async (institutionId) => {
      try {
        const response = await api.get(`/departments/institutions/${institutionId}/departments`);
        departments.value = response.data.map(department => ({ value: department.id, text: department.name }));
      } catch (error) {
        handleApiError(error, 'departments');
      }
    };

    const fetchJobPositions = async (institutionId, departmentId) => {
      try {
        const response = await api.get(`/institutions/job_positions/${institutionId}/${departmentId}?institutions_id=${institutionId}`);
        jobPositions.value = response.data.map(jobPosition => ({ value: jobPosition.id, text: jobPosition.name }));
      } catch (error) {
        handleApiError(error, 'job positions');
      }
    };

    const onInstitutionChange = () => {
      const institutionId = newEmployee.value.selectedInstitution;
      if (institutionId) {
        fetchDepartments(institutionId);
        jobPositions.value = [];
        newEmployee.value.selectedDepartment = null;
        newEmployee.value.selectedJobPosition = null;
      }
    };

    const onDepartmentChange = () => {
      const institutionId = newEmployee.value.selectedInstitution;
      const departmentId = newEmployee.value.selectedDepartment;
      if (institutionId && departmentId) {
        fetchJobPositions(institutionId, departmentId);
      }
    };
    const validateAndRegisterEmployee = async () => {
      newEmployee.value.institucion_id = newEmployee.value.selectedInstitution;
      newEmployee.value.department_id = newEmployee.value.selectedDepartment;
      newEmployee.value.city = newEmployee.value.selectedCity;
      newEmployee.value.zipcode = newEmployee.value.selectedZipCode;
      newEmployee.value.position_id = newEmployee.value.selectedJobPosition;

      try {
        const response = await api.post('/employees/register_employee', newEmployee.value);
        console.log('Employee created successfully:', response.data);
        await submitForm();
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
      fetchInstitutions();
      fetchEthnicities();
      fetchMaritalStatusOptions();
      fetchGenderOptions();
      fetchCitiesAndZipCodes();
    });

    const formFields = computed(() => [
      { label: 'Name', model: 'name', type: 'input', inputType: 'text' },
      { label: 'Number', model: 'number', type: 'input', inputType: 'text' },
      { label: 'Username', model: 'username', type: 'input', inputType: 'text' },
      { label: 'Middle Name', model: 'middle_name', type: 'input', inputType: 'text' },
      { label: 'Last Name', model: 'last_name', type: 'input', inputType: 'text' },
      { label: 'Gender', model: 'gender', type: 'select', options: genderOptions.value, placeholder: 'Select Gender' },
      { label: 'Ethnicity', model: 'ethnicity_id', type: 'select', options: ethnicities.value, placeholder: 'Select Ethnicity' },
      { label: 'Marital Status', model: 'marital_status', type: 'select', options: maritalStatusOptions.value, placeholder: 'Select Marital Status' },
      { label: 'Date of Birth', model: 'date_of_birth', type: 'input', inputType: 'date' },
      { label: 'Date Hired', model: 'date_hired', type: 'input', inputType: 'date' },
      { label: 'Contract End Date', model: 'contract_end_date', type: 'input', inputType: 'date' },
      {
        label: 'Institution',
        type: 'select',
        model: 'selectedInstitution',
        placeholder: 'Select an Institution',
        options: institutions.value,
        onChange: onInstitutionChange,
      },
      {
        label: 'Department',
        type: 'select',
        model: 'selectedDepartment',
        placeholder: 'Select a Department',
        options: departments.value,
        onChange: onDepartmentChange,
      },
      { label: 'Personal Number', model: 'personal_number', type: 'input', inputType: 'text' },
      { label: 'Salary', model: 'salary', type: 'input', inputType: 'text' },
      { label: 'Addition', model: 'addition', type: 'input', inputType: 'number' },
      {
        label: 'Job Position',
        type: 'select',
        model: 'selectedJobPosition',
        placeholder: 'Select a Job Position',
        options: jobPositions.value,
      },
      { label: 'Street', model: 'street', type: 'input', inputType: 'text' },
      {
        label: 'City',
        type: 'select',
        model: 'selectedCity',
        placeholder: 'Select a City',
        options: cities.value.map((city) => ({
          value: city.name,
          text: city.city_name,
        })),
        onChange: onCityChange,
      },
      {
        label: 'Zip Code',
        type: 'select',
        model: 'selectedZipCode',
        placeholder: 'Select a Zip Code',
        options: zipCodes.value.map((zipCode) => ({
          value: zipCode.city_name,
          text: zipCode,
        })),
      },
      { label: 'Country', model: 'country', type: 'input', inputType: 'text' },
      { label: 'Phone Number', model: 'phone_number', type: 'input', inputType: 'text' },
      { label: 'Phone Number 2', model: 'phone_number_2', type: 'input', inputType: 'text' },
      { label: 'Email', model: 'email', type: 'input', inputType: 'email' },
      { label: 'Email 2', model: 'email_2', type: 'input', inputType: 'email' },
      { label: 'Days Off', model: 'days_off', type: 'input', inputType: 'number' },
      { label: 'Transferred Days Off', model: 'transferred_days_off', type: 'input', inputType: 'number' },
      { label: 'Earned Days Off', model: 'earned_days_off', type: 'input', inputType: 'number' },
      { label: 'Next Year Earned Days Off', model: 'next_year_earned_days_off', type: 'input', inputType: 'number' },
      { label: 'CV', model: 'cv', type: 'input', inputType: 'text' },
      { label: 'The Workouts Selection', model: 'the_workouts_selection', type: 'input', inputType: 'text' },
    ]);

    const labelClass = "block text-gray-700 text-sm font-bold mb-2";
    const inputClass = "w-full px-3 py-2 border border-blue-500 rounded-md shadow-md";

    return {
      formFields,
      newEmployee,
      institutions,
      departments,
      jobPositions,
      ethnicities,
      maritalStatusOptions,
      genderOptions,
      cities,
      zipCodes,
      labelClass,
      inputClass,
      validateAndRegisterEmployee,
    };
  },
};
</script>

<style scoped>
/* Add any additional styles here */
</style> -->
