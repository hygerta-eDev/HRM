<script setup>
    import Sidebar from '../../components/Sidebar.vue';
    import Navbar from '../../components/Navbar.vue';
    import { ref, onMounted, watch } from 'vue';
    import { api } from '@/api';
    import { useRouter } from 'vue-router';
    // import DatePicker from 'vue3-datepicker';
    import VueDatePicker from '@vuepic/vue-datepicker';
    import '@vuepic/vue-datepicker/dist/main.css'
    const router = useRouter();

    const employee = ref({
        active: false,
        city: '',
        contract_end_date: '',
        country: '',
        date_hired: '',
        date_of_birth: '',
        department_id: '',
        earned_days_off: '',
        email: '',
        email_2: '',
        ethnicity_id: '',
        gender: '',
        last_name: '',
        middle_name: '',
        name: '',
        next_year_earned_days_off: '',
        number: '',
        personal_number: '',
        phone_number: '',
        phone_number_2: '',
        salary: '',
        street: '',
        transferred_days_off: '',
        zipcode: '',
        user_id: '',
        username: '',

        qualification_id: '',
        job_position_id: '',
        marital_status: '',
    });

    const departments = ref([]);
    const qualifications = ref([]);
    const jobPositions = ref([]);
    const maritalStatusOptions = ref([]);
    const ethnicityOptions = ref([]);
    const genderOptions = ref([]);

    const handleCVChange = (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            employee.value.cv = e.target.result;
        };
        reader.readAsDataURL(file);
    }
};
    const backToIndex = () => {
        router.push({ name: 'Employees' });
    };
    const getCurrentDateTime = () => {
        const now = new Date();
        return now.toISOString();
    };
    const formatDate = (date) => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
};


    const createEmployee = async () => {
        // const currentDate = getCurrentDate();
        const formattedDateOfBirth = formatDate(new Date(employee.value.date_of_birth));
        const formattedDateHired = formatDate(new Date(employee.value.date_hired));
        const formattedContractEndDate = formatDate(new Date(employee.value.contract_end_date));
        
        employee.value.date_of_birth = formattedDateOfBirth;
        employee.value.date_hired = formattedDateHired;
        employee.value.contract_end_date = formattedContractEndDate;
                employee.value.created_at = getCurrentDateTime(); 
        // const formattedDate = formatDate(selectedDate);
        console.log(formattedDateOfBirth)

        try {
            
            await api.post('/employees/create_employee', employee.value);
            router.push('/employees');
            console.log('Employee created successfully');
        } catch (error) {
            console.error('There was a problem creating the employee:', error);
        }
    };

    const fetchJobPositions = async () => {
        try {
            if (employee.value.department_id) {
                const response = await api.get(`/departments/${employee.value.department_id}/job_positions`);
                const jobPositionsData = response.data.job_positions;
                jobPositions.value = jobPositionsData.reduce((positions, position) => {
                    positions[position.id] = position.name;
                    return positions;
                }, {});
                console.log('Fetched job positions:', jobPositions.value);
            }
        } catch (error) {
            console.error('Error fetching job positions:', error);
        }
    };


    onMounted(async () => {
        try {
            const response = await api.get('/departments');
            departments.value = response.data;
        } catch (error) {
            console.error('Error fetching departments:', error);
        }
    });

    onMounted(async () => {
        try {
            const response = await api.get('/qualification');
            qualifications.value = response.data;
        } catch (error) {
            console.error('Error fetching qualifications:', error);
        }
    });

    onMounted(async () => {
        try {
            const response = await api.get('/employees/marital_status');
            maritalStatusOptions.value = response.data;
        } catch (error) {
            console.error('Error fetching marital status options:', error);
        }
    });

    onMounted(async () => {
        try {
            const response = await api.get('/employees/genders');
            genderOptions.value = response.data;
        } catch (error) {
            console.error('Error fetching marital status options:', error);
        }
    });

    onMounted(async () => {
        try {
            const response = await api.get('/ethnicities');
            ethnicityOptions.value = response.data;
            // ethnicityOptions.value = response.data.map(item => item.name);  
        } catch (error) {
            console.error('Error fetching ethnicity options:', error);
        }
    });

    watch(() => employee.value.department_id, () => {
        fetchJobPositions();
    });

</script>



<template>
    <Navbar/>
    <Sidebar />
    <main class="flex-1 p-8 sm:ml-64">
      <div class="mt-10 p-12 text-black">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-bold">Create Employee</h2>
          <button @click="backToIndex" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Back</button>
        </div>
        <form @submit.prevent="createEmployee" class="space-y-4">
          <div class="grid grid-cols-3 gap-4">
            <div>
              <label for="name" class="block mb-2 text-sm font-medium text-black dark:text-black">Name:</label>
              <input type="text" id="name" v-model="employee.name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div>
              <label for="number" class="block mb-2 text-sm font-medium text-black dark:text-black">Number:</label>
              <textarea id="number" v-model="employee.number" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></textarea>
            </div>
            <div>
              <label for="username" class="block mb-2 text-sm font-medium text-black dark:text-black">Username:</label>
              <input type="text" id="username" v-model="employee.username" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="middle_name" class="block mb-2  text-sm font-medium text-black dark:text-black">middle_name:</label>
                <input type="text" id="middle_name" v-model="employee.middle_name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="last_name" class="block mb-2  text-sm font-medium text-black dark:text-black">last_name:</label>
                <input type="text" id="last_name" v-model="employee.last_name" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="gender" class="block mb-2  text-sm font-medium text-black dark:text-black">gender:</label>
                <select v-model="employee.gender" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select an option</option>
                    <option v-for="status in genderOptions" :key="status" :value="status">{{ status }}</option>
                </select>
                <!-- <input type="text" id="gender" v-model="employee.gender" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"> -->
            </div>
            <div class="flex-1">
                <label for="ethnicity_id" class="block mb-2  text-sm font-medium text-black dark:text-black">ethnicity_id:</label>
                <select v-model="employee.ethnicity_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select an option</option>
                    <option v-for="ethnicity in ethnicityOptions" :key="ethnicity.id" :value="ethnicity.id">{{ ethnicity.name }}</option>

                    <!-- <option v-for="status in ethnicityOptions " :key="status" :value="status">{{ status }}</option> -->
                </select>            
            </div>
            <div class="flex-1">
                <label for="marital_status" class="block mb-2  text-sm font-medium text-black dark:text-black">marital_status:</label>
                <select v-model="employee.marital_status" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select an option</option>
                    <option v-for="status in maritalStatusOptions" :key="status" :value="status">{{ status }}</option>
                </select>
                <!-- <input type="text" id="marital_status" v-model="employee.marital_status" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"> -->
            </div>
            <div class="flex-1">
                <label for="date_of_birth" class="block mb-2  text-sm font-medium text-black dark:text-black">Date of Birth:</label>
                <VueDatePicker  v-model="employee.date_of_birth" type="date" placeholder="Select Date" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />     
            </div>
            <div class="flex-1">
                <label for="date_hired" class="block mb-2  text-sm font-medium text-black dark:text-black">date_hiredh:</label>
                <VueDatePicker  v-model="employee.date_hired" type="date" placeholder="Select Date" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
            </div>
            <div class="flex-1">
                 <label for="contract_end_date" class="block mb-2  text-sm font-medium text-black dark:text-black">contract_end_dateh:</label>
                <VueDatePicker  v-model="employee.contract_end_date" type="date" placeholder="Select Date" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
            </div>
            <div class="flex-1">
                <label for="department_id" class="block mb-2  text-sm font-medium text-black dark:text-black">Department:</label>
                <select id="department_id" v-model="employee.department_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select Department</option>
                    <option v-for="department in departments" :key="department.id" :value="department.id">{{ department.name }}</option>
                </select>
            </div>
            <div class="flex-1">
                <label for="personal_number" class="block mb-2  text-sm font-medium text-black dark:text-black">personal_number:</label>
                <input type="text" id="personal_number" v-model="employee.personal_number" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="salary" class="block mb-2  text-sm font-medium text-black dark:text-black">salary:</label>
                <input type="text" id="salary" v-model="employee.salary" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="addition" class="block mb-2  text-sm font-medium text-black dark:text-black">addition:</label>
                <input type="text" id="addition" v-model="employee.addition" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="job_position_id" class="block mb-2 text-sm font-medium text-black dark:text-black">Job Position:</label>
                <select id="job_position_id" v-model="employee.job_position_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select Job Position</option>
                    <option v-for="(position, index) in jobPositions" :key="index" :value="index">{{ position }}</option>
                </select>
            </div>
            <div class="flex-1">
                <label for="street" class="block mb-2  text-sm font-medium text-black dark:text-black">street:</label>
                <input type="text" id="street" v-model="employee.street" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="city" class="block mb-2  text-sm font-medium text-black dark:text-black">city:</label>
                <input type="text" id="city" v-model="employee.city" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="zipcode" class="block mb-2  text-sm font-medium text-black dark:text-black">zipcode:</label>
                <input type="text" id="zipcode" v-model="employee.zipcode" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="country" class="block mb-2  text-sm font-medium text-black dark:text-black">country:</label>
                <input type="text" id="country" v-model="employee.country" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="phone_number" class="block mb-2  text-sm font-medium text-black dark:text-black">phone_number:</label>
                <input type="text" id="phone_number" v-model="employee.phone_number" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="phone_number_2" class="block mb-2  text-sm font-medium text-black dark:text-black">phone_number_2:</label>
                <input type="text" id="phone_number_2" v-model="employee.phone_number_2" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="email" class="block mb-2  text-sm font-medium text-black dark:text-black">email:</label>
                <input type="text" id="email" v-model="employee.email" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="email_2" class="block mb-2  text-sm font-medium text-black dark:text-black">email_2:</label>
                <input type="text" id="email_2" v-model="employee.email_2" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="transferred_days_off" class="block mb-2  text-sm font-medium text-black dark:text-black">transferred_days_off:</label>
                <input type="text" id="transferred_days_off" v-model="employee.transferred_days_off" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="earned_days_off" class="block mb-2  text-sm font-medium text-black dark:text-black">earned_days_off:</label>
                <input type="text" id="earned_days_off" v-model="employee.earned_days_off" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label for="next_year_earned_days_off" class="block mb-2  text-sm font-medium text-black dark:text-black">next_year_earned_days_off:</label>
                <input type="text" id="next_year_earned_days_off" v-model="employee.next_year_earned_days_off" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div class="flex-1">
                <label class="block mb-2 text-sm font-medium text-black dark:text-black">Active:</label>
                <input type="checkbox" id="active" v-model="employee.active" class="form-checkbox h-6 w-6 text-blue-600">
                <!-- <label for="active" class="ml-2 text-sm font-medium text-black dark:text-black">Active</label> -->
            </div>

            <div class="flex-1">
                <label for="qualification_id" class="block mb-2  text-sm font-medium text-black dark:text-black">qualification_id:</label>
                <select id="qualification_id" v-model="employee.qualification_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                    <option value="" disabled>Select qualification</option>
                    <option v-for="qualification in qualifications" :key="qualification.id" :value="qualification.id">{{ qualification.name }}</option>
                </select>
                <!-- <input type="text" id="qualification_id" v-model="employee.qualification_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"> -->
            </div>
            <div class="flex-1">
                <label for="user_id" class="block mb-2  text-sm font-medium text-black dark:text-black">user_id:</label>
                <input type="text" id="user_id" v-model="employee.user_id" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            </div>
            <div>
        <label for="cv" class="block mb-2 text-sm font-medium text-black dark:text-black">CV:</label>
        <input type="file" id="cv" @change="handleCVChange" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    </div>

    <!-- The workouts selection input -->
    <div>
        <label for="the_workouts_selection" class="block mb-2 text-sm font-medium text-black dark:text-black">Workouts Selection:</label>
        <input type="text" id="the_workouts_selection" v-model="employee.the_workouts_selection" class="bg-gray-50 h-16 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
    </div>
                </div>
                <button type="submit" class="mt-7 h-12 inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Create</button>

            </form>
        </div>
    </main>
</template>