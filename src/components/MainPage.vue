<template>
    <div>
      <banner_top></banner_top>
      <MainNav></MainNav>
      <FadeSwiper class="swiperBox" style="margin-top: -21px;margin-left: 15vw" width="70vw" height="419px" v-for="(item,index) in banner_img" :key="index">
        <img class="banner" slot="item1" src="@/assets/img/banner/banner1.jpg" />
        <img class="banner" slot="item2" src="@/assets/img/banner/banner2.jpg" />
        <img class="banner" slot="item3" src="@/assets/img/banner/banner3.jpg" />
      </FadeSwiper>
    </div>
</template>

<script>
  import banner_top from "./Home/banner_top";
  import MainNav from "./Home/MainNav";
  import FadeSwiper from "./Home/FadeSwiper";
  export default {
      name: "MainPage",
      data(){
        return{
          banner_img: [
            {
              imgurl:require('../assets/img/banner/banner1.jpg')
            },
            {
              imgurl:require('../assets/img/banner/banner2.jpg')
            },
            {
              imgurl:require('../assets/img/banner/banner3.jpg')
            }
          ]
        }
      },
      components: {
        banner_top,
        MainNav,
        FadeSwiper
      }
    }
</script>

<style scoped lang="less">
  .swiperBox{
    position: absolute;
    left: 0;
    top: 230px;
    margin-top: 20px;
    display: block;
    box-shadow: 0 -1px 2px rgba(0,0,0,0.2);
    overflow: hidden;
    .banner{
      transform: scale(1.2,1);
    }
  }
</style>
