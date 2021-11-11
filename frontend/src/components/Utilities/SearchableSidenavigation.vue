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
    <ul class="search-results nav nav-fill sidebar-nav flex-column">
      <li
        v-for="item in searchResults"
        :key="item"
        class="nav-item d-flex align-items-center"
      >
        <router-link
          class="nav-link rounded text-body text-opacity-75 d-flex align-items-center"
          :to="item.route"
        >
          <i
            :class="item.icon"
          />
          <span class="">
            {{ item.name }}
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
        // Enable access to localizations
        const { t } = useI18n()
        return [{
          name: t('views.settings.categories.profile'),
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
    const searchResults = computed(() => {
      return props.items.filter((setting) => {
        return setting.name.includes(searchQuery.value)
      })
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

    .search-results li.nav-item {
      padding: 2px 0;

      .nav-link {
        padding: 0.25em 0.5em;
        text-align: start;

        &:hover {
          background-color: rgba(0, 0, 0, 0.1);
        }

        &.router-link-exact-active {
          background-color: rgba(0, 0, 0, 0.1);

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
