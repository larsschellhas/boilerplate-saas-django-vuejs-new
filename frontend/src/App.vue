<template>
  <HeaderBar
    :routes="routes"
    :title="pagetitle"
  />
  <router-view />
</template>

<script>
import HeaderBar from '@/components/Header/HeaderBar'

export default {
  components: {
    HeaderBar
  },
  setup () {
    const pagetitle = 'SimplySaaS'

    const routes = [
      {
        name: 'app.headerNavigation.links.home',
        url: '/'
      }
    ]

    return { routes, pagetitle }
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
