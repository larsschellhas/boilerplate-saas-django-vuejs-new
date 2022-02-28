<template>
  <div class="searchable-sidenavigation">
    <div class="search-bar inner-addon right-addon mb-2">
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
    <ul
      class="nav nav-fill sidebar-nav flex-column"
      :class="{ 'search-results': searchQuery}"
    >
      <li
        v-for="item in searchResults"
        :key="item"
        class="nav-item d-flex align-items-center"
      >
        <router-link
          class="nav-link rounded text-body text-opacity-75 d-flex align-items-center"
          :class="{ 'search-result': searchQuery}"
          :to="item.route"
        >
          <i
            :class="item.icon"
          />
          <span class="">
            {{ t(item.name) }}
          </span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'

export default {
  props: {
    items: {
      type: Array,
      default: () => {
        return [{
          name: 'views.settings.categories.profile',
          route: { name: 'SettingsView', params: { category: 'profile' } },
          component: 'ProfileSettings',
          icon: 'fas fa-user'
        }]
      }
    }
  },
  setup (props) {
    // Enable access to localizations
    const { t } = useI18n()

    const searchQuery = ref('')
    const lowerCaseSearchQUery = computed(() => searchQuery.value.toLowerCase())
    const searchResults = computed(() => {
      if (lowerCaseSearchQUery.value !== '') {
        const results = []
        for (const setting of props.items) {
          if (setting.subsettings) {
            const subsettingsResults = setting.subsettings.filter((subsetting) => t(subsetting.name).toLowerCase().includes(lowerCaseSearchQUery.value))
            if (subsettingsResults.length) {
              results.push(setting)
              subsettingsResults.forEach(subsetting => results.push(subsetting))
            }
          } else {
            if (t(setting.name).toLowerCase().includes(lowerCaseSearchQUery.value)) {
              results.push(setting)
            }
          }
        }
        return results
      }
      return props.items
    })

    return { t, searchQuery, searchResults }
  }
}
</script>

<style lang="scss">
  .searchable-sidenavigation {
    .search-bar {
      &.inner-addon {
        position: relative;

        .fas,
        .far,
        svg {
          position: absolute;
          margin: 8px;
          pointer-events: none;
        }

        &.left-addon {
          .fas,
          .far,
          svg {
            left: 0;
          }

          input {
            padding-left: 30px;
          }
        }

        &.right-addon {
          .fas,
          .far,
          svg {
            right: 0;
          }

          input {
            padding-right: 30px;
          }
        }
      }
    }

    .sidebar-nav li.nav-item {
      padding: 2px 0;

      .nav-link {
        padding: 0.25em 0.5em;
        text-align: start;

        &:hover {
          background-color: rgb(0 0 0 / 10%);
        }

        &:not(.search-result).router-link-exact-active {
          background-color: rgb(0 0 0 / 10%);

          &::before {
            content: "";
            display: block;
            position: absolute;
            transform: translateX(-0.5em);
            height: 1.2em;
            width: 3px;
            border-radius: 2px;
            background-color: var(--bs-primary);
          }
        }

        i,
        svg {
          width: 20px;
          margin-right: 8px;
        }
      }
    }
  }
</style>
