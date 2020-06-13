import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'normalize.css/normalize.css'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Moment from 'moment'

Vue.use(ElementUI)

Vue.filter('converTime',function(data,formatStr){
    return Moment(data).format(formatStr);
});

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')


router.beforeEach((to, from, next) => {
    if(to.path === '/login'){
        next()
    }else {
        if(store.getters.gettoken==null){
            next('/login')
        }else {
            next()
        }
    }
})


