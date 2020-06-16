import Vue from 'vue'
import VueRouter from 'vue-router'
const Home =()=>import('../views/Home.vue')
const detail =()=>import('../views/detail')
const catelogy =()=>import('../views/catelogy')
const search =()=>import('../views/search')
const cart =()=>import('../views/cart')
const login =()=>import('../views/login')
const register =()=>import('../views/register')
const user =()=>import('../views/User/User')
const MsgCenter =()=>import('../views/User/MsgCenter')
const address =()=>import('../views/User/Address')
const UserCollection =()=>import('../views/User/UserCollection')
const UserOrder =()=>import('../views/User/UserOrder')
const Integral_mall = ()=>import('../views/Integral_mall')
const discount_mall =()=>import('../views/discount_mall')
const integral_goods =()=>import('../views/User/integral_goods')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/goods',
    name: 'goods',
    component: catelogy,
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
  {
    path:'/integral_goods',
    name:'兑换的积分商品',
    component:integral_goods
  },
  { path: '/userOrder',
    name: 'userOrder',
    component:UserOrder
  },
  {
    path:'/Integral_mall',
    name:'积分商城',
    component:Integral_mall
  },
  {
    path:'/discount_mall',
    name:'折扣商城',
    component:discount_mall
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}


export default router