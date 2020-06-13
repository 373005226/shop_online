<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="12">
                <div class="card kjfs">
                    <p class="title"><i class="fa fa-th-large fa-lg"></i>快捷方式</p>
                    <ul>
                        <li>
                            <router-link to="/task" class="kjfs kjfs-bluee"><span><i
                                    class="el-icon-tickets fa-2x iconsize"></i></span><span>待分配订单</span></router-link>
                        </li>
                        <li>
                            <router-link to="/complete_order" class="kjfs kjfs-pinkk"><span><i
                                    class="el-icon-tickets iconsize"></i></span><span>有疑问订单</span></router-link>
                        </li>
                        <li>
                            <router-link to="/complete_order" class="kjfs kjfs-lightBluee">
                                <span><i class="el-icon-tickets iconsize"></i></span><span>待处理订单</span>
                            </router-link>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <router-link to="/userInfo" class="kjfs kjfs-yelloww"><span><i
                                    class="el-icon-user-solid iconsize"></i></span><span>个人信息</span></router-link>
                        </li>
                        <li>
                            <router-link to="/allorder" class="kjfs kjfs-purplee"><span><i
                                    class="fa el-icon-menu fa-2x iconsize"></i></span><span>所有订单</span></router-link>
                        </li>
                    </ul>
                </div>
            </el-col>
            <el-col :span="12">
                <div class="card dbsx">
                    <p class="title"><i class="fa fa-file-text-o"></i>待办事项</p>
                    <ul>
                        <li>
                            <router-link to="#"><span>待分配订单</span><span class="num">{{wait_complete}}</span>
                            </router-link>
                        </li>
                        <li>
                            <router-link to="#"><span>已分配订单</span><span class="num">{{checkout}}</span>
                            </router-link>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <router-link to="#"><span>有疑问订单</span><span class="num">{{isdoubt}}</span></router-link>
                        </li>
                        <li>
                            <router-link to="#"><span>我完成处理的订单</span><span class="num">{{complete}}</span></router-link>
                        </li>
                    </ul>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import {getallorder} from "../../api/order";

    export default {
        name: "order_distributor",
        data() {
            return {
                wait_complete: 0,
                checkout: 0,
                isdoubt: 0,
                complete: 0
            }
        },
        mounted() {
            getallorder().then(res => {
                for (let i of res) {
                    if (i.pay_status === 'checkout'&&i.takegoods_status==='online') {
                        this.wait_complete += 1
                    }
                    if (i.pay_status === 'checkout') {
                        this.checkout += 1
                    }
                    if (i.isdoubt === true) {
                        this.isdoubt += 1
                    }
                    if (i.inspecter === this.$store.getters.getname) {
                        this.complete += 1
                    }
                }
            })
        }
    }
</script>

<style scoped>

</style>
