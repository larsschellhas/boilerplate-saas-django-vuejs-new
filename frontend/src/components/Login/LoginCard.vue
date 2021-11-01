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
        {{ footerText }} <router-link :to="footerLinkRoute">
          {{ footerLinkText }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    footerText: {
      type: String,
      default: 'New to SimplySaaS?'
    },
    footerLinkText: {
      type: String,
      default: 'Create an account.'
    },
    footerLinkRoute: {
      type: Object,
      default: () => { return { name: 'Register' } }
    }
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
