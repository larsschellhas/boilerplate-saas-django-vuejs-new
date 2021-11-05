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
    const store = useStore()
    document.documentElement.setAttribute('lang', store.getters['localization/getLocale'])

    const routes = [
      {
        name: 'Home',
        url: '/'
      }
    ]
    const pagetitle = 'SimplySaaS'
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
