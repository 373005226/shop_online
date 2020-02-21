<template>
  <div style="background: #EDEDED">
    <div class="main" v-if="goodsList.length !=0">
      <div class="nav">
        <div>
          <a href="#" class="active">综合排序</a>
          <a href="#">综合从低到高</a>
          <a href="#">综合从高到低</a>
          <div class="price-interval">
            <input type="number" class="input" placeholder="价格" v-model="min">
            <span style="margin: 0 5px"> - </span>
            <input type="number" placeholder="价格" v-model="max">
            <el-button type="primary" size="mini" class="pricebutton">确定</el-button>
          </div>
        </div>
      </div>

      <div class="goods">
           <div class="col" v-for="(item,index) in goodsList" :key="index">
             <router-link :to="{path:'/detail',query:{id:item.id}}">
               <img :src="item.images[0].image" v-if="item.images !== undefined &&  item.images.length > 0 ">
               <p class="name">{{item.name}}</p>
               <p class="price"> ￥ <strong  v-if="item.specification !== undefined &&  item.specification.length > 0 ">{{item.specification[0].shop_price}}</strong></p>
               <a class="cartBtn"></a>
             </router-link>
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

    <div v-else style="text-align: center;">
      <img src="@/assets/img/nosearch.png">
    </div>
  </div>
</template>

<script>

  import {searchgood} from "@/api/goods"
  export default {
    name: "searchgoods",
    data() {
      return {
        min: '',
        max: '',
        total:1,
        page:1,
        goodsList: [
          // {
          //   img: require('@/assets/img/food/好丽友薯片.jpg'),
          //   name: '好丽友薯片',
          //   price: 16
          // },
          // {
          //   img: require('@/assets/img/food/奥利奥冰淇淋味夹心饼干22.8.jpg'),
          //   name: '奥利奥冰淇淋味夹心饼干',
          //   price: 22.8
          // },
          // {
          //   img: require('@/assets/img/food/奥利奥蓝莓味夹心饼干.jpg'),
          //   name: '奥利奥蓝莓味夹心饼干',
          //   price: 26
          // },
          // {
          //   img: require('@/assets/img/food/稻香村糕点礼盒53.jpg'),
          //   name: '稻香村糕点礼盒',
          //   price: 22.8
          // },
          // {
          //   img: require('@/assets/img/food/费列罗巧克力81.5.jpg'),
          //   name: '费列罗巧克力',
          //   price: 81.5
          // },
          // {
          //   img: require('@/assets/img/food/达利园糕点34.2.jpg'),
          //   name: '达利园糕点',
          //   price: 34.2
          // }
        ]
      }
    },
    methods:{
      handleCurrentChange(value){
        console.log(value)
      }
    },
    created() {
      searchgood(this.$route.query.keys).then(res=>{
        console.log(res)
        this.goodsList = res.results
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
