module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        'assets': '@/assets',
        'components': '@/components',
        'api': '@/api',
        'views': '@/views',
      }
    }
  }
}
