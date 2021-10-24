import axios from 'axios'
import store from '@/store/index.js'

console.log(store)

export const api = axios.create({
  baseURL: 'http://localhost:8000/'
})

export function storeApiPlugin (store) {
  store.watch(
    state => state.user.token,
    token => {
      if (token) {
        api.defaults.headers.common.Authorization = 'Token ' + token
      } else {
        delete api.defaults.headers.common.Authorization
      }
    }
  )
}
