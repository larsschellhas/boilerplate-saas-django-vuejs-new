<template>
  <div id="nav">
    <router-link
      v-for="route in routes"
      :key="route"
      :to="route.url"
    >
      {{ route.name }}
    </router-link>
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

<style lang="scss">
#nav {
  width: 100%;
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
