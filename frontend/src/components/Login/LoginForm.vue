<template>
  <div class="mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      Sign in to {{ pagetitle }}
    </p>
    <transition name="fade">
      <div
        v-if="errors"
        class="alert alert-danger alert-dismissible fade show w-100"
        role="alert"
      >
        Incorrect username or password!
        <button
          type="button"
          class="btn-close"
          aria-label="Close"
          @click="errors=false"
        />
      </div>
    </transition>
    <LoginCard
      :footer-text="'New to ' + pagetitle + '?'"
      footer-link-text="Create an account."
      :footer-link-route="{
        name: 'Register'
      }"
    >
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
          <div
            v-if="loading"
            class="spinner-border spinner-border-sm text-light"
            role="status"
          >
            <span class="visually-hidden">Loading...</span>
          </div>
          <span v-else>
            Submit
          </span>
        </button>
      </form>
    </LoginCard>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import LoginCard from './LoginCard'

export default {
  components: {
    LoginCard
  },
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
    const loginData = ref({
      username: '',
      password: ''
    })

    // Login - Validation
    const errors = ref(false)

    // Login - Loading spinner
    const loading = ref(false)

    // Login - Handle submit
    function handleLogin () {
      loading.value = true
      store.dispatch({
        type: 'user/login',
        username: loginData.value.username,
        password: loginData.value.password,
        target: ''
      }).then(results => {
        if (!results.success) {
          errors.value = true
          loading.value = false
        }
      })
    }
    // END - Login

    return { loginData, handleLogin, errors, loading }
  }
}

</script>
