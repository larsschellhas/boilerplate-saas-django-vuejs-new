import { watch } from 'vue'
import { AuthenticationProperties, AuthenticationState } from 'vue-auth0-plugin'

export const authenticationGuard = (to, from, next) => {
  // Ignored because of false positive - it's used in the watcher below
  // eslint-disable-next-line no-unused-vars
  const guardAction = () => {
    if (AuthenticationProperties.authenticated) {
      if (to.meta.allowAuthenticated) {
        return next()
      } else {
        return next({
          name: 'DashboardView'
        })
      }
    } else {
      if (to.meta.allowAnonymous) {
        return next()
      }
    }

    AuthenticationProperties.loginWithRedirect({ appState: { targetUrl: to.fullPath } })
  }

  // If the Auth0Plugin has loaded already, check the authentication state
  if (AuthenticationProperties.client && !AuthenticationState.loading) {
    return guardAction()
  }

  watch(AuthenticationState, async () => {
    if (AuthenticationProperties.client && !AuthenticationState.loading) {
      guardAction()
    }
  })
}
