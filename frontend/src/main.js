import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import i18n, { loadLocaleMessages } from './i18n'

loadLocaleMessages(store.getters['localization/getLocale']).then(() => {
  createApp(App).use(i18n).use(store).use(router).mount('#app')
})
