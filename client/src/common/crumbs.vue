<template>
    <div class="crumbs">
      <router-link  to="/">首页</router-link>
      <div class="el-icon-arrow-right"></div>
      <span class="">{{$route.query.goodname}}</span>
    </div>
</template>

<script>
    export default {
        name: "crumbs"
    }
</script>

<style scoped>
  .crumbs {
    font-size: 12px;
    color: #333;
    line-height: 1;
    padding-top: 20px;
    padding-bottom: 20px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    align-content: center;
  }
  .crumbs a {
    color: #333;
  }
  .crumbs .el-icon-arrow-right {
    margin: 0 5px;
    font-size: 8px;
    color: #999;
    height: 11px;
    display: inline-block;
  }
</style>
