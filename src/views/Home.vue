<template>
  <div class="home">
    <my-header></my-header>
    <banner_top></banner_top>
    <MainNav></MainNav>
    <FadeSwiper class="swiperBox" width="100vw" height="419px" v-for="(item,index) in banner_img" :key="index">
      <img class="banner" slot="item1" src="@/assets/img/banner/banner1.jpg" />
      <img class="banner" slot="item2" src="@/assets/img/banner/banner2.jpg" />
      <img class="banner" slot="item3" src="@/assets/img/banner/banner3.jpg" />
    </FadeSwiper>
    <div style="background: #f2f2f2">

      <section class="newGoods section">
        <SectionHeader title="新品首发" tips="周一周四上新，为你寻觅世间好物" moreText="更多新品>"/>
          <Slick
            :ulWidth="(266*goodsList.length)+(10*(goodsList.length-1))"
            :showWidth="widths-497"
            :height="360"
          >
          <ul class="goodsList" :style="{width:`${(266*goodsList.length)+(10*(goodsList.length-1))}px`}" slot="list">
            <GoodsItem
              v-for="(item,index) in goodsList"
              :style="{marginRight: (index+1)%4===0?'0px':'10px'}"
              :id="item.id"
              :img="item.img"
              :name="item.name"
              :price="item.price"
              :key="index"
            />
          </ul>
        </Slick>
      </section>
    <ranking></ranking>
    <catelogy></catelogy>
    <MyFooter></MyFooter>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MyHeader from "../common/MyHeader";
import banner_top from "../components/Home/banner_top";
import MainNav from "../components/Home/MainNav";
import FadeSwiper from "../components/Home/FadeSwiper";
import GoodsItem from "../components/Home/GoodsItem";
import SectionHeader from "../components/Home/SectionHeader";
import Slick from "../components/Home/Slick";
import Ranking from "../components/Home/Ranking";
import catelogy from "../components/Home/catelogy";
import MyFooter from "../common/MyFooter";
export default {
  name: 'Home',
  data(){
    return{
      widths: '',
      typeList:[
        {name: '水果蔬菜'},
        {name: '新鲜肉类'},
        {name: '酒水饮料'},
        {name: '美妆护肤'} ,
        {name: '家具用品'},
        {name: '家电产品'},
        {name: '五金工具'},
        {name: '服饰'},
        {name: '办公文具'}
      ],
      goodsList:[
        {
          img:require('@/assets/img/food/好丽友薯片.jpg'),
          name:'好丽友薯片',
          price:16
        },
        {
          img:require('@/assets/img/food/奥利奥冰淇淋味夹心饼干22.8.jpg'),
          name:'奥利奥冰淇淋味夹心饼干',
          price:22.8
        },
        {
          img:require('@/assets/img/food/奥利奥蓝莓味夹心饼干.jpg'),
          name:'奥利奥蓝莓味夹心饼干',
          price:26
        },
        {
          img:require('@/assets/img/food/稻香村糕点礼盒53.jpg'),
          name:'稻香村糕点礼盒',
          price:22.8
        },
        {
          img:require('@/assets/img/food/费列罗巧克力81.5.jpg'),
          name:'费列罗巧克力',
          price:81.5
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点1',
          price:34.2
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点2',
          price:34.2
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点3',
          price:34.2
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点4',
          price:34.2
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点5',
          price:34.2
        },
        {
          img:require('@/assets/img/food/达利园糕点34.2.jpg'),
          name:'达利园糕点6',
          price:34.2
        },
      ],
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
  created() {
    this.widths = document.body.clientWidth
    console.log(this.widths)
  },
  components: {
    MyHeader,
    banner_top,
    MainNav,
    FadeSwiper,
    GoodsItem,
    SectionHeader,
    Slick,
    Ranking,
    catelogy,
    MyFooter
  }
}
</script>

<style scoped lang="less">
  .newGoods{
    margin:450px 150px 0 200px;
  }
  .section{
    padding:30px;
    overflow: hidden;
  }
  .swiperBox{
    position: absolute;
    left: 0;
    /*top: 230px;*/
    /*margin-top: 20px;*/
    display: block;
    box-shadow: 0 -1px 2px rgba(0,0,0,0.2);
    overflow: hidden;
  .banner{
    transform: scale(1.2,1);
  }
  }
</style>
