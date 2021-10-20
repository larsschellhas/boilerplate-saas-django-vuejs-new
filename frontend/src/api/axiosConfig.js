import axios from 'axios'
import store from '@/store/index.js'

console.log(store)

export const api = axios.create({
  baseURL: 'http://localhost:8000/',
  headers: {
    // Authorization: store.getters.getToken()
  }
})

export function storeApiPlugin (store) {
  console.log('api:storeApiPlugin: Setting up the watcher now')
  // store.watch: https://vuex.vuejs.org/en/api.html
  store.watch(
    state => state.user.token,
    token => {
      console.log('storeApiPlugin: The watcher callback is called, we save the token in our axios instance')
      if (token) {
        api.defaults.headers.common.Authentication = token
      } else {
        delete api.default.headers.common.Authentication
      }
    }
  )
}
