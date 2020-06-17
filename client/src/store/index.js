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
    list: [],
    cart:[],
    userInfo: JSON.parse(window.localStorage.getItem('userInfo')) || {},
  },
  getters:{
    gettoken(state){
      return state.token
    },
    getmobile(state){
      return state.mobile
    },
    getusername(state){
    return state.userInfo
  }
  },
  mutations,
  actions
})
