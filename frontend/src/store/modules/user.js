import user from '@/api/user'
import { pushOrReload } from '../../router'

const state = () => ({
  url: '',
  email: '',
  firstName: '',
  lastName: '',
  isStaff: false,
  termsAndConditionsAccepted: false,
  accessToken: '',
  refreshToken: ''
})

const getters = {
  getUserURL: state => {
    return state.url
  },
  getEmail: state => {
    return state.email
  },
  getFirstName: state => {
    return state.firstName
  },
  getLastName: state => {
    return state.lastName
  },
  isStaff: state => {
    return state.isStaff
  },
  getTermsAndConditionsAccepted: state => {
    return state.termsAndConditionsAccepted
  },
  getAccessToken: state => {
    return state.accessToken
  },
  getRefreshToken: state => {
    return state.refreshToken
  },
  isLoggedIn: state => {
    return state.refreshToken !== ''
  }
}

const actions = {
  async register ({ commit }, { username, password, firstName, lastName, termsAndConditionsAccepted, referrerEmail, target }) {
    const result = await user.registerUser(username, password, termsAndConditionsAccepted, firstName, lastName, referrerEmail, target)
    if (result.success) {
      commit('setURL', result.data.url)
      commit('setEmail', result.data.email)
      commit('setFirstName', result.data.first_name)
      commit('setLastName', result.data.last_name)
      commit('setIsStaff', result.data.is_staff)
      commit('setTermsAndConditionsAccepted', result.data.terms_and_conditions_accepted)
      pushOrReload(target)
      return { success: true }
    } else {
      return result
    }
  },

  async login ({ commit, dispatch }, { username, password, target }) {
    const result = await user.getTokens(username, password)
    if (result.success) {
      commit('setAccessToken', result.data.access)
      commit('setRefreshToken', result.data.refresh)
      await dispatch('getCurrentUser')
      pushOrReload(target)
      return { success: true }
    } else {
      return result
    }
  },

  async getCurrentUser ({ commit }) {
    const result = await user.getCurrentUser()
    if (result.success) {
      commit('setURL', result.data.url)
      commit('setEmail', result.data.email)
      commit('setFirstName', result.data.first_name)
      commit('setLastName', result.data.last_name)
      commit('setIsStaff', result.data.is_staff)
      commit('setTermsAndConditionsAccepted', result.data.terms_and_conditions_accepted)
      return { success: true }
    } else {
      return result
    }
  },

  async logout ({ commit }, { target }) {
    commit('resetUser')
    pushOrReload(target)
    return { success: true }
  },

  async refreshAccessToken ({ commit, state }) {
    const result = await user.refreshAccessToken(state.refreshToken)
    if (result.success) {
      commit('setAccessToken', result.data)
      return { success: true }
    } else {
      return result
    }
  },

  async resetPasswordInitiate ({ state }, { username }) {
    const result = await user.resetPasswordInitiate(username)
    if (result.success) {
      return { success: true }
    } else {
      return result
    }
  },

  async resetPasswordValidate ({ commit }, { token }) {
    const result = await user.resetPasswordValidate(token)
    if (result.success) {
      commit('setResetToken', token)
      return { success: true }
    } else {
      return result
    }
  },

  async resetPasswordConfirm ({ commit, state }, { password }) {
    const result = await user.resetPasswordConfirm(password, state.token)
    commit('setResetToken', '')
    if (result.success) {
      return { success: true }
    } else {
      return result
    }
  }
}

const mutations = {
  setEmail (state, status) {
    state.email = status
  },
  setFirstName (state, status) {
    state.firstName = status
  },
  setLastName (state, status) {
    state.lastName = status
  },
  setIsStaff (state, status) {
    state.isStaff = status
  },
  setTermsAndConditionsAccepted (state, status) {
    state.termsAndConditionsAccepted = status
  },
  setURL (state, status) {
    state.url = status
  },
  setAccessToken (state, status) {
    state.accessToken = status
  },
  setRefreshToken (state, status) {
    state.refreshToken = status
  },
  resetUser (state) {
    state.url = ''
    state.email = ''
    state.firstName = ''
    state.lastName = ''
    state.isStaff = false
    state.termsAndConditionsAccepted = false
    state.accessToken = ''
    state.refreshToken = ''
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
