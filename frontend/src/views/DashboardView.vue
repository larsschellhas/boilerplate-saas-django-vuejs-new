<template>
  <div
    class="dashboard d-flex justify-content-center m-4"
  >
    <h2>{{ title }}</h2>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useI18n } from 'vue-i18n'

export default {
  name: 'DashboardView',
  setup () {
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    const title = computed(() => {
      return t('views.dashboard.title', { firstname: store.getters['user/getFirstName'], lastname: store.getters['user/getLastName'] })
    })

    return { title }
  }
}
</script>
