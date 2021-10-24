import { api } from './axiosConfig'

export default {
  async getTokens (username, password) {
    // TO-DO LOGIN
    const results = await api.post('login/', {
      email: username,
      password: password
    })
    return results.data
  },

  async refreshAccessToken (refreshToken) {
    const results = await api.post('login/refresh/', {
      refresh: refreshToken
    })
    return results.data.access
  },

  async registerUser (username, password, termsAndConditionsAccepted, firstName = '', lastName = '', referrerEmail = '') {
    // TO-DO Register
    const registerData = {
      email: username,
      password: password,
      terms_and_conditions_accepted: termsAndConditionsAccepted,
      first_name: firstName,
      last_name: lastName,
      referrer_email: referrerEmail
    }
    for (const key in registerData) {
      if (registerData[key] === '') {
        delete registerData[key]
      }
    }
    const results = await api.post('users/', registerData)
    return results.data
  },

  async updateUser (url, email = '', password = '', termsAndConditionsAccepted = '', firstName = '', lastName = '', referrerEmail = '') {
    // TO-DO Implement method in front- and backend to update a user easily
    throw TypeError('This method is not implemented, yet.')
  },

  async getCurrentUser () {
    const results = await api.get('users/')
    return results.data.results[0]
  }
}
