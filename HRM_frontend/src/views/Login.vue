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

  <template>
    <div class="flex justify-center items-center font-sans h-full min-h-screen p-4">
      <div class="absolute inset-0 z-0"
           :style="{ backgroundImage: `url(${backgroundImage})`, backgroundRepeat: 'no-repeat', backgroundSize: 'cover', filter: 'blur(3px)' }">
      </div>
      <div class="max-w-md w-full mx-auto relative z-10">
        <form class="bg-white rounded-2xl p-6 shadow-[0_2px_16px_-3px_rgba(6,81,237,0.3)]" @submit.prevent="login">
          <div class="mb-12">
            <h3 class="text-gray-800 text-3xl font-extrabold">Sign in</h3>
          </div>
  
          <div class="mb-6">
            <div class="relative flex items-center">
              <input name="username" type="text" v-model="username" required
                     class="bg-transparent w-full text-sm text-gray-800 border-b border-gray-400 focus:border-gray-800 px-2 py-3 outline-none placeholder:text-gray-800"
                     placeholder="Enter username" />
            </div>
          </div>
  
          <div class="mb-6">
            <div class="relative flex items-center">
              <input :type="showPassword ? 'text' : 'password'" v-model="password" required
                     class="bg-transparent w-full text-sm text-gray-800 border-b border-gray-400 focus:border-gray-800 px-2 py-3 outline-none placeholder:text-gray-800"
                     placeholder="Enter password" />
              <svg @click="togglePasswordVisibility" xmlns="http://www.w3.org/2000/svg" fill="#333" stroke="#333"
                   class="w-[18px] h-[18px] absolute right-2 cursor-pointer" viewBox="0 0 128 128">
                <path
                    d="M64 104C22.127 104 1.367 67.496.504 65.943a4 4 0 0 1 0-3.887C1.367 60.504 22.127 24 64 24s62.633 36.504 63.496 38.057a4 4 0 0 1 0 3.887C126.633 67.496 105.873 104 64 104zM8.707 63.994C13.465 71.205 32.146 96 64 96c31.955 0 50.553-24.775 55.293-31.994C114.535 56.795 95.854 32 64 32 32.045 32 13.447 56.775 8.707 63.994zM64 88c-13.234 0-24-10.766-24-24s10.766-24 24-24 24 10.766 24 24-10.766 24-24 24zm0-40c-8.822 0-16 7.178-16 16s7.178 16 16 16 16-7.178 16-16-7.178-16-16-16z"
                    data-original="#000000"></path>
              </svg>
            </div>
          </div>
  
          <div class="flex items-center justify-between gap-4 mb-6">
            <div class="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" v-model="rememberMe"
                     class="h-4 w-4 shrink-0 border-gray-300 rounded" />
              <label for="remember-me"
                     class="ml-3 block text-sm text-gray-800">
                Remember me
              </label>
            </div>
            <div>
              <a href="javascript:void(0);"
                 class="text-blue-600 text-sm font-semibold hover:underline">
                Forgot Password?
              </a>
            </div>
          </div>
  
          <div class="mt-6">
            <button type="submit"
                    class="w-full py-2.5 px-4 text-sm font-semibold tracking-wider rounded-full text-white bg-gray-800 hover:bg-[#222] focus:outline-none">
              Sign in
            </button>
          </div>
  
          <hr class="my-6 border-gray-400" />
  
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { api } from '@/api';
  import backgroundImage from '@/assets/img/e_tech_shpk_cover.jpeg';
  
  export default {
    data() {
      return {
        backgroundImage: backgroundImage,
        username: '',
        password: '',
        rememberMe: false,
        showPassword: false,
        error: null,
      };
    },
    mounted() {
      const rememberedUsername = localStorage.getItem('rememberedUsername');
      if (rememberedUsername) {
        this.username = rememberedUsername;
        this.rememberMe = true;
      }
    },
    methods: {
      togglePasswordVisibility() {
        this.showPassword = !this.showPassword;
      },
      async login() {
        try {
          this.error = null;
          const response = await api.post('/user/login', {
            username: this.username,
            password: this.password,
          });
  
          if (response && response.data) {
            const { access_token, user_id, employee_id, roles, permissions, name } = response.data;
            localStorage.setItem('token', access_token);
            localStorage.setItem('user_id', user_id);
            localStorage.setItem('employee_id', employee_id);
            localStorage.setItem('roles', JSON.stringify(roles));
            localStorage.setItem('permissions', JSON.stringify(permissions));
            localStorage.setItem('name', name);
  
            if (this.rememberMe) {
              localStorage.setItem('rememberedUsername', this.username);
            } else {
              localStorage.removeItem('rememberedUsername');
            }
  
            this.$router.push('/Employee'); // Redirect to the dashboard
          } else {
            // Handle unexpected response structure
            throw new Error('Unexpected response structure');
          }
        } catch (error) {
          // Check if error.response and error.response.data exist
          if (error.response && error.response.data) {
            this.error = error.response.data.detail || 'An error occurred';
          } else {
            this.error = error.message || 'An error occurred';
          }
          console.error('Error logging in:', error);
        }
      },
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user_id');
        localStorage.removeItem('employee_id');
        localStorage.removeItem('roles');
        localStorage.removeItem('permissions');
        localStorage.removeItem('name');
        // Optionally clear remembered username on logout
        localStorage.removeItem('rememberedUsername');
        this.$router.push('/login'); // Redirect to the login page
      }
    },
  };
  </script>
  
  <style scoped>
  /* Add any scoped styles if necessary */
  </style>
  