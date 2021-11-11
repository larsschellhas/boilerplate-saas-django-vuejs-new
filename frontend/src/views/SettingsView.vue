<template>
  <div
    id="settings-view"
    class="d-flex justify-content-center m-4"
  >
    <div class="settings-holder container">
      <div class="row">
        <div class="col flex-grow-0">
          <router-link
            class="rounded user-banner-link"
            :to="{ name: 'SettingsView', params: { category: 'profile' }}"
          >
            <UserBanner />
          </router-link>
          <SearchableSidenavigation :items="settings" />
        </div>
        <div class="col card shadow rounded d-flex justify-content-center align-items-center">
          <component :is="currentSettingsComponent" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import SearchableSidenavigation from '@/components/Utilities/SearchableSidenavigation'
import UserBanner from '@/components/User/UserBanner'

export default {
  name: 'SettingsView',
  components: {
    SearchableSidenavigation,
    UserBanner
  },
  props: {
    category: {
      type: String,
      default: 'profile'
    }
  },
  setup (props) {
    // Enable access to localizations
    const { t } = useI18n()

    const settings = ref([
      {
        name: t('views.settings.categories.profile'),
        route: { name: 'SettingsView', params: { category: 'profile' } },
        component: 'ProfileSettings',
        icon: 'fas fa-user'
      },
      {
        name: t('views.settings.categories.notifications'),
        route: { name: 'SettingsView', params: { category: 'notifications' } },
        icon: 'fas fa-bell'
      },
      {
        name: t('views.settings.categories.appearance'),
        route: { name: 'SettingsView', params: { category: 'appearance' } },
        icon: 'fas fa-palette'
      },
      {
        name: t('views.settings.categories.privacy-security'),
        route: { name: 'SettingsView', params: { category: 'privacy-security' } },
        icon: 'fas fa-user-shield'
      },
      {
        name: t('views.settings.categories.help-support'),
        route: { name: 'SettingsView', params: { category: 'help-support' } },
        icon: 'fas fa-question'
      },
      {
        name: t('views.settings.categories.about'),
        route: { name: 'SettingsView', params: { category: 'about' } },
        component: 'AboutSettings',
        icon: 'fas fa-info'
      }
    ])

    const currentSettingsComponent = computed(() => {
      const currentSettings = settings.value.find((setting) => {
        for (const param in setting.route.params) {
          if (setting.route.params[param] !== props[param]) { return false }
        }
        return true
      })
      if (currentSettings.component) {
        return require('@/components/Settings/' + currentSettings.component + '.vue').default
      } else {
        return require('@/components/Utilities/PageNotFound.vue').default
      }
    })

    return { t, settings, currentSettingsComponent }
  }
}
</script>

<style lang="scss">
  #settings-view {
    .user-banner-link {
      text-decoration: none;
      color: var(--bs-body-color);
      display: block;

      &:hover {
        background-color: rgba(0, 0, 0, 0.1);
      }
    }
  }
</style>
