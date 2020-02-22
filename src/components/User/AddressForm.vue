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
              v-model="formInline.selectedOptions">
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
           <el-button type="danger" plain @click="calse">取消</el-button>
      </div>

    </el-form>
  </div>
</template>

<script>
  import { regionData } from 'element-china-area-data'
  import { CodeToText } from 'element-china-area-data'
  import { useraddress } from '@/api/index'
  export default {
    name: 'AddressForm',
    data(){
      return{
        options: regionData,
        formInline:{
          selectedOptions: [],
          detail:'',
          username:'',
          phone:''
        }
      }
    },
  created(){
  },
    methods:{
      // 关闭 弹框
      calse(){
          this.$emit('calse')
      },
      submitForm(FormName){
        console.log(FormName)
        useraddress({province:CodeToText[FormName.selectedOptions[0]],city:CodeToText[FormName.selectedOptions[1]],district:CodeToText[FormName.selectedOptions[2]],address:FormName.detail,signer_name:FormName.username,signer_mobile:FormName.phone}, {headers: {Authorization: 'JWT ' + localStorage.getItem('token')}}).then(res=>{
          console.log(res)
        })
          this.$emit('calse')
      },

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
