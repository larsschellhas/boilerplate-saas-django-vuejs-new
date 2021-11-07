<template>
  <div>
    <div
      v-if="!user.isLoggedIn"
      class="login-links d-flex flex-row justify-content-center align-items-center"
    >
      <router-link
        :to="{ name: 'LoginView' }"
        class="nav-link link-light"
      >
        {{ t("components.headerNavigation.signIn") }}
      </router-link>
      <router-link
        :to="{ name: 'RegisterView' }"
        class="d-none d-lg-block"
      >
        <button
          type="button"
          class="btn btn-outline-light"
        >
          {{ t("components.headerNavigation.signUp") }}
        </button>
      </router-link>
    </div>
  <div
    class="nav-item dropdown dropdown-align-right"
  >
    <a
      v-if="user.isLoggedIn"
      id="headerUserContextMenuDrowpdownLink"
      class="nav-link link-light dropdown-toggle d-flex align-items-center"
      href="#"
      role="button"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <UserImage />
    </a>
    <ul
      v-if="user.isLoggedIn"
      class="dropdown-menu dropdown-menu-dark"
      aria-labelledby="headerUserContextMenuDrowpdownLink"
    >
      <li>
        <span class="dropdown-item-text">
          {{ t("components.headerUserContextMenu.signedInAs") }}<br>
          <b>{{ user.fullName }}</b>
        </span>
      </li>
      <li><hr class="dropdown-divider"></li>
      <li>
        <a
          class="dropdown-item"
          style="cursor: pointer;"
        >
          {{ t("components.headerUserContextMenu.yourWorkspaces") }}
        </a>
      </li>
      <li><hr class="dropdown-divider"></li>
      <li>
        <a
          class="dropdown-item"
          style="cursor: pointer;"
        >
          <i class="fas fa-arrow-up" /> {{ t("components.headerUserContextMenu.upgrade") }}
        </a>
      </li>
      <li>
        <a
          class="dropdown-item"
          style="cursor: pointer;"
        >
          <i class="fas fa-question" /> {{ t("components.headerUserContextMenu.help") }}
        </a>
      </li>
      <li>
        <router-link
          class="dropdown-item"
          style="cursor: pointer;"
          :to="{ name: 'SettingsView' }"
        >
          <i class="fas fa-cog" /> {{ t("components.headerUserContextMenu.settings") }}
        </router-link>
      </li>
      <li><hr class="dropdown-divider"></li>
      <li>
        <a
          class="dropdown-item"
          style="cursor: pointer;"
          @click.prevent="handleLogout"
        >
          <i class="fas fa-sign-out-alt" /> {{ t("components.headerUserContextMenu.signOut") }}
        </a>
      </li>
    </ul>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useStore } from 'vuex'
import UserImage from '../User/UserImage.vue'

export default {
  name: 'HeaderUserContextMenu',
  components: { UserImage },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    const user = computed(() => {
      return {
        fullName: store.getters['user/getFullName'],
        isLoggedIn: store.getters['user/isLoggedIn']
      }
    })

    const handleLogout = function () {
      store.dispatch({
        type: 'logout',
        target: { path: window.location.pathname }
      })
    }

    return { t, handleLogout, user }
  }
}
</script>

<style>
.dropdown-align-right .dropdown-menu[data-bs-popper] {
  left: auto;
  right: 0;
}
</style>
