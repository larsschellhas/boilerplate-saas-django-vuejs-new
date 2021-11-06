<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark d-flex align-items-center">
    <div class="container-fluid">
      <router-link
        id="pagetitle"
        to="/"
        class="navbar-brand mb-0 h1 d-flex flex-row align-items-center"
      >
        <img
          src="@/assets/logo.png"
          height="36"
          class="me-2"
        >
        {{ title }}
      </router-link>
      <HeaderNavigation :routes="routes" />
    </div>
  </nav>
</template>

<script>
import HeaderNavigation from '@/components/Header/HeaderNavigation.vue'

export default {
  name: 'HeaderBar',
  components: { HeaderNavigation },
  props: {
    routes: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      default: 'My Site'
    }
  }
}
</script>
