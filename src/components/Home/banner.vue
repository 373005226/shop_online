<template>
    <div>
      <el-carousel indicator-position="outside">
        <el-carousel-item v-for="(item,index) in banner_img" :key="index" style="height: 423px;">
          <div>
            <img :src="item.imgurl">
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
</template>

<script>
    export default {
      name: "banner",
      data(){
        return{
          banner_img:[
            {
              imgurl:require('../../assets/img/banner/banner1.jpg'),
              alt:'商品1'
            },
            {
              imgurl:require('../../assets/img/banner/banner2.jpg'),
              alt:'商品2'
            },
            {
              imgurl:require('../../assets/img/banner/banner3.jpg'),
              alt:'商品3'
            }
          ],
        }
      }
    }
</script>

<style scoped>
  .el-carousel{
    margin-right: 15vw;
    margin-left: 15vw;
  }
  .el-carousel--horizontal{
    height: 423px;
  }
  /*.el-carousel__item:nth-child(2n) {*/
  /*  background-color: #99a9bf;*/
  /*}*/

  /*.el-carousel__item:nth-child(2n+1) {*/
  /*  background-color: #d3dce6;*/
  /*}*/


</style>
