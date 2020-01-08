<template>
  <div>
    <el-row class="banner_top">
      <el-col :span="2" :offset="5" class="active_banner_top">
        全部分类
      </el-col>
      <el-col :span="3" v-for="(item,index) in catelogy" :key="index">
        {{item.name}}
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "banner_top",
    data(){
      return{
        catelogy:[
          {name:'秒杀商城'},
          {name:"新品专场"},
          {name:'生鲜专场'}
        ]
      }
    }
  }
</script>

<style scoped>
  .active_banner_top{
    background: #c5c5c5;
    color: #F1E7CC;
  }
  .banner_top {
    /*background: #F3780D;*/
    /*background-color: #ff6700;*/
    /*background-image: linear-gradient(62deg, #ff6700 0%, #F7CE68 100%);*/
    color: #606266;
    height: 40px;
    line-height: 40px;
    text-align: center;
  }

  .el-col-3:hover {
    color: #EDB424;
    transition: all 0.25s;
  }
</style>
