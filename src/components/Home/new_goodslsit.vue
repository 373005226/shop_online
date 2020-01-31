<template>
    <div>
      <section class="newGoods section">
        <section-header title="新品首发" tips="周一周四上新，为你寻觅世间好物" moreText="更多新品>"/>
        <slick
          :ulWidth="(266*goodsList.length)+(10*(goodsList.length-1))"
          :showWidth="widths-497"
          :height="360"
        >
          <ul class="goodsList" :style="{width:`${(266*goodsList.length)+(10*(goodsList.length-1))}px`}" slot="list">
            <li class="GoodsItem" :style="{marginRight: (index+1)%4===0?'0px':'10px'}" v-for="(item,index) in goodsList" :key="index">
              <router-link to="/detail">
                <div class="imgBox">
                  <img :src="item.images[0].image" alt="商品图片" v-if="item.images!== undefined &&  item.images.length > 0 "/>
                </div>
                <div class="goodsInfo">
                  <span class="goodsName ellipsis">{{item.name}}</span>
                  <span class="price" v-if="item.specification!== undefined &&  item.specification.length > 0 ">{{'¥'+item.specification[0].shop_price}}</span>
                </div>
              </router-link>

            </li>
          </ul>
        </slick>
      </section>
    </div>
</template>

<script>
  import SectionHeader from "./SectionHeader";
  import Slick from "./Slick";
  import {goods} from "../../api/goods";

  export default {
      name: "new_goodslsit",
      data() {
        return {
          widths: '',
          goodsList: [
            {
              img: require('@/assets/img/food/好丽友薯片.jpg'),
              name: '好丽友薯片',
              price: 16
            },
            {
              img: require('@/assets/img/food/奥利奥冰淇淋味夹心饼干22.8.jpg'),
              name: '奥利奥冰淇淋味夹心饼干',
              price: 22.8
            },
            {
              img: require('@/assets/img/food/奥利奥蓝莓味夹心饼干.jpg'),
              name: '奥利奥蓝莓味夹心饼干',
              price: 26
            },
            {
              img: require('@/assets/img/food/稻香村糕点礼盒53.jpg'),
              name: '稻香村糕点礼盒',
              price: 22.8
            },
            {
              img: require('@/assets/img/food/费列罗巧克力81.5.jpg'),
              name: '费列罗巧克力',
              price: 81.5
            },
            {
              img: require('@/assets/img/food/达利园糕点34.2.jpg'),
              name: '达利园糕点',
              price: 34.2
            }
          ],
        }
      },
      components:{
        SectionHeader,
        Slick,
      },
      created() {
        this.widths = document.body.clientWidth
        // console.log(this.widths)
        goods().then(res=>{
          // console.log(res)
          this.goodsList = res
        })
      }
    }
</script>

<style scoped lang="less">
  @import "../../assets/css/var.less";
  .newGoods {
    margin: 450px 150px 0 200px;
  }

  .section {
    padding: 30px;
    overflow: hidden;
  }
  .GoodsItem{
    display: inline-block;
    width: 266px;
    height: 360px;
    overflow: hidden;
    &:hover{
      img{
        transform:scale(1.05);
      }
    }
    .imgBox{
      width: 100%;
      height: 266px;
      overflow: hidden;
      img{
        width: 100%;
        height: 100%;
        cursor: pointer;
        transition:transform 0.5s;
      }
    }
    .goodsInfo{
      width: 100%;
      height: 60px;
      font-size: 14px;
      .goodsName{
        display: block;
        text-align: center;
        cursor: pointer;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 600;
        line-height: 20px;
        &:hover{
          color:@thirdColor;
        }
      }
      .price{
        display: block;
        text-align: center;
        color:@falseColor;
      }
    }
  }
</style>
