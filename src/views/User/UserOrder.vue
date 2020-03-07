<template>
  <div>
    <MyHeader/>
    <div class="orderBox">
      <div class="row">
        <!-- 面包屑 -->
        <div class="crumbs">
          <router-link to="/">首页</router-link>
          <div class="icon icon-right_s"></div>
          <span class="">订单管理</span>
        </div>
        <div class="content">
          <UserSide/>
          <div class="orderMain">
            <NavTab :tabList="tabList" @Click="handleClick" :init='init'/>

            <div v-if="orderList.length != 0" class="orderContent">

              <div class="table-top">
                <div class="shop">
                  商品
                </div>
                <div class="price">
                  单价
                </div>
                <div class="number">
                  数量
                </div>
                <div class="allnum">
                  合计
                </div>
                <div class="option">
                  交易操作
                </div>
              </div>
              <div v-if="orderres.length == 0" style="text-align: center;display: flex;margin: 0 410px">
                <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200307142112.png">
              </div>
              <div style="text-align: center">
                没有相关订单哦
              </div>
              <div class="allorder">
                <div class="item" v-for="(item,index) in orderres" :key='index'>
                  <!--                {{item.id}}-->

                  <div class="orderMian">
                    <div class="itemHead">
                      <div class="textInfo">
                        <span class="time">下单时间：{{item.add_time}}</span>
                        <span class="id">订单号：{{item.order_sn}}</span>
                      </div>
                      <span style="float: right">提货方式:<span v-if="item.takegoods_status=='online'"
                                                            style="padding-left: 20px;"></span>线上送货</span>

                      <div class="delete icon icon-shanchu"></div>
                    </div>

                    <div style="display: flex;flex-direction: row;">

                      <div style="display: flex;flex-direction: column;">

                        <div class="itemMain" v-for="(items,indexs) in item.goods"
                             :key="indexs">

                          <div style="width: 285px;">
                            <div class="img">
                              <img :src="items.goods.images[0].image"
                                   v-if="items.goods.images[0].image!=undefined&&items.goods.images.length!=0"
                                   style="width: 120px;height: 120px;">
                              <div>
                                {{items.goods.name}}
                              </div>
                            </div>
                          </div>

                          <div class="price"
                               v-if="items.goods.specification[0]!=undefined&&items.goods.specification.length!=0">
                            {{items.goods.specification[0].shop_price}}
                          </div>

                          <div class="number">
                            <div>{{items.goods_num}}</div>
                          </div>

                          <div class="total">
                            ￥{{items.goods.specification[0].shop_price*items.goods_num}}
                          </div>

                          <div class="option" style="margin:70px 120px;">
                            <el-button type="danger" v-if="item.pay_status =='paying'">去付款</el-button>
                            <el-button type="warning" plain v-if="item.pay_status =='TRADE_SUCCESS'">等待收款</el-button>
                            <el-button type="success" disabled v-if="item.pay_status =='success'">交易已完成</el-button>
                          </div>

                        </div>


                      </div>


                    </div>
                  </div>

                </div>
              </div>
            </div>
<!--            <NoData v-if="orderres.length == 0" position="0 -760px"/>-->

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
  import NavTab from "@/components/User/navTab.vue";
  // import NoData from "../../components/User/NoData";
  import {getorder} from '@/api/index'
  import {getorderdetail} from '@/api/index'

  export default {
    components: {MyHeader, MyFooter, UserSide, NavTab},
    name: "userCollection",
    data() {
      return {
        cur: 1,
        all: 8,
        msg: '',
        getmethods: '',
        tabList: ['全部订单', '待付款', '待发货', '已发货', '待评价'],
        init: 0,
        orderres: [],
        orderList: [
          {
            goodId: 0,
            name: '草莓',
            img: 'https://img14.360buyimg.com/n7/jfs/t25519/90/761689188/694412/a788e670/5b7bd4bbN6f5e9cdb.jpg',
            price: '36',
            number: 1,
            order_sn: '92093107',
            pay_status: "TRADE_SUCCESS",
            add_time: '2020-2.24 14:55:13',
          },
        ],
      }
    },
    created() {
      getorder({
        headers: {
          Authorization: 'JWT ' + localStorage.getItem('token')
        }
      }).then(res => {
        // console.log(res)
        for (let i of res) {
          // console.log(i)
          getorderdetail(i.id, {
            headers: {
              Authorization: 'JWT ' + localStorage.getItem('token')
            }
          }).then(result => {
            // console.log(result)
            this.orderres.push(result)
          })
        }
      })
      console.log(this.orderres)
    },
    methods: {
      getmethod(method) {
        if (method == 'online') {
          return '线上送货'
        }
        if (method == 'self_mention') {
          return '线下自提'
        }
      },
      callback(data) {
        this.cur = data
        this.msg = '你点击了' + data + '页'
      },
      handleClose(e, i) {
        this.collectionList.splice(i, 1)
      },
      handleClick(i) {
        if (i == this.init) {
          return
        }
        this.init = i
        console.log(this.init)
      }
    },
  }
</script>

<style lang="scss" scoped>
  .allorder {
    height: 1000px;
    overflow-x: hidden;
    overflow-y: scroll;
  }

  .row {
    width: 1220px;
    padding-bottom: 30px;
  }

  .table-top {
    border: 1px solid #EEEEEE;
    height: 40px;
    margin-bottom: 10px;
    line-height: 40px;
    display: flex;
    flex-direction: row;
    text-align: center;

    .shop {
      width: 300px;
    }

    .price {
      width: 150px;
    }

    .number {
      width: 150px;
    }

    .allnum {
      width: 150px;
    }

    .option {
      width: 190px;
    }
  }

  .orderBox {

    .content {
      display: flex;

      .orderContent {
        margin-top: 20px;
      }

      .orderContent {
        .item {
          border: 1px solid #e8e8e8;
        }
      }

      .orderMain {
        /*width: 890px;*/
        width: 1220px;
        margin-left: 20px;
        overflow: hidden;

        .itemHead {
          background-color: #f5f5f5;
          height: 43px;
          border-bottom: 1px solid #e8e8e8;
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-size: 12px;

          .textInfo {
            margin-left: 20px;

            .id {
              margin-left: 40px;
            }
          }

          .delete {
            margin-right: 20px;
            cursor: pointer;
          }
        }

        .itemMain {
          text-align: center;
          font-size: 14px;
          display: flex;
          padding: 20px 0;
          align-items: center;

          .img {
            margin-left: 20px;

            img {
              width: 100px;
              height: 100px;
              background-color: #f4f4f4;
              margin-right: 10px;
            }
          }

          .name {
            margin-left: 10px;
            width: 220px;
            text-align: left;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
          }

          .price {
            margin-left: 85px;
          }

          .number {
            margin-left: 135px;
          }

          .total {
            margin-left: 130px;
          }

          .option {
            margin-left: 110px;
          }
        }
      }
    }
  }
</style>

