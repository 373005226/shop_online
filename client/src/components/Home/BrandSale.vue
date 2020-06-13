<template>
    <div>
      <div class="main-title">
        <p class="lg">品牌专场</p>
        <p class="sm">BRAND SALE</p>
      </div>

      <div class="brand-floor">
        <div class="col1">
          <div class="banner-wrapper">
            <ul class="banner">
              <li class="banner-item">
                <a>
                  <img src="@/assets/img/brand/brand_big.png">
                </a>
              </li>
            </ul>
          </div>
        </div>
<!--        <div class="col">-->
<!--          <ul class="clearfix">-->
<!--            <li v-for="(item,index) in brand_img" :key="index">-->
<!--              <a>-->
<!--                <img :src="item.img">-->
<!--              </a>-->
<!--            </li>-->
<!--          </ul>-->
<!--        </div>-->
      </div>
    </div>
</template>

<script>
    export default {
        name: "BrandSale",
      data(){
          return{
            brand_img:[
              {
                id:1,
                img:require('@/assets/img/brand/rice.jpg')
              },
              {
                id:2,
                img:require('@/assets/img/brand/foods.png')
              },
              {
                id:3,
                img:require('@/assets/img/brand/orange.png')
              },
              {
                id:4,
                img:require('@/assets/img/brand/machine.png')
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

  .brand-floor {
    position: relative;
    width: 1190px;
    height: 360px;
    margin: 10px auto;
    overflow: hidden;
  }
  /*以下部分是左边的大品牌*/
  .brand-floor .col1 {
    float: left;
    position: relative;
    width: 390px;
    height: 360px;
    background: #fff;
    margin-right: 10px;
  }
  .brand-floor .col1 .banner-wrapper {
    position: absolute;
    width: 390px;
    height: 280px;
    left: 0;
    top: 0;
  }
  .brand-floor .col1 .banner-wrapper .banner {
    width: 100%;
    height: 100%;
  }
  .brand-floor .col1 .banner-wrapper .banner .banner-item {
    display: none;
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
  }
  .brand-floor .col1 .banner-wrapper .banner .banner-item img {
    display: block;
    width: 100%;
    height: 100%;
  }
  li {
    list-style-type:none;
  }
</style>
