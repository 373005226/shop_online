<template>
  <div class="nodata">
    <div class="nodataImg" :style="{'background-position':position}">

    </div>
    <div class="nodataText">
      {{nodataText}}
    </div>
  </div>
</template>

<script>
  export default {
    name: 'nodata',
    props:{
      position:{
        tpye:String,
        default:' ' // 0 -760px;
      },
      nodataText:{
        type:String,
        default:'暂无数据'
      }
    }
  }
</script>

<style lang="scss" scoped>
  .nodata{
    margin: 150px auto 150px;
    text-align: center;
    .nodataImg{
      height: 180px;
      width: 180px;
      background-image: url(../../assets/img/nodata.png);
      background-repeat: no-repeat;
      background-size: cover;
      margin: 0 auto;
    }
    .nodataText{
      font-size: 16px;
      color: #999;
    }
  }
</style>
