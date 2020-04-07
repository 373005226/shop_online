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

            <transition name="el-fade-in-linear">
              <div v-if="orderList.length !== 0&&this.init===0" class="orderContent">

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
                <div v-if="orderinformation.length == 0" style="text-align: center;display: flex;margin: 0 410px">
                  <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200307142112.png">
                </div>
                <div style="text-align: center" v-if="orderinformation.length == 0">
                  没有相关订单哦
                </div>

                <div class="allorder">
                  <div class="item" v-for="(item,index) in orderres" :key='index'>
                    <!--                {{item.id}}-->

                    <div class="orderMian">
                      <div class="itemHead">
                        <div class="textInfo">
                          <span class="time">下单时间：{{gettime(item.add_time)}}</span>
                          <span class="id">订单号：{{item.order_sn}}</span>
                        </div>
                        <span style="float: right">提货方式:<span
                          style="padding-left: 20px;"></span>{{getorderinformation(item.takegoods_status)}}</span>
                        <span>订单状态:<span
                          style="padding-left: 20px;color: #E36844">{{getstatus(item.pay_status)}}</span></span>
                        <div class="delete icon icon-shanchu" @click="init=4">
                          <div v-if="item.takegoods_status==='trade_evaluate'">
                            去评价
                          </div>
                        </div>
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

                            <!--                          <div class="option" style="margin:70px 120px;">-->
                            <!--                            <el-button type="danger" v-if="item.pay_status =='paying'">去付款</el-button>-->
                            <!--                            <el-button type="warning" plain v-if="item.pay_status =='TRADE_SUCCESS'">等待收款</el-button>-->
                            <!--                            <el-button type="success" disabled v-if="item.pay_status =='success'">交易已完成</el-button>-->
                            <!--                          </div>-->

                          </div>
                          <div class="itemMain" v-for="(items,indexs) in item.intergralgoods"
                               :key="indexs">

                            <div style="width: 285px;">
                              <div class="img">
                                <img :src="items.inter_goods.image"
                                     style="width: 120px;height: 120px;">
                                <div>
                                  {{items.inter_goods.name}}
                                  <span style="color: #F56C6C">[赠品]</span>
                                </div>
                              </div>
                            </div>

                            <div class="price">
                            </div>

                            <div class="number">
                              <div>{{items.goods_num}}</div>
                            </div>

                            <div class="total">
                              ￥0
                            </div>

                          </div>
                          <div style="position:relative;bottom: 100px;left: 850px;color: #409EFF"
                               v-if="item.pay_status!='paying'">
                            <el-button round @click="logistics(item.id)">查看物流</el-button>
                          </div>

                        </div>

                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </transition>

            <transition name="el-fade-in-linear">
              <div v-if="this.init===4">
                <div class="allorder">
                  <div class="item" v-for="(item,index) in orderres" :key='index'>

                    <div v-if="item.pay_status==='trade_evaluate'">
                      <div class="orderMian">
                        <div class="itemHead">
                          <div class="textInfo">
                            <span class="time">下单时间：{{gettime(item.add_time)}}</span>
                            <span class="id">订单号：{{item.order_sn}}</span>
                          </div>
                          <span style="float: right">提货方式:<span
                            style="padding-left: 20px;"></span>{{getorderinformation(item.takegoods_status)}}</span>
                          <span>订单状态:<span
                            style="padding-left: 20px;color: #E36844">{{getstatus(item.pay_status)}}</span></span>
                          <div class="delete icon icon-shanchu" @click="init=4"></div>
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
                              </div>

                            </div>
                            <div style="position:relative;bottom: 100px;left: 850px;color: #409EFF"
                                 v-if="item.pay_status!='paying'">
                              <el-button round @click="evaluate(item.id)">评价</el-button>
                            </div>

                          </div>

                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </transition>
          </div>

        </div>
      </div>
    </div>

    <el-dialog
      title="提示"
      :visible.sync="logisticsDialogVisible"
      width="30%">

      <el-timeline>
        <el-timeline-item :timestamp="logisticsinformations.picker_time" placement="top">
          <el-card>
            <h4>订单开始拣货</h4>
          </el-card>
        </el-timeline-item>

        <el-timeline-item :timestamp="logisticsinformations.Picking_complete" placement="top" v-if="logisticsinformations.pay_status==='Picking_complete'">
          <el-card>
            <h4>订单二次检验完毕，等待二次验货</h4>
          </el-card>
        </el-timeline-item>

        <el-timeline-item :timestamp="logisticsinformations.inspecter_time" placement="top" v-if="logisticsinformations.takegoods_status==='self_mention'&&logisticsinformations.inspecter!==''">
          <el-card>
            <h4>订单二次检验完毕，请尽快来超市提取</h4>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.inspecter_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='online'&&logisticsinformations.inspecter!==''">
          <el-card>
            <h4>订单二次检验完毕，等待订单分配送货任务</h4>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.distributor_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='online'&&logisticsinformations.distributor!==''">
          <el-card>
            <h4>订单已经分配完毕，等待配送人员提取货品</h4>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.distributor_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='online'&&logisticsinformations.distributor!==''&&logisticsinformations.pay_status==='Deliverying'">
          <el-card>
            <h4>订单已由送货小哥提取完毕，订单正在配送中，请您保持手机的接通状态</h4>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.delivery_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='online'&&logisticsinformations.deliveryman!==''">
          <el-card>
            <h4>配送小哥正在配送商品，请留意配送小哥电话</h4>
            <p>配送小哥电话：{{logisticsinformations.deliveryman_phone}}</p>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.success_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='online'&&logisticsinformations.success_time!==''">
          <el-card>
            <h4>订单结束，祝您购物愉快</h4>
          </el-card>
        </el-timeline-item>
        <el-timeline-item :timestamp="logisticsinformations.success_time" placement="top"
                          v-if="logisticsinformations.takegoods_status==='self_mention'&&logisticsinformations.success_time!==''&&logisticsinformations.pay_status==='trade_evaluate'||logisticsinformations.pay_status==='TRADE_SUCCESS'">
          <el-card>
            <h4>自提任务订单结束，祝您购物愉快</h4>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </el-dialog>

    <el-dialog
      title="商品评价"
      :visible.sync="evaluateDialogVisible"
      width="30%">
      <div v-for="(item,index) in evaluateinformation.goods" :key="index">
        <div style="display: flex;flex-direction: row;">
          <div style="display: flex;flex-direction: column;">
            <img :src="item.goods.images[0].image" style="width: 150px;height: 150px;">
            <span style="padding-left: 35px;padding-top: 10px;">{{item.goods.name}}</span>
          </div>

          <div style="width: 500px">
            <el-form :model="evaluateform" label-width="120px">

              <el-form-item label="评分">
                <el-rate
                  v-model="evaluateform.score"
                  show-text
                  :colors="colors" style="padding-top: 10px;font-size: 10px">
                </el-rate>
              </el-form-item>

              <!--              <el-form-item label="心得">-->
              <!--                <el-input type="textarea" v-model="evaluateform.common" :autosize="{ minRows: 5, maxRows: 8}"></el-input>-->
              <!--              </el-form-item>-->
            </el-form>
            <el-form :model="evaluateform" label-width="120px">

              <el-form-item label="心得">
                <el-input type="textarea" v-model="evaluateform.common"
                          :autosize="{ minRows: 5, maxRows: 8}"></el-input>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
      <div style="text-align: center;">
        <el-button type="primary" @click="submitevaluate">
          提交评论
        </el-button>
      </div>
    </el-dialog>


    <MyFooter/>
  </div>
</template>
<script>
  import MyHeader from "@/common/header/MyHeader.vue";
  import MyFooter from "@/common/footer/MyFooter.vue";
  import UserSide from "@/common/UserSide.vue";
  import NavTab from "@/components/User/navTab.vue";
  import {getorder} from '@/api/index'
  import {getorderdetail, postcommon, putorder} from '@/api/index'

  export default {
    components: {MyHeader, MyFooter, UserSide, NavTab},
    name: "userCollection",
    data() {
      return {
        activities: [],
        id: '',
        cur: 1,
        all: 8,
        msg: '',
        getmethods: '',
        orderid: '',
        tabList: ['全部订单', '待付款', '待发货', '已发货', '待评价'],
        init: 0,
        logisticsDialogVisible: false,
        evaluateDialogVisible: false,
        orderres: [],
        evaluateinformation: [],
        orderinformation: [],
        logisticsinformations: [],
        colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
        evaluateform: {
          score: 5,
          common: '',
          goods: 0
        },
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
        for (let i of res) {
          getorderdetail(i.id, {
            headers: {
              Authorization: 'JWT ' + localStorage.getItem('token')
            }
          }).then(result => {
            this.orderres.push(result)
          })
        }
      })
      console.log(this.orderres)
      this.orderinformation = this.orderres
    },
    methods: {
      submitevaluate() {
        console.log(this.evaluateform)
        postcommon({
          commenttext: this.evaluateform.common,
          score: this.evaluateform.score,
          goods: this.evaluateform.goods
        }, {
          headers: {
            Authorization: 'JWT ' + localStorage.getItem('token')
          }
        }).then(res => {
          console.log(res)
          putorder(this.orderid, {
            pay_status: 'TRADE_SUCCESS',
          }, {
            headers: {
              Authorization: 'JWT ' + localStorage.getItem('token')
            }
          }).then(res => {
            console.log(res)
            location.reload()
          })
        }).catch(error => {
          console.log(error)
        })
        this.evaluateDialogVisible = false
      },
      evaluate(id) {
        console.log(id)
        this.orderid = id
        this.evaluateDialogVisible = true
        for (let i of this.orderres) {
          if (i.id === id) {
            this.evaluateinformation = i
            console.log(this.evaluateinformation)
          }
        }
        this.evaluateform.goods = this.evaluateinformation.goods[0].goods.id
        console.log(this.evaluateform.goods)
      },


      logistics(id) {
        console.log(id)
        this.logisticsDialogVisible = true
        for (let i of this.orderres) {
          if (i.id === id) {
            this.logisticsinformations = i
            console.log(this.logisticsinformations)
          }
        }
      },
      getstatus(index) {
        if (index == 'TRADE_SUCCESS') {
          return '订单已完成'
        }
        if (index == "trade_evaluate") {
          return '订单已完成，等待用户评价'
        }
        if (index == 'paying') {
          return '订单支付中'
        } else {
          return '正在进行中'
        }
      },
      getorderinformation(information) {
        if (information == 'online') {
          return '线上送货'
        } else {
          return '线下自提'
        }
      },
      gettime(time) {
        return time.substring(0, 10)
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
  .Form {
    position: relative;
    width: 700px;
    /*height: 422px;*/
    padding: 30px 40px 0;
    min-height: 274px;
    margin: 0 auto;
    background-color: #fff;
    z-index: 10;

    .FormHead {
      font-size: 18px;
      margin-bottom: 40px;
      line-height: 1;
    }

    .icon {
      display: inline-block;
      overflow: hidden;
      vertical-align: top;
      font-size: 12px;
      word-spacing: normal;
      letter-spacing: normal;
      width: 24px;
      font-size: 24px;
      height: 24px;
      right: 40px;
      top: 20px;
      position: absolute;
      cursor: pointer;
    }
  }

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
            color: #E36844;
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

