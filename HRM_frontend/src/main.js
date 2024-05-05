import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { useStorage } from '@vueuse/core'

import { createI18n } from 'vue-i18n';
import messages from '@intlify/unplugin-vue-i18n/messages'
const defaultLocale = useStorage('locale', navigator?.language || 'en')

const app = createApp(App)
const i18n = createI18n({
    locale: defaultLocale.value,
    messages,
})
  
app.use(i18n); 
app.use(router)
app.mount('#app')
