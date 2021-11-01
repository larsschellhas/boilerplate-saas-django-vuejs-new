<template>
  <div class="d-flex align-items-center flex-column mt-4">
    <img
      src="@/assets/logo.png"
      height="60"
    >
    <ResetPasswordForm
      pagetitle="SimplySaaS"
      :token="token"
    />
  </div>
</template>

<script>
import ResetPasswordForm from '@/components/Login/ResetPasswordForm'

export default {
  components: {
    ResetPasswordForm
  },
  props: {
    token: {
      type: String,
      default: ''
    }
  }
}

</script>
