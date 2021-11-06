import { createI18n } from 'vue-i18n'
import supportedLocales from '@/localization/supported-locales'
import store from '@/store/index.js'

const i18n = createI18n({
  legacy: false,
  locale: store.getters['localization/getLocale'],
  fallbackLocale: store.getters['localization/getFallbackLocale']
})

export default i18n

export async function setLocale (locale) {
  // Lazy load locale messages asynchronously based on the currently seleted locale
  const messages = await import(/* webpackChunkName: "locale-[request]" */ '@/localization/' + locale + '.json')
  // set locale and locale message
  i18n.global.setLocaleMessage(locale, messages.default)
  // Set global locale to new value from store
  i18n.global.locale.value = locale
  // Update lang-property of html document with new languade code
  document.documentElement.setAttribute('lang', i18n.global.locale.value)
  return Promise.resolve()
}

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
  store.subscribe(function (mutation) {
    if (mutation.type === 'localization/setLocale') {
      setLocale(mutation.payload)
    }
  })
}
