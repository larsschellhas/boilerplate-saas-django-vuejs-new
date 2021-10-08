<template>
  <NavigationMain :routes="routes" />
  <router-view />
</template>

<script>
import NavigationMain from '@/components/NavigationMain.vue'

export default {
  components: { NavigationMain },
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
    return { routes }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
