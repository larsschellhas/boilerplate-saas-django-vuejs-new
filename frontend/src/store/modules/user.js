import user from '@/api/user'

const state = () => ({
  email: '',
  firstName: '',
  lastName: '',
  token: ''
})

const getters = {
  getToken: state => {
    return state.token
  }
}

const actions = {
  login ({ commit, state }, { username, password }) {
    user.login(username, password)
      .then(data => {
        commit('setToken', data.token)
      })
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
  setToken (state, status) {
    state.token = status
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
