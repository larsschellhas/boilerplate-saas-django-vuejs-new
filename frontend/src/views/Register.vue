<template>
  <div class="d-flex align-items-center flex-column mt-4">
    <img
      src="@/assets/logo.png"
      height="60"
    >
    <RegisterForm pagetitle="SimplySaaS" />
  </div>
</template>

<script>
import RegisterForm from '@/components/Login/RegisterForm.vue'

export default {
  components: {
    RegisterForm
  }
}

</script>
