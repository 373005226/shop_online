<template>
  <div class="main">
        <div class="main-nav">
            <div class="nav-first" @mouseenter="isNavEnter = true" @mouseleave="isNavEnter = false">
              <ul>
                <li v-for="(item,index) in navFirst" :key="index"
                    :class="{active: item.type === selected}"
                    @click="togoods(item.id,item.name)"
                    @mouseenter="selected = item.type">
                  <p>
                    <span>{{item.name}}</span>
                    <span class="icon">></span>
                  </p>
                </li>
              </ul>
            </div>

            <div class="nav-sec" v-show="isNavEnter || isMenuEnter"
                 @mouseenter="isMenuEnter = true" @mouseleave="isMenuEnter = false">
              <ul v-for="(item,index) in navFirst" v-show="item.type === selected" :key="index">
                <li v-for="(key,index) in navSec[item.type]" :key="index">
                  <div class="product">
                    <a :href="key.link">
                      <img :src="key.imgUrl" alt="">
                      <p class="title">{{key.title}}</p>
                    </a>
                  </div>
                </li>
              </ul>
            </div>
        </div>

  </div>
</template>

<script>
  import {catelogy} from "../../api/goods";

  export default {
    name:'MainNav',
    data() {
      return {
        selected: '',
        isNavEnter: false,
        isMenuEnter: false,
        navFirst: [
          {id:1,name: '水果蔬菜', type: 'phone'},
          {id:2,name: '肉类、海鲜', type: 'live'},
          {id:3,name: '酒水、饮料、冲饮', type: 'pad'},
          {id:4,name: '粮油、零食、宠物', type: 'tv'},
          {id:5,name: '美妆个护', type: 'charger'} ,
          {id:6,name: '医疗保健', type: 'earphone'},
          {id:7,name: '家电、家居产品', type: 'protect'},
          {id:8,name: '五金工具', type: 'card'},
          {id:9,name: '办公文具 ', type: 'bag'},
          {id:10,name: '服饰', type: 'bag'}
        ],
        navSec: {
          phone: [
            {title: '小米6', imgUrl: './static/img/xm6.png', link: 'https://www.mi.com/mi6/'},
          ],
          pad: [
            {title: '小米平板3 64GB', imgUrl: './static/img/mipad3.png', link: 'https://www.mi.com/mipad3/'},
          ],
          tv: [
            {title: '小米电视4 49英寸', imgUrl: './static/img/xmds_49.png', link: 'https://www.mi.com/mitv4/49/'},
          ],
          charger: [
            {title: '小米移动电源', imgUrl: './static/img/dianyuan.jpg', link: 'https://www.mi.com/dianyuan/'},
          ],
          earphone: [
            {title: '小米头戴式耳机', imgUrl: './static/img/toudai.jpg', link: 'https://www.mi.com/miwifihd/'},
          ],
          protect: [
            {title: '贴膜', imgUrl: './static/img/tiemo.jpg', link: 'https://list.mi.com/9'},
          ],
          card: [
            {title: '线材', imgUrl: './static/img/xiancai.jpg', link: 'https://list.mi.com/16'},
          ],
          bag: [
            {title: '箱包', imgUrl: './static/img/xiangbao.jpg', link: 'https://list.mi.com/23'},
          ],
          live: [
            {title: '米兔玩偶', imgUrl: './static/img/mitu.jpg', link: 'http://mitu.mi.com/'},
          ]
        }
      }
    },
    methods:{
      togoods(goodid,name){
        this.$router.push({
          path:'/goods',
          query:{goodid:goodid,goodname:name}
          })
      }
    },
    created() {
      catelogy().then(res=>{
        console.log(res)
        this.navFirst = res
      }).catch(err=>{
        console.log(err)
      })
    }
  }
</script>

<style lang="scss" scoped>
  .main{
    width: 1220px;
    margin: 0 auto;
  }
  .main-nav {
    font-size: 14px;
    width: 1226px;
    background: #fff;
    /*margin: 0 auto;*/
    position: absolute;
    display: flex;
    justify-content: flex-start;

    > .nav-first {
      /*width: 215px;*/
      width: 180px;
      text-align: center;
      /*height: 458px;*/
      position: relative;
      z-index: 1;
      /*padding-top: 22px;*/

      ul {
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        background: rgba(0, 0, 0, 0.3);
        padding: 5px 0;
        color: #fff;

        li {
          padding-left: 30px;
          height: 45.5px;
          line-height: 45.5px;
          cursor: pointer;

          &:hover {
            /*background: #ff6700;*/
            background: #f5803c;
            opacity: 0.7;
            transition: all 0.25s;
          }

          > p {
            display: flex;
            justify-content: space-between;

            > .icon {
              margin-right: 20px;
              font-weight: bold;
            }
          }
        }
      }
    }

    .nav-sec {
      height: 420px;
      /*margin-top: 22px;*/
      /*width: 992px;*/
      width: 40vw;
      position: relative;
      top: 0;
      left: 0.06vw;
      /*right: 1.5%;*/
      background: #fff;
      opacity: 0.6;
      z-index: 1;
      overflow: hidden;
      border: 1px solid #e0e0e0;
      border-left: none;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.35);

      ul {
        height: 458px;
        display: flex;
        flex-flow: wrap;
        flex-direction: column;
        align-items: flex-start;
        align-content: flex-start;
        justify-content: flex-start;

        li {
          width: 265px;
          height: 76px;

          .product {
            a {
              display: flex;
              justify-content: flex-start;
              align-items: center;
              transition: color .2s;
              width: 265px;
              padding: 20px 20px;

              &:hover {
                color: #ff6700;
              }

              img {
                width: 40px;
                height: 40px;
                margin-right: 12px;
              }
            }
          }
        }
      }
    }
  }
  li {
    list-style-type:none;
  }
</style>
