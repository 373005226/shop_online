<template>
  <div style="background: #EDEDED;padding:30px;">
    <div class="main">

      <div class="goods">
        <div class="col" v-for="(item,index) in goodsList" :key="index">
<!--          <router-link :to="{path:'/detail',query:{id:item.id}}">-->
<!--            <img :src="item.images[0].image" v-if="item.images !== undefined &&  item.images.length > 0 ">-->
<!--            <p class="name">{{item.name}}</p>-->
<!--            <p class="price"> ￥ <strong  v-if="item.specification !== undefined &&  item.specification.length > 0 ">{{item.specification[0].shop_price}}</strong></p>-->
<!--            <a class="cartBtn"></a>-->
<!--           </router-link>-->
                <img :src="item.image">
                <p class="name">{{item.name}}</p>
                <p class="price"><strong style="padding-right: 10px">{{item.integral}}</strong>积分</p>
                <a class="cartBtn" @click="open"></a>
        </div>
      </div>

      <div class="page">
        <el-pagination
          @current-change="handleCurrentChange"
          :hide-on-single-page="false"
          background
          layout="prev, pager, next"
          :total="total">
        </el-pagination>
      </div>
    </div>

  </div>
</template>

<script>

  import {integralgoods} from "@/api/goods"
  export default {
    name: "Goods",
    data() {
      return {
        min: '',
        max: '',
        total:1,
        page:1,
        goodsList: [
          {
            img: "https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200309205853.png",
            name: '维达纸巾',
            price: 1600
          },
          {
            img: require('@/assets/img/food/奥利奥冰淇淋味夹心饼干22.8.jpg'),
            name: '奥利奥冰淇淋味夹心饼干',
            price: 2280
          },
          {
            img: require('@/assets/img/food/奥利奥蓝莓味夹心饼干.jpg'),
            name: '奥利奥蓝莓味夹心饼干',
            price: 2600
          },
          {
            img: require('@/assets/img/food/稻香村糕点礼盒53.jpg'),
            name: '稻香村糕点礼盒',
            price: 2280
          },
          {
            img: require('@/assets/img/food/费列罗巧克力81.5.jpg'),
            name: '费列罗巧克力',
            price: 8150
          },
          {
            img: require('@/assets/img/food/达利园糕点34.2.jpg'),
            name: '达利园糕点',
            price: 3420
          },
          {
            img: require('@/assets/img/food/费列罗巧克力81.5.jpg'),
            name: '费列罗巧克力',
            price: 8150
          }
        ]
      }
    },
    methods:{
      handleCurrentChange(value){
        console.log(value)
        integralgoods(value).then(res=>{
          console.log(res)
          this.goodsList = res.results
        })
      },
      open() {
        this.$confirm('积分商品兑换后，需要在下一次购买才能一并领取', '提示', {
          confirmButtonText: '确认兑换',
          cancelButtonText: '取消兑换',
          type: 'warning'
        }).then(() => {
          this.$message({
            type: 'success',
            message: '兑换成功!'
          });
        })
      }
    },
    created() {
      this.total = this.goodsList.length
      integralgoods(this.page).then(res=>{
        console.log(res)
        this.goodsList = res.results
        this.total = res.count
      })
    }
  }
</script>

<style scoped lang="scss">
  .page{
    text-align: center;
  }
  .col{
    width: 226px;
    height: 280px;
    background: white;
    margin-right: 12px;
    margin-bottom: 15px;
    position: relative;

    &:hover{
      color: red;
    }

      img{
        width: 100%;
        max-width: 226px;
        height: 180px;
        cursor: pointer;
        transition:transform 0.5s;

        &:hover{
          transform: scale(1.03);
        }
    }
    .name{
      width: 190px;
      height: 40px;
      padding-left: 20px;
      padding-top: 20px;
      font: 12px/20px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
      margin-left: 30px;
      margin-bottom: 14px;
      letter-spacing: 1.17px;
      -webkit-transition: all 0.3s;
      transition: all 0.3s;
    }
    .price{
      color: #e42e3c;
      font: 12px/25px "Microsoft Yahei", tahoma, arial, "Hiragino Sans GB";
      margin-left: 45px;
    }

    .cartBtn{
      position: absolute;
      width: 19px;
      height: 18px;
      background: url("../assets/img/购物车.png") no-repeat;
      /*background-position: -931px 0;*/
      right: 22px;
      bottom: 20px;
      cursor: pointer;
    }
  }
  .goods{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
  }

  .pricebutton{
    margin-left: 10px;
    background: #5D84E4;

    &:hover{
      background: #3664e3;
    }
  }
  .main {
    max-width: 1190px;
    margin: 0 auto;
  }
  .nav {
    height: 60px;
    line-height: 60px;
    > div {
      display: flex;
      align-items: center;
      a {
        padding: 0 15px;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        color: #999;
        &.active {
          color: #5683EA;
        }
        &:hover {
          color: #5683EA;
        }
      }
      input {
        width: 80px;
        height: 30px;
        border: 1px solid #ccc;
      }
      input + input {
        margin-left: 10px;
      }
    }
    .price-interval {
      padding: 0 15px;
      display: flex;
      align-items: center;
      justify-content: center;
      input[type=number] {
        border: 1px solid #ccc;
        text-align: center;
        background: none;
        border-radius: 5px;
      }
      input::-webkit-input-placeholder{
        font-size: 12px;
        color: #999999;
      }
    }
  }


</style>
