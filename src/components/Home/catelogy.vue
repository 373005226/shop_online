<template>
  <div>
    <div class="main-title">
      <p class="lg">超市生鲜</p>
      <p class="sm">RANKING LIST</p>
    </div>

    <div class="c-comm-floor">
      <div class="c-title">
        <p class="icon"></p>
        <div>
          <p class="title">超市生鲜</p>
        </div>
      </div>
      <div class="col1">
        <a>
          <img class="bg" src="@/assets/img/catelogy_list/生鲜.jpg">
        </a>
        <div class="c-cards">
          <ul class="clearfix">
            <li><a>新鲜蔬菜</a></li>
            <li><a>新鲜肉类</a></li>
            <li><a>新鲜海鲜</a></li>
            <li><a>新鲜水果</a></li>
          </ul>
        </div>
      </div>

      <div class="col2">
        <ul class="clearfix">
          <li v-for="(item,index) in catelogy_list" :key="index">
            <a href="#">
              <img :src="item.img">
              <p class="name">{{item.name}}</p>
              <p class="price">
                ¥&nbsp;
                <strong>{{item.price}}</strong>
              </p>
            </a>
            <a class="cartBtn"></a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "catelogy",
      data(){
          return{
            catelogy_list:[
              {
                id:1,
                img:require('@/assets/img/catelogy_list/01.jpg'),
                name:'新虹宝 南美白虾仁（中号）200g/袋 22-26只 海鲜水产',
                price:23
              },
              {
                id:2,
                img:require('@/assets/img/catelogy_list/02.jpg'),
                name:'三全 速冻素水饺韭菜鸡蛋口味 450g（30只左右）蔬菜饺子清淡早晚餐皮薄馅大方便食品',
                price:10.9
              },
              {
                id:3,
                img:require('@/assets/img/catelogy_list/03.jpg'),
                name:'春雪食品 爆汁鸡米花500g/袋装 国产出口日本级 清真食品 鸡肉块 盐酥鸡 鸡米花',
                price:19.8
              },
              {
                id:4,
                img:require('@/assets/img/catelogy_list/04.png'),
                name:'纯色本味 冷冻舟山精品带鱼段 纯中段 无内脏 500g 海鲜水产',
                price:24.8
              },{
                id:5,
                img:require('@/assets/img/catelogy_list/05.jpg'),
                name:'新虹宝 精选青虾滑（96%虾仁）200g/袋 海鲜水产 火锅食材',
                price:23.6
              },{
                id:6,
                img:require('@/assets/img/catelogy_list/06.jpg'),
                name:'【第2件半价 5件更优惠】濠礼記 广味腊肠 200g 自制7分瘦广东特产腊肠正宗甜味香肠',
                price:19.8
              },{
                id:7,
                img:require('@/assets/img/catelogy_list/07.png'),
                name:'【天府生鲜】云南水果玉米 9斤 箱装 香甜可口 可以生吃的玉米 时令水果蔬菜 奥奇健',
                price:29.9
              },{
                id:8,
                img:require('@/assets/img/catelogy_list/08.jpg'),
                name:'【新鲜采摘 甜糯可口】山东烟薯地瓜红心小香薯单果约100g以上5斤装',
                price:15.9
              },
            ]
          }
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
