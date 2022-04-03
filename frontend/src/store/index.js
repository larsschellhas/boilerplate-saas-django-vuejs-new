import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import localization from './modules/localization'
import user from './modules/user'
import { storeLocalizationPlugin } from '@/i18n'

export default createStore({
  strict: process.env.NODE_ENV !== 'production',
  actions: {
    async logout ({ commit, dispatch }) {
      commit('localization/resetState')
      dispatch('user/logout')
    }
  },
  modules: {
    localization,
    user
  },
  plugins: [
    storeLocalizationPlugin,
    createPersistedState()
  ]
})
