<template>
    <div class="main">
      <div class="main-title">
        <p class="lg">销售排行榜</p>
        <p class="sm">RANKING LIST</p>
      </div>
      <div class="c-rank">

        <div class="c-rank-nav">
          <ul>
            <li v-for="(item,index) in catelogy" :key="index">
              <img :src="item.icon">
              <p class="name">{{item.name}}</p>
            </li>
          </ul>
        </div>

        <div class="c-rank-cont">
          <ul class="clearfix">
            <li v-for="(item,index) in ranklist" :key="index">
              <a href="#">
                <img :src="item.img">
                <p class="name">{{item.name}}</p>
                <p class="price">
                  ￥&nbsp;
                  <strong>{{item.price}}</strong>
                </p>
                <a class="cartBtn">
                </a>
              </a>
            </li>
          </ul>
        </div>

      </div>
    </div>
</template>

<script>
  import {catelogy} from "../../api/goods";

  export default {
      name: "Ranking",
      data(){
        return{
          catelogy:[
            {
              img:require('@/assets/img/icon/生鲜蔬菜.png'),
              name:'生鲜蔬菜'
            },
            {
              img:require('@/assets/img/icon/生鲜肉类.png'),
              name:'新鲜肉类'
            },
            {
              img:require('@/assets/img/icon/酒.png'),
              name:'酒水饮料'
            },
            {
              img:require('@/assets/img/icon/零食.png'),
              name:'零食'
            },
            {
              img:require('@/assets/img/icon/粮油.png'),
              name:'粮油副食'
            },
            {
              img:require('@/assets/img/icon/美妆.png'),
              name:'美妆个护'
            },
            {
              img:require('@/assets/img/icon/医疗.png'),
              name:'医疗保健'
            },
            {
              img:require('@/assets/img/icon/家电.png'),
              name:'家电家居'
            },
            {
              img:require('@/assets/img/icon/文具.png'),
              name:'五金、文具'
            },
            {
              img:require('@/assets/img/icon/服饰.png'),
              name:'服饰'
            },
          ],
          ranklist:[
            {
              img:require('@/assets/img/food/xiandanguoshu/包菜5斤18.jpg'),
              name:'包菜5斤',
              price:18
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/东北大蒜2.5斤16.8.jpg'),
              name:'东北大蒜2.5斤',
              price:16.8
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/土豆5斤21.png'),
              name:'土豆5斤',
              price:21
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/地瓜2.5斤7.6.jpg'),
              name:'地瓜2.5斤',
              price:7.6
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/小南瓜2.5斤23.8.jpg'),
              name:'小南瓜2.5斤23.8',
              price:23.8
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/小米辣5斤39.8.jpg'),
              name:'小米辣5斤',
              price:39.8
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/山东水萝卜2.5kg22.8.jpg'),
              name:'山东水萝卜2.5kg',
              price:22.8
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/广西圣女果5斤29.8.jpg'),
              name:'广西圣女果5斤',
              price:29.8
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/玉米9斤29.9.png'),
              name:'玉米9斤29.9',
              price:29.9
            },
            {
              img:require('@/assets/img/food/xiandanguoshu/生姜5斤23.9.jpg'),
              name:'生姜5斤',
              price:23.9
            },
          ]
        }
      },
    methods:{
    },
      created() {
        catelogy().then(res=>{
          console.log(res)
          this.catelogy = res
        })
      }
  }
</script>

<style scoped lang="less">
  .main{
    width: 1220px;
    margin: 0 auto;
  }
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
  .c-rank {
    position: relative;
    width: 1190px;
    margin: 10px auto;
  }
  .c-rank .c-rank-nav {
    width: 1190px;
    /*height: 88px;*/
    height: 100px;
    margin-bottom: 10px;
    background: #fff;
    overflow: hidden;
  }
  .c-rank .c-rank-nav ul{
    padding-top: 13px;
    line-height: 36px ;
  }
  .c-rank .c-rank-nav ul li {
    margin: 0 11px;
    float: left;
    width: 97px;
    height: 86px;
    background: #fff;
    /*border: 1px solid #fff;*/
    text-align: center;
  }
  .c-rank .c-rank-nav ul li:hover{
    border-bottom: 3px solid orange;
    transition: all 0.1s;
  }
  .c-rank .c-rank-nav ul li:hover p{
    color: orange;
    transition: all 0.1s;
  }
  /*hoverfont{*/
  /*  color: orange;*/
  /*  transition: all 0.1s;*/
  /*}*/
  .c-rank .c-rank-nav ul li img{
    height: 40px;
  }
  .c-rank .c-rank-nav ul li .name {
    padding-top: 2px;
    width: 97px;
    height: 16px;
    color: #444;
    text-align: center;
    font: 12px/16px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    overflow: hidden;
    letter-spacing: 1px;
  }
  li, ol, ul {
    list-style: none;
  }

  /*排行榜整体能显示的框，超出部分不显示*/
  .c-rank .c-rank-cont {
    /*display: none;*/
    height: 600px;
    overflow: hidden;
    background: #eee;
  }
  /*排行榜内容区域*/
  .c-rank .c-rank-cont ul {
    margin-right: -10px;
  }
  /*内容横向排版*/
  .c-rank .c-rank-cont ul li {
    float: left;
    position: relative;
    width: 230px;
    height: 295px;
    margin-right: 10px;
    margin-bottom: 10px;
    background: #fff;
    overflow: hidden;
  }
  /*图片显示*/
  .c-rank .c-rank-cont ul li img {
    display: block;
    width: 180px;
    height: 180px;
    margin: 20px 25px 10px;
    /*-webkit-transition: -webkit-transform .5s;*/
    /*transition: -webkit-transform .5s;*/
    transition: all 0.5s;
    cursor: pointer;
    /*transition: transform 0.5s,-webkit-transform .5s;*/
  }
  /*hover时候放大*/
  .c-rank .c-rank-cont ul li:hover img{
    transform: scale(1.08);
  }
  /*hover时候文字放大*/
  .c-rank .c-rank-cont ul li:hover .name{
    color: red;
  }
  /*图片的文字说明*/
  .c-rank .c-rank-cont ul li .name {
    width: 140px;
    height: 40px;
    font: 12px/20px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    margin-left: 45px;
    margin-bottom: 14px;
    letter-spacing: 1.17px;
    transition: all 0.3s;
  }
  /*价格文字要缩小*/
  .c-rank .c-rank-cont ul li .price {
    color: #e42e3c;
    font: 12px/25px "Microsoft Yahei",tahoma,arial,"Hiragino Sans GB";
    margin-left: 45px;
  }
  /*购物车icon*/
  .c-rank .c-rank-cont ul li .cartBtn {
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
