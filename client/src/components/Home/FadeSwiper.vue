<template>
    <div class="FadeSwiper" :style="{width:width,height:height}">
      <div class="swiperWrapper">
        <div class="swiperItem" v-for="(item,index) in banner_list" :style="{opacity:curIndex===index?1:0}" :key="index">
          <img :src="item.image">
        </div>
      </div>
      <div class="prev arrow" @click="prev"><i class="el-icon-arrow-left" /></div>
      <div class="next arrow" @click="next"><i class="el-icon-arrow-right" /></div>
      <div class="circles">
        <span v-for="(item,index) in banner_list" :key="index" @click="selectPage(index)" :class="curIndex===index?'selected':''"></span>
      </div>
    </div>
</template>

<script>
  import {banner} from "@/api/goods";

  export default {
  name: 'FadeSwiper',
  props:{
    width:{
      type:String,
      default:''
    },
    height:{
      type:String,
      default:''
    },
  },
  computed:{
  },
  data(){
    return{
      len:Object.keys(this.$slots).length,
      curIndex:0,
      timer:null,
      banner_list:[
        {
          img:require('@/assets/img/banner/banner1.jpg')
        },
        {
          img:require('@/assets/img/banner/banner2.jpg')
        },
        {
          img:require('@/assets/img/banner/banner3.jpg')
        }
      ]
    }
  },
  methods:{
    prev(){
      if(this.curIndex<=0){
        this.curIndex = this.len-1;
        return;
      }
      this.curIndex = this.curIndex-1;
    },
    next(){
      if(this.curIndex>=(this.len-1)){
        this.curIndex = 0;
        return;
      }
      this.curIndex = this.curIndex+1;
    },
    selectPage(index){
      this.curIndex=index;
    },
    clearTimer(){
      clearInterval(this.timer);
      this.timer = null;
    },
    setTimer(){
      this.timer = setInterval(this.next,5000);
    }
  },
  mounted(){
    this.setTimer();
  },
  beforeDestroyed(){
    this.clearTimer();
  },
  created() {
    banner().then(res=>{
      // console.log(res)
      this.banner_list = res
    })
  }
}
</script>

<style scoped lang="less">
@import "../../assets/css/var.less";
.FadeSwiper{
  position: relative;
  overflow: hidden;
  width: 1536px;
  margin: 0 auto;
  .swiperWrapper{
    /*width: 1536px;*/
    /*width: 100%;*/
    height: 100%;
    margin: 0 auto;
    /*position: absolute;*/
    /*top: 0;*/
    /*left: 0;*/
    .swiperItem{
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      transition: opacity 0.3s;
      overflow: hidden;
      &>*{
        width: 100%;
        height: 100%;
        display: block;
      }
    }
  }
  .arrow{
    width: 54px;
    height: 54px;
    line-height: 54px;
    top: 50%;
    /*margin-top: -27px;*/
    position: absolute;
    display: inline-block;
    vertical-align: middle;
    background-color: #FAB677;
    border-radius: 50%;
    text-align: center;
    cursor: pointer;
    opacity: 0.7;
    &:hover{
      opacity:1;
    }
    i{
      color:white;
      font-size: 20px;
    }
  }
  .prev{
    left: 2vw;
  }
  .next{
    right: 2vw;
  }
  .circles{
    position: absolute;
    bottom: 10px;
    width: 100%;
    text-align: center;
    span{
      display: inline-block;
      width: 13px;
      height: 13px;
      margin: 0 7px;
      border-radius: 50%;
      background-color: rgb(191,187,186);
      cursor: pointer;
    }
    .selected{
      background-color: rgba(0,0,0,0);
      border: 2px solid #b4a078;
      box-shadow: 0 0 0 4px #dfcead;
    }
  }
}
</style>
