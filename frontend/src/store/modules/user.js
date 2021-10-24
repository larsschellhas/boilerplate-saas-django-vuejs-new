import user from '@/api/user'

const state = () => ({
  url: '',
  email: '',
  firstName: '',
  lastName: '',
  isStaff: false,
  termsAndConditionsAccepted: false,
  token: ''
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
  getToken: state => {
    return state.token
  },
  isLoggedIn: state => {
    return state.token !== ''
  }
}

const actions = {
  login ({ commit }, { username, password, target }) {
    user.login(username, password)
      .then(data => {
        commit('setToken', data.token)
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
  setToken (state, status) {
    if (status !== '') {
      state.token = status
    } else {
      throw TypeError('Cannot set an empty token. Use "resetUser" to remove existing tokens.')
    }
  },
  resetUser (state) {
    state.url = ''
    state.email = ''
    state.firstName = ''
    state.lastName = ''
    state.isStaff = false
    state.termsAndConditionsAccepted = false
    state.token = ''
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
