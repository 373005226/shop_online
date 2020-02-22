<template>
    <div>
        <MyHeader />
        <div class="collectionBox">
            <div class="row">
                <!-- 面包屑 -->
                <div class="crumbs">
                    <router-link  to="/">首页</router-link>
                    <div class="icon icon-right_s"></div>
                    <span class="">我的收藏</span>
                </div>
                <div class="content">
                    <UserSide />
                    <div v-if="collectionList.length != 0" class="collectionContent">
                        <div class="item" v-for="(item,index) in collectionList" :key=index>
                            <div class="main">
<!--                                <div @click="handleClose(item,index)" class="close icon icon-close"></div>-->
                              <div  @click="todetail(item.goods.id)">
                                <img :src="item.goods.images[0].image" v-if="item.goods.images !== undefined &&  item.goods.images.length > 0 ">
                                {{item.goods.name}}
                              </div>

                                <div class="price">
                                    ￥<strong  v-if="item.goods.specification !== undefined &&  item.goods.specification.length > 0 ">{{item.goods.specification[0].shop_price}}</strong>
                                </div>
                                <div class="btns">
                                    <a href="javascript:;" @click="cancelfav(item.goods.id)">取消收藏</a>
                                    <a href="javascript:;">加入购物车</a>
                                </div>
                            </div>
                        </div>
<!--                        <VuePage :cur="cur" :all="all" :callback="callback" />-->
<!--                      <div class="page">-->
<!--                        <el-pagination style="text-align: center"-->
<!--                                       background-->
<!--                                       layout="prev, pager, next"-->
<!--                                       :total="1000"-->
<!--                        >-->
<!--                        </el-pagination>-->
<!--                      </div>-->
                    </div>
                  <div class="none" v-else>
                    <img src="@/assets/img/none.png">
                  </div>
                </div>
            </div>
        </div>
        <MyFooter />
    </div>
</template>
<script>
import MyHeader from "@/common/header/MyHeader.vue";
import MyFooter from "@/common/footer/MyFooter.vue";
import UserSide from "@/common/UserSide.vue";
import {getallfav ,deletefav} from '@/api/index'
// import VuePage from "@/components/page/page.vue"

export default{
  components: {  MyHeader,  MyFooter ,UserSide},
    name:"UserCollection",
    data(){
        return{
            cur: 1,
            all: 8,
            collectionList:[
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:0},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:1},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:0},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:1},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:0},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:1},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:0},
                // {name:'男/女 轻柔色纺纱家居拖鞋',img:'https://yanxuan-item.nosdn.127.net/072a79db3d9e3f4a1d652f498311e102.png?quality=95&thumbnail=200x200&imageView',price:'43.9',id:1},
            ]
        }
    },
    created(){
      getallfav({
        headers: {
          Authorization: 'JWT '+localStorage.getItem('token')
        }
      }).then(res=>{
        console.log(res)
        this.collectionList = res
      })
    },
    mounted(){

    },
    methods:{
      cancelfav(id){
        console.log(id)
        deletefav(id,{headers: {Authorization: 'JWT ' + localStorage.getItem('token')}}).then(res=>{
          console.log(res)
          location.reload()
        })
      },
      todetail(id){
        console.log(id)
        this.$router.push(
          {
            path:'/detail',query:{id:id}
          }
          )
      },
        callback(data) {
          this.cur = data;
        },
        handleClose(e,i){
            this.collectionList.splice(i,1)
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
    .collectionBox{
        .content{
            display: flex;
            .collectionContent{
                width: 890px;
                margin-left: 20px;
                display: flex;
                flex-wrap: wrap;
                align-content: baseline;
                .item{
                    width: 215px;
                    height: 330px;
                    margin-right: 10px;
                    margin-bottom: 10px;
                    &:hover{
                        box-shadow: 1px 1px 8px rgba(0,0,0,.2);
                        background-color: #f4f0ea;
                    }
                    &:nth-child(4n+4){
                        margin-right: 0;
                    }
                    .main{
                        width: 100%;
                        height: 100%;
                        cursor: pointer;
                        position: relative;
                        text-align: center;
                        font-size: 14px;
                        &:hover .close{
                            display: flex;
                        }
                        .close{
                            z-index: 2;
                            cursor: pointer;
                            display: none;
                            position: absolute;
                            top: 0;
                            right: 0px;
                            background-color: rgba(0,0,0,0.5);
                            color: #fff;
                            justify-content: center;
                            align-items: center;
                        }
                        a,img{
                            display: inline-block;
                        }
                        img{
                            width: 215px;
                            height: 200px;
                            background-color: #aaaaaa;
                        }
                        .name{
                            color: #333;
                            font-weight: bold;
                            margin-top: 10px;
                            &:hover{
                                color: #b4a078;
                            }
                        }
                        .price{
                            margin-top: 10px;
                            color:red;
                        }
                        .btns{
                            justify-content: center;
                            margin-top: 10px;
                            display: flex;
                            a{
                                height: 28px;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                width: 90px;
                                background: #F5F5F5;
                                border: 1px solid #ddd;
                                border-radius: 0;
                                &:hover{
                                    background-color: #fff;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
  .page{
    margin: 0 auto;
  }
</style>

