<template>
  <div
    id="dashboard-view"
    class="d-flex justify-content-center m-4"
  >
    <ProductOverview />
  </div>
</template>

<script setup>
import { injectAuth } from 'vue-auth0-plugin'
import ProductOverview from '@/components/Product/ProductOverview.vue'
// import { useI18n } from 'vue-i18n'
import { onMounted } from 'vue'
import { useStore } from 'vuex'

// // Enable access to localizations
// const { t } = useI18n()
// Enable access to auth service
const auth = injectAuth()
// Enable access to vuex store
const store = useStore()

async function updateUser () {
  if (auth.client && !auth.loading) {
    console.log(store.getters['user/getUserURL'])
    if (store.getters['user/getUserURL'] === '') {
      await store.dispatch({
        type: 'user/getCurrentUser'
      })
    }
    console.log(auth)
    store.dispatch({
      type: 'user/updateProfileData',
      email: auth.user.email,
      first_name: auth.user.first_name,
      last_name: auth.user.last_name
    })
  } else {
    setTimeout(updateUser, 500)
    console.log('Wait for 500 ms')
  }
}

onMounted(() => {
  updateUser()
})

</script>
