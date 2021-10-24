import { api } from './axiosConfig'

export default {
  login (username, password) {
    // TO-DO LOGIN
    return api.post('login/', {
      username: username,
      password: password
    }).then(results => { return results.data })
  },

  logout () {
    // TO-DO Logout
    throw TypeError('This method is not implemented, yet.')
  },

  register (username, password, password2, termsAndConditionsAccepted) {
    // TO-DO Register
    return api.post('users/', {
      username: username,
      password: password,
      password2: password2,
      terms_and_conditions_accepted: termsAndConditionsAccepted
    }).then(results => { return results.data })
  },

  getCurrentUser () {
    return api.get('users/')
      .then(results => {
        debugger
        return results.data.results[0]
      })
  }
}
