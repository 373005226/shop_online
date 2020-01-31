<template>
    <div class="sub">
        <div class="sideBar">
            <div class="sideItem" v-for="(item,index) in sideDta" :key='index'>
                <div class="sideText">{{item.title}}</div>
                <div class="bd">
                    <ul>
                        <li v-for="(itema,indexa) in item.list" :key='indexa'>
                            <router-link :to="itema.url" :class="nowRouter == itema.url ? 'active' : ''" class="sideText">{{itema.text}}</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    export default{
        data(){
            return{
              nowRouter:this.$route.path,
                sideDta:[
                    {title:'帐号管理',list:[
                        {url:'/user',text:'个人中心'},
                        {url:'/msgCenter',text:'消息通知'},
                        {url:'',text:'账号信息'},
                        {url:'/address',text:'地址管理'},
                        {url:'',text:'账号安全'},
                        {url:'',text:'我的积分'},
                        {url:'/userCollection',text:'我的收藏'},
                        {url:'',text:'我的足迹'},
                        {url:'',text:'我的甄选家'}
                    ]},
                    {title:'交易管理',list:[
                        {url:'/userOrder',text:'订单管理'},
                        {url:'',text:'津贴'},
                        {url:'',text:'回馈金'},
                        {url:'',text:'我的红包'},
                        {url:'',text:'优惠卷'},
                        {url:'',text:'礼品卡'},
                        {url:'',text:'优先购'},
                        {url:'',text:'我的众筹'},
                    ]},
                    {title:'服务中心',list:[
                        {url:'',text:'售后记录'},
                        {url:'',text:'价格保护'},
                        {url:'',text:'帮助中心'}
                    ]},
                ]
            }
        },
        created(){

        }
    }
</script>

<style lang="scss"  scoped>
    .sub{
        position: relative;
        width: 180px;
        margin-bottom: 30px;
        .sideBar{
            border: 1px solid #eaeaea;
            padding-top: 24px;
            width: 180px;
            .sideItem{
                text-align: left;
                color: #333;
                margin-bottom: 40px;
                .sideText{
                    padding-left: 43px;
                    font-size: 16px;
                    color: #333;
                    font-weight: 700;
                    line-height: 18px;
                    margin: 16px 0;
                }
                .bd{
                    text-align: left;
                    ul{
                        li{
                            a.sideText{
                                display: block;
                                font-size: 14px;
                                display: block;
                                padding-left: 41px;
                                border-left: 2px solid #fff;
                                border-right: 2px solid #fff;
                                color: #666;
                                line-height: 18px;
                                margin: 16px 0;
                                &:hover{
                                    color: #b4a078;
                                }
                                &.active{
                                    color: #b4a078;
                                    border-left-color: #BEA988;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
</style>
