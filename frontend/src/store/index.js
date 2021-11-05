import { createStore } from 'vuex'
import { storeApiPlugin } from '@/api/axiosConfig'
import createPersistedState from 'vuex-persistedstate'
import user from './modules/user'
import localization from './modules/localization'
import { storeLocalizationPlugin } from '@/i18n'

export default createStore({
  strict: process.env.NODE_ENV !== 'production',
  actions: {
    async logout ({ commit, dispatch }, { target }) {
      commit('localization/resetState')
      dispatch('user/logout', { target })
    }
  },
  modules: {
    user,
    localization
  },
  plugins: [
    storeApiPlugin,
    storeLocalizationPlugin,
    createPersistedState()
  ]
})
