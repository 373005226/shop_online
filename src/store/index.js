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
    list: [
      {
        "productId": "600100002115",
        "productName": "黄鹤楼香烟",
        "productPrice": 19,
        "productQuantity": 1,
        "productImage": "../../static/images/goods-1.jpg",
        "parts": [
          {
            "partsId": "10001",
            "partsName": "打火机",
            "imgSrc": "../../static/images/part-1.jpg"
          }
        ]
      },
      {
        "productId": "600100002120",
        "productName": "加多宝",
        "productPrice": 8,
        "productQuantity": 5,
        "productImage": "../../static/images/goods-2.jpg",
        "parts": [
          {
            "partsId": "20001",
            "partsName": "吸管",
            "imgSrc": "../../static/images/part-2.jpg"
          }
        ]
      },
      {
        "productId": "600100002117",
        "productName": "金装黄鹤楼",
        "productPrice": 25,
        "productQuantity": 2,
        "productImage": "../../static/images/goods-1.jpg",
        "parts": [
          {
            "partsId": "10001",
            "partsName": "黄金打火机",
            "imgSrc": "../../static/images/part-1.jpg"
          },
          {
            "partsId": "10002",
            "partsName": "钻石打火机",
            "imgSrc": "../../static/images/part-1.jpg"
          }
        ]
      }
    ],
    cart:[
      {
        id:1,
        name:'奥利奥',
        img:'https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200223155448.jpg',
        nums:1,
        goods_num:98,
        selected:true,
        specification:[
          {
            specification_text: "3斤",
            shop_price: 54.0,
            promotion_price: null,
          }
        ]
      },
      {
        id:2,
        name:'达利园蛋糕',
        img:'https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200223160703.jpg',
        nums:2,
        goods_num:16,
        selected:false,
        specification:[
          {
            specification_text: "1斤",
            shop_price: 16.0,
            promotion_price: null,
          }
        ]
      }
    ]
  },
  mutations,
  actions
})
