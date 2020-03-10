<template>
  <div>
    <my-header></my-header>
    <div>
      <ol class="step" style="cursor: pointer;">
        <li :class="{active:active1}" @click="activef">
          <i class="step-icon">1</i>
          查看购物车
        </li>
        <li :class="{active:active2}" @click="activel">
          <i class="step-icon">2</i>
          付款
        </li>
      </ol>
    </div>


    <div v-if="active1== true">

      <div class="cart" v-if="productList.length!=0">
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
                <input type="checkbox" @click="clickchange(item)" :checked="ischeck">
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
              <div class="price"
                   v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">
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
                  <el-button type="danger" size="mini" plain class="sets_button" @click="delccart(item.goods.id)">移除
                  </el-button>
                </el-row>
              </div>
            </div>

            <div class="item" v-for="(item,index) in productList" :key="index">
              <div class="checkout">
<!--                <input type="checkbox" @click="clickchange(item)" :checked="ischeck">-->
              </div>

              <div class="goodInfo">
                  <div class="pic">
                    <img src="http://127.0.0.1:8000/media/goods/integralgoods/b188d2be3cad0ab4.jpg"
                        >
                  </div>
                  <div class="nameCon">
                    <span style="color: #F56C6C">[积分赠品]</span>黑人牙膏
                    <div class="type">1支</div>
                  </div>
              </div>

            </div>
          </div>
          <div class="cart-total">
            <div class="w-chkbox">
              <input type="checkbox" :checked="true">
              <span>全选</span>
            </div>
            <div class="textInfo">
              <div class="leftInfo">
                <div class="itemsPrice">
                  <div class="linetext">
                    <!--                  <span>商品合计 : </span>-->

                    <!--                  <span>¥{{total}}</span>-->
                  </div>
                  <!--                <div class="linetext">-->
                  <!--                  <span>已优惠 :  </span>-->
                  <!--                  <span>-¥0.00</span>-->
                  <!--                </div>-->
                </div>
              </div>
              <div class="rightInfo">
                <div class="shouldPayMoney">
                  <!--                <span>应付总额：</span>-->
                  <!--                <span>¥ {{alltotal}}</span>-->
                </div>
              </div>
            </div>
            <div class="info">
              <button @click="tonext">下一步</button>
            </div>
          </div>
        </div>
      </div>


      <div v-else style="width: 1220px;margin: 0 auto;padding-bottom: 20px;">
        <div style="text-align: center;">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200307101617.png">
        </div>
      </div>
    </div>


    <div v-if="active2 == true">
      <el-form :model="orderform">

        <div class="main">
          <div class="title">填写并核对订单信息</div>
          <div class="content">

            <div class="methods">
              <div class="content_title">
                <div style="padding-left: 10px;">配送方式</div>
              </div>
              <div style="display: flex;flex-direction: row;padding-left: 10px;padding-top: 10px;cursor: pointer; ">
                <div class="method" @click="online" :class="{'activemethods': shippingMethod === 1}">
                  线上送货
                </div>
                <div style="margin-left: 10px;" class="method" :class="{'activemethods': shippingMethod === 2}"
                     @click="self_men">线下自提
                </div>
              </div>
            </div>


            <div class="methods" style="cursor: pointer" v-if="this.shippingMethod===1">
              <div class="content_title">
                <div style="padding-left: 10px;">收货地址</div>
                <div style="padding-left: 10px;font-weight: normal;color: #3A88FD">[修改]</div>
              </div>

              <div style="display: flex;flex-direction: row;">
                <div class="methods_content" v-for="(item,index) in alladdress" :key="index">
                  <div style="width: 300px;" :class="{'addressactive':addressselect[item.id]}"
                       @click="selectaddress(item)">
                    <div>{{item.signer_mobile}}</div>
                    <div>{{item.signer_name}}</div>
                    <div> {{item.province}}-{{item.city}}-{{item.district}}-{{item.address}}
                    </div>
                  </div>
                </div>
              </div>
            </div>


            <div class="methods" v-if="this.shippingMethod===1">
              <div class="content_title">
                <div style="padding-left: 10px;">收货时间</div>
              </div>
              <div class="methods_content">

                <el-time-select
                  v-model="orderform.time"
                  :picker-options="{
    start: starttime,
    step: '00:15',
    end: '19:00'
  }"
                  placeholder="选择时间">
                </el-time-select>
              </div>
            </div>


            <div class="methods" v-if="this.shippingMethod===2">
              <div class="content_title">
                <div style="padding-left: 10px;">请选择您的自提时间</div>
              </div>
              <div class="methods_content">
                <el-time-select
                  v-model="orderform.time"
                  :picker-options="{
    start: starttime,
    step: '00:15',
    end: '21:00'
  }"
                  placeholder="选择时间">
                </el-time-select>
              </div>
            </div>

            <div class="methods">
              <div class="content_title">
                <div style="padding-left: 10px;">支付方式</div>
              </div>
              <div class="methods_content">
                <div
                  style="border: 2px solid #EE7A23;width: 120px;height: 60px;display: flex;flex-direction: row;padding-left: 5px;">
                  <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200307011420.png"
                       style="width: 40px;height: 40px">
                  <span style="padding-top: 10px;padding-left: 5px">支付宝</span>
                </div>
              </div>
            </div>

            <div class="cart" v-if="productList.length!=0">
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
                      <!--                    <input type="checkbox" @click="clickchange(item)">-->
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
                    <div class="price"
                         v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">
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
                        <el-button type="danger" size="mini" plain class="sets_button" @click="delccart(item.goods.id)">
                          移除
                        </el-button>
                      </el-row>
                    </div>
                  </div>
                </div>
                <div class="cart-total">
                  <div class="w-chkbox">
                    <!--                  <input type="checkbox">-->
                    <!--                  <span>全选</span>-->
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
                    <button @click="toorder" type="button">下单</button>
                  </div>
                </div>
              </div>
            </div>


          </div>
        </div>
      </el-form>
    </div>
    <my-footer></my-footer>

  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import {getcart, deletecart, getuseraddress, postorder} from '@/api/index'
  import {putcart} from "../api";

  export default {
    name: "cart",
    components: {
      MyHeader,
      MyFooter
    },
    data() {
      return {
        value: '',
        isallcheck: false,
        is_show1: true,
        is_show2: false,
        active1: true,
        active2: false,
        addressselect: [],
        currentAddress: 0,
        shippingMethod: 1,
        payingMethod: 1,
        totalMoney: 0,
        productList: [],
        checkedAllFlag: false,
        starttime:'',
        alladdress: [],
        orderform: {
          methods: '',
          address: [],
          time: ''
        },
      }
    },
    computed: {
      total() {
        let total = 0
        for (let i of this.productList) {
          total += i.nums * i.goods.specification[0].shop_price
        }
        return total
      },
      alltotal() {
        if (this.shippingMethod == 1) {
          return this.total + 10
        } else {
          return this.total
        }
      }
    },
    methods: {
      selectaddress(item) {
        this.addressselect[item.id] = true
        console.log(item)
        console.log(this.addressselect[item.id])
        this.orderform.address = item
      },
      online() {
        this.shippingMethod = 1
        this.orderform.methods = 'online'
      },
      self_men() {
        this.shippingMethod = 2
        this.orderform.methods = 'self_mention'
      },
      activef() {
        this.active1 = true
        this.active2 = false
      },
      activel() {
        this.active1 = false
        this.active2 = true
      },
      checkbox() {
        if (this.isallcheck == true) {
          this.ischeck = true
        }
      },
      ischeck() {
        return false
      },
      clickchange(item) {
        console.log(item)
        putcart(item.goods.id, {
          nums: item.nums,
          goods: item.goods.id,
          selected: !item.selected
        }, {
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
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
      tonext() {
        this.active2 = true
        this.active1 = false
      },
      totext() {
        console.log(this.orderform)
        console.log(this.orderform.time)
        console.log(this.orderform.address.province +'-'+this.orderform.address.city +'-'+this.orderform.address.district +'-' +this.orderform.address.address)
      },
      toorder() {
        postorder({
          pay_status: 'paying',
          order_mount: this.alltotal,
          gettime:this.orderform.time,
          takegoods_status: this.orderform.methods,
          address: this.orderform.address.province +'-'+this.orderform.address.city +'-'+this.orderform.address.district +'-' +this.orderform.address.address ,
          signer_name: this.orderform.signer_name,
          singer_mobile: this.orderform.address.signer_mobile
        }, {
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          console.log(res)
          window.location.href = res.alipay_url
        })
      },
      delccart(id) {
        console.log(id)
        deletecart(id, {
          headers: {Authorization: 'JWT ' + localStorage.getItem('token')}
        }).then(res => {
          console.log(res)
          location.reload()
        })
      },
    },


    created() {
      this.orderform.methods = 'online'
      let myDate = new Date()
      let house = myDate.getHours()+1
      let minutes = myDate.getMinutes()
      this.starttime =house +':'+minutes
      console.log(this.starttime)

      if(this.starttime>'19:00'){
        console.log('error')
        this.$message.error('时间已经超过19:00，不能继续下单')
      }else {
        console.log('succsess')
        this.$message({
          message: '正在营业时间范围内，可以继续访问',
          type: 'success'
        });
      }

      this.orderform.time = this.starttime


      getuseraddress({
        headers: {
          Authorization: 'JWT ' + localStorage.getItem('token')
        }
      }).then(res => {
        console.log(res)
        this.alladdress = res
        this.addressselect[res[0].id] = true
        this.orderform.address = res[0]
      })

      getcart({
        headers: {
          Authorization: 'JWT ' + localStorage.getItem('token')
        }
      }).then(res => {
        console.log(res)
        this.productList = res

      })
      // this.productList = this.$store.state.cart
      // console.log(this.productList)
    }
  }
</script>

<style scoped lang="scss">
  .addressactive {
    border: 2px solid #E36844;
    padding-bottom: 10px;
    padding-left: 10px;
  }

  .step {
    width: 990px;
    color: #999;
    margin: 0 auto;
    margin-top: 20px;
    font-size: 0;
    text-align: center;
    margin-bottom: 50px;
    border-bottom: 2px solid #e6e6e6;

    .active {
      color: #3e3e3e;
      margin-bottom: -1px;
      border-bottom: 2px solid #c40000;

      .step-icon {
        background: url("../assets/img/step_active.png") no-repeat;
        display: inline-block;
        width: 24px;
        height: 24px;
        font-size: 14px;
        text-align: center;
        line-height: 24px;
        color: #fff;
      }
    }

    li {
      display: inline-block;
      width: 180px;
      height: 46px;
      padding-left: 30px;
      line-height: 46px;
      font-size: 16px;
      font-weight: 700;
      font-family: "微软雅黑", "华文细黑", arial;
    }
  }

  .main {
    border: 5px solid #FAF6F7;
    /*height: 1200px;*/
    width: 1220px;
    margin: 20px auto;

    .title {
      background: #FAF6F7;
      padding-left: 10px;
      padding-top: 10px;
      padding-bottom: 10px;
      font-weight: bold;
      color: #999999;
    }

    .content {
      padding-top: 10px;
      padding-bottom: 10px;

      .methods {
        border-bottom: 10px solid #FAF6F7;
        padding-bottom: 20px;
      }


      .methods_content {
        padding-left: 10px;
        padding-top: 20px;

        div {
          padding-top: 10px;
        }
      }

      .content_title {
        color: #666666;
        font-weight: bold;
        display: flex;
        flex-direction: row;
        padding-top: 20px;
      }
    }

  }

  .method {
    padding: 5px;
  }

  .activemethods {
    border: 2px solid #EE7A23;
  }

  .checkout-title {
    position: relative;
    /*margin-bottom: 41px;*/
    text-align: center;
    width: 1220px;
    margin: 20px auto;

    span {
      position: relative;
      padding: 0 1em;
      background-color: #fff;
      font-family: "moderat", sans-serif;
      font-weight: bold;
      font-size: 20px;
      color: #605F5F;
      z-index: 1;
    }
  }

  .checkout-title:before {
    position: absolute;
    top: 50%;
    left: 0;
    content: "";
    width: 100%;
    height: 1px;
    background: #ccc;
    z-index: 0;
  }

  .addr-list-wrap {
    min-height: 300px;
    width: 1220px;
    margin: 0 auto;
    border: 1px solid #999999;
    padding-left: 30px;
    padding-top: 30px;
    margin-top: 30px;
  }

  .addr-list ul:after {
    visibility: hidden;
    display: block;
    content: " ";
    clear: both;
  }

  .addr-list li {
    position: relative;
    float: left;
    width: 23.5%;
    height: 162px;
    margin: 10px 2% 10px 0;
    padding: 20px 20px 40px 20px;
    background: #fff;
    border: 2px solid #e9e9e9;
    overflow: hidden;
    cursor: pointer;
  }

  .addr-list li dt {
    margin-bottom: 10px;
    font-size: 18px;
  }

  .addr-list li dd {
    margin-bottom: 6px;
    line-height: 20px;
  }

  .addr-list li .address {
    height: 40px;
    overflow: hidden;
  }

  .addr-list li .tel {
    color: #605F5F;
  }

  .addr-list li .addr-opration {
    position: absolute;
  }

  .addr-list li .addr-opration .icon {
    width: 100%;
    height: 100%;
  }

  .addr-list li .addr-opration:hover .icon {
    fill: #EE7A23;
  }

  .addr-list li .addr-edit {
    display: none;
    top: 20px;
    right: 20px;
    width: 20px;
    height: 20px;
  }

  .addr-list li .addr-del {
    display: none;
    bottom: 20px;
    right: 20px;
    width: 20px;
    height: 20px;
  }

  .addr-list li .addr-set-default, .addr-list li .addr-default {
    bottom: 15px;
    left: 20px;
    color: #EE7A23;
  }

  .addr-list li .addr-set-default {
    display: none;
  }

  .addr-list li:nth-child(4n) {
    margin-right: 0;
  }

  .addr-list li:hover {
    border-color: #EE7A23;
  }

  .addr-list li.addr-new {
    color: #333;
    text-align: center;
  }

  .addr-list li.addr-new .add-new-inner {
    padding-top: 20px;
  }

  .addr-list li.addr-new .add-new-inner .icon-add {
    display: inline-block;
    width: 50px;
    height: 50px;
  }

  .addr-list li.addr-new .add-new-inner .icon-add .icon-add {
    width: 50px;
    height: 50px;
    fill: #605F5F;
  }

  .addr-list li.addr-new .add-new-inner p {
    margin-top: 10px;
  }

  .addr-list li.check {
    border-color: #EE7A23;
    border-width: 2px;
  }

  .addr-list li.check .addr-opration {
    display: block;
  }

  .shipping-method-wrap {
    padding-bottom: 65px;
  }

  .shipping-method {
    text-align: center;
  }

  .shipping-method li {
    display: inline-block;
    width: 300px;
    margin: 5px;
    padding: 10px;
    background: #fff;
    border: 2px solid #e9e9e9;
    font-size: 18px;
    line-height: 26px;
    text-align: center;
    color: #999;
    font-family: "Moderat";
    cursor: pointer;
  }

  .shipping-method li img {
    width: 50px;
    height: 50px;
  }

  .shipping-method li .price {
    font-weight: bold;
  }

  .shipping-method li.check {
    border-color: #EE7A23;
    color: #333;
  }


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



