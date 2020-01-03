<template>
    <div>
      <el-row>
        <el-col :span="12">
          <div class="grid-content ">
            <el-row :gutter="20">
              <el-col :span="6" :offset="4">
                <div class="nav-title">欢迎来到线上超市!</div>
              </el-col>
              <el-col :span="5">
                <div class="nav-title">
                  <span>登录</span>
                  <span>|</span>
                  <span>注册</span>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content">

          </div>
        </el-col>
      </el-row>
    </div>
</template>

<script>
    export default {
        name: "header"
    }
</script>

<style scoped>
  .grid-content {
    background: #EEEEEE;
    border-radius: 4px;
    min-height: 36px;
  }
  .nav-title{
    line-height: 36px;
  }
  .nav-title span{
    padding-left: 30px
  }
</style>
