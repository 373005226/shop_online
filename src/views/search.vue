<template>
    <div>
      <my-header></my-header>
      <div class="searchBox">
        <div class="row">
          <!-- 面包屑 -->
          <crumbs></crumbs>
          <!-- content -->
          <div class="content">
            <!-- 排序 -->
            <div class="sortBar">
              <div class="sorts">
                <span class="name">排序：</span>
                <a class="sort sort-default">默认</a>
                <a class="sort sort-default">综合</a>
                <a class="sort" @click="change_price">
                  <span>价格</span>
                  <div class="icons">
                    <img src="@/assets/img/上下.png" v-if="price_default==0">
                    <img src="@/assets/img/上.png" v-if="price_default==1">
                    <img src="@/assets/img/下.png" v-if="price_default==2">
                  </div>
                </a>
                <a class="sort" @click="change_sale">
                  <span>销量</span>
                  <div class="icons">
                    <img src="@/assets/img/上下.png" v-if="sale_default==0">
                    <img src="@/assets/img/上.png" v-if="sale_default==1">
                    <img src="@/assets/img/下.png" v-if="sale_default==2">
                  </div>
                </a>
              </div>
            </div>
            <!-- 内容 -->
            <div class="resultList">
              <div class="resultList">
                <ul class="itemList clearfix">
                  <li class="item" v-for="(item,index) in $store.state.searchList" :key='index'>
                    <div class="product">
                      <div class="hd">
                        <router-link :to="'/detail?id='+item.id">
                          <img :src="item.img" alt="item.name">
                        </router-link>
                      </div>
                      <div class="bd">
                        <h4 class="name">
                          <router-link :to="'/?id='+item.id">
                            <span>{{item.name}}</span>
                          </router-link>
                        </h4>
                        <p class="price">
                          <span>￥</span>
                          <span>{{item.price}}</span>
                        </p>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <el-pagination style="text-align: center"
                           background
                           layout="prev, pager, next"
                           :total="1000">
            </el-pagination>
          </div>


        </div>
      </div>
      <my-footer></my-footer>
    </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import crumbs from "../common/crumbs";
    export default {
      name: "search",
      components:{
          MyHeader,
          MyFooter,
          crumbs
      },
      data(){
        return{
          price_default:0,
          sale_default:0
        }
      },
      methods:{
        change_price(){
          if (this.price_default==0){
            this.price_default=1
          }
          if(this.price_default==1){
            this.price_default=2
          }else if(this.price_default==2){
            this.price_default=1
          }
          this.sale_default = 0
        },
        change_sale(){
          if (this.sale_default==0){
            this.sale_default=1
          }
          if(this.sale_default==1){
            this.sale_default=2
          }else if(this.sale_default==2){
            this.sale_default=1
          }
          this.price_default = 0
        }
      }
    }
</script>

<style lang="scss" scoped>
  .searchBox{
    background-color: #f5f5f5;
    .content{
      padding: 0 40px;
      background-color: #fff;
      .sortBar{
        border-bottom: 1px solid #eaeaea;
        overflow: hidden;
        .active{
          color: #b4a078;
        }
        .sorts{
          position: relative;
          overflow: hidden;
          padding: 20px 0;
          line-height: 1;
          display: flex;
          border-top: 1px dashed #dedede;
          &:first-child {
            border-top: none;
          }
          a{
            cursor: pointer;
            display: flex;
            div.icons{
              position: relative;
              img{
                height: 13px;
                width: 13px;
                padding-left: 2px;
                padding-top: 1px;
              }
              /*i{*/
              /*  font-size: 12px;*/
              /*  &.active{*/
              /*    color: #b4a078;*/
              /*  }*/
              /*  &:nth-child(1){*/
              /*    position: absolute;*/
              /*    top:2px;*/
              /*  }*/
              /*  &:nth-child(2){*/
              /*    position: absolute;*/
              /*    top:5px;*/
              /*  }*/
              /*}*/
            }
          }
          .sort{
            margin-right: 30px;
            font-size: 14px;
          }
          .name{
          }
        }
      }
      .resultList{
        margin: 25px auto 0;
        .itemList{
          margin-right: -10px;
          .item{
            float: left;
            margin-right: 10px;
            margin-bottom: 50px;
            .product{
              line-height: 1;
              text-align: center;
              font-size: 13px;
              position: relative;
              width: 245px;
              height: 320px;
              &:hover{
                box-shadow: 1px 1px 8px rgba(0,0,0,.2);
                background-color: #f4f0ea;
              }
              .img {
                width: 245px;
                height: 245px;
                transition: transform 1s;
                background-color: #f4f4f4;
                color: #f4f4f4;
                display: block;
                margin: 0 auto;
              }
              .name{
                margin-bottom: 4px;
                height: 20px;
                line-height: 20px;
                padding: 0 10px;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
              }
              .price{
                color: #d4282d;
                text-align: center;
                display: block;
                span {
                  display: inline-block;
                  overflow: hidden;
                  height: 20px;
                  line-height: 22px;
                }
              }
              .hd{
                position: relative;
                margin-bottom: 8px;
                overflow: hidden;
                background-color: #f4f4f4;
                a{

                }
              }
              .bd{
                .prdtTags{
                  height: 20px;
                  font-size: 0;
                  color: #fff;
                  width: 200px;
                  margin: 0 auto 3px;
                  overflow: hidden;
                  .itemTag{
                    display: inline-block;
                    height: 20px;
                    line-height: 20px;
                    color: #fff;
                    padding: 0 5px;
                    font-size: 12px;
                    background-color: #e36844;
                    &:first-child {
                      margin-left: 0;
                    }
                    &.hot{
                      background-color: #F28F2D;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
</style>


