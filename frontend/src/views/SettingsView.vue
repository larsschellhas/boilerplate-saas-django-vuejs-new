<template>
  <div
    id="settings-view"
    class="dashboard d-flex justify-content-center m-4"
  >
    <h2>{{ t("views.settings.title") }}</h2>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'

export default {
  name: 'SettingsView',
  setup (props) {
    // Enable access to localizations
    const { t } = useI18n()
    return { t }
  }
}
</script>
