<template>
  <HeaderBar
    :routes="routes"
    :title="pagetitle"
  />
  <a
    href="#!"
    class="button"
    @click.prevent="payments.openCheckout(productId=26474)"
  >Buy Now!</a>
  <router-view />
</template>

<script setup>
import HeaderBar from '@/components/Header/HeaderBar'
import { onMounted } from 'vue'
import { injectAuth } from 'vue-auth0-plugin'
import { useStore } from 'vuex'
import payments from './subscriptions'

const pagetitle = 'SimplySaaS'

const routes = [
  {
    name: 'app.headerNavigation.links.home',
    url: '/'
  }
]

// BEGIN: Update user from data provided from auth provder
// Enable access to auth service
const auth = injectAuth()
// Enable access to vuex store
const store = useStore()

async function updateUserFromAuth () {
  if (auth.client && !auth.loading) {
    if (auth.authenticated) {
      if (store.getters['user/getUserURL'] === '') {
        await store.dispatch({
          type: 'user/getCurrentUser'
        })
      }
      store.dispatch({
        type: 'user/updateProfileData',
        email: auth.user.email,
        first_name: auth.user.first_name,
        last_name: auth.user.last_name
      })
    }
  } else {
    setTimeout(updateUserFromAuth, 500)
  }
}

onMounted(() => {
  updateUserFromAuth()
})
// END: Update user from data provided from auth provder

auth.handleRedirectCallback()
payments.setup()
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
