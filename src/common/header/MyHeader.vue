<template>
  <div class="header" style="height: 176px;">
    <div class="top">
      <!-- topInfo -->
       <div class="siteNav">
        <div class="row">
          <!-- left信息 -->
          <div class="siteNav-l">
            <div class="siteNavItem">
              <div class="siteNavItemHd">
                <div class="noticeList">
                  <div class="noticeListUL">
                    <div class="noticeItem">
                      <a href="" class="noticeTxt" title="text">欢迎来到多点超市，新用户首单9.5折！优惠多多</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- right信息 -->
          <div class="siteNav-r">
            <div class="siteNavItem">
              <div class="siteNavItemHd">
                <div v-if="$store.state.login  == false">
                  <a class="siteNavItem" @click="Login">登录</a>
                  <span class="siteNavItem">/</span>
                  <a class="siteNavItem">注册</a>
                </div>
              </div>
            </div>
            <div class="siteNavItem" v-for="(item,index) in siteNavList" :key="index">
              <div class="siteNavItemHd pipe">
                <a :href="item.url">{{item.text}}</a>
                <i v-if="item.more" class="icon icon-down_s"></i>
              </div>
              <div class="siteNavItemBd" v-if="item.more">
                <div class="dropdownMenu" >
                  <router-link class="dropdownMenuItem" v-for="(itema,indexa) in item.more" :key="indexa" :to="item.url">{{itema.text}}</router-link>
                  <!-- <a href="" class="dropdownMenuItem" v-for="(itema,indexa) in item.more" :key="indexa">{{itema.text}}</a> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 主信息 -->
      <MyTop v-if="isShowTitle" />
      <!-- 次信息 -->
      <div v-else class="systemTop">
        <div class="row">
          <div class="left">
            <router-link to="/">
              <i class="logoIcon"></i>
            </router-link>
            <span class="systemName">{{title}}</span>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import MyTop from "./MyTop.vue"
export default {
  components:{  MyTop },
  name: 'MyHeader',
  props:{
    headType:{
      type:Boolean,
      default:true
    },
    title:{
      type:String,
      default:''
    }
  },
  data(){
    return{
      isShowTitle:this.headType,
      siteNavList :[
        {text:'我的订单',url:'/login'},
        {text:'会员中心',url:'/user'},
        // {text:'企业采购通道',url:'',
        //   more:[
        //     {text:'企业购',url:''},
        //     {text:'礼品卡',url:''},
        //     {text:'联系我们',url:''},
        //   ]
        // },
        // {text:'客户服务',url:'',
        //   more:[
        //     {text:'在线客服',url:''},
        //     {text:'帮助中心',url:''},
        //     {text:'商务合作',url:''},
        //     {text:'开放平台',url:''},
        //   ]
        // },
      ]
    }
  },
  created(){

  },
  mounted(){
  },
  methods:{
    // 显示login
    Login(){
      this.$router.push('/login')
    },
    // 隐藏 login
    closeLogin(){
      this.$refs.login.close()
    }
  },
}
</script>

<style lang="scss">
  .header{
    .top{
      position: relative;
      z-index: 2;
    }
    .systemTop{
      height: 100px;
      line-height: 100px;
      background: #fff;
      box-shadow: 0 1px 10px 0 rgba(0,0,0,.1);
      .row{height: 100%}
      .left{
        display: flex;
        align-content: center;
        height: 100%;
        align-items: center;
        a{
          display: inline-block;
        }
        .logoIcon{
          display: block;
          background-position: 0 -98px;
          height: 30px;
          width: 90px;
          /*background-image: -webkit-image-set(url(../../assets/img/iconMore.png) 2x);*/
          background-position: 0 -272px;
        }
      }
      .systemName {
        display: inline-block;
        padding-left: 17px;
        margin-left: 20px;
        font-size: 24px;
        line-height: 24px;
        font-weight: 400;
        color: #b4a078;
        border-left: 1px solid #b4a078;
        vertical-align: middle;
      }
    }
    .siteNav {
        position: relative;
        height: 36px;
        line-height: 36px;
        background-color: #333;
        z-index: 5;
        a{
          display: inline-block;
          color: #ccc;
        }
        .siteNav-l{
          .siteNavItem{
            cursor: pointer;
            float: left;
            margin-left: 10px;
            position: relative;
            color: #ccc;
            .siteNavItemHd {
              font-size: 12px;
              height: 36px;
              line-height: 36px;
              cursor: pointer;
              .noticeList {
                margin-left: 2px;
                overflow: hidden;
                height: 36px;
                line-height: 36px;
                background: url(//yanxuan.nosdn.127.net/d132c2561f18f1149d566a60d05fd9b7.gif) center left no-repeat;
                .noticeListUL {
                  position: relative;
                  list-style: none;
                  top: 0;
                  .noticeItem {
                    padding-left: 26px;
                    height: 36px;
                    .noticeTxt {
                      color: #b4a078;
                      font-size: 12px;
                      &:hover {
                        color: #fff;
                      }
                    }

                  }
                }
              }
            }
          }
        }
        .siteNav-r{
          float: right;
          .siteNavItem{
            float: left;
            margin-left: 10px;
            position: relative;
            color: #ccc;
            &:hover .siteNavItemBd{
              display: block;
            }
            .pipe:before {
              content: '';
              display: inline-block;
              height: 16px;
              border-left: 1px solid #5c5c5c;
              vertical-align: middle;
            }
            .pipe:before {
              margin-right: 10px;
            }
            .siteNavItemHd{
              font-size: 12px;
              height: 36px;
              line-height: 36px;
              cursor: pointer;
            }
            .siteNavItemBd{
              display: none;
              .dropdownMenu {
                position: absolute;
                background-color: #fff;
                border: 1px solid #ddd;
                min-width: 83px;
                padding: 3px 0;
                box-shadow: 0 0 3px 0 rgba(0,0,0,.2);
                .dropdownMenuItem {
                  position: relative;
                  display: block;
                  margin: 0 13px;
                  color: #999;
                  text-align: center;
                  line-height: 38px;
                  border-top: 1px solid #ddd;
                  white-space: nowrap;
                  font-size: 12px;
                  text-decoration: none;
                  cursor: pointer;
                  &:hover {
                    color: #b4a078;
                  }
                }
                .dropdownMenuItem:first-child {
                      border-top: 0;
                  }
              }
            }
          }
        }
      }


  }
</style>
