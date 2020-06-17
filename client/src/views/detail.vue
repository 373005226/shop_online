<template>
  <div>
    <my-header></my-header>
    <div class="detailBox">
      <div class="row">
        <!-- 面包屑 -->
        <crumbs></crumbs>
        <!-- content -->
        <div class="content clearfixs">
          <!-- 主信息 -->
          <div class="detailHd">
            <div class="slide">
              <div class="picsWrap">
                <div class="view">
                  <div class="smallPic" v-for="(item,index) in this.goods_detail.images" :key="index">
                    <!--                    <img class="thumbImg" :src="imgs[imgInit]" alt="">-->
                    <img class="thumbImg" :src="item.image" alt="">
                  </div>
                </div>
              </div>
              <div class="list">
                <ul>
                  <li @click="imgInit = index" :class="index == imgInit? 'active' : ''"
                      v-for="(item,index) in this.goods_detail.images" :key="index">
                    <a href="javascript:;">
                      <img :src="item.image" alt="">
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="info">
              <div class="intro">
                <div class="nameInfo">
                  <div class="name">{{this.goods_detail.name}}</div>
                  <div class="desc">{{this.goods_detail.goods_brief}}</div>
                  <div class="data">
                    <span>销量</span>：{{this.goods_detail.sold_num}}
                    <span style="padding-left: 20px;">库存:{{this.goods_detail.goods_num}}</span>
                  </div>
                </div>
              </div>
              <div class="price">
                <div class="field">
                  <span class="label">价格</span>
                  <div class="data">
                    <span class="text">￥</span>
                    <span class="num"
                          v-if="this.goods_detail.specification !== undefined &&  this.goods_detail.specification.length > 0 ">{{this.goods_detail.specification[cmInit].shop_price}}</span>
                  </div>
                </div>
                <div class="field" v-if="this.goods_detail.is_discount===false">
                  <span class="label">限制</span>
                  <div class="pointCt">该商品不可使用优惠券，不可退换货</div>
                </div>
                <div class="field" v-if="this.goods_detail.is_discount===true">
                  <span class="label">优惠</span>
                  <div class="pointCt">该商品可以使用优惠券</div>
                </div>
                <hr/>
                <div class="field" v-if="this.goods_detail.is_refund===true">
                  <span class="label">服务</span>
                  <div class="policyBox">
                    ･ 支持3天无忧退换货 ･ 3小时快速退款 ･ 满150元免邮费
                  </div>
                </div>
              </div>
              <div class="">
                <div class="parampicker">
                  <!--                  <div class="specProp">-->
                  <!--                    <span class="type">颜色</span>-->
                  <!--                    <div class="cont">-->
                  <!--                      <ul class="tabs">-->
                  <!--                        <li @click="colorInit = index" class="tab-con tab tab-pic" v-for="(item,index) in colors" :key='index'>-->
                  <!--                          <a :class="index == colorInit ? 'tab-sel' : ''"  class="tab-pic" href="javascript:;">-->
                  <!--                            <img :src="item.img" alt="">-->
                  <!--                            <i class="icon-normal"></i>-->
                  <!--                          </a>-->
                  <!--                        </li>-->
                  <!--                      </ul>-->
                  <!--                    </div>-->
                  <!--                  </div>-->
                  <div class="specProp">
                    <span class="type">规格</span>
                    <div class="cont">
                      <ul class="tabs">
                        <li @click="selectspecification(index)" class="tab  tab-con"
                            v-for="(item,index) in this.specification" :key='index'>
                          <a :class="index === cmInit ? 'tab-sel' : ''" class=' tab-txt ' href="javascript:;">
                            <span>{{item.specification_text}}</span>
                          </a>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <div class="specProp">
                    <span class="type">数量</span>
                    <!--                    <div class="number cont">-->
                    <!--                      <span :class="number <= 1? 'noActive' :''" @click="numReduce" class="el-icon-minus"></span>-->
                    <!--                      <span class="number">{{number}}</span>-->
                    <!--                      <span @click="number++" class="el-icon-plus"></span>-->
                    <!--                    </div>-->
                    <div class="number cont">
                      <el-input-number v-model="num" :min="1" :max="goodtotal" label="描述文字"
                                       size="small"></el-input-number>

                    </div>
                  </div>
                </div>
              </div>
              <div class="btns">
                <el-row>
                  <el-button type="danger" @click="addcart">加入购物车</el-button>
                  <el-button type="primary" class="sets_button" @click="addfav(id)" v-if="isfav === false">
                    收藏
                  </el-button>
                  <el-button type="primary" class="sets_button" @click="delfav(id)" v-else>
                    已收藏
                  </el-button>
                </el-row>
              </div>


            </div>
          </div>
          <!-- 详情 -->
          <div class="detailBd">
            <!-- 左侧 -->
            <div class="leftInfo">
              <!-- navTab -->
              <div class="detailNavTab">
                <ul>
                  <li @click="navTabInit = index" :class="navTabInit == index ? 'active' : ''" class="item"
                      v-for="(item,index) in detailNavTab" :key="index">
                    {{item}}
                  </li>
                </ul>
              </div>
              <!-- tabContent -->
              <div class="tabContent">
                <div v-if="navTabInit == 0">
                  <img v-for="(item,index) in desc" :key='index' class="descImg" :src="item" alt="">
                </div>
                <div class="commentList" ref="comm" v-if="navTabInit === 1">
                  <!--                  <div class="navWrap">-->
                  <!--                    <div class="goodRates">-->
                  <!--                      <div class="label">好评率</div>-->
                  <!--                      <div class="goodRate">99.7%</div>-->
                  <!--                    </div>-->
                  <!--                  </div>-->
                  <div class="commons" v-for="(item,index) in userCommons" :key='index'>
                    <div class="item" v-if="item.comment!==[]">
                        <div class="commentUser">
                          <div class="avatarWarp">
                            <img :src="item.user.avatar" :alt="item.name">
                          </div>
                          <div class="username">
                            {{item.user.name}}
                          </div>
                        </div>
                        <div class="commentItem">
                          <div class="skuInfo">
                            <span style="padding-right: 10px;padding-top: 3px;">评价</span>
                            <el-rate
                              v-model="item.score"
                              disabled
                              show-score
                              text-color="#ff9900"
                              score-template="{value}">
                            </el-rate>
                          </div>
                          <div class="content">{{item.commenttext}}</div>
                        </div>
                    </div>

                  </div>

<!--                                    <el-pagination style="text-align: center"-->
<!--                                      background-->
<!--                                      layout="prev, pager, next"-->
<!--                                      :total="100">-->
<!--                                    </el-pagination>-->
                </div>

              </div>
            </div>
            <!-- 右侧热销 -->
            <div class="rightInfo">

            </div>
          </div>
        </div>
        <!-- 推荐 -->
        <!--                 <Recom />-->
      </div>
    </div>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import crumbs from "../common/crumbs";
  import {detail} from "@/api/goods";
  import {adduserfavs, getallfav, deletefav} from "@/api/index"
  import {addcart} from '@/api/index'

  export default {
    name: "detail",
    components: {
      MyHeader,
      MyFooter,
      crumbs
    },
    data() {
      return {
        id: '',
        isfav: false,
        goodtotal: 20,
        num: 1,
        imgInit: 0,
        goods_detail: [],
        imgs: [],
        // 颜色
        colorInit: 0,
        colors: [],
        // 尺码
        cmInit: 0,
        cms: [
          {id: 0, text: 'S*（165/84A）'},
        ],
        // 数量
        number: 1,
        // navTab
        navTabInit: 0,
        detailNavTab: [
          '详情', '评价',
        ],
        desc: [
          'https://yanxuan-item.nosdn.127.net/9c866dd74ed282a6516a7557aff27cad.jpg',
          'https://yanxuan-item.nosdn.127.net/ef92646728bad4d1f402a56895b19a81.jpg'
        ],
        specification:[],
        userCommons: []
      }
    },
    methods: {
      selectspecification(index){
        this.cmInit = index
        console.log(this.cmInit)
      },
      addfav(id) {
        adduserfavs({goods: id}, {
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          console.log(res)
          // location.reload()
          this.getfav()
          this.$message({
            message: '收藏商品成功',
            type: 'success'
          });
        }).catch(error => {
          if (error.response.status === 401) {
            this.$message.error('收藏失败，您尚未登录')
          }
        })
      },
      delfav(id) {
        deletefav(id, {
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          console.log(res)
          this.$message({
            message: '取消收藏商品成功',
            type: 'success'
          });
          this.getfav()
        }).catch(error => {
          if (error.response.status === 401) {
            this.$message.error('收藏失败，您尚未登录')
          }
        })
      },

      addcart() {
        addcart({
          nums: this.num,
          goods: this.id,
        }).then(res => {
          console.log(res)
          this.getdetail()
          this.$message({
            message: '加入购物车成功',
            type: 'success'
          })
        }).catch(error => {
          if (error.response.status === 401) {
            this.$message.error('加入购物车失败，您尚未登录')
          }
        })
      },
      //  判断用户是否是否收藏
      getfav() {
        getallfav({
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          this.isfav = !!(res.find(item => item.goods.id === this.id))
        })
      },
      getdetail() {
        detail(this.$route.query.id).then(res => {
          console.log(res)
          this.id = res.id
          this.goods_detail = res
          this.goodtotal = res.goods_num
          this.userCommons = res.comment
          this.specification = res.specification
        })
      }
    },
    //获取商品详情
    mounted() {
      this.getdetail()
      this.getfav()
    }
  }
</script>

<style scoped lang="scss">
  .view {
    width: 412px;
    height: 428px;
    overflow: hidden;
    display: inline-block;

    img {
      width: 412px;
      height: 428px;
    }
  }

  .collection {
    background: #FAB677;
    border-color: #FAB677;
    color: #FFF;

    &:hover {
      background: orange;
      border-color: orange;
    }
  }

  .detailBox {
    .content {
      padding: 0 0 80px;

      .detailHd {
        display: flex;
        justify-content: space-between;

        .slide {
          width: 430px;

          .picsWrap {
            height: 430px;
          }

          .view {
            position: relative;
            height: 430px;
            border: 1px solid #e8e8e8;
            margin-right: 16px;

            .thumbImg {
              display: block;
              width: 100%;
              height: 428px;
              background-color: #f4f4f4;
            }
          }

          .list {
            overflow: hidden;
            margin-top: 14px;

            ul {
              position: relative;

              li {
                position: relative;
                zoom: 1;
                width: 78px;
                height: 78px;
                overflow: hidden;
                margin-left: 10px;
                vertical-align: top;
                float: left;

                &:first-child {
                  margin-left: 0;
                }

                &.active a {
                  margin: 0;
                  border: 2px solid #35AFFB;
                }

                a {
                  box-sizing: border-box;
                  display: block;
                  width: 78px;
                  height: 78px;
                  border: 1px solid #e8e8e8;

                  img {
                    display: inline-block;
                    width: 100%;
                    height: 100%;
                  }
                }
              }
            }
          }
        }

        .info {
          width: 620px;
          word-break: break-all;
          word-wrap: break-word;
          position: relative;

          hr {
            margin: 10px 20px 10px 10px;
            overflow: hidden;
            border: none;
            height: 1px;
            border-bottom: 1px dashed #d2d2d2;
          }

          .comment {
            display: inline-block;
            position: absolute;
            top: 0;
            right: 0;
            line-height: 1.2;
            text-align: right;
            z-index: 1;
            font-weight: 400;
          }

          .intro {
            overflow: hidden;
            margin: 20px 0;
            display: flex;
            justify-content: space-between;

            .nameInfo {
              .name {
                font-size: 20px;
                font-weight: 700;
                line-height: 20px;
                margin-bottom: 7px;
                position: relative;
                padding-right: 65px;
              }

              .desc {
                width: 520px;
                font-size: 14px;
                line-height: 20px;
                color: #999;
              }

              .data {
                padding-top: 20px;
                width: 520px;
                font-size: 14px;
                line-height: 20px;
                color: #606266;
                display: flex;
                flex-direction: row;
              }
            }

            .comm {
              .num {
                color: #E36844;
                font-size: 20px;
              }

              .text {
                cursor: pointer;
                font-size: 13px;
              }
            }
          }

          .price {
            background-color: #f5f3ef;
            border-top: 1px dotted #dedede;
            border-bottom: 1px dotted #dedede;
            padding: 0 0 13px;
            line-height: 24px;
            font-size: 13px;
            position: relative;

            .field {
              display: flex;

              &:first-child .label {
                line-height: 30px;
                margin-top: 16px;
              }

              .label {
                width: 55px;
                font-size: 13px;
                float: left;
                color: #666;
                margin-left: 10px;
              }

              .data {
                font-size: 18px;
                font-weight: 700;
                margin-right: 1px;
                margin-top: 13px;
                margin-left: 0;
                height: 30px;

                .text {
                  margin-left: 0;
                  line-height: 30px;
                  color: #d7282d;
                  font-size: 18px;
                }

                .num {
                  font-size: 28px;
                  line-height: 30px;
                  margin-left: 2px;
                  color: #d7282d;
                }
              }

              .pointCt {
                color: #666;
              }

              .policyBox {
                margin-left: 0px;
                padding-top: 2px;
                line-height: 20px;
                color: #666;
              }
            }
          }

          .parampicker {
            margin-left: 10px;
            margin-top: 20px;

            .specProp {
              margin-top: 10px;
              position: relative;
              line-height: 1;
              display: flex;

              .type {
                float: left;
                font-size: 12px;
                color: #666;
                width: 54px;
                line-height: 50px;
              }

              .cont {
                position: relative;
                width: 550px;
                margin-top: 9px;

                .tabs {
                  /*margin-top: 8px;*/
                  .tab-txt {
                    padding: 0 16px;
                    line-height: 28px;
                    height: 28px;
                    font-size: 12px;
                    color: #333;
                    overflow: hidden;
                  }

                  .tab-con {
                    float: left;
                    position: relative;
                    margin-right: 10px;
                    margin-bottom: 15px;
                    vertical-align: middle;
                    padding: 1px;
                  }

                  .tab-pic {
                    width: 50px;
                    height: 50px;

                    img {
                      display: block;
                      width: 100%;
                      height: 100%;
                    }
                  }

                  .tab-sel {
                    line-height: 26px;
                    border: 2px solid #35AFFB;
                    color: #333;
                    margin-left: -1px;
                    margin-right: -1px;
                    display: block;
                    box-sizing: border-box;
                  }

                  .tab {
                    border: 1px solid #ddd;
                    float: left;
                    cursor: pointer;
                    position: relative;
                  }
                }
              }

              div.number {
                display: flex;

                span {
                  border: 1px solid #ddd;
                  text-align: center;
                  font-weight: bold;
                  color: #999;
                  cursor: pointer;
                  display: block;
                  position: relative;
                  float: left;
                  width: 36px;
                  height: 30px;
                  line-height: 28px;
                  background: #fff;
                }

                span.number {
                  width: 50px;
                }

                .noActive {
                  color: #ddd;
                }
              }
            }
          }

          .btns {
            margin-left: 12px;
            margin-top: 30px;
            font-size: 0;
            display: flex;

            .button {
              display: inline-block;
              margin-right: 10px;
              width: 168px;
              height: 50px;
              line-height: 50px;
              font-size: 18px;
              text-align: center;
            }

            .ghost {
              color: #b4a078;
              border: 1px solid #b4a078;
              background-color: #f5f3ef;
            }

            .addCart {
              color: #fff;
              border: 1px solid #b4a078;
              background-color: #b4a078;

              .icon {
                margin: 12px 8px 0 0;
                font-size: 20px;
              }
            }

            .addSc {
              position: relative;
              display: inline-block;
              height: 49px;
              width: 50px;
              border: 1px solid #CCC;
              overflow: hidden;
              text-align: center;
              cursor: pointer;

              .icon {
                position: relative;
                overflow: hidden;
                height: 24px;
                font-size: 20px;
              }

              .text {
                height: 23px;
                font-size: 13px;
                line-height: 23px;
                color: #999;
              }
            }
          }
        }
      }

      .detailBd {
        margin-top: 30px;
        display: flex;

        .leftInfo {
          width: 750px;
          margin-right: 40px;
          background-color: #f5f5f5;

          .detailNavTab {
            border-top: 1px solid #e8e8e8;
            border-bottom: 1px solid #e8e8e8;

            ul {
              display: flex;
            }

            .item {
              width: 124px;
              border-top: none;
              border-bottom: none;
              border: 1px solid #e8e8e8;
              border-left: none;
              background-color: #f5f5f5;
              height: 42px;
              box-sizing: border-box;
              line-height: 40px;
              font-size: 14px;
              position: relative;
              text-align: center;
              cursor: pointer;

              &.active {
                border-top: 3px solid #b4a078;
                background-color: #fff;
                border-bottom: 1px solid #fff;
                color: #b4a078;
              }
            }
          }

          .tabContent {
            .descImg {
              width: 100%;
              display: block;
              margin-bottom: 30px;
            }
          }

          .tabContent {
            .commentList {
              height: 800px;
              overflow: scroll;
              margin: 0 0 16px;
              border-top: none;
              background-color: #fff;
              padding-top: 27px;

              .navWrap {
                display: flex;
                padding-bottom: 20px;
                border-bottom: 1px dashed #dedede;

                .goodRates {
                  border-right: 1px solid #eaeaea;
                  width: 126px;
                  text-align: center;
                  padding-top: 4px;
                  margin-right: 20px;

                  .label {
                    font-size: 14px;
                    color: #666;
                    line-height: 14px;
                    margin-bottom: 15px;
                  }

                  .goodRate {
                    font-size: 36px;
                    color: #E36844;
                    line-height: 36px;
                    margin-bottom: 8px;
                  }
                }

                .commentNav {
                  margin: 0 20px;
                  padding: 4px 0 6px;
                  overflow: hidden;
                  font-size: 14px;

                  .title {
                    overflow: hidden;
                    line-height: 1;
                    padding-bottom: 14px;
                  }

                  .labelList {
                    span {
                      display: inline-block;
                      margin: 0 10px 10px 0;
                      padding: 0 7px 0 7px;
                      line-height: 26px;
                      border-radius: 100px;
                      background-color: #F5F3EF;
                      cursor: pointer;
                    }
                  }
                }
              }
            }
          }

          .commons {
            .addtime{
              font-size: 12px;
              padding-right: 30px;
              color: #909399;
            }
            .item {
              padding: 27px 0 30px;
              margin-left: 30px;
              margin-right: 23px;
              border-bottom: 1px dashed #e8e8e8;
              display: flex;

              &:last-child {
                border: none;
              }

              .commentUser {
                min-height: 10px;
                width: 70px;

                .avatarWarp {
                  position: relative;
                  width: 50px;
                  height: 50px;
                  margin: 0 auto;

                  img {
                    display: block;
                    width: 100%;
                    height: 100%;
                  }
                }

                .username {
                  margin-top: 12px;
                  width: 100%;
                  height: 18px;
                  line-height: 18px;
                  text-align: center;
                }
              }

              .commentItem {
                margin-left: 20px;
                font-size: 14px;
                width: 603px;

                .skuInfo {
                  color: #999;
                  line-height: 1;
                  padding-bottom: 10px;
                  display: flex;
                  flex-direction: row;
                }

                .content {
                  line-height: 20px;
                  font-size: 14px;
                  color: #333;
                  margin-bottom: 10px;
                  word-break: break-word;
                  padding: 0;
                }
              }
            }
          }
        }
      }
    }
  }
</style>


