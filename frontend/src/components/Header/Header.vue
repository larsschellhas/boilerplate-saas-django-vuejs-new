<template>
  <div id="header">
    <router-link
      id="pagetitle"
      to="/"
    >
      {{ title }}
    </router-link>
    <div class="divider" />
    <HeaderNavigation :routes="routes" />
  </div>
</template>

<script>
import HeaderNavigation from '@/components/Header/HeaderNavigation.vue'

export default {
  components: { HeaderNavigation },
  props: {
    routes: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      default: 'My Site'
    }
  }
}
</script>

<style lang="scss">
#header {
  width: 100%;
  box-sizing: border-box;
  background-color: #e2e2e2;
  height: 60px;
  padding: 12px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  box-shadow: 0 0 12px 0 rgba(0, 0, 0, 0.5);

  #pagetitle {
    font-size: 24px;
    font-weight: 600;
    color: inherit;
    text-decoration: none;
  }
}

.divider {
  display: flex;
  flex-grow: 1;
}
</style>
