<template>
  <div class="addr" >
    <el-form :model="formInline">
      <div class="row-addr">
        <div class="label">
          <span>*</span>
          <span class="text">所在地区 :</span>
        </div>
        <div class="data">
          <!--              <v-distpicker province="" city="" area=""></v-distpicker>-->
          <el-cascader
            size="large"
            :options="options"
            v-model="formInline.selectedOptions"
            @change="handleChange">
          </el-cascader>
        </div>
      </div>
      <div class="row-addr">
        <div class="label">
          <span>*</span>
          <span class="text">详细地址 :</span>
        </div>
        <div class="data">
          <textarea placeholder="详细地址，街道、门牌号等" name="address" id="" cols="30" rows="10" tabindex="6" class="w-textarea" v-model="formInline.detail" ></textarea>
        </div>
      </div>
      <div class="row-addr inp">
        <div class="col-2">
          <div class="label">
            <span>*</span>
            <span class="text">收货人 :</span>
          </div>
          <div class="data">
            <input type="text" class="w-ipt" name="name" value="" tabindex="1" v-model="formInline.username" >
          </div>
        </div>
        <div class="col-2">
          <div class="label">
            <span>*</span>
            <span class="text">手机号码 :</span>
          </div>
          <div class="data">
            <input type="text" class="w-ipt" name="phone" value="" tabindex="1"  v-model="formInline.phone">
          </div>
        </div>

      </div>
      <div class="btns">
        <el-button type="primary" plain @click="submitForm(formInline)">提交</el-button>
        <el-button type="danger" plain @click="calsechange">取消</el-button>
      </div>

    </el-form>
  </div>
</template>

<script>
  import { regionData } from 'element-china-area-data'
  import { CodeToText } from 'element-china-area-data'
  import {TextToCode } from 'element-china-area-data'
  import axios from 'axios'
  export default {
    name: 'changeAddressForm',
    props:['information'],
    data(){
      return{
        options: regionData,
        id:'',
        formInline:{
          selectedOptions: [],
          detail:'',
          username:'',
          phone:''
        }
      }
    },
    created(){
      console.log(this.information.changeaddressform.$attrs.information[0])
      // console.log(TextToCode[this.information.changeaddressform.$attrs.information[0].province].code)
      // console.log(TextToCode[this.information.changeaddressform.$attrs.information[0].province][this.information.changeaddressform.$attrs.information[0].city].code)
      // console.log(TextToCode[this.information.changeaddressform.$attrs.information[0].province][this.information.changeaddressform.$attrs.information[0].city][this.information.changeaddressform.$attrs.information[0].district].code)
      // console.log(this.information.changeaddressform.$attrs.information[0].address)
      // console.log(this.information.changeaddressform.$attrs.information[0].signer_name)
      // console.log(this.information.changeaddressform.$attrs.information[0].signer_mobile)
      this.id = this.information.changeaddressform.$attrs.information[0].id
      this.formInline.selectedOptions[0] = TextToCode[this.information.changeaddressform.$attrs.information[0].province].code
      this.formInline.selectedOptions[1] = TextToCode[this.information.changeaddressform.$attrs.information[0].province][this.information.changeaddressform.$attrs.information[0].city].code
      this.formInline.selectedOptions[2] = TextToCode[this.information.changeaddressform.$attrs.information[0].province][this.information.changeaddressform.$attrs.information[0].city][this.information.changeaddressform.$attrs.information[0].district].code
      this.formInline.detail = this.information.changeaddressform.$attrs.information[0].address
      this.formInline.username = this.information.changeaddressform.$attrs.information[0].signer_name
      this.formInline.phone = this.information.changeaddressform.$attrs.information[0].signer_mobile


    },
    methods:{
      // 关闭 弹框
      calsechange(){
        this.$emit('calsechange')
      },
      handleChange (value) {
        console.log(value)
        console.log(CodeToText[value[0]]+CodeToText[value[1]]+CodeToText[value[2]])
      },
      submitForm(FormName){
        console.log(FormName)
        axios({
          method: 'put',
          url:'http://127.0.0.1:8000/address/'+ this.id +'/',
          data:{
            id:this.id,
            province:CodeToText[FormName.selectedOptions[0]],
            city:CodeToText[FormName.selectedOptions[1]],
            district:CodeToText[FormName.selectedOptions[2]],
            address:FormName.detail,
            signer_name:FormName.username,
            signer_mobile:FormName.phone
          },
          headers:{
            'Authorization' : 'JWT '+localStorage.getItem('token')
          },
          timeout:1000
        }).then(res=>{
          console.log(res)
        }).catch(error =>{
          console.log(error)
        })

        this.$emit('calsechange')
      }
    },
    computed:{
    }
  }
</script>

<style lang="scss" scoped>
  .addr{
    font-size: 14px;
    width: 617px;
    .inp{
      display: flex;
      justify-content: space-between;
    }
    .row-addr{
      margin-top: 20px;
      line-height: 1;
      position: relative;
      clear: both;
      display: flex;
      .label{
        width: 70px;
        margin-right: 20px;
        display: inline-block;
        font-size: 14px;
        text-align: right;
        line-height: 40px;
        span{
          &:nth-child(1){
            color:red;
          }
        }
      }
      .data{
        font-size: 14px;
        line-height: 14px;
        textarea{
          height: 70px;
          background-color: #fff;
          border: 1px solid #ddd;
          padding: 9px;
          width: 520px;
          color: #333;
          font-size: 14px;
          line-height: 14px;
        }
      }

      .col-2{
        width: 287px;
        font-size: 0;
        display: flex;
        align-items: center;
        &:nth-child(2){
          width: 290px;
        }
        .w-ipt{
          width: 200px;
          height: 34px;
          line-height: 28px;
          border: 1px solid #ddd;
          font-size: 12px;
          padding-left: 9px;
        }
      }
    }
    .btns{
      display: flex;
      /*justify-content: flex-end;*/
      /*margin: 20px 20px 0 0;*/
      width: 255px;
      margin: 20px auto;
      button{
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
        /*color: #333;*/
        /*border: 1px solid #ccc;*/
        /*background-color: #f5f5f5;*/
        height: 42px;
        line-height: 40px;
        font-size: 16px;
      }
    }
  }
</style>
