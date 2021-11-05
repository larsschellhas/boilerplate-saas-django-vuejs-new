<template>
  <Header
    :routes="routes"
    :title="pagetitle"
  />
  <router-view />
</template>

<script>
import Header from '@/components/Header/Header'
import { useStore } from 'vuex'

export default {
  components: { Header },
  setup () {
    // Enable access to vuex store
    const store = useStore()
    document.documentElement.setAttribute('lang', store.getters['localization/getLocale'])

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
