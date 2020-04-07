<template>
  <div class="main">
    <div class="main-title">
      <p class="lg">销售排行榜</p>
      <p class="sm">RANKING LIST</p>
    </div>
    <div class="c-rank">

      <div class="c-rank-nav">
        <ul>
          <li v-for="(item,index) in catelogy" :key="index" @mouseover="changecatelogy(item.id)">
            <img :src="item.icon">
            <p class="name">{{item.name}}</p>
          </li>
        </ul>
      </div>

      <div class="c-rank-cont">
        <ul class="clearfix">
          <li v-for="item in ranklist" :key="item.id">
            <router-link :to="{path:'/detail',query:{id:item.id}}">

            <a href="#">
                <img :src="item.images[0].image">
                <p class="name">{{item.name}}</p>
                <p class="price">
                  ￥&nbsp;
                  <strong>{{item.specification[0].shop_price}}</strong>
                </p>
                <a class="cartBtn">
                </a>
              </a>

            </router-link>
          </li>
        </ul>
      </div>

    </div>
  </div>
</template>

<script>
  import {catelogy, searchcatelogy} from "../../api/goods";

  export default {
    name: "Ranking",
    data() {
      return {
        params: 1,
        catelogy: [],
        ranklist: []
      }
    },
    methods: {
      //获取所有的分类
      getcatelogydata() {
        catelogy().then(res => {
          console.log(res)
          this.catelogy = res
        })
      },
      //根据移动分类数据来显示不同的商品
      changecatelogy(index) {
        this.params = index
        this.getcatelogy()
      },
      //  获取分类的数据
      getcatelogy() {
        searchcatelogy(this.params).then(res => {
          this.ranklist = res.results
        })
      }
    },
    created() {
      this.getcatelogydata()
      this.getcatelogy()
    }
  }
</script>

<style scoped lang="less">
  .main {
    width: 1220px;
    margin: 0 auto;
  }

  .main-title {
    position: relative;
    width: 1190px;
    margin: 20px auto 10px;
    text-align: center;
  }

  .main-title .lg {
    display: inline-block;
    height: 45px;
    color: #222;
    font: 32px/45px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
    margin-bottom: 8px;
    letter-spacing: 15px;
    text-indent: 15px;
  }

  .main-title .sm {
    color: #999;
    font: 14px/22px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
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

  .c-rank .c-rank-nav ul {
    padding-top: 13px;
    line-height: 36px;
  }

  .c-rank .c-rank-nav ul li {
    margin: 0 11px;
    float: left;
    width: 110px;
    height: 86px;
    background: #fff;
    /*border: 1px solid #fff;*/
    text-align: center;
  }

  .c-rank .c-rank-nav ul li:hover {
    border-bottom: 3px solid orange;
    transition: all 0.1s;
  }

  .c-rank .c-rank-nav ul li:hover p {
    color: orange;
    transition: all 0.1s;
  }

  /*hoverfont{*/
  /*  color: orange;*/
  /*  transition: all 0.1s;*/
  /*}*/
  .c-rank .c-rank-nav ul li img {
    height: 40px;
  }

  .c-rank .c-rank-nav ul li .name {
    padding-top: 2px;
    width: 97px;
    height: 16px;
    color: #444;
    text-align: center;
    font: 12px/16px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
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
  .c-rank .c-rank-cont ul li:hover img {
    transform: scale(1.08);
  }

  /*hover时候文字放大*/
  .c-rank .c-rank-cont ul li:hover .name {
    color: red;
  }

  /*图片的文字说明*/
  .c-rank .c-rank-cont ul li .name {
    width: 140px;
    height: 40px;
    font: 12px/20px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
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
    font: 12px/25px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
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
