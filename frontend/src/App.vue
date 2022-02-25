<template>
  <HeaderBar
    :routes="routes"
    :title="pagetitle"
  />
  <router-view />
</template>

<script setup>
import HeaderBar from '@/components/Header/HeaderBar'
import { injectAuth } from 'vue-auth0-plugin'

// Enable access auth0
const auth = injectAuth()

const pagetitle = 'SimplySaaS'

const routes = [
  {
    name: 'app.headerNavigation.links.home',
    url: '/'
  }
]

auth.handleRedirectCallback()
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
