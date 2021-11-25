<template>
  <div class="auth-form px-3 mb-0">
    <div class="card bg-light shadow rounded mb-4 w-100">
      <div class="card-body">
        <slot />
      </div>
    </div>
    <div
      v-if="footerText || footerLinkText"
      class="card w-100"
    >
      <div class="card-body text-center">
        {{ t(footerText, {pagetitle: pagetitle}) }} <router-link :to="footerLinkRoute">
          {{ t(footerLinkText, {pagetitle: pagetitle}) }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'

export default {
  props: {
    footerText: {
      type: String,
      default: 'components.loginForm.footerText'
    },
    footerLinkText: {
      type: String,
      default: 'components.loginForm.footerLinkText'
    },
    footerLinkRoute: {
      type: Object,
      default: () => { return { name: 'RegisterView' } }
    },
    pagetitle: {
      type: String,
      default: 'SimplySaaS'
    }
  },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()

    return { t }
  }
}
</script>

<style>
.auth-form {
  width: 350px;
  max-width: 350px;
  margin: 0 auto;
}
</style>
