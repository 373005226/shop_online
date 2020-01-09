<template>
  <div style="display: flex;flex-direction: row;height: 150px;">
      <span>
        <img src="@/assets/img/L的小店.png" class="logo">
      </span>
    <div style="display: flex;flex-direction: row;padding-top: 47px;position:absolute;left: 45vw">
        <el-input v-model="input" style="width: 360px;" placeholder="搜索你想要的商品" clearable ></el-input>
      <el-button style="height: 40px;">搜索</el-button>
    </div>
  </div>
</template>

<script>
  export default {
    name: "search",
    data() {
      return {
        input: ''
      }
    }
  }
</script>

<style scoped>
  .logo{
    height: 130px;
    padding-left: 10vw;
  }
</style>
