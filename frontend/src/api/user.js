import { api } from './axiosConfig'

function removeEmptyKeys (dict) {
  for (const key in dict) {
    if (dict[key] === '') {
      delete dict[key]
    }
  }
  return dict
}

export default {
  async getTokens (username, password) {
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

  async registerUser (username, password, termsAndConditionsAccepted, firstname = '', lastname = '', referrerEmail = '') {
    // TO-DO Register
    const registerData = removeEmptyKeys({
      email: username,
      password: password,
      terms_and_conditions_accepted: termsAndConditionsAccepted,
      first_name: firstname,
      last_name: lastname,
      referrer_email: referrerEmail
    })
    try {
      const response = await api.post('users/', registerData)
      const data = {}
      data.username = response.data.email
      data.firstname = response.data.first_name
      data.lastname = response.data.last_name
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

  async updateProfileData (url, username = '', password = '', firstname = '', lastname = '', profilePicture = '', initialSetupDone = '') {
    const updateData = removeEmptyKeys({
      email: username,
      password: password,
      first_name: firstname,
      last_name: lastname,
      profile_picture_uid: profilePicture,
      initial_setup_done: initialSetupDone
    })
    try {
      const response = await api.patch(url, updateData)
      if (response.data.profile_picture !== null) {
        response.data.profile_picture = `${api.defaults.baseURL}fp/load/?id=${response.data.profile_picture.upload_id}`
      } else {
        response.data.profile_picture = ''
      }
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        const errors = {}
        errors.username = error.response.data.email
        errors.password = error.response.data.password
        errors.firstname = error.response.data.first_name
        errors.lastname = error.response.data.last_name
        errors.profilePicture = error.response.data.profile_picture
        return { success: false, errors: errors }
      } else {
        return { success: false, errors: error }
      }
    }
  },

  async getCurrentUser () {
    try {
      const response = await api.get('users/')
      const userData = response.data.results[0]
      debugger
      if (userData.profile_picture !== null) {
        userData.profile_picture = `${api.defaults.baseURL}fp/load/?id=${userData.profile_picture.upload_id}`
      } else {
        userData.profile_picture = ''
      }
      return { success: true, data: userData }
    } catch (error) {
      debugger
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
