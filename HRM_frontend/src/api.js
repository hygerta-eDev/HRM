import axios from 'axios'

export const api = axios.create({
    baseURL: 'http://127.0.0.1:8081/',
    timeout: 7000, // Increase timeout to 5000ms (5 seconds)
})

api.interceptors.request.use(config => {
    // Retrieve the userId from localStorage or another source
    const userId = localStorage.getItem('user_id'); // Adjust according to your local storage structure
    if (userId) {
      config.headers['x-user-id'] = userId;
    }
    // Optionally, you can also include the Authorization token if needed
    // const authToken = localStorage.getItem('auth_token'); // Adjust according to your local storage structure
    // if (authToken) {
    //   config.headers['Authorization'] = `Bearer ${authToken}`;
    // }
    return config;
  }, error => {
    return Promise.reject(error);
  });