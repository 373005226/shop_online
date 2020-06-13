<template>
  <div>
    <MyHeader/>
    <div class="collectionBox">
      <div class="row">
        <!-- 面包屑 -->
        <div class="crumbs">
          <router-link to="/">首页</router-link>
          <div class="icon icon-right_s"></div>
          <span class="">我的收藏</span>
        </div>
        <div class="content">
          <UserSide/>
          <div v-if="collectionList.length !== 0" class="collectionContent">
            <div class="item" v-for="(item,index) in collectionList" :key=index>
              <div class="main">
                <div @click="todetail(item.goods.id)">
                  <img :src="item.goods.images[0].image"
                       v-if="item.goods.images !== undefined &&  item.goods.images.length > 0 " style="border-radius: 7px;">
                  {{item.goods.name}}
                </div>

                <div class="price">
                  ￥<strong v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">{{item.goods.specification[0].shop_price}}</strong>
                </div>
                <div class="btns">
                  <el-button @click="cancelfav(item.goods.id)" size="small" round>取消收藏</el-button>
                  <el-button @click="addcart(item.goods.id)" size="small" round>加入购物车</el-button>
                </div>
              </div>
            </div>
          </div>
          <div class="none" v-else>
            <img src="@/assets/img/none.png" style="width: 300px;height: 200px;">
          </div>
        </div>
      </div>
    </div>
    <MyFooter/>
  </div>
</template>
<script>
  import MyHeader from "@/common/header/MyHeader.vue";
  import MyFooter from "@/common/footer/MyFooter.vue";
  import UserSide from "@/common/UserSide.vue";
  import {getallfav, deletefav} from '@/api/index'
  import {addcart} from '@/api/index'

  export default {
    components: {MyHeader, MyFooter, UserSide},
    name: "UserCollection",
    data() {
      return {
        cur: 1,
        all: 8,
        collectionList: []
      }
    },
    mounted() {
      this.getfav()
    },
    methods: {
      getfav(){
        getallfav({
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          console.log(res)
          this.collectionList = res
        })
      },
      cancelfav(id) {
        console.log(id)
        deletefav(id, {headers: {Authorization: 'JWT ' + localStorage.getItem('token')}}).then(res => {
          console.log(res)
          this.getfav()
          this.$message({
            message: '取消收藏商品成功',
            type: 'success'
          });
        })
      },
      todetail(id) {
        console.log(id)
        this.$router.push(
          {
            path: '/detail', query: {id: id}
          }
        )
      },
      //添加到购物车
      addcart(id) {
        addcart({
          nums: 1,
          goods: id,
        }, {
          headers: {Authorization: 'JWT ' + localStorage.getItem('token')}
        }).then(res => {
          console.log(res)
          this.$message({
            message: '加入购物车成功',
            type: 'success'
          })
        }).catch(error => {
          if (error.response.status === 401) {
            this.$message.error('加入购物车失败，您尚未登录')
          }
        })
      }
    },
  }
</script>

<style lang="scss" scoped>
  .none {
    width: 100px;
    margin: 0 auto;

    img {
      height: 350px;
      margin-top: 150px;
    }
  }

  .collectionBox {
    .content {
      display: flex;

      .collectionContent {
        width: 890px;
        margin-left: 20px;
        display: flex;
        flex-wrap: wrap;
        align-content: baseline;

        .item {
          width: 215px;
          height: 330px;
          margin-right: 10px;
          margin-bottom: 10px;

          &:hover {
            box-shadow: 1px 1px 8px rgba(0, 0, 0, .2);
            background-color: #D9ECFF;
            transition: .2s;
          }

          &:nth-child(4n+4) {
            margin-right: 0;
          }

          .main {
            width: 100%;
            height: 100%;
            cursor: pointer;
            position: relative;
            text-align: center;
            font-size: 14px;

            &:hover .close {
              display: flex;
            }

            .close {
              z-index: 2;
              cursor: pointer;
              display: none;
              position: absolute;
              top: 0;
              right: 0px;
              background-color: rgba(0, 0, 0, 0.5);
              color: #fff;
              justify-content: center;
              align-items: center;
            }

            a, img {
              display: inline-block;
            }

            img {
              width: 215px;
              height: 200px;
              background-color: #aaaaaa;
            }

            .name {
              color: #333;
              font-weight: bold;
              margin-top: 10px;

              &:hover {
                color: #b4a078;
              }
            }

            .price {
              margin-top: 10px;
              color: red;
            }

            .btns {
              justify-content: center;
              margin-top: 10px;
              display: flex;

              a {
                height: 28px;
                display: flex;
                justify-content: center;
                align-items: center;
                width: 90px;
                background: #F5F5F5;
                border: 1px solid #ddd;
                border-radius: 0;

                &:hover {
                  background-color: #fff;
                }
              }
            }
          }
        }
      }
    }
  }

  .page {
    margin: 0 auto;
  }
</style>

