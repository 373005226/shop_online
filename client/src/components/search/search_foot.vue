<template>
  <div class="nav-sub fixed">
    <div class="nav-sub-wrapper fixed">
      <div>
        <div class="nav-list2">
          <div class="home">
            <router-link :to="{name:'home'}">
              首页
            </router-link>
          </div>
          <div class="search">
            搜索
            <strong>"{{$route.query.keys}}"</strong>
            共
            <strong>{{$store.state.searchlist.results.length}}条</strong>
            结果
          </div>
        </div>
        <div></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "search_foot",
    data(){
      return{
        searchnum:0,
      }
    },
    created() {

    }
  }
</script>

<style scoped lang="scss">
  .search{
    padding-left: 20px;
  }
  .home{
    padding-left: 20px;
    cursor: pointer;
    &:hover{
      color: #95C3ED;
    }
  }
  .nav-sub {
    position: relative;
    z-index: 20;
    height: 50px;
    background: #f7f7f7;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .04);
    &.fixed {
      /*height: 60px;*/
      left: 0;
      right: 0;
      border-bottom: 1px solid #dadada;
      background-image: -webkit-linear-gradient(#fff, #f1f1f1);
      background-image: linear-gradient(#fff, #f1f1f1);
    }
    .nav-sub-wrapper {
      padding: 31px 0;
      height: 90px;
      position: relative;
      &.fixed {
        padding: 0;
        height: 100%;
        display: flex;
        align-items: center;
        margin: 0 auto;
        width: 1220px;
      }
      &:after {
        content: " ";
        position: absolute;
        top: 89px;
        left: 50%;
        margin-left: -610px;
        width: 1220px;
        background: #000;
        height: 1px;
        display: none;
        opacity: 0;
        -webkit-transition: opacity .3s ease-in;
        transition: opacity .3s ease-in;
      }
    }
    .w {
      display: flex;
      justify-content: space-between;
    }
    .nav-list2 {
      height: 28px;
      line-height: 28px;
      display: flex;
      align-items: center;
      height: 100%;
      li:before {
        content: ' ';
        position: absolute;
        left: 0;
        top: 13px;
        width: 2px;
        height: 2px;
        background: #bdbdbd;
      }
    }
  }
</style>
