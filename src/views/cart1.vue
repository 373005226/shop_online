<template>
  <div>
    <my-header></my-header>
    <div>
      <ol class="step" style="cursor: pointer">
        <li :class="{active:active1}" @click="activef">
          <i class="step-icon">1</i>
          查看订单
        </li>
        <li :class="{active:active2}" @click="activel">
          <i class="step-icon">2</i>
          付款
        </li>
      </ol>
    </div>
    <div class="main">
      <div class="title">填写并核对订单信息</div>
      <div class="content">

        <div class="methods">
          <div class="content_title">
            <div style="padding-left: 10px;">配送方式</div>
          </div>
          <div style="display: flex;flex-direction: row;padding-left: 10px;padding-top: 10px;cursor: pointer; ">
            <div class="method"  @click="shippingMethod = 1" :class="{'activemethods': shippingMethod === 1}">线下自提</div>
            <div style="margin-left: 10px;" class="method" :class="{'activemethods': shippingMethod === 2}"
                 @click="shippingMethod = 2">线上送货
            </div>
          </div>
        </div>


        <div class="methods" v-if="this.shippingMethod===1">
          <div class="content_title">
            <div style="padding-left: 10px;">收货地址</div>
            <div style="padding-left: 10px;font-weight: normal;color: #3A88FD">[修改]</div>
          </div>
          <div class="methods_content">
            <div>15918891965</div>
            <div>刘生</div>
            <div> 广东省-广州市-从化区-广州大学华软软件学院
            </div>
          </div>
        </div>



        <div class="methods" v-if="this.shippingMethod===1">
          <div class="content_title">
            <div style="padding-left: 10px;">收货时间</div>
          </div>
          <div class="methods_content">
            <el-date-picker
              v-model="value"
              type="datetime"
              placeholder="选择日期时间"
              default-time="12:00:00">
            </el-date-picker>
          </div>
        </div>


        <div class="methods" v-if="this.shippingMethod===2">
          <div class="content_title">
            <div style="padding-left: 10px;">请选择您的自提时间</div>
          </div>
          <div class="methods_content">
            <el-date-picker
              v-model="value"
              type="datetime"
              placeholder="选择日期时间"
              default-time="12:00:00">
            </el-date-picker>
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

<!--        <div>-->
<!--          <div class="content_title">-->
<!--            <div style="padding-left: 10px;">物品清单</div>-->
<!--          </div>-->

<!--          <div class="cart">-->
<!--            <div class="row">-->
<!--              <div class="cartHead">-->
<!--                <div class="checkbox">-->
<!--                </div>-->
<!--                <div class="goodInfo">商品信息</div>-->
<!--                <div class="price">单价</div>-->
<!--                <div class="number">数量</div>-->
<!--                <div class="total">小计</div>-->
<!--                <div class="sets">操作</div>-->
<!--              </div>-->
<!--              <div class="cartMain">-->
<!--                <div class="item" v-for="(item,index) in productList" :key="index">-->
<!--                  <div class="checkout">-->
<!--                    <input type="checkbox" @click="clickchange(item)" v-model="item.selected" :checked="item.selected">-->
<!--                  </div>-->
<!--                  <div class="goodInfo">-->
<!--                    <router-link :to="'/detail?id='+item.goods.id">-->
<!--                      <div class="pic">-->
<!--                        <img :src="item.goods.images[0].image"-->
<!--                             v-if="item.goods.images !== undefined &&  item.goods.images.length > 0 ">-->
<!--                      </div>-->
<!--                      <div class="nameCon">-->
<!--                        {{item.goods.name}}-->
<!--                        <div class="type">{{item.goods.specification[0].specification_text}}</div>-->
<!--                      </div>-->
<!--                    </router-link>-->
<!--                  </div>-->
<!--                  <div class="price"-->
<!--                       v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">-->
<!--                    ¥{{item.goods.specification[0].shop_price}}-->
<!--                  </div>-->

<!--                  <div class="number">-->
<!--                    <el-input-number v-model="item.nums" :min="1" :max="item.goods.goods_num" label="描述文字"-->
<!--                                     size="mini"></el-input-number>-->
<!--                  </div>-->
<!--                  <div class="total">-->
<!--                    ¥{{item.goods.specification[0].shop_price*item.nums}}-->
<!--                  </div>-->
<!--                  <div class="sets">-->
<!--                    <el-row>-->
<!--                      <el-button type="danger" size="mini" plain class="sets_button" @click="delccart(item.goods.id)">移除-->
<!--                      </el-button>-->
<!--                    </el-row>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="cart-total">-->
<!--                <div class="w-chkbox">-->
<!--                  &lt;!&ndash;                  <input type="checkbox">&ndash;&gt;-->
<!--                  &lt;!&ndash;                  <span>全选</span>&ndash;&gt;-->
<!--                </div>-->
<!--                <div class="textInfo">-->
<!--                  <div class="leftInfo">-->
<!--                    &lt;!&ndash;                    <div class="itemsPrice">&ndash;&gt;-->
<!--                    &lt;!&ndash;                      <div class="linetext">&ndash;&gt;-->
<!--                    &lt;!&ndash;                        <span>商品合计 : </span>&ndash;&gt;-->
<!--                    &lt;!&ndash;                        <span>¥{{total}}</span>&ndash;&gt;-->
<!--                    &lt;!&ndash;                      </div>&ndash;&gt;-->
<!--                    &lt;!&ndash;                      <div class="linetext">&ndash;&gt;-->
<!--                    &lt;!&ndash;                        <span>已优惠 :  </span>&ndash;&gt;-->
<!--                    &lt;!&ndash;                        <span>-¥0.00</span>&ndash;&gt;-->
<!--                    &lt;!&ndash;                      </div>&ndash;&gt;-->
<!--                    &lt;!&ndash;                    </div>&ndash;&gt;-->
<!--                  </div>-->
<!--                  <div class="rightInfo">-->
<!--                    <div class="shouldPayMoney">-->
<!--                      &lt;!&ndash;                      <span>应付总额：</span>&ndash;&gt;-->
<!--                      &lt;!&ndash;                      <span>¥ {{alltotal}}</span>&ndash;&gt;-->
<!--                    </div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="info">-->
<!--                  <button @click="toorder">下单</button>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->

<!--        </div>-->

      </div>
    </div>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";

  export default {
    name: "cart1",
    components: {MyFooter, MyHeader},
    data() {
      return {
        currentAddress: 0,
        shippingMethod: 1,
        value: '',
        active1: true,
        active2: false,
      }
    },
    methods:{
      activef(){
        this.active1 = true
        this.active2 = false
      },
      activel(){
        this.active1 = false
        this.active2 = true
      }
    }
  }
</script>

<style scoped lang="less">
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
</style>
