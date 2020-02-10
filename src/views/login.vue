<template>
    <div>
      <my-header></my-header>
      <div class="bg">
        <div class="login_content">
          <form>
            <div class="content">
              <h3>手机登录</h3>
              <div class="username">
                <el-input
                  placeholder="用户名/手机号"
                  v-model="username"
                  class="usernameinput"
                  prefix-icon="el-icon-phone"
                  clearable>
                </el-input>
              </div>
              <div class="password">
                <el-input placeholder="请输入密码"
                          v-model="password"
                          prefix-icon="el-icon-goods"
                          show-password></el-input>
<!--                <el-button type="primary" class="send">发送验证码</el-button>-->
              </div>
              <button type="sub mit" class="login">
                登录
              </button>
              <h6 class="register">
                <router-link :to="{path:'register'}">
                  立即注册
                </router-link>
              </h6>
              <h6 class="forget">忘记密码</h6>
              <div class="bottom">
                <a href="#" class="wechat">
                  <img src="@/assets/img/wechat.png">
                  <span>微信登录</span>
                </a>
                <a href="#" class="ali">
                  <img src="@/assets/img/ali.png">
                  <span>支付宝登录</span>
                </a>
                <a href="#" class="phone">
                  <img src="@/assets/img/phone.png">
                  <span>手机号登录</span>
                </a>
              </div>
            </div>
          </form>
        </div>
      </div>
      <my-footer></my-footer>
    </div>
</template>

<script>
  import MyHeader from "../common/header/MyHeader";
  import MyFooter from "../common/footer/MyFooter";
  export default {
    name: "login",
    data(){
      return{
        username:'',
        password:''
      }
    },
    components:{
      MyHeader,
      MyFooter
    }
  }
</script>

<style scoped>
  .bg{
    background-image: url('../assets/img/bg.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    width: 100%;
    height: 700px;
  }
  .login_content{
    position: absolute;
    height: 400px;
    width: 350px;
    /*background: rgba(233,233,242,0.97);*/
    background: white;
    right: 300px;
    top: 330px;
    box-shadow: 15px 5px 20px 1px rgba(33,34,127,0.25);
    border-radius: 3px;
  }
  .content{
    /*border: 1px solid black;*/
    height: 350px;
    width: 90%;
    margin-top: 30px;
    margin-left: 18px;
  }
  .content h3{
    font-weight: bold;
  }
  .username{
    margin-top: 50px;
    border: 1px solid white;
  }
  .usernameinput{
    width: 100% ;
  }
  .password{
    margin-top: 10px;
    border: 1px solid white;
  }
  .passwordinout{
    width: 100%;
  }
  input::-webkit-input-placeholder{
    font-size: 12px;
    padding-left: 10px;
    color: #999999;
  }
  .send{
    height: 46px;
    width: 30%;
  }
  .el-button{
    padding: 0;
  }
  .login{
    width: 100%;
    margin-top: 25px;
    height: 47px;
    background-color: #FF4400;
    color: white;
    font-weight: bold;
    box-shadow: 0px 0px 0px;
    border-radius: 3px;
    border: 0px;
    cursor: pointer;
  }
  .login:hover{
    background-color: #f52b00;
  }
  .register{
    float: left;
    padding-top: 20px;
    cursor: pointer;
  }
  .register:hover{
    color: orange;
  }
  .forget{
    float: right;
    padding-top: 20px;
    padding-right: 10px ;
    cursor: pointer;
  }
  .forget:hover{
    color: orange;
  }
  .bottom{
    height: 45px;
    width: 100%;
    margin-top: 70px;
    padding-top: 20px;
  }
  .bottom img{
    height: 20px;
    width: 20px;
  }
  .bottom span{
    font-size: 12px;
    padding-left: 5px;
  }
  .wechat{
    border-right: 1px solid #999999;
    padding-right: 9px;
  }
  .wechat:hover{
    color: orange;
  }
  .ali{
    padding-left: 10px;
    border-right: 1px solid #999999;
    padding-right: 9px;
  }
  .ali:hover{
    color: orange;
  }
  .phone{
    padding-left: 10px;
  }
  .phone:hover{
    color: orange;
  }
</style>
