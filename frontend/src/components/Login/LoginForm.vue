<template>
  <div class="auth-form px-3 mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      Sign in to {{ pagetitle }}
    </p>
    <div class="card bg-light shadow rounded mb-4 w-100">
      <div class="card-body">
        <form>
          <div class="mb-3">
            <label
              for="email1"
              class="form-label"
            >Email address</label>
            <input
              id="email1"
              v-model="loginData.username"
              type="email"
              class="form-control"
              aria-describedby="emailHelp"
            >
            <div
              id="emailHelp"
              class="form-text"
            />
          </div>
          <div class="mb-3">
            <label
              for="password1"
              class="form-label"
            >Password</label>
            <input
              id="password1"
              v-model="loginData.password"
              type="password"
              class="form-control"
            >
          </div>
          <button
            type="submit"
            class="btn btn-success w-100"
            @click.prevent="handleLogin"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
    <div class="card w-100">
      <div class="card-body text-center">
        New to {{ pagetitle }}? <router-link to="/register">
          Create an account.
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue'
import { useStore } from 'vuex'

export default {
  props: {
    pagetitle: {
      type: String,
      default: 'SimplySaaS'
    }
  },
  setup (props) {
    // Enable access to vuex store
    const store = useStore()

    // BEGIN - Login
    // Login - Data
    const loginData = reactive({
      username: '',
      password: ''
    })

    // Login - Handle submit
    function handleLogin () {
      store.dispatch({
        type: 'user/login',
        username: loginData.username,
        password: loginData.password,
        target: window.location.href
      })
    }
    // END - Login

    return { loginData, handleLogin }
  }
}

</script>

<style>




}
</style>
