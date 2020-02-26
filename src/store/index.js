import Vue from 'vue'
import Vuex from 'vuex'
import actions from './action'
import mutations from './mutations'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    mobile:'',    //用户名
    token:'',       //token
    searchlist:[],  //搜索结果
    cartList: [],   // 购物车列表
    userInfo: null, // 用户信息
    list: [],
    cart:[]
  },
  mutations,
  actions
})
