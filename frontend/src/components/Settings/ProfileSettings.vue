<template>
  <SettingsSubPage
    id="profile-settings"
    title="components.profileSettings.title"
  >
    <template #header-button>
      Header Button
    </template>
    <template #default>
      <SettingsSubPageSection
        anchor="profile-picture"
        title="components.profileSettings.profilePicture.title"
      >
        <div />
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-name"
        title="components.profileSettings.name.title"
      >
        <div />
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-email"
        title="components.profileSettings.email.title"
      >
        <div />
      </SettingsSubPageSection>
      <SettingsSubPageSection
        anchor="profile-password"
        title="components.profileSettings.password.title"
      >
        <div />
      </SettingsSubPageSection>
    </template>
  </SettingsSubPage>
</template>

<script>
import { useI18n } from 'vue-i18n'
import SettingsSubPage from '@/components/Settings/SettingsSubPage'
import SettingsSubPageSection from '@/components/Settings/SettingsSubPageSection'

export default {
  name: 'ProfileSettings',
  components: {
    SettingsSubPage,
    SettingsSubPageSection
  },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()

    return { t }
  }
}
</script>
