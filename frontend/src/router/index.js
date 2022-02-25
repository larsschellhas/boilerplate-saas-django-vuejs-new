import { createRouter, createWebHistory } from 'vue-router'
import { authenticationGuard } from './authenticationGuard'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import(/* webpackChunkName: "Home" */ '../views/HomeView.vue'),
    meta: {
      allowAnonymous: true,
      allowAuthenticated: false
    },
    beforeEnter: authenticationGuard
  },
  {
    path: '/dashboard',
    name: 'DashboardView',
    component: () => import(/* webpackChunkName: "Dashboard" */ '../views/DashboardView.vue'),
    meta: {
      allowAnonymous: false,
      allowAuthenticated: true
    },
    beforeEnter: authenticationGuard
  },
  {
    path: '/settings/:category',
    name: 'SettingsView',
    props: true,
    component: () => import(/* webpackChunkName: "Settings" */ '../views/SettingsView.vue'),
    meta: {
      allowAnonymous: false,
      allowAuthenticated: true
    },
    beforeEnter: authenticationGuard
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        left: 0,
        top: 64,
        behavior: 'smooth'
      }
    } else {
      return {
        left: 0,
        top: 0,
        behavior: 'smooth'
      }
    }
  }
})

export default router

export function pushOrReload (route) {
  if (route !== '' && route.name !== router.currentRoute.value.name && route.path !== router.currentRoute.value.path) {
    router.push(route)
  } else {
    router.go(0)
  }
}
