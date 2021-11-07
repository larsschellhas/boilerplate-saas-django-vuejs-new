<template>
  <div
    id="navbarNavigation"
    class="collapse navbar-collapse"
  >
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li
        v-for="route in routes"
        :key="route"
        class="nav-item text-center"
      >
        <router-link
          :to="route.url"
          class="nav-link"
        >
          {{ t(route.name) }}
        </router-link>
      </li>
    </ul>
    <LocaleSwitch />
    <!-- <HeaderUserContextMenu v-if="isLoggedIn" /> -->
    <div
      v-if="!isLoggedIn"
      class="login-links d-flex flex-row justify-content-center align-items-center"
    >
      <router-link
        :to="{ name: 'LoginView' }"
        class="nav-link link-light"
      >
        {{ t("components.headerNavigation.signIn") }}
      </router-link>
      <router-link :to="{ name: 'RegisterView' }">
        <button
          type="button"
          class="btn btn-outline-light"
        >
          {{ t("components.headerNavigation.signUp") }}
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useI18n } from 'vue-i18n'
import LocaleSwitch from '../LocaleSwitch.vue'

export default {
  components: {
    LocaleSwitch
  },
  props: {
    routes: {
      type: Array,
      required: true
    }
  },
  setup (props) {
    // Enable access to localizations
    const { t } = useI18n()
    // Enable access to vuex store
    const store = useStore()

    const isLoggedIn = computed(() => store.getters['user/isLoggedIn'])

    return { t, store, isLoggedIn }
  }
}
</script>

<style>
#navbarNavigation .nav-link {
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
