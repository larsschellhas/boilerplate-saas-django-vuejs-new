import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import(/* webpackChunkName: "Home" */ '../views/HomeView.vue'),
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/',
    name: 'DashboardView',
    component: () => import(/* webpackChunkName: "Dashboard" */ '../views/DashboardView.vue'),
    meta: {
      allowAnonymous: false
    }
  },
  {
    path: '/settings/:category',
    name: 'SettingsView',
    props: true,
    component: () => import(/* webpackChunkName: "Settings" */ '../views/SettingsView.vue'),
    meta: {
      allowAnonymous: false
    }
  },
  {
    path: '/login/',
    name: 'LoginView',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login/LoginView.vue'),
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/register/',
    name: 'RegisterView',
    component: () => import(/* webpackChunkName: "register" */ '../views/Login/RegisterView.vue'),
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/login/reset/',
    name: 'ResetPasswordView',
    component: () => import(/* webpackChunkName: "register" */ '../views/Login/ResetPasswordView.vue'),
    props: route => ({ token: route.query.token }),
    meta: {
      allowAnonymous: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (!to.meta.allowAnonymous && !store.getters['user/isLoggedIn']) {
    next({
      name: 'LoginView',
      query: { redirect: to.fullPath }
    })
  } else if (to.meta.allowAnonymous && store.getters['user/isLoggedIn']) {
    next({
      name: 'DashboardView'
    })
  } else {
    next()
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
