import Vue from 'vue'
import VueRouter from 'vue-router'
const Home =()=>import('../views/Home.vue')
const detail =()=>import('../views/detail')
const search =()=>import('../views/search')
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
  },
  {
    path:'/search',
    name:'search',
    component:search
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
