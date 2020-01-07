<template>
    <div>
      <el-carousel indicator-position="outside">
        <el-carousel-item v-for="item in 4" :key="item">

        </el-carousel-item>
      </el-carousel>
    </div>
</template>

<script>
    export default {
        name: "banner"
    }
</script>

<style scoped>
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
