/* eslint-disable no-undef */
import { loadScript } from 'vue-plugin-load-script'
import { AuthenticationProperties, AuthenticationState } from 'vue-auth0-plugin'

const payments = {
  setup: async () => {
    loadScript('https://cdn.paddle.com/paddle/paddle.js')
      .then(() => {
        // Initial setup of paddle
        Paddle.Setup({
          vendor: parseInt(process.env.VUE_APP_PADDLE_VENDOR),
          eventCallback: function (data) {
            if (data.event === 'Checkout.Complete') {
              console.log(data.eventData)
            }
          }
        })

        // Set environment to sandbox if not set to production
        if (process.env.VUE_APP_PRODUCTION === 'False') {
          console.log('Paddle: Sandbox')
          Paddle.Environment.set('sandbox')
        }
        payments.resumeCheckout()
      })
  },
  openCheckout: async (productId) => {
    if (AuthenticationProperties.client && !AuthenticationState.loading) {
      if (AuthenticationState.authenticated) {
        Paddle.Checkout.open({
          product: parseInt(productId),
          email: AuthenticationState.user.email,
          disableLogout: true
        })
      } else {
        AuthenticationProperties.loginWithRedirect({ appState: { targetUrl: window.location.href + '?openCheckout=' + productId } })
      }
    } else {
      setTimeout(() => { payments.openCheckout(productId) }, 100)
    }
  },
  resumeCheckout: async () => {
    const searchParams = new URLSearchParams(window.location.search)
    if (searchParams.get('openCheckout')) {
      payments.openCheckout(searchParams.get('openCheckout'))
    } else if (searchParams.get('state')) {
      setTimeout(payments.resumeCheckout, 100)
    }
  }
}

export default payments
