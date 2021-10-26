import user from '@/api/user'

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
      window.location.href = target
      return { sucess: true }
    } else {
      return result
    }
  },

  async login ({ commit }, { username, password, target }) {
    const result = await user.getTokens(username, password)
    if (result.success) {
      commit('setAccessToken', result.data.access)
      commit('setRefreshToken', result.data.refresh)
      const currentUser = await user.getCurrentUser()
      commit('setURL', currentUser.url)
      commit('setEmail', currentUser.email)
      commit('setFirstName', currentUser.first_name)
      commit('setLastName', currentUser.last_name)
      commit('setIsStaff', currentUser.is_staff)
      commit('setTermsAndConditionsAccepted', currentUser.terms_and_conditions_accepted)
      window.location.href = target
      return { sucess: true }
    } else {
      return result
    }
  },

  logout ({ commit }, { target }) {
    commit('resetUser')
    window.location.href = target
    return true
  },

  async refreshAccessToken ({ commit, state }) {
    const accessToken = await user.refreshAccessToken(state.refreshToken)
    commit('setAccessToken', accessToken)
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
