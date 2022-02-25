import 'bootstrap'
import '@/styles/global.scss'
import '@fortawesome/fontawesome-free/js/all'
import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import i18n, { loadFallbackLocale, setLocale } from '@/i18n'
import VueAuth0Plugin from 'vue-auth0-plugin'

const auth0domain = process.env.VUE_APP_AUTH0_DOMAIN
const auth0clientID = process.env.VUE_APP_AUTH0_CLIENT_ID
const auth0audience = process.env.VUE_APP_AUTH0_API_IDENTIFIER

Promise.all([
  setLocale(store.getters['localization/getLocale']),
  loadFallbackLocale()
])
  .then(() => {
    createApp(App)
      .use(VueAuth0Plugin,
        {
          domain: auth0domain,
          client_id: auth0clientID,
          audience: auth0audience,
          redirect_uri: window.location.origin
        }
      )
      .use(i18n)
      .use(store)
      .use(router)
      .mount('#app')
  })
