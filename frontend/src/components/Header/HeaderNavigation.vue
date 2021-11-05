<template>
  <button
    class="navbar-toggler"
    type="button"
    data-bs-toggle="collapse"
    data-bs-target="#navbarNavigation"
    aria-controls="navbarNavigation"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon" />
  </button>
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
          {{ route.name }}
        </router-link>
      </li>
    </ul>
    <LocaleSwitch />
    <div
      v-if="isLoggedIn"
      class="login-links d-flex flex-row justify-content-center align-items-center"
    >
      <a
        class="nav-link link-light"
        style="cursor: pointer;"
        @click.prevent="handleLogout"
      >
        Sign out
      </a>
    </div>
    <div
      v-else
      class="login-links d-flex flex-row justify-content-center align-items-center"
    >
      <router-link
        :to="{ name: 'Login' }"
        class="nav-link link-light"
      >
        Sign in
      </router-link>
      <router-link :to="{ name: 'Register' }">
        <button
          type="button"
          class="btn btn-outline-light"
        >
          Sign up
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
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
    const store = useStore()

    const isLoggedIn = computed(() => store.getters['user/isLoggedIn'])

    const handleLogout = function () {
      store.dispatch({
        type: 'logout',
        target: { path: window.location.pathname }
      })
    }
    return { store, isLoggedIn, handleLogout }
  }
}
</script>
