<template>
  <div>
    <my-header></my-header>
    <div>
      <ol class="step">
        <li :class="{active:active1}">
          <i class="step-icon">1</i>
          查看订单
        </li>
        <li :class="{active:active2}">
          <i class="step-icon">2</i>
          付款
        </li>
      </ol>
    </div>
    <el-form>

      <div class="checkout-title">
        <span>配送地址</span>
      </div>

      <div class="addr-list-wrap">
        <div class="addr-list">
          <ul>
            <li v-for="(address, index) in filterAddress" :class="{'check': index === currentAddress}" :key="index"
                @click="currentAddress = index">
              <dl>
                <dt>{{address.userName}}</dt>
                <dd class="address">{{address.streetName}}</dd>
                <dd class="tel">{{address.tel}}</dd>
              </dl>
              <div class="addr-opration addr-edit">
                <a href="javascript:;" class="addr-edit-btn">
                  <svg class="icon icon-edit">
                    <use xlink:href="#icon-edit"></use>
                  </svg>
                </a>
              </div>
              <div class="addr-opration addr-del">
                <a href="javascript:;" class="addr-del-btn">
                  <svg class="icon icon-del">
                    <use xlink:href="#icon-del"></use>
                  </svg>
                </a>
              </div>
              <div class="addr-opration addr-set-default" v-if="!address.isDefault">
                <a href="javascript:;" class="addr-set-default-btn"
                   @click="setDefault(address.addressId)"><i>设为默认</i></a>
              </div>
              <div class="addr-opration addr-default" v-if="address.isDefault">默认地址</div>
            </li>

            <li class="addr-new">
              <div class="add-new-inner">
                <i class="icon-add">
                  <i class="iconfont icon-jia">
                    <use xlink:href="#icon-add"></use>
                  </i>
                </i>
                <p>添加新地址</p>
              </div>
            </li>
          </ul>
        </div>

      </div>      <div class="checkout-title">
      <span>配送方式</span>
    </div>

      <div class="shipping-method-wrap">
        <div class="shipping-method">
          <ul>
            <li :class="{'check': shippingMethod === 1}" @click="shippingMethod = 1">
              <div class="name">送货到家</div>
              <div class="price">￥10</div>
            </li>
            <li :class="{'check': shippingMethod === 2}" @click="shippingMethod = 2">
              <div class="name">线下自提</div>
              <div class="price">￥0.0</div>
            </li>
          </ul>
        </div>
      </div>

      <div class="checkout-title">
        <span>付款方式</span>
      </div>

      <div class="shipping-method-wrap">
        <div class="shipping-method">
          <li :class="{'check': payingMethod === 1}" @click="payingMethod = 1">
            <img src="@/assets/img/ali.png">
            <div class="price">支付宝</div>
          </li>
          <li :class="{'check': payingMethod === 2}" @click="payingMethod = 2">
            <img src="@/assets/img/wechat.png">
            <div class="price">微信</div>
          </li>
        </div>
      </div>







      <div style="text-align: center;padding-bottom: 30px;">
        <el-button style="width: 550px;">提交订单</el-button>
      </div>

    </el-form>


    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";

  export default {
    name: "Order",
    components: {MyFooter, MyHeader},
    data() {
      return {
        is_show1: true,
        is_show2: false,
        active1: true,
        active2: false,
        currentAddress: 0,
        shippingMethod: 1,
        payingMethod: 1,
        filterAddress: [
          {
            "addressId": "100001",
            "userName": "JackBean",
            "streetName": "北京市朝阳区朝阳公园1",
            "postCode": "100001",
            "tel": "12345678901",
            "isDefault": true
          },
          {
            "addressId": "100002",
            "userName": "JackBean",
            "streetName": "北京市朝阳区朝阳公园2",
            "postCode": "100001",
            "tel": "12345678901",
            "isDefault": false
          },
        ]
      }
    }
  }
</script>

<style scoped lang="less">
  .orderform{
    margin-bottom: 50px;
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
  }

  .step li {
    display: inline-block;
    width: 180px;
    height: 46px;
    padding-left: 30px;
    line-height: 46px;
    font-size: 16px;
    font-weight: 700;
    font-family: "微软雅黑", "华文细黑", arial;
  }

  .step-icon {
    background: url("../assets/img/step.png") no-repeat;
    display: inline-block;
    width: 24px;
    height: 24px;
    font-size: 14px;
    text-align: center;
    line-height: 24px;
    color: #fff;
  }

  .addr-list-wrap {
    min-height: 300px;
    width: 1220px;
    margin: 0 auto;
  }

  .checkout-title {
    position: relative;
    /*margin-bottom: 41px;*/
    text-align: center;
    width: 1220px;
    margin: 20px auto;
  }

  .checkout-title span {
    position: relative;
    padding: 0 1em;
    background-color: #fff;
    font-family: "moderat", sans-serif;
    font-weight: bold;
    font-size: 20px;
    color: #605F5F;
    z-index: 1;
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
</style>
