import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import i18n, { loadFallbackLocale, setLocale } from './i18n'

Promise.all([
  setLocale(store.getters['localization/getLocale']),
  loadFallbackLocale()
])
  .then(() => {
    createApp(App).use(i18n).use(store).use(router).mount('#app')
  })
