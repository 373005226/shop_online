<template>
  <div>
    <my-header></my-header>
      <div class="register">
        <div>
          <ol class="step">
            <li :class="{active:active1}">
              <i class="step-icon">1</i>
              同意用户协议
            </li>
            <li :class="{active:active2}">
              <i class="step-icon">2</i>
              填写用户信息
            </li>
          </ol>
        </div>


        <transition name="el-fade-in">
          <div class="rg-tip" v-if="is_show1">
              <h4>注册协议</h4>
            <p>
              <strong>【审慎阅读】</strong>
              您在申请注册流程中点击同意前，应当认真阅读以下协议。
              <em>请您务必审慎阅读、充分理解协议中相关条款内容，其中包括：</em>
            </p>
            <p>
              "1、":
              <em>与您约定免除或限制责任的条款；</em>
            </p>
            <p>
              "2、":
              <em>与您约定法律适用和管辖的条款；</em>
            </p>
            <p>
              "3、":
              <em>其他以粗体下划线标识的重要条款。</em>
            </p>
            <p>如您对协议有任何疑问，可向平台客服咨询。</p>
            <p>
              <strong>【特别提示】</strong>
              当您按照注册页面提示填写信息、阅读并同意协议且完成全部注册程序后，
              即表示您已充分阅读、理解并接受协议的全部内容。如您因平台服务与本超市发生争议的，适用于
              《XXXXX平台服务协议》处理，最终解释权由本超市所有。
            </p>
            <p>
              <em>
              阅读协议的过程中，如果您不同意相关协议或其中任何条款约定，您应立即停止注册程序。
              </em>
            </p>
            <p><button class="rg-btn" @click="torgphone">同意协议</button></p>
          </div>
        </transition>

        <transition name="el-fade-in">
          <div class="rgisterphone" v-if="is_show2" >
            <el-form :model="phoneForm" status-icon  ref="phoneForm" label-width="100px">
              <el-form-item label="手机号:" prop="phone">
                <el-input type="text" v-model="phoneForm.userphone" autocomplete="off">
                  <template slot="prepend">中国大陆 +86:</template>
                </el-input>
              </el-form-item>

              <el-form-item label="验证码:" prop="code">
                <el-input type="text" v-model="phoneForm.phonecode" autocomplete="off" class="codeinput"></el-input>
                <el-button type="primary" @click="sendMessage" :disabled="btnDisabled">{{btnText}}</el-button>
              </el-form-item>

              <el-form-item label="确认密码" prop="checkPass">
                <el-input type="password" v-model="phoneForm.checkPass" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm(phoneForm)">提交</el-button>
                <el-button @click="resetForm('phoneForm')">重置</el-button>
              </el-form-item>
            </el-form>
          </div>
        </transition>

      </div>
    <my-footer></my-footer>
  </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  import {sendcode} from "@/api/index"
  import {userregister} from "@/api/index"
  export default {
    name: "register",
    components: {MyFooter, MyHeader},
    data(){
      return{
        is_show1:true,
        is_show2:false,
        active1:true,
        active2:false,
        btnText:'发送验证码',
        btnDisabled:false,
        totalTime: 60,
        phoneForm:{
          userphone:'',
          phonecode:'',
          checkPass:''
        }
      }
    },
    methods:{
      torgphone(){
        this.is_show1 = false
        this.active1 = false
        this.is_show2 = true
        this.active2 = true
      },
      resetForm(formName) {
        this.$refs[formName].resetFields()
      },
      submitForm(phoneForm){
        console.log(phoneForm)
        userregister({username:phoneForm.userphone,code:phoneForm.phonecode,mobile:phoneForm.userphone,password:phoneForm.checkPass}).then(res=>{
          console.log(res)
          // this.$store.commit('logintoken',res.token)
          // this.$store.commit('loginusername',phoneForm.userphone)
          this.userInfo.token = 'JWT '+res.token
          this.userInfo.username = phoneForm.userphone
          window.localStorage.setItem('userInfo', JSON.stringify(this.userInfo))
          // console.log(this.$store.state.mobile)
          // console.log(this.$store.state.token)
          this.$router.push({
            path:'/'
          })
        })
      },

      sendMessage() {
        if (this.btnDisabled) {
          return;
        }
        sendcode({mobile:this.phoneForm.userphone}).then(res=>{
          console.log(res)
        })
        this.getSecond(60);
      },

      //发送验证码
      getSecond(wait){
        let _this=this;
        let _wait = wait;
        if(wait == 0) {
          this.btnDisabled=false;
          this.btnText="获取验证码"
          wait = _wait;
        } else {
          this.btnDisabled=true;
          this.btnText="(" + wait + "s)后重新发送验证码"
          wait--;
          setTimeout(function() {
              _this.getSecond(wait);
            },
            1000);
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  .codeinput{
    width: 46%;
  }
  .register{
    width: 1020px;
    margin: 0 auto;
    margin-top: 30px;
  }
  .information{
    width: 1020px;
    margin: 0 auto;
    margin-top: 30px;
  }
  .step{
    width: 990px;
    color: #999;
    margin: 0 auto;
    font-size: 0;
    text-align: center;
    margin-bottom: 50px;
    border-bottom: 2px solid #e6e6e6;
    .active{
      color: #3e3e3e;
      margin-bottom: -1px;
      border-bottom: 2px solid #c40000;
      .step-icon{
        background: url("../assets/img/step_active.png") no-repeat;
        display: inline-block;
        width: 24px;
        height: 24px;
        font-size: 14px;
        text-align: center;
        line-height: 24px;
        color: #fff;
      }
    }
  }
  .step li{
    display: inline-block;
    width: 180px;
    height: 46px;
    padding-left: 30px;
    line-height: 46px;
    font-size: 16px;
    font-weight: 700;
    font-family: "微软雅黑","华文细黑",arial;
  }
  .step-icon{
    background: url("../assets/img/step.png") no-repeat;
    display: inline-block;
    width: 24px;
    height: 24px;
    font-size: 14px;
    text-align: center;
    line-height: 24px;
    color: #fff;
  }

  .rg-tip{
    margin: 30px auto;
    width: 680px;
    height: 390px;
    padding: 20px;
    font: 12px/1.5 tahoma,arial,'Hiragino Sans GB',sans-serif;
    background: #fff;
    z-index: 1000;
    border: 2px solid #ccc;
    border-top-color: #c40000;

    h4{
      font-size: 16px;
      color: #3e3e3e;
    }
    strong{
      font-weight: bold;
    }
    p{
      font-size: 12px;
      margin-top: 8px;
      margin-left: 15px;
    }
    em{
      font-weight: bold;
      text-decoration: underline;
      font-style: normal;
    }
    .rg-btn{
      width: 180px;
      height: 36px;
      text-align: center;
      font-size: 16px;
      color: #fff;
      font-weight: bold;
      border-radius: 3px;
      border: none;
      clear: both;
      display: block;
      margin: 37px auto;
      background: #e42e3c;
      cursor: pointer;
      float: none;

      &:hover{
        background: red;
        border: 1px solid red;
      }
    }
  }

  .rgisterphone{
    width: 450px;
    margin: 0 auto;
  }
  .registerinformation{
    width: 360px;
    margin: 0 auto;
  }
</style>
