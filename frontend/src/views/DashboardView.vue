<template>
  <div
    id="dashboard-view"
    class="d-flex justify-content-center m-4"
  >
    <h2>{{ title }}</h2>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { injectAuth } from 'vue-auth0-plugin'

// Enable access to localizations
const { t } = useI18n()
// Enable access to auth service
const auth = injectAuth()

const title = computed(() => {
  return t('views.dashboard.title', { firstname: auth.user.name, lastname: auth.user.lastname })
})
</script>
