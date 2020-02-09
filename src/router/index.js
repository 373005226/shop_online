import Vue from 'vue'
import VueRouter from 'vue-router'
const Home =()=>import('../views/Home.vue')
const detail =()=>import('../views/detail')
const search =()=>import('../views/search')
const cart =()=>import('../views/cart')
const login =()=>import('../views/login')
const register =()=>import('../views/register')
const user =()=>import('../views/User/User')
const MsgCenter =()=>import('../views/User/MsgCenter')
const address =()=>import('../views/User/Address')
const UserCollection =()=>import('../views/User/UserCollection')
const UserOrder =()=>import('../views/User/UserOrder')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/detail',
    name:'商品详情',
    component:detail
  },
  {
    path:'/search',
    name:'搜索',
    component:search
  },
  {
    path:'/cart',
    name:'购物车',
    component: cart
  },
  {
    path:'/login',
    name:'login',
    component:login
  },
  {
    path:'/register',
    name:'register',
    component:register
  },
  {
    path:'/user',
    name:'user',
    component:user
  },
  {
    path:'/msgCenter',
    name:'msgCenter',
    component:MsgCenter
  },
  {
    path:'/address',
    name:'address',
    component:address
  },
  {
    path:'/userCollection',
    name:'userCollection',
    component:UserCollection
  },
  { path: '/userOrder',
    name: 'userOrder',
    component:UserOrder
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
