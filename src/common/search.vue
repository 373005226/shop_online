<template>
  <div style="display: flex;flex-direction: row;height: 150px;">
      <span>
        <img src="@/assets/img/L的小店.png" style="height: 130px;padding-left: 335px;">
      </span>
    <div style="display: flex;flex-direction: row;padding-top: 47px;padding-left: 100px;">
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
</style>s
