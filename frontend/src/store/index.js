import { createStore } from 'vuex'
import { storeApiPlugin } from '@/api/axiosConfig'
import createPersistedState from 'vuex-persistedstate'
import user from './modules/user'

export default createStore({
  strict: process.env.NODE_ENV !== 'production',
  actions: {
    async logout ({ commit, dispatch }, { target }) {
      dispatch('user/logout', { target })
    }
  },
  modules: {
    user
  },
  plugins: [
    storeApiPlugin,
    createPersistedState()
  ]
})
