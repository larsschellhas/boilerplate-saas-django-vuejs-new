module.exports = {
  configureWebpack: {
    devtool: 'source-map'
  },
  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'localization',
      enableLegacy: false,
      runtimeOnly: false,
      compositionOnly: true,
      fullInstall: true
    }
  }
}
