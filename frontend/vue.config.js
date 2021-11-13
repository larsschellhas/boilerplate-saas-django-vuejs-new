const StyleLintPlugin = require('stylelint-webpack-plugin')
process.env.VUE_APP_VERSION = require('./package.json').version

module.exports = {
  configureWebpack: {
    devtool: 'source-map',
    plugins: [
      new StyleLintPlugin({
        files: ['src/**/*.{vue,scss}']
      })
    ]
  },
  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'localization',
      enableLegacy: false,
      runtimeOnly: true,
      compositionOnly: true,
      fullInstall: true
    }
  }
}
