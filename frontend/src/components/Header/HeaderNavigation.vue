<template>
  <div
    id="navbar-navigation"
    class="collapse navbar-collapse"
  >
    <ul
      class="navbar-nav me-auto mb-2 mb-md-0"
    >
      <li
        v-for="route in routes"
        :key="route"
        class="nav-item text-center"
      >
        <router-link
          :to="route.url"
          class="nav-link"
          @click="closeMenu('navbar-navigation')"
        >
          {{ t(route.name) }}
        </router-link>
      </li>
    </ul>
    <LocaleSwitch />
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useI18n } from 'vue-i18n'
import LocaleSwitch from '../Utilities/LocaleSwitch.vue'

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

    const closeMenu = (id) => {
      const menuShown = document.getElementById(id).classList.contains('show')
      if (menuShown) {
        const menuToggle = document.getElementsByClassName('navbar-toggler')[0]
        menuToggle.click()
      }
    }

    return { t, store, isLoggedIn, closeMenu }
  },
  watch: {
    $route (to, from) {
      const menuShown = document.getElementById('navbar-navigation').classList.contains('show')
      if (menuShown) {
        const menuToggle = document.getElementsByClassName('navbar-toggler')[0]
        menuToggle.click()
      }
    }
  }
}
</script>

<style>
#navbar-navigation .nav-link {
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
