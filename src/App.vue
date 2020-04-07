<template>
  <div>
    <transition name="fade" mode="out-in">
      <router-view class="body"/>
    </transition>
  </div>
</template>

<style lang="less">
  @import "./assets/css/base.css";
  body{
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: all 0.12s ease;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0;
  }
</style>

