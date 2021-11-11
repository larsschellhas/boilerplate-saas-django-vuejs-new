<template>
  <div class="locale-changer">
    <select
      v-model="locale"
      class="px-2 mx-auto nav-link link-light"
    >
      <option
        v-for="availableLocale in getSupportedLocales()"
        :key="`locale-${availableLocale}`"
        class="bg-dark"
        :value="availableLocale.code"
      >
        {{ availableLocale.name }}
      </option>
    </select>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'
import { getSupportedLocales } from '@/i18n'
import { useStore } from 'vuex'
import { computed } from 'vue'

export default {
  name: 'HelloI18n',
  setup () {
    const { t } = useI18n()
    const store = useStore()

    const locale = computed({
      get: () => { return store.getters['localization/getLocale'] },
      set: (value) => { store.commit('localization/setLocale', value) }
    })

    return { t, locale, getSupportedLocales }
  }
}
</script>

<style lang="scss">
.locale-changer {
  display: grid;

  select {
    background-color: transparent;
    border: none;
    color: #fff;
    font-family: inherit;
    font-size: inherit;
    cursor: inherit;
    line-height: inherit;
    outline: none;

    option {
      text-align: right;
    }
  }
}
</style>
