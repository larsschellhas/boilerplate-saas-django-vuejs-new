<template>
  <div class="mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      {{ t("components.registerForm.title", {pagetitle: pagetitle}) }}
    </p>
    <LoginCard
      :footer-text="t('components.registerForm.alreadyHaveAnAccount')"
      :footer-link-text="t('components.registerForm.signIn')"
      :footer-link-route="{
        name: 'Login'
      }"
    >
      <form class="">
        <div class="mb-3">
          <label
            for="email1"
            class="form-label"
          >{{ t("forms.email") }}</label>
          <input
            id="email1"
            v-model="registerData.username"
            type="email"
            class="form-control"
            :class="{
              'is-invalid': errors.username && validated,
              'is-valid': !errors.username && validated,
            }"
            aria-describedby="emailHelp"
          >
          <div
            v-if="errors.username"
            class="invalid-feedback"
          >
            <span
              v-for="(error, index) in errors.username"
              :key="index"
            >
              {{ error }} </span>
          </div>
        </div>
        <div class="mb-3">
          <label
            for="password"
            class="form-label"
          >{{ t("forms.password") }}</label>
          <input
            id="password"
            v-model="registerData.password"
            type="password"
            class="form-control"
            :class="{
              'is-invalid': errors.password && validated,
              'is-valid': !errors.password && validated,
            }"
          >
          <div
            v-if="errors.password"
            class="invalid-feedback"
          >
            <span
              v-for="(error, index) in errors.password"
              :key="index"
            >
              {{ error }} </span>
          </div>
        </div>
        <div class="mb-3 form-check">
          <input
            id="termsAndConditions"
            v-model="registerData.termsAndConditionsAccepted"
            type="checkbox"
            class="form-check-input"
            :class="{
              'is-invalid': errors.termsAndConditionsAccepted && validated,
              'is-valid': !errors.termsAndConditionsAccepted && validated,
            }"
          >
          <label
            class="form-check-label"
            for="termsAndConditions"
          >{{ t("components.registerForm.acceptTermsAndConditions") }}</label>
          <div
            v-if="errors.termsAndConditionsAccepted"
            class="invalid-feedback"
          >
            <span
              v-for="(error, index) in errors.termsAndConditionsAccepted"
              :key="index"
            >
              {{ error }} </span>
          </div>
        </div>
        <button
          type="submit"
          class="btn btn-success w-100"
          @click.prevent="handleRegistration"
        >
          <div
            v-if="loading"
            class="spinner-border spinner-border-sm text-light"
            role="status"
          >
            <span class="visually-hidden">{{ t("forms.loading") }}</span>
          </div>
          <span v-else>
            {{ t("components.registerForm.createAccount") }}
          </span>
        </button>
      </form>
    </LoginCard>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'
import { ref } from 'vue'
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
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    // BEGIN - Registration
    // Registration - Data
    const registerData = ref({
      username: '',
      password: '',
      firstName: '',
      lastname: '',
      termsAndConditionsAccepted: false
    })

    // Registration - Validation
    const validated = ref(false)
    const errors = ref({
      username: '',
      password: '',
      termsAndConditionsAccepted: ''
    })

    // Registration - Loading spinner
    const loading = ref(false)

    // Registration - Handle submit
    function handleRegistration () {
      loading.value = true
      store.dispatch({
        type: 'user/register',
        username: registerData.value.username,
        password: registerData.value.password,
        firstName: registerData.value.firstName,
        lastName: registerData.value.lastName,
        termsAndConditionsAccepted: registerData.value.termsAndConditionsAccepted,
        referrerEmail: registerData.value.referrerEmail,
        target: { name: 'Login' }
      }).then(results => {
        if (!results.success) {
          for (const key in results.errors) {
            errors.value[key] = results.errors[key]
          }
          validated.value = true
          loading.value = false
        }
      })
    }
    // END - Registration

    return { t, registerData, handleRegistration, errors, validated, loading }
  }
}

</script>
