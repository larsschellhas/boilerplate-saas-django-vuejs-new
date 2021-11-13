<template>
  <div class="subpage-section">
    <div
      :id="anchor"
      class="subpage-anchor"
    />
    <h5>{{ t(title) }}</h5>
    <slot />
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'

export default {
  props: {
    anchor: {
      type: String,
      default: 'anchor'
    },
    title: {
      type: String,
      default: 'Title'
    }
  },
  setup () {
    // Enable access to localizations
    const { t } = useI18n()

    return { t }
  }
}
</script>

<style lang="scss">
  .subpage-anchor {
    position: relative;
    top: -82px;
  }
</style>
