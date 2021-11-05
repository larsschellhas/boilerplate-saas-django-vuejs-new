import { getSupportedLocales } from '@/i18n'

const getDefaultState = () => {
  return {
    locale: '',
    fallbackLocale: 'en'
  }
}

const state = getDefaultState()

const getters = {
  getLocale (state, getters) {
    if (state.locale) {
      return state.locale
    } else {
      const supportedLocales = getSupportedLocales().map(locale => locale.code)
      for (const key in navigator.languages) {
        if (supportedLocales.includes(navigator.languages[key])) {
          return navigator.languages[key]
        }
      }
      return getters.getFallbackLocale
    }
  },
  getFallbackLocale (state) {
    return state.fallbackLocale
  }
}

const actions = {}

const mutations = {
  setLocale (state, status) {
    state.locale = status
  },
  setFallbackLocale (state, status) {
    state.fallbacklocale = status
  },
  resetState (state) {
    Object.assign(state, getDefaultState())
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
