<template>
    <div>
      <my-header></my-header>
      <div class="bg">
        <div class="login_content">
          <form>
            <div class="content">
              <h3>手机登录</h3>
              <div class="username">
                <input type="text" class="usernameinput" placeholder="用户名/手机号">
              </div>
              <div class="password">
                <input type="text" class="passwordinout" placeholder="验证码">
                <el-button type="primary" class="send">发送验证码</el-button>
              </div>
              <button type="sub mit" class="login">
                登录
              </button>
              <h6 class="bottom">忘记密码</h6>
              <h6 class="bottom">注册用户</h6>
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
    background: rgba(233,233,242,0.9);
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
    height: 47px;
    width: 100% ;
  }
  .password{
    margin-top: 10px;
    border: 1px solid white;
  }
  .passwordinout{
    height: 47px;
    width: 70%;
  }
  input::-webkit-input-placeholder{
    font-size: 16px;
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
  }
  .login:hover{
    background-color: #f52b00;
  }
  .bottom{
    float: right;
    padding-top: 20px;
    padding-right: 10px ;
    cursor: pointer;
  }
  .bottom:hover{
    color: orange;
  }
</style>
