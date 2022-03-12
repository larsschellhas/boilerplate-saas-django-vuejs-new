import { api } from '@/api/axiosConfig'
import { removeEmptyKeys } from '@/api/utils'

export default {
  async updateProfileData (url, email = '', firstName = '', lastName = '') {
    const updateData = removeEmptyKeys({
      email: email,
      first_name: firstName,
      last_name: lastName
    })
    try {
      const response = await api.patch(url, updateData)
      return { success: true, data: response.data }
    } catch (error) {
      if (error.response.data) {
        const errors = {}
        errors.email = error.response.data.email
        errors.firstName = error.response.data.first_name
        errors.lastName = error.response.data.last_name
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
      return { success: true, data: userData }
    } catch (error) {
      if (error.response.data) {
        return { success: false, errors: error.response.data }
      } else {
        return { success: false, errors: error }
      }
    }
  }
}
