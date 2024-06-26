import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'  // Add this line
import store from '../store'  // Add this line

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },

  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta :{
      requireLogin: true
    }
  },
  
  {
  path: '/dashboard/my-account',
  name: 'MyAccount',
  component: MyAccount,
  meta :{
    requireLogin: true
  }
}

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin)) {
    if (!store.state.isAuthenticated) {
      next({ name: 'LogIn' })
    } else {
      next()
    }
  } else {
    next()
  }
})
export default router
