import axios from 'axios'
import store from '@/store'
import { AuthenticationProperties } from 'vue-auth0-plugin'

export const api = axios.create({
  baseURL: process.env.VUE_APP_BACKEND_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

api.interceptors.request.use(
  async (config) => {
    if (AuthenticationProperties.authenticated) {
      const token = await AuthenticationProperties.getTokenSilently()
      config.headers.common.Authorization = 'Bearer ' + token
    }
    return config
  }
)

api.interceptors.response.use(
  (res) => {
    return res
  },
  async (err) => {
    if (err.response && err.response.status === 401) {
      // If access Token was expired
      store.dispatch({
        type: 'logout',
        target: { path: window.location.pathname }
      })
    }
    return Promise.reject(err)
  }
)
