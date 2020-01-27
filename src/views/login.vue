<template>
    <div>
      <my-header></my-header>
      <div class="bg">
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
</style>
