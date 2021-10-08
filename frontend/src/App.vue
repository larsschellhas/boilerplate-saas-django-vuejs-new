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
      },
      {
        name: 'Login',
        url: '/login'
      }
    ]
    const pagetitle = 'SimplySaaS'
    return { routes, pagetitle }
  }
}
</script>

<style>
body {
  padding: 0;
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
