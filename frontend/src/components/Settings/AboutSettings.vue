<template>
  <SettingsSubPage
    id="about-settings"
    :title="t('components.aboutSettings.title')"
  >
    <p>{{ t('components.aboutSettings.appVersion') }}: {{ packageVersion }}</p>
  </SettingsSubPage>
</template>

<script>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import SettingsSubPage from '@/components/Settings/SettingsSubPage'

export default {
  name: 'AboutSettings',
  components: {
    SettingsSubPage
  },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()

    const packageVersion = computed(() => {
      return process.env.VUE_APP_VERSION
    })
    return { t, packageVersion }
  }
}
</script>
