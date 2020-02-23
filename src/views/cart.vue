<template>
  <div>
    <my-header></my-header>
    <div class="cart">
      <div class="row">
        <div class="cartHead">
          <div class="checkbox">
          </div>
          <div class="goodInfo">商品信息</div>
          <div class="price">单价</div>
          <div class="number">数量</div>
          <div class="total">小计</div>
          <div class="sets">操作</div>
        </div>
        <div class="cartMain">
          <div class="item" v-for="(item,index) in productList" :key="index">
            <div class="checkout">
              <input type="checkbox" @click="clickchange(item)" v-model="item.selected">
            </div>
            <div class="goodInfo">
              <router-link :to="'/detail?id='+item.goods.id">
                <div class="pic">
                  <img :src="item.goods.images[0].image"
                       v-if="item.goods.images !== undefined &&  item.goods.images.length > 0 ">
                </div>
                <div class="nameCon">
                  {{item.goods.name}}
                  <div class="type">{{item.goods.specification[0].specification_text}}</div>
                </div>
              </router-link>
            </div>
            <div class="price" v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">
              ¥{{item.goods.specification[0].shop_price}}
            </div>

            <div class="number">
              <el-input-number v-model="item.nums" :min="1" :max="item.goods.goods_num" label="描述文字"
                               size="mini"></el-input-number>
            </div>
            <div class="total">
              ¥{{item.goods.specification[0].shop_price*item.nums}}
            </div>
            <div class="sets">
              <el-row>
                <el-button type="danger" size="mini" plain class="sets_button">移除</el-button>
              </el-row>
            </div>
          </div>
        </div>
        <div class="cart-total">
          <div class="w-chkbox">
            <input type="checkbox" @click="checkedAll" v-model="checkedAllFlag">
            <span>全选</span>
          </div>
          <div class="textInfo">
            <div class="leftInfo">
              <div class="itemsPrice">
                <div class="linetext">
                  <span>商品合计 : </span>
                  <span>¥{{total}}</span>
                </div>
                <div class="linetext">
                  <span>已优惠 :  </span>
                  <span>-¥0.00</span>
                </div>
              </div>
            </div>
            <div class="rightInfo">
              <div class="shouldPayMoney">
                <span>应付总额：</span>
                <span>¥ {{alltotal}}</span>
              </div>
            </div>
          </div>
          <div class="info">
            <button @click="toorder">下单</button>
          </div>
        </div>
      </div>
    </div>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import {getcart,putcart} from '@/api/index'

  export default {
    name: "cart",
    components: {
      MyHeader,
      MyFooter
    },
    data() {
      return {
        totalMoney: 0,
        productList: [],
        checkedAllFlag: false
      }
    },
    computed: {
      total() {
        let total = 0
        for (let i of this.productList) {
          // console.log(i)
          if (i.selected == true){
            total += i.nums * i.goods.specification[0].shop_price
          }
        }
        return total
      },
      alltotal() {
        return this.total
      }
    },
    methods: {
      clickchange(item){
        console.log(item)
        putcart(item.goods.id,{
          nums:item.nums,
          goods:item.goods.id,
          selected:!item.selected
        },{
          headers: {
            Authorization: 'JWT '+localStorage.getItem('token')
          }
        }).then(res=>{
          console.log(res)
        })
      },
      // 数量减
      numReduce() {
        if (this.number <= 1) {
          this.number = 1
          return
        }
        this.number--
      },
      toorder() {
        // this.$router.push({
        //   path: '/order'
        // })
      },
      checkedAll() {
        console.log(this)
        if(this.checkedAllFlag === false){
          for(let i of this.productList){
            console.log(i)
            putcart(i.goods.id,{
              nums:i.nums,
              goods:i.goods.id,
              selected:true
            },{
              headers: {
                Authorization: 'JWT '+localStorage.getItem('token')
              }
            }).then(res=>{
              console.log(res)
            })
          }
        }else{
          for(let i of this.productList){
            // i.selected = true
            putcart(i.goods.id,{
              nums:i.nums,
              goods:i.goods.id,
              selected:false
            },{
              headers: {
                Authorization: 'JWT '+localStorage.getItem('token')
              }
            }).then(res=>{
              console.log(res)
            })
          }
        }
      }
    },
    created() {
      getcart({
        headers: {
          Authorization: 'JWT ' + localStorage.getItem('token')
        }
      }).then(res => {
        console.log(res)
        let len = 0
        for (let i of res) {
          if (i.selected == true) {
            len++
          }
        }
        if (len == res.length) {
          this.checkedAllFlag = true
          console.log('全选了')
        } else {
          console.log('没有全选')
          this.checkedAllFlag = false
        }
        this.productList = res
      })
      // this.productList = this.$store.state.cart
      // console.log(this.productList)
    }
  }
</script>

<style scoped lang="scss">
  .row {
    width: 1220px;
  }

  .sets_button {
    width: 75px;
  }

  .click:hover {
    color: #9AD7FD;
    cursor: pointer;
  }

  .cart {
    padding: 20px 0 0;

    .cartHead {
      display: flex;
      text-align: center;
      border: 1px solid #ddd;

      div {
        padding: 12px 0;
        background-color: #f5f5f5;
      }

      .checkbox {
        width: 138px;
        display: flex;
        align-items: center;
        justify-content: center;

        input {
          width: 18px;
          height: 18px;
          vertical-align: middle !important;
        }

        .all {
          margin-left: 20px;
        }
      }

      .goodInfo {
        width: 300px;
        text-align: left;
        padding-left: 20px;
      }

      .price {
        width: 230px;
      }

      .number {
        width: 120px
      }

      .total {
        width: 195px;
      }

      .sets {
        width: 235px
      }
    }

    .cartMain {
      border: 1px solid #ddd;
      padding-left: 20px;

      .item {
        padding: 20px 0;
        display: flex;
        align-items: center;
        border-bottom: 1px dashed #eaeaea;

        &:last-child {
          border: none;
        }

        .checkout {
          text-align: center;
          position: relative;
          color: #999;
          width: 60px;

          input {
            display: inline-block;
            width: 18px;
            height: 18px;
          }
        }

        .goodInfo {
          display: flex;

          .pic {
            top: 50%;
            float: left;
            height: 100px;
            width: 100px;
            border: 1px solid #eaeaea;

            img {
              width: 100%;
              height: 100%;
              background-color: #f4f4f4;
            }
          }

          .nameCon {
            margin-left: 15px;
            font-size: 14px;
            padding-top: 10px;
            text-align: left;
            width: 300px;
            min-height: 100px;
            float: left;
            line-height: 1;

            .type {
              color: #999;
              margin-top: 10px;
            }
          }
        }

        .price {
          width: 155px;
          /*text-align: center;*/
          padding: 36px;
          position: relative;
          color: #999;
        }

        .number {
          width: 170px;
          display: flex;
          align-items: center;
          justify-content: center;

          span, input {
            display: inline-block;
            width: 24px;
            height: 24px;
            line-height: 22px;
            border: 1px solid #ddd;
            text-align: center;
            line-height: 24px;
            box-sizing: border-box;
            outline: none;
          }

          input {
            display: inline-block;
            width: 80px;
          }
        }

        .total {
          text-align: center;

          position: relative;
          color: #999;
          width: 150px;
        }

        .sets {
          /*position: relative;*/
          /*color: #999;*/
          text-align: center;
          width: 235px;
          padding-left: 75px;
        }
      }
    }

    .cart-total {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: 20px 0;
      font-size: 14px;
      position: relative;
      background-color: #f5f5f5;
      border: 1px solid #ddd;
      height: 70px;

      .w-chkbox {
        margin-left: 20px;

        input {
          width: 18px;
          height: 18px;
          vertical-align: middle !important;
        }

        span {
          margin-left: 14px;
        }

        a {
          margin-left: 30px;
        }
      }

      .textInfo {
        display: flex;
        align-content: center;

        .leftInfo {
          .itemsPrice {
            margin: 10px 0;
            padding: 0 30px;
            border-right: 1px solid #ddd;
            line-height: 14px;
            height: 50px;

            .linetext {
              display: flex;
              color: #999;
              line-height: 30px;

              span {
                &:first-child {
                  width: 80px;
                  margin-right: 20px;
                  text-align: right;
                }
              }
            }
          }
        }

        .rightInfo {
          margin-left: 20px;

          .shouldPayMoney {
            line-height: 60px;

            span {
              &:last-child {
                font-size: 22px;
                font-weight: 700;
                color: #BE4141;
              }
            }
          }
        }
      }

      .info {
        button {
          cursor: pointer;
          outline: none;
          border-radius: 0;
          width: 140px;
          height: 70px;
          margin-top: -1px;
          margin-right: -1px;
          line-height: 50px;
          font-size: 18px;
          color: #fff;
          border: 1px solid #35AFFB;
          background-color: #35AFFB;

          &:hover {
            background-color: #3A88FD;
          }
        }
      }
    }
  }
</style>

