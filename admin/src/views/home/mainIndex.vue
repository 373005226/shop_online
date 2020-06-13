<template>
    <div>
        <shop_inspector v-if="$store.getters.getrole==='shop_inspector'"></shop_inspector>
        <order_distributor v-if="$store.getters.getrole=='order_distributor'"></order_distributor>

        <el-row :gutter="20">
            <el-col :span="8">
                <div class="main-center clearfix" id="mainleft">
                    <div class="pull-left center-left">
                        <ul>
                            <li class="accout" style="padding-top: 20px">我的账户</li>
                            <li class="tou">
                                <img src="https://txy-tc-ly-1256104767.cos.ap-guangzhou.myqcloud.com/20200313181357.png">
                                <br>
                                <span>
                  {{$store.getters.getname}}
                  <br>
                  <span>{{getrole($store.getters.getrole)}}</span>
                </span>
                            </li>
                            <li class="mobile">手机号：{{$store.getters.getmobile}}</li>
                            <!-- <li class="username">用户名：zyh</li> -->
                            <li class="time">系统版本：1.0.0</li>
                        </ul>
                    </div>
                </div>
            </el-col>


            <el-col :span="16">
                <mainEcharts id="mainEcharts" height="355px" ref="echarts"></mainEcharts>
            </el-col>
        </el-row>

        <el-row v-if="$store.getters.getusername ==='inspecter'">
            <el-col :span="24">
                <inspecter_mainIndex id="maintable"></inspecter_mainIndex>
            </el-col>
        </el-row>
        <el-row v-if="$store.getters.getusername ==='distributer'">
            <el-col :span="24">
                <order_mainIndex id="distributer"></order_mainIndex>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import mainEcharts from "../../components/ECharts/mainEcharts";
    import inspecter_mainIndex from '../../components/Table/inspecter_mainIndex'
    import order_mainIndex from "../../components/Table/order_mainIndex";
    import shop_inspector from "../../components/shortcut/shop_inspector";
    import order_distributor from "../../components/shortcut/order_distributor";

    export default {
        name: 'mainIndex',
        components: {
            mainEcharts,
            inspecter_mainIndex,
            shop_inspector,
            order_distributor,
            order_mainIndex
        },
        data() {
            return {
                wait_complete: 0,
                checkout: 0,
                isdoubt: 0,
                complete: 0
            }
        },
        mounted() {
            this.selfAdaption()
            console.log(this.getNowFormatDate())
        },
        methods: {
            getNowFormatDate() {
                var date = new Date();
                var seperator1 = "-";//设置成自己想要的日期格式 年/月/日
                var seperator2 = ":";//设置成自己想要的时间格式 时:分:秒
                var month = date.getMonth() + 1;//月
                var strDate = date.getDate();//日
                var House = date.getHours()
                var Minutes = date.getMinutes()
                if (month >= 1 && month <= 9) {
                    month = "0" + month;
                }
                if (strDate >= 0 && strDate <= 9) {
                    strDate = "0" + strDate;
                }
                if (House > 0 && House <= 9) {
                    House = "0" +House
                }
                if (Minutes > 0 && Minutes <= 9) {
                    Minutes = "0" +Minutes
                }
                var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate
                    + " " + House + seperator2 + Minutes
                    + seperator2 + date.getSeconds();
                return currentdate;
            },
            getrole() {
                if (this.$store.getters.getrole === 'boss') {
                    return '超级管理员'
                }
                if (this.$store.getters.getrole === 'order_distributor') {
                    return '订单分配员'
                }
                if (this.$store.getters.getrole === 'shop_inspector') {
                    return '超市自提商品管理员'
                }
                if (this.$store.getters.getrole === 'manager') {
                    return '后台管理员'
                }
            },
            // echart自适应
            selfAdaption() {
                let that = this
                setTimeout(() => {
                    window.onresize = function () {
                        if (that.$refs.echarts) {
                            that.$refs.echarts.chart.resize()
                        }
                    }
                }, 10)
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
    $pinkk: #eec2d3;
    $bluee: #409eff;
    $yelloww: #f4d884;
    $grennn: #89dda0;
    $purplee: #78a2ea;
    $lightBluee: #b8d6ff;

    $list: bluee pinkk yelloww grennn purplee lightBluee;
    $list1: $bluee $pinkk $yelloww $grennn $purplee $lightBluee;
    %shadow {
        background: #fff;
        -webkit-box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.2);
        box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.2);
        border-color: rgba(0, 0, 0, 0.2);

        .title {
            font-size: 14px;
            padding: 10px;

            i {
                margin-#{$right}: 5px;
            }
        }
    }

    @mixin flex($direction:row,$content:space-between) {
        display: flex;
        flex-direction: $direction;
        justify-content: space-between;
    }

    .main-center {
        width: 100%;
        /*margin-top: 20px;*/
    }

    .center-left {
        width: 100%;
        text-align: center;
        background: #FFFFFF;
        font-size: 16px;
        color: #666666;
        padding-bottom: 60px;
        -webkit-box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
        box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
        border-color: rgba(0, 0, 0, 0.05);

        .accout {
            text-align: left;
            margin: 20px;
        }

        .tou {
            margin-bottom: 20px;

            img {
                width: 85px;
                height: 85px;
                border-radius: 50%;
            }

            span {
                line-height: 25px;
            }
        }

        .mobile,
        .time {
            line-height: 30px;
        }
    }

    .card {
        color: #666;
        @extend %shadow;

        ul {
            @include flex;

            li {
                flex: 1;

                a {
                    font-size: 15px;
                    color: #666666;
                    align-items: center;
                    padding-#{$top}: 20px;
                    padding-#{$bottom}: 20px;
                    @include flex(column);

                    span {
                        height: 44px;
                    }

                    .num {
                        line-height: 44px;
                        font-size: 42px;
                        color: $bluee;
                        margin: 0px;
                    }
                }

                .iconsize {
                    font-size: 25px;
                }

                .kjfs-bluee {
                    color: $bluee;
                }

                .kjfs-pinkk {
                    color: $pinkk;
                }

                .kjfs-yelloww {
                    color: $yelloww;
                }

                .kjfs-grennn {
                    color: $grennn;
                }

                .kjfs-purplee {
                    color: $purplee;
                }

                .kjfs-lightBluee {
                    color: $lightBluee;
                }

                &:hover {
                    .kjfs-bluee {
                        color: #ffffff;
                        background: $bluee;
                    }

                    .kjfs-pinkk {
                        color: #ffffff;
                        background: $pinkk;
                    }

                    .kjfs-yelloww {
                        color: #ffffff;
                        background: $yelloww;
                    }

                    .kjfs-grennn {
                        color: #ffffff;
                        background: $grennn;
                    }

                    .kjfs-purplee {
                        color: #ffffff;
                        background: $purplee;
                    }

                    .kjfs-lightBluee {
                        color: #ffffff;
                        background: $lightBluee;
                    }
                }
            }
        }

        .table {
            padding: 21px;

            p {
                height: 52px;
                line-height: 52px;
                border: 1px solid #cccccc;
                overflow: hidden;
                border-#{$top}: none;
                @include flex(null, start);

                &:first-child {
                    border-#{$top}: 1px solid #cccccc;
                }

                span {
                }

                .tit {
                    width: 90px;
                    min-width: 90px;
                    height: 100%;
                    text-align: center;
                    border-#{$right}: 1px solid #cccccc;
                    margin-#{$right}: 18px;
                }

                span.gitbox {
                    flex: 1;
                    height: 100%;
                    overflow: hidden;
                    @include flex(row, start);

                    a {
                        &:first-child {
                            margin-#{$right}: 30px;
                        }
                    }
                }
            }
        }
    }

    #mainleft {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        border-radius: 10px;
        @extend %shadow;
    }

    #mainEcharts {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        border-radius: 10px;
        @extend %shadow;
    }

    #maintable {
        margin-#{$top}: 30px;
        padding-#{$top}: 10px;
        border-radius: 10px;
        @extend %shadow;
    }

    #distributer {
        margin-#{$top}: 30px;
        padding-#{$top}: 10px;
        border-radius: 10px;
        @extend %shadow;
    }

    #lineEcharts {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        border-radius: 10px;
        @extend %shadow;
    }

    #salestoday {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        border-radius: 10px;
        @extend %shadow;
    }

    #profit {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        border-radius: 10px;
        @extend %shadow;
    }

    #userinfo {
        margin-#{$top}: 20px;
        padding-#{$top}: 30px;
        padding-left: 30px;
        padding-bottom: 30px;
        border-radius: 10px;
        @extend %shadow;
    }
</style>
