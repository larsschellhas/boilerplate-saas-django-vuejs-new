<template>
  <Header
    :routes="routes"
    :title="pagetitle"
  />
  <router-view />
</template>

<script>
import Header from '@/components/Header/Header'

export default {
  components: { Header },
  setup () {
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
