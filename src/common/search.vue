<template>
    <div>
      <el-row>
        <el-col :span="12">
          <el-col :offset="8">
            <img src="../assets/img/L的小店.png" style="height: 130px;">
          </el-col>
        </el-col>

        <el-col :span="12">
          <el-col :span="8" style="padding-top: 47px;display: flex;flex-direction: row;">
            <el-input v-model="input" placeholder="搜索你想要的商品" clearable  ></el-input>
            <el-button>搜索</el-button>
          </el-col>
        </el-col>
      </el-row>
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

</style>
