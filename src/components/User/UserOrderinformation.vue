<template>
  <div>
    <div>
<!--      如果商品的信息为拣货中-->
      <div style="color: #999999;padding-bottom: 70px" v-if="orderstatus=='Picking'">
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308155005.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">工作人员开始拣货</div>
        </div>
      </div>

      <div style="color: #999999;padding-bottom: 70px" v-if="orderstatus=='checkout'">
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308154310.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">开始由工作人员开始拣货</div>
        </div>
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308155005.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">订单已完成第二次检验，可以自提</div>
        </div>
      </div>

      <div style="color: #999999;padding-bottom: 70px" v-if="orderstatus=='Delivery'">
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308154310.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">开始由工作人员开始拣货</div>
        </div>
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308154310.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">订单已完成第二次检验</div>
        </div>
        <div style="display: flex;flex-direction: row">
          <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200308155005.png" style="width: 25px;height: 25px;">
          <div style="padding-bottom: 30px;margin-top: 3px;margin-left: 5px;">订单商品已开始送货，请留意送货人员的电话:
            <span style="color: #409EFF">{{mobile}}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="btns">
      <el-button type="primary" plain @click="calseorder">确定</el-button>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'UserOrderinformation',
    props: ['information', 'orderid'],
    data(){
      return{
        orderinformation:[],
        id:'',
        mobile:'',
        orderstatus:''
      }
    },
    created(){
      this.orderinformation = this.information.UserOrderinformation.$attrs.information
      console.log(this.orderinformation)
      this.id = this.information.UserOrderinformation.$attrs.orderid
      console.log(this.id)
      for(let i of this.orderinformation){
        if(i.id == this.id){
          console.log(i)
          this.mobile = i.operator_phone
          this.orderstatus = i.pay_status
        }
      }
      console.log(this.mobile)
      console.log(this.orderstatus)
    },
    methods:{
      // 关闭 弹框
      calseorder() {
        this.$emit('calseorder')
      },
    },
    computed:{
    }
  }
</script>

<style lang="scss" scoped>
  .btns {
    position: absolute;
    bottom: 20px;
    right: 25px;
    button {
      outline: none;
      cursor: pointer;
      border-radius: 2px;
      width: 140px;
      height: 28px;
      padding: 0;
      letter-spacing: normal;
      line-height: 26px;
      font-size: 12px;
      text-align: center;
      height: 42px;
      line-height: 40px;
      font-size: 16px;
    }
  }
</style>
