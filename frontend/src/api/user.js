import { api } from './axiosConfig'

export default {
  async getTokens (username, password) {
    // TO-DO LOGIN

    try {
      const response = await api.post('login/', {
        email: username,
        password: password
      })
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        const errors = {}
        errors.username = error.response.data.email
        errors.password = error.response.data.password
        return { success: false, errors: errors }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async refreshAccessToken (refreshToken) {
    try {
      const response = await api.post('login/refresh/', {
        refresh: refreshToken
      })
      return { success: true, data: response.data.access }
    } catch (error) {
      if (error.response.data) {
        return { success: false, errors: error.response.data }
      } else {
        return { success: false, errors: error }
      }
    }
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
    try {
      const response = await api.post('users/', registerData)
      const data = {}
      data.username = response.data.email
      data.termsAndConditionsAccepted = response.data.terms_and_conditions_accepted

      return { success: true, data: data }
    } catch (error) {
      if (error.response.data) {
        const errors = {}
        errors.username = error.response.data.email
        errors.password = error.response.data.password
        errors.termsAndConditionsAccepted = error.response.data.terms_and_conditions_accepted
        return { success: false, errors: errors }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async updateUser (url, email = '', password = '', termsAndConditionsAccepted = '', firstName = '', lastName = '', referrerEmail = '') {
    // TO-DO Implement method in front- and backend to update a user easily
    throw TypeError('This method is not implemented, yet.')
  },

  async getCurrentUser () {
    try {
      const response = await api.get('users/')
      return { success: true, data: response.data.results[0] }
    } catch (error) {
      if (error.response.data) {
        return { success: false, errors: error.response.data }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async resetPasswordInitiate (email) {
    try {
      const response = await api.post('login/reset/', { email: email })
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        const errors = {}
        errors.username = error.response.data.email
        return { success: false, errors: errors }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async resetPasswordValidate (token) {
    try {
      const response = await api.post('login/reset/validate_token/', { token: token })
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        return { success: false, errors: error.response.data }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async resetPasswordConfirm (password, token) {
    try {
      const response = await api.post('login/reset/confirm/', { password: password, token: token })
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        return { success: false, errors: error.response.data }
      } else {
        return { success: false, errors: error }
      }
    }
  }
}
