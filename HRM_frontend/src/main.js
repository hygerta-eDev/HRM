import './assets/style.css';
import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import { createPinia } from 'pinia';
import Lara from '@/presets/lara'; 
import 'primevue/resources/primevue.min.css';
import Tooltip from 'primevue/tooltip';

import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(PrimeVue, {
    pt: Lara 
});

app.directive('tooltip', Tooltip);

app.use(createPinia());
app.use(router);

app.mount('#app');
