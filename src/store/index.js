import Vue from 'vue'
import Vuex from 'vuex'
import actions from './action'
import mutations from './mutations'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    mobile:'',    //用户名
    token:'',       //token
    cartList: [],   // 购物车列表
    userInfo: null, // 用户信息
    searchList:[
      {id:0,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
    ],              //搜索结果
    addressList:[
      // {user_name:'景冰川',province:'山西省',city:'太原市',area:'小店区',detailed:'testtesttesttesttest',user_phone:'1388888888',isDefault:true},
    ]
  },
  mutations,
  actions
})
