import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchList:[
      {id:0,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
      {id:1,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
      {id:2,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
      {id:3,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
      {id:4,img:'https://yanxuan-item.nosdn.127.net/8abef0cae05a3b25767d50ad94c6937a.png?quality=95&thumbnail=245x245&imageView',name:'皮毛一体后包男/女家居拖鞋',price:'239'},
    ],
    addressList:[
      {user_name:'景冰川',province:'山西省',city:'太原市',area:'小店区',detailed:'test',user_phone:'1388888888',isDefault:true},
      {user_name:'景冰川',province:'山西省',city:'太原市',area:'小店区',detailed:'test',user_phone:'1388888888',isDefault:false},
      {user_name:'景冰川',province:'山西省',city:'太原市',area:'小店区',detailed:'test',user_phone:'1388888888',isDefault:false},
    ]
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
