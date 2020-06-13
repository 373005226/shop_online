import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/login/index'
import Layout from "../views/layout/layout";
import NotFound from '../views/error/error'

//以下都是要懒加载的数据
const HomeMain = () => import('../views/home/mainIndex')
const order = () => import('../views/order/order')
const order_question = () => import('../views/order/order_question')
const task = () => import('../views/task/task')
const ctask = () => import('../views/task/ctask')
const sales_table = () => import('../views/sales_char/sales_table')
const comment = () => import('../views/comment/comment')
const article = () => import('../views/article/article')
const userInfo = () => import('../views/User/userinfo')
const distributer =()=>import('../views/distributer/distributer')
const cdistributer =()=>import('../views/distributer/cdistributer')


Vue.use(VueRouter)

let routes = [
    {
        path: '/',
        redirect: '/index',
        hidden: true,
        children: []
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        hidden: true,
        children: []
    },
    {
        path: '/index',
        iconCls: 'el-icon-s-home', // 图标样式class
        name: '主菜单',
        component: Layout,
        meta: {requireAuth: true,roles:['order_distributor','shop_inspector','manager','boss']},
        alone: true,
        children: [
            {
                path: '/index',
                iconCls: 'el-icon-s-home', // 图标样式class
                name: '主页',
                component: HomeMain,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-tickets', // 图标样式class
        name: '任务',
        component: Layout,
        meta: {requireAuth: true, roles: ['shop_inspector', 'manager','boss']},
        children: [
            {
                path: '/task',
                iconCls: 'el-icon-edit-outline', // 图标样式class
                name: '待验货的订单',
                component: task,
                children: []
            },
            {
                path: '/complete_order',
                iconCls: 'el-icon-edit-outline', // 图标样式class
                name: '待提取的订单',
                component: ctask,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-tickets', // 图标样式class
        name: '待分配订单',
        component: Layout,
        meta: {requireAuth: true, roles: ['order_distributor', 'manager']},
        children: [
            {
                path: '/distributer',
                iconCls: 'el-icon-edit-outline', // 图标样式class
                name: '待分配的订单',
                component: distributer,
                children: []
            },
            {
                path: '/complete_distributer',
                iconCls: 'el-icon-edit-outline', // 图标样式class
                name: '已分配的订单',
                component: cdistributer,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-s-order', // 图标样式class
        name: '订单',
        component: Layout,
        meta: {requireAuth: true, roles: ['shop_inspector','order_distributor', 'manager','boss']},
        children: [
            {
                path: '/order_question',
                iconCls: 'fa fa-life-ring', // 图标样式class
                name: '有疑问订单',
                component: order_question,
                children: []
            },
            {
                path: '/allorder',
                iconCls: 'fa fa-life-ring', // 图标样式class
                name: '所有订单',
                component: order,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-s-order', // 图标样式class
        name: '数据销量图',
        meta: {requireAuth: true,roles:['manager','boss']},
        component: Layout,
        children: [
            {
                path: '/sales_today',
                iconCls: 'fa fa-life-ring', // 图标样式class
                name: '数据图标',
                component: sales_table,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-s-order', // 图标样式class
        name: '评论管理',
        meta: {requireAuth: true,roles:['manager','boss']},
        component: Layout,
        children: [
            {
                path: '/comment',
                iconCls: 'fa fa-life-ring', // 图标样式class
                name: '用户评论',
                component: comment,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-s-order', // 图标样式class
        name: '商品文章编辑',
        meta: {requireAuth: true,roles:['manager','boss']},
        component: Layout,
        children: [
            {
                path: '/article',
                iconCls: 'fa fa-life-ring', // 图标样式class
                name: '商品推销图',
                component: article,
                children: []
            }
        ]
    },
    {
        path: '/',
        iconCls: 'el-icon-user-solid', // 图标样式class
        name: '个人中心',
        meta: {requiresAuth: true,roles:['order_distributor','shop_inspector','manager','boss']},
        component: Layout,
        children: [
            {
                path: '/userInfo',
                iconCls: 'el-icon-user-solid', // 图标样式class
                name: '个人信息',
                component: userInfo,
                children: []
            }
        ]
    },
    {
        path: '/404',
        component: NotFound,
        name: '404',
        hidden: true,
        children: []
    }
]


const router = new VueRouter({
    routes
})

// export default new VueRouter({
//     routes: defaultRouter
// })

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

// export {defaultRouter}

export default router
