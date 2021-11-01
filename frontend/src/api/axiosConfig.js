import axios from 'axios'
import store from '@/store/index.js'

export const api = axios.create({
  baseURL: 'http://localhost:8000/',
  headers: {
    'Content-Type': 'application/json'
  }
})

api.interceptors.response.use(
  (res) => {
    return res
  },
  async (err) => {
    const originalConfig = err.config
    if (err.response) {
      // If access Token was expired
      if (err.response.status === 401 && originalConfig.url !== 'login/') {
        if (!originalConfig._retry && originalConfig.url !== 'login/refresh/' && store.state.user.refreshToken !== '') {
          originalConfig._retry = true
          await store.dispatch('user/refreshAccessToken')
          originalConfig.headers.Authorization = 'Bearer ' + store.state.user.accessToken
          return api(originalConfig)
        } else {
          store.dispatch({
            type: 'user/logout',
            target: { path: window.location.pathname }
          })
        }
      }
    }
    return Promise.reject(err)
  }
)

export function storeApiPlugin (store) {
  store.subscribe((mutation) => {
    if (mutation.type === 'user/setAccessToken') {
      if (mutation.payload) {
        api.defaults.headers.common.Authorization = 'Bearer ' + mutation.payload
      } else {
        delete api.defaults.headers.common.Authorization
      }
    }
  })
}
