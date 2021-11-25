<template>
  <div class="mt-4 d-flex flex-column align-items-center">
    <p class="fs-4 text fw-light">
      {{ t('components.resetPasswordForm.title') }}
    </p>
    <transition name="fade">
      <div
        v-if="resetSent && token === ''"
        class="alert alert-success fade show w-100 my-0"
        role="alert"
      >
        {{ t('components.resetPasswordForm.tokenSentConfirmation') }}
      </div>
    </transition>
    <transition name="fade">
      <div
        v-if="passwordReset"
        class="alert alert-success fade show w-100 my-0"
        role="alert"
      >
        {{ t('components.resetPasswordForm.passwordResetConfirmation') }}
      </div>
    </transition>
    <LoginCard v-if="!resetSent && !passwordReset">
      <form v-if="token === ''">
        <div class="mb-3">
          <label
            for="email1"
            class="form-label"
          >{{ t("forms.email") }}</label>
          <input
            id="email1"
            v-model="resetPasswordData.username"
            type="email"
            class="form-control"
            :class="{
              'is-invalid': errors.username
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
        <button
          type="submit"
          class="btn btn-success w-100 text-light fw-bold"
          @click.prevent="handlePasswordResetInitiate"
        >
          <div
            v-if="loading"
            class="spinner-border spinner-border-sm text-light"
            role="status"
          >
            <span class="visually-hidden">{{ t("forms.loading") }}</span>
          </div>
          <span v-else>
            {{ t('components.resetPasswordForm.resetPassword') }}
          </span>
        </button>
      </form>
      <div v-else>
        <div
          v-if="!tokenValid && loading"
          class="spinner-border spinner-border text-primary d-block mx-auto"
          role="status"
        >
          <span class="visually-hidden">{{ t("forms.loading") }}</span>
        </div>
        <form v-if="tokenValid">
          <div class="mb-3">
            <label
              for="password1"
              class="form-label"
            >{{ t('components.resetPasswordForm.newPassword') }}</label>
            <input
              id="password1"
              v-model="resetPasswordData.password"
              type="password"
              class="form-control"
              :class="{
                'is-invalid': errors.password
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
          <button
            type="submit"
            class="btn btn-success w-100 text-light fw-bold"
            @click.prevent="handlePasswordResetConfirm"
          >
            <div
              v-if="loading"
              class="spinner-border spinner-border-sm text-light"
              role="status"
            >
              <span class="visually-hidden">{{ t("forms.loading") }}</span>
            </div>
            <span v-else>
              {{ t("forms.submit") }}
            </span>
          </button>
        </form>
      </div>
    </LoginCard>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useI18n } from 'vue-i18n'
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
    // Enable access to localizations
    const { t } = useI18n()
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
    const passwordReset = ref(false)

    // Reset password - Loading spinner
    const loading = ref(false)

    // Errors
    const errors = ref({
      username: '',
      password: ''
    })

    // Reset password - Handle password reset initiate
    function handlePasswordResetInitiate () {
      loading.value = true
      store.dispatch({
        type: 'user/resetPasswordInitiate',
        username: resetPasswordData.value.username
      }).then(results => {
        if (results.success) {
          resetSent.value = true
        } else {
          errors.value.username = results.errors.username
        }
        loading.value = false
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
          router.push({ name: 'ResetPasswordView' })
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
          passwordReset.value = true
          setTimeout(() => { router.push({ name: 'LoginView' }) }, 5000)
        } else {
          errors.value.password = results.errors.password
          passwordReset.value = false
        }
        loading.value = false
      })
    }

    onMounted(() => {
      if (props.token !== '') {
        handlePasswordResetValidate()
      }
    })
    // END - Reset password

    return { t, resetPasswordData, handlePasswordResetInitiate, handlePasswordResetValidate, handlePasswordResetConfirm, resetSent, passwordReset, tokenValid, loading, store, errors }
  }
}
</script>
