import user from '@/api/user'

const getDefaultState = () => {
  return {
    url: '',
    email: '',
    firstName: '',
    lastName: '',
    isStaff: false,
    termsAndConditionsAccepted: false,
    profilePicture: '',
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
  getFirstName: state => {
    return state.firstName
  },
  getLastName: state => {
    return state.lastName
  },
  getFullName: state => {
    return state.firstName + ' ' + state.lastName
  },
  isStaff: state => {
    return state.isStaff
  },
  getTermsAndConditionsAccepted: state => {
    return state.termsAndConditionsAccepted
  },
  getProfilePicture: state => {
    return state.profilePicture
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
  async updateProfileData ({ commit, getters }, { email, firstname, lastname }) {
    const result = await user.updateProfileData(getters.getUserURL, email, firstname, lastname)
    if (result.success) {
      if ('email' in result.data) {
        commit('setEmail', result.data.email)
      }
      if ('first_name' in result.data) {
        commit('setFirstName', result.data.first_name)
      }
      if ('last_name' in result.data) {
        commit('setLastName', result.data.last_name)
      }
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
      return { success: true }
    } else {
      return result
    }
  },

  async logout ({ commit }) {
    commit('resetState')
    return { success: true }
  }
}

const mutations = {
  setURL (state, status) {
    state.url = status
  },
  setEmail (state, status) {
    state.email = status
  },
  setFirstName (state, status) {
    state.firstname = status
  },
  setLastName (state, status) {
    state.lastname = status
  },
  setIsStaff (state, status) {
    state.isStaff = status
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
