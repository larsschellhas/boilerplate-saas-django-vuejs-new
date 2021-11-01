<template>
  <div class="mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      Reset your password
    </p>
    <transition name="fade">
      <div
        v-if="resetSent && token === ''"
        class="alert alert-success fade show w-100 my-0"
        role="alert"
      >
        If this email exists, a password reset link has been sent!
      </div>
    </transition>
    <LoginCard v-if="!resetSent">
      <form v-if="token === ''">
        <div class="mb-3">
          <label
            for="email1"
            class="form-label"
          >Email address</label>
          <input
            id="email1"
            v-model="resetPasswordData.username"
            type="email"
            class="form-control"
            aria-describedby="emailHelp"
          >
        </div>
        <button
          type="submit"
          class="btn btn-success w-100"
          @click.prevent="handlePasswordResetInitiate"
        >
          <div
            v-if="loading"
            class="spinner-border spinner-border-sm text-light"
            role="status"
          >
            <span class="visually-hidden">Loading...</span>
          </div>
          <span v-else>
            Reset password
          </span>
        </button>
      </form>
      <form v-else>
        <div
          v-if="!tokenValid && loading"
          class="spinner-border spinner-border text-primary d-block mx-auto"
          role="status"
        >
          <span class="visually-hidden">Loading...</span>
        </div>
      </form>
    </LoginCard>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import router from '../../router'
import LoginCard from './LoginCard'

export default {
  components: {
    LoginCard
  },
  props: {
    token: {
      type: String,
      default: ''
    }
  },
  setup (props) {
    // Enable access to vuex store
    const store = useStore()

    // BEGIN - Reset password
    // Reset password - Data
    const resetPasswordData = ref({
      username: '',
      password: ''
    })

    // Reset password - Validation
    const resetSent = ref(false)
    const tokenValid = ref(false)
    const passwordReseted = ref(false)

    // Reset password - Loading spinner
    const loading = ref(false)

    // Reset password - Handle password reset initiate
    function handlePasswordResetInitiate () {
      loading.value = true
      store.dispatch({
        type: 'user/resetPasswordInitiate',
        username: resetPasswordData.value.username
      }).then(results => {
        if (!results.success) {
          resetSent.value = true
          loading.value = false
        }
      })
    }

    // Reset password - Handle password reset validate
    function handlePasswordResetValidate () {
      loading.value = true
      store.dispatch({
        type: 'user/resetPasswordValidate',
        token: props.token
      }).then(results => {
        if (results.success) {
          tokenValid.value = true
        } else {
          router.push({ name: 'ResetPassword' })
        }
        loading.value = false
      })
    }

    // Reset password - Handle password reset validate
    function handlePasswordResetConfirm () {
      loading.value = true
      store.dispatch({
        type: 'user/resetPasswordConfirm',
        password: resetPasswordData.value.password,
        token: props.token
      }).then(results => {
        if (results.success) {
          passwordReseted.value = true
          setTimeout(() => { router.push({ name: 'Login' }) }, 5000)
        } else {
          console.log(results)
          debugger
          passwordReseted.value = false
        }
        loading.value = false
      })
    }

    onMounted(() => {
      handlePasswordResetValidate()
    })
    // END - Reset password

    return { resetPasswordData, handlePasswordResetInitiate, handlePasswordResetValidate, handlePasswordResetConfirm, resetSent, tokenValid, loading, store }
  }
}
</script>
