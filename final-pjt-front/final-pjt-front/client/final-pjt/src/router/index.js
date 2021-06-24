import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Community from '../views/Community.vue'
import Recommend from '../views/Recommend.vue'
import Login from '../components/Accounts/Login.vue'
import Logout from '../components/Accounts/Logout.vue'
import Signup from '../components/Accounts/Signup.vue'
import Profile from '../views/Profile.vue'
import MovieDetail from '../components/Home/MovieDetail.vue'
import ReviewForm from '../components/Review/ReviewForm.vue'
import ReviewForm2 from '../components/Review/ReviewForm2.vue'
import ReviewDetail from '../components/Review/ReviewDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: '/community',
    name: 'Community',
    component: Community

  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/movieDetail/:id',
    component: MovieDetail
  },
  {
    path: '/reviewForm/',
    name: 'reviewForm',
    component: ReviewForm
  },
  {
    path: '/reviewForm2/',
    name: 'ReviewForm2',
    component: ReviewForm2
  },
  {
    path: '/reviewDetail/:id',
    name: 'ReviewDetail',
    component: ReviewDetail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
