import { createI18n } from 'vue-i18n'
import supportedLocales from '@/localization/supported-locales'
import store from '@/store/index.js'

/**
 * Load locale messages
 *
 * The loaded `JSON` locale messages is pre-compiled by `@intlify/vue-i18n-loader`, which is integrated into `vue-cli-plugin-i18n`.
 * See: https://github.com/intlify/vue-i18n-loader#rocket-i18n-resource-pre-compilation
 */
function loadLocaleMessages () {
  const locales = require.context('./localization', true, /[A-Za-z0-9-_,\s]+\.json$/i)
  const messages = {}
  locales.keys().forEach(key => {
    const matched = key.match(/([A-Za-z0-9-_]+)\./i)
    if (matched && matched.length > 1) {
      const locale = matched[1]
      messages[locale] = locales(key).default
    }
  })
  return messages
}

const i18n = createI18n({
  legacy: false,
  locale: store.getters['localization/getLocale'],
  fallbackLocale: store.getters['localization/getFallbackLocale'],
  messages: loadLocaleMessages()
})

export default i18n

// Export a list of supported locales from 'localization/supported-locales.js'
export function getSupportedLocales () {
  const annotatedLocales = []
  for (const code of Object.keys(supportedLocales)) {
    annotatedLocales.push({
      code,
      name: supportedLocales[code]
    })
  }
  return annotatedLocales
}

// Export a vuex store plugin to update the global locale when its value is changed in the store
export function storeLocalizationPlugin (store) {
  store.subscribe((mutation) => {
    if (mutation.type === 'localization/setLocale') {
      // Set global locale to new value from store
      i18n.global.locale.value = mutation.payload
      // Update lang-property of html document with new languade code
      document.documentElement.setAttribute('lang', mutation.payload)
    }
  })
}
