<template>
  <nav class="navbar sticky-top navbar-expand-md navbar-dark bg-dark d-flex align-items-center">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbar-navigation"
        aria-controls="navbar-navigation"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon" />
      </button>
      <router-link
        id="pagetitle"
        to="/"
        class="navbar-brand mb-0 h1 d-flex flex-row align-items-center"
        :style="pagetitleStyle"
      >
        <img
          src="@/assets/logo.png"
          height="36"
          class="me-2"
        >
        <span>{{ title }}</span>
      </router-link>
      <HeaderUserContextMenu class="d-md-none" />
      <HeaderNavigation :routes="routes" />
      <HeaderUserContextMenu class="d-none d-md-block" />
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import HeaderNavigation from '@/components/Header/HeaderNavigation.vue'
import HeaderUserContextMenu from '@/components/Header/HeaderUserContextMenu.vue'

defineProps(
  {
    routes: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      default: 'My Site'
    }
  }
)

const pagetitleStyle = ref('')

const centerPagetitle = function () {
  const logo = document.getElementById('pagetitle')
  if (window.innerWidth < 768) {
    const translation = (window.innerWidth - logo.clientWidth) / 2 - logo.offsetLeft
    pagetitleStyle.value = `transform: translatex(${translation}px)`
  } else {
    pagetitleStyle.value = ''
  }
}

onMounted(() => {
  window.onresize = centerPagetitle
  centerPagetitle()
})
</script>

<style lang="scss">
@import "@/styles/global";

#pagetitle span {
  display: none;

  @include media-breakpoint-up(sm) {
    display: block;
  }
}
</style>
