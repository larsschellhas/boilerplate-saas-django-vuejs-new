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
  },

  register (username, password, password2) {
    // TO-DO Register
  }
}
