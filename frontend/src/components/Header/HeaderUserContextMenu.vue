<template>
  <div>
    <div
      v-if="!auth.authenticated"
      class="login-links d-flex flex-row justify-content-center align-items-center"
    >
      <a
        class="nav-link link-light cursor-pointer"
        @click.prevent="login()"
      >
        {{ t("components.headerNavigation.signIn") }}
      </a>
      <a
        class="d-none d-lg-block"
        @click.prevent="signup()"
      >
        <button
          type="button"
          class="btn btn-outline-light"
        >
          {{ t("components.headerNavigation.signUp") }}
        </button>
      </a>
    </div>
    <div
      class="nav-item dropdown dropdown-align-right"
    >
      <a
        v-if="auth.authenticated"
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
        v-if="auth.authenticated"
        class="dropdown-menu dropdown-menu-dark"
        aria-labelledby="headerUserContextMenuDrowpdownLink"
      >
        <li>
          <router-link
            class="dropdown-item"
            style="cursor: pointer;"
            :to="{ name: 'SettingsView', params: { category: 'profile' } }"
          >
            <span class="dropdown-item-text">
              {{ t("components.headerUserContextMenu.signedInAs") }}<br>
              <b>{{ user.name }}</b>
            </span>
          </router-link>
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
          <router-link
            class="dropdown-item"
            style="cursor: pointer;"
            :to="{ name: 'SettingsView', params: { category: 'help-support' } }"
          >
            <i class="fas fa-question" /> {{ t("components.headerUserContextMenu.help") }}
          </router-link>
        </li>
        <li>
          <router-link
            class="dropdown-item"
            style="cursor: pointer;"
            :to="{ name: 'SettingsView', params: { category: 'profile' } }"
          >
            <i class="fas fa-cog" /> {{ t("components.headerUserContextMenu.settings") }}
          </router-link>
        </li>
        <li><hr class="dropdown-divider"></li>
        <li>
          <a
            class="dropdown-item"
            style="cursor: pointer;"
            @click.prevent="logout()"
          >
            <i class="fas fa-sign-out-alt" /> {{ t("components.headerUserContextMenu.signOut") }}
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { injectAuth } from 'vue-auth0-plugin'
import UserImage from '../User/UserImage.vue'

// Enable access to localizations
const { t } = useI18n()
// Enable access auth0
const auth = injectAuth()

const user = computed(() => {
  if (auth.user) {
    return auth.user
  }
  return {}
})

const login = function () {
  auth.loginWithRedirect({
    appState: { targetUrl: window.location.origin + '/dashboard' }
  })
}

const signup = function () {
  auth.loginWithRedirect({
    appState: { targetUrl: window.location.origin + '/dashboard' },
    screen_hint: 'signup'
  })
}

const logout = function () {
  auth.logout({
    returnTo: window.location.origin
  })
}

</script>

<style>
.dropdown-align-right .dropdown-menu[data-bs-popper] {
  left: auto;
  right: 0;
}

.cursor-pointer {
  cursor: pointer;
}
</style>
