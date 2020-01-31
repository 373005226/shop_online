<template>
  <div class="navTab" onselectstart="return false">
    <div class="innerWrap">
      <ul>
        <li class="item" :class="index == Init ? 'active' : ''" v-for="(item,index) in tabList" :key='index'>
          <a @click="handleClick(index)">{{item}}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'navTab',
    props:{
      tabList:{
        type:Array,
        default:()=>[]
      },
      init:{
        type:Number,
        default:0,
      }
    },
    watch:{
      init(val){
        this.Init = val
      }
    },
    data(){
      return{
        Init:this.init
      }
    },
    methods:{
      handleClick(i){
        this.$emit('Click',i)
      }
    }
  }
</script>

<style lang="scss" scoped>
  .navTab{
    .innerWrap{
      overflow: hidden;
      position: relative;
      display: block;
      ul{
        height:38px;
        border-bottom: 2px solid #eaeaea;
        li.item{
          box-sizing: border-box;
          position: relative;
          float: left;
          text-align: center;
          cursor: pointer;
          width: 150px;
          padding: 10px 0;
          height: 38px;
          font-weight: 900;
          font-size: 18px;
          color: #333;
          margin-bottom: -2px;
          &.active{
            border-bottom: 2px solid #b4a078;
          }
          &.active a {
            color: #b4a078;
          }
          &:first-child a {
            border: none;
          }
          a{
            display: block;
            width:100%;
            font-size: 18px;
            height: 18px;
            line-height: 1;
            border-left: 1px solid #eaeaea;
            cursor: pointer;
          }
        }
      }
    }
  }
</style>
