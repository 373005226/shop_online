<template>
  <div class="nav-title">
    <div style="padding-left: 260px;">
      欢迎来到小L的店，一站式线上选购平台
    </div>
    <div style="margin-left: auto;margin-right: 500px;">
      <div style="position: absolute;left: 1150px;">
        <span @mouseover="change_person(true)" @mouseout="change_person(false)">
          <img src="@/assets/img/person.png">
        </span>

        <div class="person_position" v-show="showperson">
          <div class="person_style">
            <div class="person_style_triangle">
            </div>
          </div>
        </div>

      </div>

      <div style="position:absolute;left: 1300px;">
        <span @mouseover="change_cart(true)" @mouseout="change_cart(false)">
          <img src="@/assets/img/buy.png">
          <span class="cart_nums">0</span>
        </span>

        <div class="cart_position" v-show="showcart">
          <div class="cart_style">
            <div class="cart_style_triangle">
            </div>
            <p style="padding-top: 170px;color: #999999;">购物车为空哦</p>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: "headers",
    data() {
      return {
        showcart: false,
        showperson: false
      }
    },
    methods: {
      change_cart(state) {
        this.showcart = state
      },
      change_person(state) {
        this.showperson = state
      }
    }
  }
</script>

<style scoped>
  .nav-title {
    line-height: 36px;
    width: 100%;
    /*height: 30px;*/
    height: 36px;
    background-image: linear-gradient(#fff, #f1f1f1);
    border-bottom: 1px solid #dadada;
    border-radius: 4px;
    display: flex;
    flex-direction: row;
  }

  .cart_nums {
    background: #9B9B9B;
    color: white;
    border: 5px;
    padding-left: 5px;
    border-radius: 10px;
    padding-right: 5px;
  }

  .cart_position {
    position: relative;
    left: -185px;
    top: 0px;
    z-index: 1;
    background: white;
  }

  .cart_style {
    height: 300px;
    width: 250px;
    border-radius: 10px;
    box-shadow: 5px 5px 20px 0 rgba(0, 0, 0, 0.15);
    text-align: center;
    background: url("../assets/img/cart-empty-new.png") no-repeat center center;
  }

  .cart_style_triangle {
    height: 25px;
    width: 25px;
    background: #FFFFFF;
    -webkit-transform: rotate(45deg); /* Safari 和 Chrome */;
    position: relative;
    top: -6px;
    left: 192px;
  }

  .person_position {
    position: relative;
    left: -60px;
    top: 0px;
    z-index: 1;
    background: white;
  }

  .person_style {
    height: 300px;
    width: 150px;
    background: #FFFFFF;
    border-radius: 10px;
    box-shadow: 5px 5px 20px 0 rgba(0, 0, 0, 0.15);
  }

  .person_style_triangle {
    height: 25px;
    width: 25px;
    background: #FFFFFF;
    -webkit-transform: rotate(45deg); /* Safari 和 Chrome */;
    position: relative;
    top: -6px;
    left: 65px;
  }
</style>
