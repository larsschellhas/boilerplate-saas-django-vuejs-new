<template>
  <div
    id="login-view"
    class="d-flex align-items-center flex-column mt-4"
  >
    <img
      src="@/assets/logo.png"
      height="60"
    >
    <LoginForm pagetitle="SimplySaaS" />
  </div>
</template>

<script>
import LoginForm from '@/components/Login/LoginForm'

export default {
  name: 'LoginView',
  components: {
    LoginForm
  }
}
</script>
