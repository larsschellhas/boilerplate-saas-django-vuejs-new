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
  login ({ commit }, { username, password, target }) {
    user.getTokens(username, password)
      .then(data => {
        commit('setAccessToken', data.access)
        commit('setRefreshToken', data.refresh)
      })
      .then(() => {
        return user.getCurrentUser()
      })
      .then(user => {
        commit('setURL', user.url)
        commit('setEmail', user.email)
        commit('setFirstName', user.first_name)
        commit('setLastName', user.last_name)
        commit('setIsStaff', user.is_staff)
        commit('setTermsAndConditionsAccepted', user.terms_and_conditions_accepted)
      })
      .then(() => {
        window.location.href = target
      })
  },
  logout ({ commit }, { target }) {
    commit('resetUser')
    window.location.href = target
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
