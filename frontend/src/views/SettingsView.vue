<template>
  <div
    id="settings-view"
    class="settings-holder d-flex justify-content-center align-items-stretch py-4"
  >
    <div class="row container p-0">
      <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4 sidebar-col">
        <router-link
          class="rounded user-banner-link"
          :to="{ name: 'SettingsView', hash: '#profile-settings', params: { category: 'profile' }}"
        >
          <UserBanner />
        </router-link>
        <SearchableSidenavigation :items="settings" />
      </div>
      <div class="col-12 col-md-6 col-lg-8 col-xl-9 content-col card shadow rounded p-0">
        <component :is="currentSettingsComponent" />
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
        name: 'views.settings.categories.profile',
        route: { name: 'SettingsView', hash: '#profile-settings', params: { category: 'profile' } },
        component: 'ProfileSettings',
        icon: 'fas fa-user',
        subsettings: [
          {
            name: 'views.settings.subsettings.changeName',
            route: { name: 'SettingsView', hash: '#profile-name', params: { category: 'profile' } },
            icon: 'fas fa-chevron-right'
          },
          {
            name: 'views.settings.subsettings.changePicture',
            route: { name: 'SettingsView', hash: '#profile-picture', params: { category: 'profile' } },
            icon: 'fas fa-chevron-right'
          },
          {
            name: 'views.settings.subsettings.changeEmail',
            route: { name: 'SettingsView', hash: '#profile-email', params: { category: 'profile' } },
            icon: 'fas fa-chevron-right'
          },
          {
            name: 'views.settings.subsettings.changePassword',
            route: { name: 'SettingsView', hash: '#profile-password', params: { category: 'profile' } },
            icon: 'fas fa-chevron-right'
          }
        ]
      },
      {
        name: 'views.settings.categories.notifications',
        route: { name: 'SettingsView', hash: '#notifications-settings', params: { category: 'notifications' } },
        icon: 'fas fa-bell'
      },
      {
        name: 'views.settings.categories.appearance',
        route: { name: 'SettingsView', hash: '#appearance-settings', params: { category: 'appearance' } },
        icon: 'fas fa-palette'
      },
      {
        name: 'views.settings.categories.privacy-security',
        route: { name: 'SettingsView', hash: '#privacy-security-settings', params: { category: 'privacy-security' } },
        icon: 'fas fa-user-shield'
      },
      {
        name: 'views.settings.categories.help-support',
        route: { name: 'SettingsView', hash: '#help-support', params: { category: 'help-support' } },
        icon: 'fas fa-question'
      },
      {
        name: 'views.settings.categories.about',
        route: { name: 'SettingsView', hash: '#about-settings', params: { category: 'about' } },
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
  @import "src/styles/global";

  #settings-view {
    @include media-breakpoint-up(md) {
      max-height: calc(100vh - 64px);
    }

    .row {
      .content-col {
        max-height: 100%;
      }

      .sidebar-col {
        .user-banner-link {
          text-decoration: none;
          color: var(--bs-body-color);
          display: block;

          &:hover {
            background-color: rgb(0 0 0 / 10%);
          }
        }
      }
    }
  }
</style>
