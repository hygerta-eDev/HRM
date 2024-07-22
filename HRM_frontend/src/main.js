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
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import App from './App.vue';
import router from './router';
import { createI18n } from 'vue-i18n';
import en from '@/locales/en.json';
import al from '@/locales/al.json';
const i18n = createI18n({
    locale: 'en',
    fallbackLocale: 'al',
    messages: {
      en,
      al
    }
  });
  export default i18n;

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
app.use(i18n); // Include i18n here

app.component('VueDatePicker', VueDatePicker);

// Initialize PrimeVue toast service
// app.use(ToastService);

app.mount('#app');
