<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark d-flex align-items-center">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavigation"
        aria-controls="navbarNavigation"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon" />
      </button>
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
      <HeaderUserContextMenu class="d-lg-none" />
      <HeaderNavigation :routes="routes" />
      <HeaderUserContextMenu class="d-none d-lg-block" />
    </div>
  </nav>
</template>

<script>
import HeaderNavigation from '@/components/Header/HeaderNavigation.vue'
import HeaderUserContextMenu from '@/components/Header/HeaderUserContextMenu.vue'

export default {
  name: 'HeaderBar',
  components: { HeaderNavigation, HeaderUserContextMenu },
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
