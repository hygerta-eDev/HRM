<template>
  <div class="p-6 max-w-8xl mx-auto bg-white shadow-lg rounded-lg">
    <h2 class="text-3xl font-bold mb-6 text-gray-800">Create Assessment</h2>
    <div class="flex gap-8">
      <!-- Assessment Form -->
      <div class="ml-10 min-w-[600px] bg-gray-50 p-8 rounded-lg shadow-lg border border-gray-200">
        <h3 class="text-2xl font-semibold mb-6 text-gray-800">Assessment Details</h3>
        <form @submit.prevent="createAssessment" class="space-y-6">
          <!-- Employee Details -->
          <div class="flex flex-col">
            <label for="employee_name" class="text-lg font-semibold mb-2 text-gray-700">Employee:</label>
            <input type="text" :value="employeeName" readonly class="border border-gray-300 rounded-lg p-3 bg-gray-100 text-gray-700"/>
          </div>

          <input type="number" :value="userId" readonly class="hidden"/>
          
          <!-- Job Position ID -->
          <div class="flex flex-col">
            <label for="job_position_id" class="text-lg font-semibold mb-2 text-gray-700">Job Position ID:</label>
            <input type="number" v-model="assessment.job_position_id" required class="border border-gray-300 rounded-lg p-3"/>
          </div>

          <!-- Evaluation Period -->
          <div class="flex flex-col">
            <label for="evaluation_period" class="text-lg font-semibold mb-2 text-gray-700">Evaluation Period:</label>
            <input type="text" v-model="assessment.evaluation_period" required class="border border-gray-300 rounded-lg p-3"/>
          </div>

          <!-- Rate -->
          <div class="flex flex-col">
            <label for="rate" class="text-lg font-semibold mb-2 text-gray-700">Rate:</label>
            <input type="number" v-model="assessment.rate" required class="border border-gray-300 rounded-lg p-3"/>
          </div>

          <!-- Finished Checkbox -->
          <div class="flex items-center space-x-2">
            <input type="checkbox" v-model="assessment.finished" class="h-5 w-5"/>
            <label for="finished" class="text-lg font-semibold text-gray-700">Finished</label>
          </div>

          <!-- Status -->
          <div class="flex flex-col">
            <label for="status" class="text-lg font-semibold mb-2 text-gray-700">Status:</label>
            <input type="text" v-model="assessment.status" required class="border border-gray-300 rounded-lg p-3"/>
          </div>

          <!-- Performance Objectives -->
          <div class="flex flex-col">
            <label for="performance_objectives" class="text-lg font-semibold mb-2 text-gray-700">Performance Objectives:</label>
            <textarea v-model="assessment.performance_objectives" required class="border border-gray-300 rounded-lg p-3 resize-none"></textarea>
          </div>

          <!-- General Evaluation -->
          <div class="flex flex-col">
            <label for="general_evaluation" class="text-lg font-semibold mb-2 text-gray-700">General Evaluation:</label>
            <textarea v-model="assessment.general_evaluation" required class="border border-gray-300 rounded-lg p-3 resize-none"></textarea>
          </div>

          <!-- Submit Button -->
          <button type="submit" class="bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors duration-300">
            Create Assessment
          </button>
        </form>
      </div>
            <!-- Assessment Questions -->
            <div class="min-w-[600px] bg-gray-50 p-8 rounded-lg shadow-lg border border-gray-200">
        <h3 class="text-2xl font-semibold mb-6 text-gray-800">Assessment Questions</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <!-- First Question -->
          <div v-if="questions.length > 0" class="bg-white p-6 rounded-lg shadow-md border border-gray-300">
            <h4 class="text-xl font-semibold text-gray-800">{{ questions[0].title }}</h4>
            <p class="text-gray-600 text-justify p-4">{{ questions[0].description }}</p>
            <div class="flex flex-col mt-4">
              <select v-model="questions[0].selected_option" :id="'selected_option_0'" class="border border-gray-300 rounded-lg p-3">
                <option value="" disabled>Select an option</option>
                <option v-for="option in parsedOptions" :key="option" :value="option">
                  {{ option }}
                </option>
              </select>
            </div>
          </div>

          <div v-for="(question, index) in questions.slice(2)" :key="index + 2" class="flex items-center justify-center bg-white p-6 rounded-lg shadow-md border border-gray-300">
            <div class="w-full max-w-[400px]">
              <h4 class="text-xl font-semibold text-gray-800">{{ question.title }}</h4>
              <p class="text-gray-600 text-justify p-4">{{ question.description }}</p>
              <div class="flex flex-col mt-4">
                <select v-model="question.selected_option" :id="'selected_option_' + (index + 1)" class="border border-gray-300 rounded-lg p-3">
                  <option value="" disabled>Select an option</option>
                  <option v-for="option in parsedOptions" :key="option" :value="option">
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '@/api';

export default {
  setup() {
    const route = useRoute();
    const employeeId = ref(route.params.id); // Get employee ID from route parameters
    const userId = ref(parseInt(localStorage.getItem('user_id'), 10) || null);
    const assessment = ref({
      employee_id: employeeId.value,
      user_id: userId.value,
      job_position_id: '',
      evaluation_period: '',
      rate: '',
      finished: false,
      status: '',
      performance_objectives: '',
      general_evaluation: '',
      created_at: ''
    });
    const questions = ref([
      { id: null, title: "Cilësia e punës", description: "Puna është përfunduar me saktësi (me pak ose aspak gabime), në mënyrë efikase dhe brenda afateve me mbikëqyrje minimale.", selected_option: '' },
      { id: null, title: "Besueshmëria", description: "Në vazhdimësi përformon në nivel të lartë, menaxhon kohën dhe ngarkesën e punës në mënyrë efektive duke i përmbushur përgjegjësitë.", selected_option: '' },
      { id: null, title: "Gjykimi dhe vendimarrja", description: "Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.", selected_option: '' },
      { id: null, title: "Aftësitë komunikuese", description: "Komunikimet me shkrim dhe me gojë janë te qarta, të organizuara dhe efektive. I dëgjon mire dhe kupton mire natyrën e problemeve.", selected_option: '' },
      { id: null, title: "Iniciativa dhe fleksibiliteti", description: "Demostron iniciativë, shpesh duke kërkuar përgjegjësi shtesë, identifikon probemet dhe zgjidhjet. Përshtatet me sfidat e reja dhe ndryshimet e papritura.", selected_option: '' },
      { id: null, title: "Bashkëpunimi dhe puna ekipore", description: "Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.", selected_option: '' },
      { id: null, title: "Njohuritë për pozitën e punës:", description: "Merr vendime të menduara, të arsyetuara mire, ushtron gjykim të mire, shkathtësi dhe kreativitet në zgjidhjen e problemeve.", selected_option: '' },
      { id: null, title: "Trajnimi dhe zhvillimi", description: "Vazhdimisht kërkon mënyra për të forcuar performancën dhe monitoron rregullisht zhvillimet e reja në fushën e punës.", selected_option: '' }
    ]);
    const parsedOptions = ["I tejkalon pritjet", "I plotëson pritjet", "Ka nevojë për përmirësim", "E papranueshme"];
    const employee = ref(null);
    
    const employeeName = computed(() => employee.value ? employee.value.name : 'Loading...');

    const fetchEmployee = async () => {
      try {
        const response = await api.get(`/employees/employees/${employeeId.value}`); // Endpoint to fetch employee by ID
        employee.value = response.data;
      } catch (error) {
        console.error('Error fetching employee:', error);
      }
    };

    const createAssessment = async () => {
      try {
        const now = new Date().toISOString();
        assessment.value.created_at = now;

        const response = await api.post('/assessment/create_assessment', assessment.value);
        const createdAssessment = response.data;

        if (!createdAssessment.id) {
          throw new Error('Failed to create assessment. No ID returned.');
        }

        console.log('Assessment created with ID:', createdAssessment.id);

        questions.value = questions.value.map(q => ({
          ...q,
          id: createdAssessment.questions.find(assessQ => assessQ.title === q.title)?.id || q.id
        }));

        console.log('Questions after mapping:', questions.value);

        for (const question of questions.value) {
          if (question.id) {
            const selectedOption = question.selected_option || '';
            console.log(`Updating question ${question.id} with selected option ${selectedOption}`);
            
            const updateResponse = await api.put(`/assessment/update_assessment_question_option/${question.id}`, {
              selected_option: selectedOption
            });

            console.log(`Response from updating question ${question.id}:`, updateResponse.data);
          }
        }

        alert('Assessment created and updated successfully!');
      } catch (error) {
        console.error('Error creating or updating assessment:', error);
        alert('Error creating or updating assessment.');
      }
    };

    onMounted(() => {
      fetchEmployee();
    });

    return {
      userId,
      assessment,
      questions,
      parsedOptions,
      employeeName,
      createAssessment
    };
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}

div {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input, textarea, select, button {
  padding: 8px;
  margin-top: 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
.text-justify {
  text-align: justify;
}
textarea {
  resize: vertical;
}
</style>
