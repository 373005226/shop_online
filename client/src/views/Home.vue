<template>
  <div>
    <my-header></my-header>
    <banner_top></banner_top>
    <main-nav></main-nav>
    <fade-swiper class="swiperBox" width="100vw" height="419px"></fade-swiper>
    <div style="background: #f2f2f2">
      <new_goodslsit></new_goodslsit>
      <ranking></ranking>
      <catelogy></catelogy>
      <my-footer></my-footer>
    </div>
  </div>
</template>

<script>
  // @ is an alias to /src
  import {addvisitor} from '../api/information'
  import MyHeader from "../common/header/MyHeader";
  import banner_top from "../components/Home/banner_top";
  import MainNav from "../components/Home/MainNav";
  import FadeSwiper from "../components/Home/FadeSwiper";
  import new_goodslsit from "../components/Home/new_goodslsit";
  import Ranking from "../components/Home/Ranking";
  import catelogy from "../components/Home/catelogy";
  import MyFooter from "../common/footer/MyFooter";
  export default {
    name: 'Home',
    components: {
      MyHeader,
      banner_top,
      MainNav,
      FadeSwiper,
      new_goodslsit,
      Ranking,
      catelogy,
      MyFooter
    },
    created() {
      addvisitor({count:1}).then(()=>{
        console.log('访问量+1')
      })
    }
  }
</script>

<style scoped lang="less">
  .swiperBox {
    position: absolute;
    left: 0;
    /*top: 230px;*/
    /*margin-top: 20px;*/
    display: block;
    box-shadow: 0 -1px 2px rgba(0, 0, 0, 0.2);
    overflow: hidden;

    .banner {
      transform: scale(1.2, 1);
    }
  }
</style>
