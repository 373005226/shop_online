<template>
  <div style="background: #EDEDED">
    <div class="banner_top">
      <div class="el-col-3">
        首页
      </div>
      <div class="el-col-3" v-for="(item,index) in catelogy" :key="index">
        {{item.name}}
      </div>
    </div>
<!--    <el-row class="banner_top">-->
<!--      <el-col :span="3" :offset="3" class="active_banner_top">-->
<!--        首页-->
<!--      </el-col>-->
<!--      <el-col :span="3" v-for="(item,index) in catelogy" :key="index">-->
<!--        {{item.name}}-->
<!--      </el-col>-->
<!--    </el-row>-->
  </div>
</template>

<script>
  export default {
    name: "banner_top",
    data(){
      return{
        catelogy:[
          {name:'折扣专场'},
          {name:"积分商城"},
          {name:'生鲜专场'},
        ]
      }
    }
  }
</script>

<style scoped>
  .active_banner_top{
    /*background: rgba(0, 0, 0, 0.25);*/
    /*color: #EBEEF5;*/
  }
  .banner_top {
    /*background: #F3780D;*/
    /*background-color: #ff6700;*/
    /*background-image: linear-gradient(62deg, #ff6700 0%, #F7CE68 100%);*/
    color: #606266;
    width: 1155px;
    margin: 0 auto;
    height: 40px;
    line-height: 40px;
    text-align: center;
  }

  .el-col-3:hover {
    color: #EDB424;
    transition: all 0.25s;
    cursor: pointer;
  }
  .el-col-3{
    padding-left: 60px;
  }
</style>
