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
  display: flex;
  justify-content: flex-end;
  align-items: center;

  a {
    font-weight: bold;
    color: #2c3e50;
    padding: 12px;
    border-radius: 4px;

    &:hover {
      background-color: #d2d2d2;
    }
  }
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
