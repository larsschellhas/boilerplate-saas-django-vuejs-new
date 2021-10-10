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
    <div class="login-links d-flex flex-row justify-content-center align-items-center">
      <router-link
        to="/login"
        class="nav-link link-light"
      >
        Sign in
      </router-link>
      <router-link to="/register">
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
export default {
  props: {
    routes: {
      type: Array,
      required: true
    }
  }
}
</script>
