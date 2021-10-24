<template>
  <div class="auth-form px-3 mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      Sign up for {{ pagetitle }}
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
              v-model="registerData.username"
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
              for="password"
              class="form-label"
            >Password</label>
            <input
              id="password"
              v-model="registerData.password"
              type="password"
              class="form-control"
            >
          </div>
          <div class="mb-3 form-check">
            <input
              id="termsAndConditions"
              v-model="registerData.termsAndConditionsAccepted"
              type="checkbox"
              class="form-check-input"
            >
            <label
              class="form-check-label"
              for="termsAndConditions"
            >I accept the terms and conditions</label>
          </div>
          <button
            type="submit"
            class="btn btn-success w-100"
            @click.prevent="handleRegistration"
          >
            Create account
          </button>
        </form>
      </div>
    </div>
    <div class="card w-100">
      <div class="card-body text-center">
        Already have an account? <router-link to="/login">
          Sign in.
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from 'vuex'
import { reactive } from 'vue'

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

    // BEGIN - Registration
    // Registration - Data
    const registerData = reactive({
      username: '',
      password: '',
      firstName: '',
      lastname: '',
      termsAndConditionsAccepted: false
    })

    // Registration - Handle submit
    function handleRegistration () {
      store.dispatch({
        type: 'user/register',
        username: registerData.username,
        password: registerData.password,
        firstName: registerData.firstName,
        lastName: registerData.lastName,
        termsAndConditionsAccepted: registerData.termsAndConditionsAccepted,
        referrerEmail: registerData.referrerEmail,
        target: window.location.origin + '/login/'
      })
    }
    // END - Registration

    return { registerData, handleRegistration }
  }
}

</script>
