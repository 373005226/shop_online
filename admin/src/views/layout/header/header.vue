<template>
  <div>
    <el-header id="header">
      <span class="hideAside" @click="collapse"><i class="el-icon-s-fold" style="font-size: 25px"></i></span>
      <span class="hideAside"></span>
      <ul class="personal">
        <li>{{getrole($store.getters.getrole)}}</li>
        <li>
          <el-dropdown @command="handleCommand">
                  <span class="el-dropdown-link">
                    {{$store.getters.getname}}<i class="el-icon-arrow-down el-icon--right"></i>
                  </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="userinfo">基本资料</el-dropdown-item>
              <el-dropdown-item command="logout" divided >退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </li>
        <li class="icon"><img :src="avatar"/></li>
      </ul>
    </el-header>
<!--    <tabNav></tabNav>-->
  </div>
</template>

<script>
  // import Cookies from 'js-cookie'
  // import langSelect from '../../../components/lang/langSelect'
  // import tabNav from './tabNav'

  export default {
    name: 'Header',
    data () {
      return {
        isfullScreen: true,
        avatar: '',
      }
    },
    created() {
      this.avatar = this.$store.getters.getavatar
    },
    methods: {
      getrole(){
        if(this.$store.getters.getrole ==='boss'){
          return '超级管理员'
        }
        if(this.$store.getters.getrole === 'order_distributor'){
          return '订单分配员'
        }
        if(this.$store.getters.getrole === 'shop_inspector'){
          return '超市自提商品管理员'
        }
        if(this.$store.getters.getrole === 'manager'){
          return '后台管理员'
        }
      },
      collapse () {
      },
      handleCommand (command) {
        if (command === 'userinfo') {
          this.$router.push('/userinfo')
        }
        console.log(command)
        if (command === 'logout'){
          this.$store.commit('logout')
          this.$router.push({
            path:'/login'
          })
        }
      }
    }
  }
</script>

<style lang="scss">
  $top: top;
  $bottom: bottom;
  $left: left;
  $right: right;
  $leftright: ($left, $right);
  %w100 {
    width: 100%;
  }

  %h100 {
    height: 100%;
  }

  %cursor {
    cursor: pointer;
  }

  html, body, #app, .el-container, #asideNav, ul.el-menu {
    @extend %h100;
  }

  @mixin set-value($side, $value) {
    @each $prop in $leftright {
      #{$side}-#{$prop}: $value;
    }
  }

  #header {
    max-height: 50px;
    line-height: 50px;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, .05);
    display: flex;
    justify-content: space-between;
    .hideAside {
      @extend %cursor;
    }
    .personal {
      display: flex;
      flex-direction: row;
      li {
        @include set-value(margin, 13px);
        font-size: 12px;
      }
      .fullScreen {
        @extend %cursor;
      }
      .el-dropdown-link {
        @extend %cursor;
      }
      .icon img {
        margin-#{$top}: 7px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        width: 40px;
        height: 40px;
      }
    }
  }
</style>
