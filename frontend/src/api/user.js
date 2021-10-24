import { api } from './axiosConfig'

export default {
  async getTokens (username, password) {
    // TO-DO LOGIN
    const results = await api.post('api/token/', {
      email: username,
      password: password
    })
    return results.data
  },

  async refreshAccessToken (refreshToken) {
    const results = await api.post('api/token/refresh/', {
      refresh: refreshToken
    })
    return results.data.access
  },

  logout () {
    // TO-DO Logout
    throw TypeError('This method is not implemented, yet.')
  },

  async register (username, password, password2, termsAndConditionsAccepted) {
    // TO-DO Register
    const results = await api.post('users/', {
      username: username,
      password: password,
      password2: password2,
      terms_and_conditions_accepted: termsAndConditionsAccepted
    })
    return results.data
  },

  async getCurrentUser () {
    const results = await api.get('users/')
    return results.data.results[0]
  }
}
