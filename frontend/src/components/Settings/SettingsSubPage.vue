<template>
  <div class="subpage w-100">
    <div class="subpage-header p-4 d-flex justify-content-between align-items-center border-bottom">
      <h3 class="subpage-title">
        {{ t(title) }}
      </h3>
      <slot name="header-button" />
    </div>
    <div class="subpage-content p-4">
      <slot />
    </div>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'

export default {
  props: {
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
  .subpage {
    max-height: 100%;

    .subpage-header {
      position: sticky;
      top: 64px;
      height: 82px;
      background-color: #fff;

      .subpage-title {
        margin: 0;
      }
    }

    .subpage-content {
      max-height: calc(100% - 82px);
      overflow-y: auto;
    }
  }
</style>
