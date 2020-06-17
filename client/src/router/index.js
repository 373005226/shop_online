import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'home',
    component: ()=>import('../views/Home.vue'),
  },
  {
    path: '/goods',
    name: 'goods',
    component: ()=>import('../views/catelogy'),
  },
  {
    path: '/detail',
    name:'商品详情',
    component:()=>import('../views/detail')
  },
  {
    path:'/search',
    name:'搜索',
    component:()=>import('../views/search')
  },
  {
    path:'/cart',
    name:'购物车',
    component: ()=>import('../views/cart')
  },
  {
    path:'/login',
    name:'login',
    component:()=>import('../views/login')
  },
  {
    path:'/register',
    name:'register',
    component:()=>import('../views/register')
  },
  {
    path:'/user',
    name:'user',
    component:()=>import('../views/User/User')
  },
  {
    path:'/msgCenter',
    name:'msgCenter',
    component:()=>import('../views/User/MsgCenter')
  },
  {
    path:'/address',
    name:'address',
    component:()=>import('../views/User/Address')
  },
  {
    path:'/userCollection',
    name:'userCollection',
    component:()=>import('../views/User/UserCollection')
  },
  {
    path:'/integral_goods',
    name:'兑换的积分商品',
    component:()=>import('../views/User/integral_goods')
  },
  { path: '/userOrder',
    name: 'userOrder',
    component:()=>import('../views/User/UserOrder')
  },
  {
    path:'/Integral_mall',
    name:'积分商城',
    component:()=>import('../views/Integral_mall')
  },
  {
    path:'/discount_mall',
    name:'折扣商城',
    component:()=>import('../views/discount_mall')
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
