import user from '@/api/user'
import { pushOrReload } from '../../router'

const getDefaultState = () => {
  return {
    url: '',
    email: '',
    firstname: '',
    lastname: '',
    isStaff: false,
    termsAndConditionsAccepted: false,
    accessToken: '',
    refreshToken: ''
  }
}

const state = getDefaultState()

const getters = {
  getUserURL: state => {
    return state.url
  },
  getEmail: state => {
    return state.email
  },
  getFirstname: state => {
    return state.firstname
  },
  getLastname: state => {
    return state.lastname
  },
  getFullName: state => {
    return state.firstname + ' ' + state.lastname
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
  async register ({ commit }, { username, password, firstname, lastname, termsAndConditionsAccepted, referrerEmail, target }) {
    const result = await user.registerUser(username, password, termsAndConditionsAccepted, firstname, lastname, referrerEmail)
    if (result.success) {
      commit('setURL', result.data.url)
      commit('setEmail', result.data.email)
      commit('setFirstname', result.data.first_name)
      commit('setLastname', result.data.last_name)
      commit('setIsStaff', result.data.is_staff)
      commit('setTermsAndConditionsAccepted', result.data.terms_and_conditions_accepted)
      pushOrReload(target)
      return { success: true }
    } else {
      return result
    }
  },

  async update ({ commit, getters }, { username, password, firstname, lastname }) {
    const result = await user.updateUser(getters.getUserURL, username, password, firstname, lastname)
    if (result.success) {
      commit('setEmail', result.data.email)
      commit('setFirstname', result.data.first_name)
      commit('setLastname', result.data.last_name)
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
      commit('setFirstname', result.data.first_name)
      commit('setLastname', result.data.last_name)
      commit('setIsStaff', result.data.is_staff)
      commit('setTermsAndConditionsAccepted', result.data.terms_and_conditions_accepted)
      return { success: true }
    } else {
      return result
    }
  },

  async logout ({ commit }, { target }) {
    commit('resetState')
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
      return { success: true }
    } else {
      return result
    }
  },

  async resetPasswordConfirm ({ commit }, { password, token }) {
    const result = await user.resetPasswordConfirm(password, token)
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
  setFirstname (state, status) {
    state.firstname = status
  },
  setLastname (state, status) {
    state.lastname = status
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
