import Vue from 'vue'
import VueRouter from 'vue-router'
const Home =()=>import('../views/Home.vue')
const detail =()=>import('../views/detail')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/detail',
    name:'detail',
    component:detail
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
