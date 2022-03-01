import { watch } from 'vue'
import { AuthenticationProperties, AuthenticationState } from 'vue-auth0-plugin'

export const authenticationGuard = (to, from) => {
  const guardAction = () => {
    if (AuthenticationProperties.authenticated) {
      if (to.meta.allowAuthenticated) {
        return true
      } else {
        return { name: 'DashboardView' }
      }
    } else if (to.meta.allowAnonymous) {
      return true
    }

    AuthenticationProperties.loginWithRedirect({ appState: { targetUrl: to.fullPath } })
  }

  // If the Auth0Plugin has loaded already, check the authentication state
  if (AuthenticationProperties.client && !AuthenticationState.loading) {
    return guardAction()
  }

  watch(AuthenticationState, async () => {
    if (AuthenticationProperties.client && !AuthenticationState.loading) {
      return guardAction()
    }
  })
}
