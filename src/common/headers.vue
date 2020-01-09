<template>
  <div class="nav-title">
    <div class="nav">
      <div class="title">
        欢迎来到小L的店，一站式线上选购平台
      </div>
      <div style="position:absolute;left: 80vw;">

        <div style="position: absolute;">
          <span @mouseover="change_person(true)" @mouseout="change_person(false)">
            <img src="@/assets/img/person.png">
          </span>
          <div class="person_position" v-show="showperson">
            <div class="person_style">
              <div class="person_style_triangle"></div>
            </div>
          </div>
        </div>

        <div style="position:absolute;left: 5vw;">
           <span @mouseover="change_cart(true)" @mouseout="change_cart(false)">
            <img src="@/assets/img/buy.png">
           </span>

          <div class="cart_position" v-show="showcart">
            <div class="cart_style">
              <div class="cart_style_triangle"></div>
              <p class="cart_none_text">购物车为空哦</p>
            </div>
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
    padding: 0px 300px 0 370px;
  }
  .title{
    font-size: 15px;
    position: relative;
  }
  .nav{
    margin: 0% auto;
    width: 90%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  .cart_none_text{
    padding-top: 170px;
    color: #999999;
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
