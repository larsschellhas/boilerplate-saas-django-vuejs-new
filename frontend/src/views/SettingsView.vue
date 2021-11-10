<template>
  <div
    id="settings-view"
    class="d-flex justify-content-center m-4"
  >
    <div class="settings-holder container">
      <div class="row">
        <div class="col flex-grow-0">
          <router-link
            class="rounded userBannerLink"
            :to="{ name: 'SettingsView', params: { category: 'profile' }}"
          >
            <UserBanner />
          </router-link>
          <div class="search-settings inner-addon right-addon mb-2">
            <i class="fas fa-search" />
            <input
              id="searchfield"
              v-model="searchQuery"
              type="text"
              class="form-control form-control-sm"
              aria-describedby="emailHelp"
              :placeholder="t('views.settings.search')"
            >
          </div>
          <!-- <div
            v-if="searchResults"
            class="search-settings-results"
          >
            {{ searchResults }}
          </div> -->
          <ul class="settings-nav nav nav-fill sidebar-nav flex-column">
            <li
              v-for="setting in searchResults"
              :key="setting"
              class="nav-item d-flex align-items-center"
            >
              <router-link
                class="nav-link rounded text-body text-opacity-75 d-flex align-items-center"
                :to="setting.route"
              >
                <i
                  :class="setting.icon"
                />
                <span class="">
                  {{ setting.name }}
                </span>
              </router-link>
            </li>
          </ul>
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
import UserBanner from '@/components/User/UserBanner'

export default {
  name: 'SettingsView',
  components: {
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
        return require('@/components/PageNotFound.vue').default
      }
    })

    const searchQuery = ref('')
    const searchResults = computed(() => {
      return settings.value.filter((setting) => {
        return setting.name.includes(searchQuery.value)
      })
    })

    return { t, settings, currentSettingsComponent, searchQuery, searchResults }
  }
}
</script>

<style lang="scss">
  #settings-view {

    .search-settings {
      &.inner-addon {
        position: relative;

        .fas, .far, .svg-inline--fa {
          position: absolute;
          margin: 8px;
          pointer-events: none;
        }

        &.left-addon {
          .fas, .far, .svg-inline--fa {
            left: 0px;
          }
          input {
            padding-left: 30px;
          }
        }

        &.right-addon {
          .fas, .far, .svg-inline--fa {
            right: 0px;
          }
          input {
            padding-right: 30px;
          }
        }
      }
    }

    .userBannerLink{
      text-decoration: none;
      color: var(--bs-body-color);
      display: block;
      &:hover {
        background-color: rgba(0,0,0,0.1);
      }
    }

    li.nav-item {
      padding: 2px 0;

      .nav-link {
        padding: 0.25em 0.5em;
        text-align: start;
        &:hover {
          background-color: rgba(0,0,0,0.1);
        }
        &.router-link-exact-active {
          background-color: rgba(0,0,0,0.1);
          &:before{
            content: '';
            display: block;
            position: absolute;
            transform: translatex(-0.5em);
            height: 1.2em;
            width: 3px;
            border-radius: 2px;
            background-color: var(--bs-primary)
          }
        }

        i, svg {
          width: 20px;
          margin-right: 8px;
        }
      }
    }
  }
</style>
