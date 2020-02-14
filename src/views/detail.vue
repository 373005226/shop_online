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
                  <li @click="imgInit = index" :class="index == imgInit? 'active' : ''" v-for="(item,index) in this.goods_detail.images" :key="index">
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
                </div>
                <div class="comm">
                  <div class="num">99.7%</div>
                  <a class="text">
                    <span @click="goComm">好评率</span>
                    <span class="el-icon-arrow-right"></span>
                  </a>
                </div>
              </div>
              <div class="price">
                <div class="field">
                  <span class="label">价格</span>
                  <div class="data">
                    <span class="text">￥</span>
                    <span class="num" v-if="this.goods_detail.specification !== undefined &&  this.goods_detail.specification.length > 0 ">{{this.goods_detail.specification[0].shop_price}}</span>
                  </div>
                </div>
                <div class="field">
                  <span class="label">限制</span>
                  <div class="pointCt">该商品不可使用优惠券</div>
                </div>
                <hr />
                <div class="field">
                  <span class="label">服务</span>
                  <div class="policyBox">
                    ･ 支持30天无忧退换货    ･ 48小时快速退款    ･ 满88元免邮费
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
                        <li @click="cmInit = index" class="tab  tab-con" v-for="(item,index) in this.goods_detail.specification" :key='index'>
                          <a :class="index == cmInit ? 'tab-sel' : ''"  class=' tab-txt ' href="javascript:;">
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
                      <el-input-number v-model="num" :min="1" :max="goodtotal" label="描述文字" size="small"></el-input-number>

                    </div>
                  </div>
                </div>
              </div>

<!--              <div class="btns">-->
<!--                <a @click="handleBuy" href="javascript:;" class="button ghost">立即购买</a>-->
<!--                <a href="javascript:;" class="button addCart"><span class="icon icon-gouwuche"></span> 加入购物车</a>-->
<!--                <div class="addSc">-->
<!--                  <div class="icon el-icon-star-off"></div>-->
<!--                  <div class="text">收藏</div>-->
<!--                </div>-->
<!--              </div>-->

              <div class="btns">
                <el-row>
                  <el-button type="danger">加入购物车</el-button>
                  <el-button icon="el-icon-star-on" class="collection">收藏</el-button>
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
                  <li @click="navTabInit = index" :class="navTabInit == index ? 'active' : ''" class="item" v-for="(item,index) in detailNavTab" :key="index">
                    {{item}}
                  </li>
                </ul>
              </div>
              <!-- tabContent -->
              <div class="tabContent">
                <div v-if="navTabInit == 0">
                  <img v-for="(item,index) in desc" :key='index' class="descImg" :src="item" alt="">
                </div>
                <div class="commentList" ref="comm" v-if="navTabInit == 1">
                  <div class="navWrap">
                    <div class="goodRates">
                      <div class="label">好评率</div>
                      <div class="goodRate">99.7%</div>
                    </div>
                    <div class="commentNav">
                      <div class="title">大家都在说：</div>
                      <div class="labelList">
                        <span v-for="(item,index) in comments" :key="index">{{item.text}}</span>
                      </div>
                    </div>
                  </div>
                  <div class="commons">
                    <div class="item" v-for="(item,index) in userCommons" :key='index'>
                      <div class="commentUser">
                        <div class="avatarWarp">
                          <img :src="item.img" :alt="item.name">
                        </div>
                        <div class="username">
                          {{item.name}}
                        </div>
                      </div>
                      <div class="commentItem">
                        <div class="skuInfo">{{item.type}}</div>
                        <div class="content">{{item.content}}</div>
                      </div>
                    </div>
                  </div>

                  <el-pagination style="text-align: center"
                    background
                    layout="prev, pager, next"
                    :total="100">
                  </el-pagination>

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
  import {detail} from "../api/goods";

  export default {
      name: "detail",
      components:{
        MyHeader,
        MyFooter,
        crumbs
      },
      data(){
        return{
          goodtotal:20,
          num:1,
          imgInit:0,
          goods_detail:[],
          imgs:[
            '//imgservice.suning.cn/uimg1/b2c/image/H-ybAAwUE1JVQD91xY_zlg.jpg_800w_800h_4e',
            '//imgservice.suning.cn/uimg1/b2c/image/66jxuFpIDQPWI3Sb5YWXhg.jpg_800w_800h_4e ',
            '//imgservice.suning.cn/uimg1/b2c/image/xEAGTRKFnOvPhVj82a83lA.jpg_800w_800h_4e',
            '//imgservice.suning.cn/uimg1/b2c/image/QI1d_pxunf6nQKidqE3MXg.jpg_800w_800h_4e',
            '//imgservice.suning.cn/uimg1/b2c/image/yNDGowzk4MtByRCNdnwnXg.jpg_800w_800h_4e'
          ],
          // 颜色
          colorInit:0,
          colors:[
            {id:0,img:'https://yanxuan-item.nosdn.127.net/68527c3e88af6ae1328fdcf0d1686aff.png?type=webp&imageView&thumbnail=430x430&quality=95',},
            {id:0,img:'https://yanxuan-item.nosdn.127.net/68527c3e88af6ae1328fdcf0d1686aff.png?type=webp&imageView&thumbnail=430x430&quality=95',},
            {id:0,img:'https://yanxuan-item.nosdn.127.net/68527c3e88af6ae1328fdcf0d1686aff.png?type=webp&imageView&thumbnail=430x430&quality=95',},
            {id:0,img:'https://yanxuan-item.nosdn.127.net/68527c3e88af6ae1328fdcf0d1686aff.png?type=webp&imageView&thumbnail=430x430&quality=95',},
            {id:0,img:'https://yanxuan-item.nosdn.127.net/68527c3e88af6ae1328fdcf0d1686aff.png?type=webp&imageView&thumbnail=430x430&quality=95',},
          ],
          // 尺码
          cmInit:0,
          cms:[
            {id:0,text:'S*（165/84A）'},
          ],
          // 数量
          number:1,
          // navTab
          navTabInit:0,
          detailNavTab:[
            '详情','评价（100）',
          ],
          desc:[
            'https://yanxuan-item.nosdn.127.net/9c866dd74ed282a6516a7557aff27cad.jpg',
            'https://yanxuan-item.nosdn.127.net/ef92646728bad4d1f402a56895b19a81.jpg'
          ],
          comments:[
            {text:'质量上乘'},
            {text:'性价比高'},
            {text:'很舒服'}
          ],

          userCommons:[
            {name:'1****9',img:'//yanxuan.nosdn.127.net/485ff1be6912be6ae696b6d360d1b101.png',content:'此款秋衣秋裤穿着柔软亲肤非常舒服暖和，我家人这两年都喜欢穿，以前买的纯棉的木代尔的都不穿了，现在穿的都是这款面料的是最爱了，好评！',type:'尺码:XL 颜色:藏青保暖套装',time:'2019-10-16 07:57'},
            {name:'1****9',img:'//yanxuan.nosdn.127.net/485ff1be6912be6ae696b6d360d1b101.png',content:'此款秋衣秋裤穿着柔软亲肤非常舒服暖和，我家人这两年都喜欢穿，以前买的纯棉的木代尔的都不穿了，现在穿的都是这款面料的是最爱了，好评！',type:'尺码:XL 颜色:藏青保暖套装',time:'2019-10-16 07:57'},
          ]
        }
      },
      methods:{
        _getdetailgoods(id){
          detail(id).then(res=>{
            console.log(res)
            this.goods_detail = res
            this.goodtotal = res.goods_num
          })
        },
        // 去评论
        goComm(){
          this.navTabInit = 1;
          this.$nextTick(() => {
            let commTop = this.$refs.comm.offsetTop + 80;
            // 实现滚动效果
            const timeTop = setInterval(() => {
              document.body.scrollTop = document.documentElement.scrollTop = commTop -= 10;
              if (commTop == document.documentElement.scrollTop) {
                clearInterval(timeTop);
              }
            }, 10);
          })

        },
        // 数量减
        numReduce(){
          if(this.number <= 1){
            this.number = 1;
            return
          }
          this.number--;
        },
        // 购买
        handleBuy(){
          this.$router.push('/order')
        }
      },
      created() {
        console.log(this.$route.query.id)
        this._getdetailgoods(this.$route.query.id)
        console.log(this.$route)
      }
    }
</script>

<style scoped lang="scss">
.view{
  width: 412px;
  height: 428px;
  overflow: hidden;
  display: inline-block;

  img{
    width: 412px;
    height: 428px;
  }
}

  .collection{
    background: #FAB677;
    border-color: #FAB677;
    color: #FFF;

    &:hover{
      background: orange;
      border-color: orange;
    }
  }
  .detailBox{
    .content{
      padding: 0 0 80px;
      .detailHd{
        display: flex;
        justify-content: space-between;
        .slide{
          width: 430px;
          .picsWrap{
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
          .list{
            overflow: hidden;
            margin-top: 14px;
            ul{
              position: relative;
              li{
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
                a{
                  box-sizing: border-box;
                  display: block;
                  width: 78px;
                  height: 78px;
                  border: 1px solid #e8e8e8;
                  img{
                    display: inline-block;
                    width: 100%;
                    height: 100%;
                  }
                }
              }
            }
          }
        }
        .info{
          width: 620px;
          word-break: break-all;
          word-wrap: break-word;
          position: relative;
          hr{
            margin: 10px 20px 10px 10px;
            overflow: hidden;
            border: none;
            height: 1px;
            border-bottom: 1px dashed #d2d2d2;
          }
          .comment{
            display: inline-block;
            position: absolute;
            top: 0;
            right: 0;
            line-height: 1.2;
            text-align: right;
            z-index: 1;
            font-weight: 400;
          }
          .intro{
            overflow: hidden;
            margin: 20px 0;
            display: flex;
            justify-content: space-between;
            .nameInfo{
              .name{
                font-size: 20px;
                font-weight: 700;
                line-height: 20px;
                margin-bottom: 7px;
                position: relative;
                padding-right: 65px;
              }
              .desc{
                width: 520px;
                font-size: 14px;
                line-height: 20px;
                color: #999;
              }
            }
            .comm{
              .num{
                color: #E36844;
                font-size: 20px;
              }
              .text{
                cursor: pointer;
                font-size: 13px;
              }
            }
          }
          .price{
            background-color: #f5f3ef;
            border-top: 1px dotted #dedede;
            border-bottom: 1px dotted #dedede;
            padding: 0 0 13px;
            line-height: 24px;
            font-size: 13px;
            position: relative;
            .field{
              display: flex;
              &:first-child .label{
                line-height: 30px;
                margin-top: 16px;
              }
              .label{
                width: 55px;
                font-size: 13px;
                float: left;
                color: #666;
                margin-left: 10px;
              }
              .data{
                font-size: 18px;
                font-weight: 700;
                margin-right: 1px;
                margin-top: 13px;
                margin-left: 0;
                height: 30px;
                .text{
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
              .pointCt{
                color: #666;
              }
              .policyBox{
                margin-left: 0px;
                padding-top: 2px;
                line-height: 20px;
                color: #666;
              }
            }
          }
          .parampicker{
            margin-left: 10px;
            margin-top: 20px;
            .specProp{
              margin-top: 10px;
              position: relative;
              line-height: 1;
              display: flex;
              .type{
                float: left;
                font-size: 12px;
                color: #666;
                width: 54px;
                line-height: 50px;
              }
              .cont{
                position: relative;
                width: 550px;
                margin-top: 9px;
                .tabs{
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
                    img{
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
              div.number{
                display: flex;
                span{
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
                span.number{
                  width: 50px;
                }
                .noActive{
                  color: #ddd;
                }
              }
            }
          }
          .btns{
            margin-left: 12px;
            margin-top: 30px;
            font-size: 0;
            display: flex;
            .button{
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
            .addCart{
              color: #fff;
              border: 1px solid #b4a078;
              background-color: #b4a078;
              .icon{
                margin: 12px 8px 0 0;
                font-size: 20px;
              }
            }
            .addSc{
              position: relative;
              display: inline-block;
              height: 49px;
              width: 50px;
              border: 1px solid #CCC;
              overflow: hidden;
              text-align: center;
              cursor: pointer;
              .icon{
                position: relative;
                overflow: hidden;
                height: 24px;
                font-size: 20px;
              }
              .text{
                height: 23px;
                font-size: 13px;
                line-height: 23px;
                color: #999;
              }
            }
          }
        }
      }
      .detailBd{
        margin-top: 30px;
        display: flex;
        .leftInfo{
          width: 750px;
          margin-right: 40px;
          background-color: #f5f5f5;
          .detailNavTab{
            border-top: 1px solid #e8e8e8;
            border-bottom: 1px solid #e8e8e8;
            ul{
              display: flex;
            }
            .item{
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
          .tabContent{
            .descImg{
              width: 100%;
              display: block;
              margin-bottom: 30px;
            }
          }
          .tabContent{
            .commentList{
              margin: 0 0 16px;
              border-top: none;
              background-color: #fff;
              padding-top: 27px;
              .navWrap{
                display: flex;
                padding-bottom: 20px;
                border-bottom: 1px dashed #dedede;
                .goodRates{
                  border-right: 1px solid #eaeaea;
                  width: 126px;
                  text-align: center;
                  padding-top: 4px;
                  margin-right: 20px;
                  .label{
                    font-size: 14px;
                    color: #666;
                    line-height: 14px;
                    margin-bottom: 15px;
                  }
                  .goodRate{
                    font-size: 36px;
                    color: #E36844;
                    line-height: 36px;
                    margin-bottom: 8px;
                  }
                }
                .commentNav{
                  margin: 0 20px;
                  padding: 4px 0 6px;
                  overflow: hidden;
                  font-size: 14px;
                  .title{
                    overflow: hidden;
                    line-height: 1;
                    padding-bottom: 14px;
                  }
                  .labelList{
                    span{
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
          .commons{
            .item{
              padding: 27px 0 30px;
              margin-left: 30px;
              margin-right: 23px;
              border-bottom: 1px dashed #e8e8e8;
              display: flex;
              &:last-child {
                border: none;
              }
              .commentUser{
                min-height: 10px;
                width: 70px;
                .avatarWarp{
                  position: relative;
                  width: 50px;
                  height: 50px;
                  margin: 0 auto;
                  img{
                    display: block;
                    width: 100%;
                    height: 100%;
                  }
                }
                .username{
                  margin-top: 12px;
                  width: 100%;
                  height: 18px;
                  line-height: 18px;
                  text-align: center;
                }
              }
              .commentItem{
                margin-left: 20px;
                font-size: 14px;
                width: 603px;
                .skuInfo{
                  color: #999;
                  line-height: 1;
                  padding-bottom: 10px;
                }
                .content{
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


