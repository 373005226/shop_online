<template>
    <div>
        <MyHeader />
        <div class="addressBox">
            <div class="row">
                <!-- 面包屑 -->
                <div class="crumbs">
                    <router-link  to="/">首页</router-link>
                    <div class="icon icon-right_s"></div>
                    <span class="">地址管理</span>
                </div>
                <div class="content">
                    <UserSide />
                    <div class="addressContent">
                        <div class="addressHeader">
                            <div class="leftInfo">已保存收货地址(地址最多20条，还能保存19条)</div>
                            <a @click="showForm" class="rightInfo" href="javascript:;">+新建地址</a>
                        </div>
                        <table class="addressList">
                            <tbody>
                                <tr>
                                    <th>收货人</th>
                                    <th>地址</th>
                                    <th>联系方式</th>
                                    <th>操作</th>
                                    <th></th>
                                </tr>
                            </tbody>
                            <tbody v-if="$store.state.addressList.length !=0">
                                <tr v-for="(item,index) in $store.state.addressList" :key='index'>
                                    <td >{{item.user_name}}</td>
                                    <td >{{item.province}}{{item.city}}{{item.area}}{{item.detailed}}</td>
                                    <td>{{item.user_phone}}</td>
                                    <td>
                                        <a class="update" href="javascript:;" @click="showForm">编辑</a>
                                        <a class="delete" href="javascript:;">删除</a>
                                    </td>
                                    <td>
                                        <span v-if="item.isDefault" class="ghost">{{item.isDefault ? '默认地址' :''}}</span>
                                        <a v-else href="javascript:;" class="setDefault">设为默认地址</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                      <div v-if="$store.state.addressList.length ==0" class="none">
                        <img src="@/assets/img/nosearch.png">
                      </div>
                    </div>
                </div>
            </div>
        </div>
        <MyFooter />
        <Popup ref="addressForm" :custom="false" :maskClick="false" type="center" >
            <div class="Form">
                <div class="FormHead">新建地址</div>
                <div @click="calse" class="icon icon-close"></div>
                <AddressForm @calse='calse' />
            </div>
		</Popup>
        <!-- 添加修改 -->

    </div>
</template>

<script>
import MyHeader from "@/common/header/MyHeader.vue";
import MyFooter from "@/common/footer/MyFooter.vue";
import UserSide from "@/common/UserSide.vue";
import AddressForm from "@/components/User/AddressForm.vue";
import Popup from "@/components/User/Popup.vue"

export default{
  components: {  MyHeader,  MyFooter ,UserSide,AddressForm,Popup},
    name:"Address",
    data(){
        return{
        }
    },
    created(){
      this.$store.state.mobile = localStorage.getItem('mobile')
      this.$store.state.token = localStorage.getItem('token')
      console.log(localStorage.getItem('token'))
    },
    mounted(){

    },
    methods:{
        showForm(){
            this.$refs.addressForm.open()
        },
        calse(){
            this.$refs.addressForm.close()
        }
    },
}
</script>

<style lang="scss" scoped>
  .none{
    text-align: center ;

    img{
      height: 350px;
      margin-top: 150px;
    }
  }
    .addressBox{
        .content{
            display: flex;
            .addressContent{
                width: 890px;
                margin-left: 20px;
                overflow: hidden;
                z-index: 1;
                padding-bottom: 80px;
                .addressHeader{
                    display: flex;
                    justify-content: space-between;
                    .leftInfo{
                        font-size: 14px;
                        padding-left: 10px;
                    }
                    .rightInfo{
                        color: #69c;
                        font-size: 14px;
                        padding-right: 3px;
                    }
                }
                .addressList{
                    border: 1px solid #e8e8e8;
                    margin-top: 20px;
                    margin-bottom: 20px;
                    font-size: 14px;
                    border-collapse: collapse;
                    border-spacing: 0;
                    table-layout: fixed;
                    font-weight: 400;
                    th {
                        width: 140px;
                        text-align: center;
                        font-weight: 400;
                        height: 43px;
                        color: #999;
                        border-bottom: 1px solid #e8e8e8;
                        background-color: #f5f5f5;
                        &:nth-child(2){
                            width: 320px;
                        }
                        &:nth-child(3){
                            width: 170px;
                        }
                    }
                    tr:hover{
                        background-color: #f5f5f5;
                    }
                    td {
                        height: 100px;
                        text-align: center;
                        word-wrap: break-word;
                        word-break: break-all;
                        .update{
                            color: #69c;
                        }
                        .delete{
                            color: #69c;
                            margin-left: 15px;
                        }
                    }
                    .ghost{
                        display: inline-block;
                        border-radius: 2px;
                        width: 96px;
                        height: 28px;
                        padding: 0;
                        letter-spacing: normal;
                        line-height: 26px;
                        font-size: 12px;
                        text-align: center;
                        color: #c0ae8a;
                        border: 1px solid #c0ae8a;
                        background-color: #fff;
                        cursor: pointer;
                    }
                    .setDefault{
                        color: #69c;
                    }
                }
            }
        }
    }

    .Form{
        position: relative;
        width: 697px;
        height: 422px;
        padding: 30px 40px 0;
        min-height: 274px;
        margin: 0 auto;
        background-color: #fff;
        z-index: 10;
        .FormHead{
            font-size: 18px;
            margin-bottom: 40px;
            line-height: 1;
        }
        .icon{
            display: inline-block;
            overflow: hidden;
            vertical-align: top;
            font-size: 12px;
            word-spacing: normal;
            letter-spacing: normal;
            width: 24px;
            font-size: 24px;
            height: 24px;
            right:40px;
            top: 20px;
            position: absolute;
            cursor: pointer;
        }
    }
</style>

