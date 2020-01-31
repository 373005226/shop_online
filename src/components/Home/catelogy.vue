<template>
  <div>
    <div v-for="(item,index) in catelogy_list" :key="index">
    <div class="main-title">
      <p class="lg">{{item.name}}</p>
      <p class="sm">RANKING LIST</p>
    </div>

    <div class="c-comm-floor">
      <div class="c-title">
        <p class="icon"></p>
        <div>
          <p class="title">{{item.name}}</p>
        </div>
      </div>
      <div class="col1">
        <a>
          <img class="bg" :src="item.image">
        </a>
<!--        <div class="c-cards">-->
<!--          <ul class="clearfix">-->
<!--            <li><a>新鲜蔬菜</a></li>-->
<!--            <li><a>新鲜肉类</a></li>-->
<!--            <li><a>新鲜海鲜</a></li>-->
<!--            <li><a>新鲜水果</a></li>-->
<!--          </ul>-->
<!--        </div>-->
      </div>

      <div class="col2">
        <ul class="clearfix">
          <li v-for="(items,indexs) in item.goods_catelogy" :key="indexs">
            <a href="#">

              <img :src="items.images[0].image">
              <p class="name">{{items.name}}</p>
              <p class="price">
                ¥&nbsp;
                <strong>{{items.specification[0].shop_price}}</strong>
              </p>
            </a>
            <a class="cartBtn"></a>
          </li>
        </ul>
      </div>

    </div>
    </div>
  </div>
</template>

<script>
  import {catelogy} from "../../api/goods";

  export default {
        name: "catelogy",
      data(){
          return{
            catelogy_list:[]
          }
      },
    created() {
      catelogy().then(res=>{
        console.log(res)
        for(let i of res){
          // console.log(i)
          if(i.image != null){
            console.log(i)
            this.catelogy_list = res
          }
        }
      })
    }
  }
</script>

<style scoped>
  .main-title{
    position: relative;
    width: 1190px;
    margin: 20px auto 10px;
    text-align: center;
  }
  .main-title .lg {
    display: inline-block;
    height: 45px;
    color: #222;
    font: 32px/45px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    margin-bottom: 8px;
    letter-spacing: 15px;
    text-indent: 15px;
  }
  .main-title .sm {
    color: #999;
    font: 14px/22px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    letter-spacing: 1px;
  }
  /*定义了商品分类的面积*/
  .c-comm-floor {
    position: relative;
    width: 1190px;
    height: 637px;
    margin: 25px auto 10px;
    overflow: hidden;
  }
  /*分类标题的长宽*/
  .c-comm-floor .c-title {
    float: left;
    width: 100%;
    height: 25px;
    margin-bottom: 12px;
  }
  /*靠左边的方块*/
  .c-comm-floor .c-title .icon {
    float: left;
    width: 5px;
    height: 18px;
    background: #e42e3c;
    margin-top: 3px;
    margin-right: 20px;
  }
  /*标题*/
  .c-comm-floor .c-title .title {
    float: left;
    font: 18px/25px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    color: #222;
    letter-spacing: 1.8px;
    margin-right: 12px;
  }
  /*分类的靠左边的地区*/
  .c-comm-floor .col1 {
    float: left;
    position: relative;
    width: 231px;
    height: 600px;
    background: #ddd;
  }
  /*分类的图片*/
  .c-comm-floor .col1 .bg {
    position: absolute;
    width: 231px;
    height: 600px;
    left: 0;
    top: 0;
    z-index: 0;
  }
  /*显示在左边图片的分类*/
  .c-comm-floor .col1 .c-cards {
    position: absolute;
    width: 196px;
    height: 130px;
    top: 40px;
    left: 20px;
  }
  .c-comm-floor .col1 .c-cards ul {
    margin-right: -10px;
  }
  .clearfix {
    zoom: 1;
  }
  .c-comm-floor .col1 .c-cards ul li {
    float: left;
    max-width: 84px;
    height: 24px;
    text-align: center;
    border-radius: 20px;
    border: 1px solid #fff;
    margin: 0 10px 10px 0;
    overflow: hidden;
    background: rgba(255,255,255,.2);
  }
  .c-comm-floor .col1 .c-cards ul li a {
    display: block;
    padding: 0 10px;
    color: #fff;
    font: 12px/24px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    overflow: hidden;
  }
/*  显示图片右边的分类*/
  .c-comm-floor .col2 {
    float: left;
    width: 959px;
    height: 600px;
    background: #eee;
    overflow: hidden;
  }
  .c-comm-floor .col2 ul {
    float: left;
    margin-right: -10px;
  }
  .c-comm-floor .col2 ul li {
    float: left;
    position: relative;
    width: 230px;
    height: 295px;
    background: #fff;
    margin: 0 0 10px 10px;
    overflow: hidden;
  }
  .c-comm-floor .col2 ul li:hover img{
    transform: scale(1.08);
  }
  .c-comm-floor .col2 ul li:hover .name{
    color: red;
  }
  .c-comm-floor .col2 ul li img {
    display: block;
    width: 180px;
    height: 180px;
    margin: 20px 25px 10px;
    -webkit-transition: -webkit-transform .5s;
    transition: -webkit-transform .5s;
    transition: transform .5s;
    transition: transform .5s,-webkit-transform .5s;
  }
  .c-comm-floor .col2 ul li .name {
    width: 140px;
    height: 40px;
    font: 12px/20px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    margin-left: 45px;
    margin-bottom: 10px;
    letter-spacing: 1.17px;
    transition: all 0.3s;
    }
  .c-comm-floor .col2 ul li .price {
    color: #e42e3c;
    height: 25px;
    font: 12px/25px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    margin-left: 45px;
  }
  .c-comm-floor .col2 ul li .cartBtn {
    position: absolute;
    width: 19px;
    height: 18px;
    background: url("../../assets/img/购物车.png") no-repeat;
    /*background-position: -931px 0;*/
    right: 41px;
    bottom: 11px;
    cursor: pointer;
  }
  /*使得字体变成正常*/
  .ng-iconfont, em, i {
    font-style: normal;
  }
</style>
