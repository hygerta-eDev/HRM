import './assets/style.css';
import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import { createPinia } from 'pinia';
import Lara from '@/presets/lara'; 
import 'primevue/resources/primevue.min.css';
import Tooltip from 'primevue/tooltip';
import '@fortawesome/fontawesome-free/css/all.min.css';
import Vue3Toasity from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(PrimeVue, {
    pt: Lara 
});

app.directive('tooltip', Tooltip);

app.use(createPinia());
app.use(router);
app.use(Vue3Toasity, {
    autoClose: 3000,
})

// Initialize PrimeVue toast service
// app.use(ToastService);

app.mount('#app');
