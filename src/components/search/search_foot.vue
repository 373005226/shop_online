<template>
  <div class="nav-sub fixed">
    <div class="nav-sub-wrapper fixed">
      <div>
        <ul class="nav-list2">
          <li>
            <router-link :to="{name: 'home'}">首页</router-link>
          </li>
          <li style="font-weight: bold;">
            搜索"苹果"共5条结果
          </li>
        </ul>
        <div></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "search_foot"
  }
</script>

<style scoped lang="scss">
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

      li{
        list-style: none;
      }

      li:first-child {
        padding-left: 0;
        a {
          padding-left: 10px;
        }
      }
       li {
        position: relative;
        float: left;
        padding-left: 2px;
        a {
          display: block;
          padding: 0 10px;
          color: #666;
          &.active {
            font-weight: bold;
          }
        }
        a:hover {
          color: #5683EA;
        }
      }
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
