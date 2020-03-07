<template>
    <div>
      <my-header></my-header>
        <div class="row">
            <!-- 侧栏 -->
            <UserSide />
            <!-- 内容 -->
            <div class="main">
                <div class="userInfo">
                    <div class="info">
                        <div class="infoWrap">
                            <router-link to="/" class="avatar">
                                <img src="@/assets/img/userimg.png" alt="">
                            </router-link>
                            <div class="name">
                                <div class="nickname">
                                    <router-link to="/">
                                        {{$store.state.mobile}}
                                    </router-link>
                                </div>
                            </div>
                        </div>
                        <div class="growWrap">
                            <div class="growNum">
                                <span class="f-left">
                                    <a >成长值 >></a>
                                </span>
                                <span class="f-right">
                                    <span>0</span>
                                    <span>
                                        <span>/</span>
                                        <span>1</span>
                                    </span>
                                </span>
                            </div>
                            <div class="process">
                                <div class="num" :style="{'width':0+'px'}"></div>
                            </div>
                        </div>
                    </div>
                    <div class="assets">
                        <div class="inner">
                            <div class="item" v-for="(item,index) in monerInfo" :key="index">
                                <div class="label">{{item.text}}</div>
                                <router-link :to="item.url">
                                    <span v-if="item.type == 0">￥</span>
                                    <span>{{item.number}}</span>
                                    <span v-if="item.type == 1">{{item.company}}</span>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
<!--                <div class="orderList">-->
<!--                    <div class="orderListHd">-->
<!--                        <h3>-->
<!--                            <span>未完成订单</span>-->
<!--                            <router-link class="seeAllOrder" to="/userOrder">查看全部订单</router-link>-->
<!--                        </h3>-->
<!--                    </div>-->
<!--&lt;!&ndash;                    <NoData position="0 -2000px" />&ndash;&gt;-->

<!--                </div>-->
            </div>
        </div>
        <!-- 底部 -->
        <MyFooter />
    </div>
</template>

<script>
import MyHeader from "@/common/header/MyHeader.vue";
import MyFooter from "@/common/footer/MyFooter.vue";
// import Recom from "@/components/Recom/Recom.vue";
import UserSide from "@/common/UserSide.vue";
export default{
  components: {MyHeader, MyFooter ,UserSide},
    name:"User",
    data(){
        return{
            monerInfo:[
                {text:'我的红包',number:'0.00',type:0,company:'',url:''},
                {text:'津贴',number:'0.00',type:0,company:'',url:''},
                {text:'回馈金',number:'0.00',type:0,company:'',url:''},
                {text:'可兑返利',number:'0.00',type:0,company:'',url:''},
                {text:'优惠券',number:'0.00',type:0,company:'张',url:''},
                {text:'我的积分',number:'0.00',type:0,company:'',url:''},
                {text:'礼品卡',number:'0.00',type:0,company:'',url:''},
                {text:'待领礼包',number:'0.00',type:0,company:'个',url:''},
            ]
        }
    },
  created() {
    this.$store.state.mobile = localStorage.getItem('mobile')
  }
}
</script>

<style lang="scss" scoped>
    .row{
        display: flex;
      margin-top: 52px;
    }
    .main{
        position: relative;
        width: 890px;
        margin-left: 20px;
        overflow: hidden;
        padding-bottom: 40px;
        z-index: 1;
        .userInfo{
            display: flex;
            padding: 40px 0;
            border: 1px solid #eaeaea;
            font-size: 14px;
            .info{
                width: 378px;
                margin-top: 10px;
                padding-left: 60px;
                .infoWrap {
                    margin-bottom: 30px;
                    .avatar {
                        display: inline-block;
                        width: 80px;
                        height: 80px;
                        margin-right: 40px;
                        border: 2px solid #f1f1f1;
                        border-radius: 50%;
                        img {
                            border-radius: 50%;
                            width: 100%;
                            height: 100%;
                        }
                    }
                    .name {
                        .nickname {
                            margin: 11px 0 16px;
                            max-width: 134px;
                            overflow: hidden;
                            text-overflow: ellipsis;
                            white-space: nowrap;
                        }
                    }
                    .levelname{

                    }
                }
                .growWrap {
                    width: 265px;
                }
                .process{
                    border-radius: 5px;
                    overflow: hidden;
                    margin-bottom: 19px;
                    background-color: #fff;
                    .num{
                        height: 8px;
                        background-color: #BEA988;
                    }
                }
            }
            .assets{
                width: 510px;
                padding-left: 50px;
                border-left: 1px dashed rgba(180,160,120,.38);
                line-height: 22px;
                overflow: hidden;
                .inner{
                    margin-bottom: -30px;
                    .item{
                        float: left;
                        width: 210px;
                        margin-bottom: 30px;
                        .label{
                            float: left;
                            width: 56px;
                            margin-right: 20px;
                            text-align: left;
                        }
                        .content{
                            float: left;
                            a{
                                color: #333;
                            }
                        }
                    }
                }
            }
        }
        .orderList{
            border: 1px solid #eaeaea;
            margin-top: 20px;
            color: #333;
            font-size: 14px;
            .orderListHd{
                height: 43px;
                padding: 0 30px 0 20px;
                border: 1px solid #eaeaea;
                border: none;
                background-color: #f4f4f4;
                line-height: 42px;
                h3{
                    font-weight: 400;
                    font-size: 16px;
                    color: #333;
                    display: flex;
                    justify-content: space-between;
                    .seeAllOrder{
                        font-size: 14px;
                        color: #333;
                    }
                }
            }
            .listNullWraper{
                height: 528px;
                text-align: center;
                overflow: hidden;
                .emptyStatus{
                    margin: 150px auto 0;
                    text-align: center;
                    .icon{
                        display: inline-block;
                        text-align: center;
                        height: 180px;
                        font-size: 50px;
                        width: 180px;
                    }
                    .emptyText{
                        font-size: 16px;
                        color: #999;
                    }
                    a.button{
                        display: inline-block;
                        text-align: center;
                        margin-top: 10px;
                        width: 96px;
                        height: 28px;
                        font-size: 14px;
                        line-height: 26px;
                        color: #b4a078;
                        border: 1px solid #b4a078;
                        background-color: #f5f3ef;
                    }
                }
            }
        }
    }
</style>

