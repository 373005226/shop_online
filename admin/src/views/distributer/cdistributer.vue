<template>
    <div>
        <el-table
                border
                :data="tableData"
                style="width: 100%">
            <el-table-column
                    type="index">
            </el-table-column>
            <el-table-column
                    sortable
                    prop="order_sn"
                    label="订单号"
            >
            </el-table-column>
            <el-table-column
                    label="检验员"
                    prop="inspecter"
                    width="200">
            </el-table-column>
            <el-table-column
                    label="检验员备注"
                    prop="remarks"
                    width="200">
            </el-table-column>
            <el-table-column
                    label="订单状态"
                    prop="pay_status"
                    :formatter="formatorder"
                    width="250">
            </el-table-column>
            <el-table-column
                    prop="deliveryman"
                    label="配送人"
                    width="100"
            >
            </el-table-column>
            <el-table-column
                    prop="deliveryman_phone"
                    label="配送人手机号"
                    width="150"
            >
            </el-table-column>
            <el-table-column
                    prop="signer_name"
                    label="收货人"
                    width="100"
            >
            </el-table-column>
            <el-table-column
                    prop="singer_mobile"
                    label="收货人手机号"
                    width="200"
            >
            </el-table-column>
            <el-table-column
                    prop="address"
                    label="送货地址"
                    width="250"
            >
            </el-table-column>
            <el-table-column
                    prop="gettime"
                    label="需要送达时间"
                    width="150"
            >
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">详情
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-dialog title="订单列表" :visible.sync="dialogTableVisible">
            111
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, changeOrder} from "../../api/order";
    import {getalluser} from "../../api/user"

    export default {
        name: 'cdistributer',
        data() {
            return {
                tableData: [],
                ordergoods: [],
                orderdetail: [],
                deliveryphone: '',
                options: [],
                value: '',
                dialogTableVisible: false,
            }
        },
        methods: {
            formatorder(row) {
                if (row.pay_status === "checkout") {
                    return '二次检验完毕，等待分配送货员'
                }
                if(row.pay_status==='Delivery'){
                    return '订单商品等待送货员提取'
                }
                if(row.pay_status==='Deliverying'){
                    return '订单商品送货中'
                }
                if(row.takegoods_status==='online'&&row.pay_status==='trade_evaluate'||row.pay_status==='TRADE_SUCCESS'){
                    return '订单配送完成'
                }
            },
            getpaymethods(info) {
                if (info === 'online') {
                    return '线上支付'
                } else {
                    return '线下自提'
                }
            },

            cancel() {
                console.log(this.value)
                this.dialogTableVisible = false
            },
            sure() {
                //查询配送人员的手机号一并到修改状态中
                getalluser().then(res => {
                    console.log(res)
                    for (let i of res) {
                        if (i.id === this.value) {
                            console.log(i)
                            this.deliveryphone = i.mobile
                            //把送货人，送货人手机号，订单状态一并修改状态
                            if (this.orderdetail.takegoods_status === 'online') {
                                changeOrder(this.orderdetail.id, {
                                    pay_status: 'Delivery',
                                    singer_mobile: this.orderdetail.singer_mobile,
                                    user: this.orderdetail.user,
                                    distributor: this.$store.getters.getname,
                                    deliveryman: this.value,
                                    deliveryman_phone:this.deliveryphone
                                }).then(res => {
                                    console.log(res)
                                    this.tableData = []
                                    this.getorder()
                                })
                            }
                        }
                    }
                })
                this.dialogTableVisible = false
            },
            handleEdit(index, row) {
                console.log(index, row.id)
                this.$message({
                    showClose: true,
                    message: index, row,
                    type: 'success'
                })
                this.dialogTableVisible = true
            },
            filterTag(value, row) {
                return row.tag === value
            },
            getorder() {
                getallorder().then(res => {
                    for (let i of res) {
                        if (i.pay_status === 'Delivery' && i.takegoods_status === 'online') {
                            this.tableData.push(i)
                        }
                    }
                })
            },
            getuser() {
                getalluser().then(res => {
                    console.log(res)
                    this.options = []
                    for (let i of res) {
                        // console.log(i)
                        if (i.role === "delivery") {
                            this.options.push(i)
                        }
                    }
                    console.log(this.options)
                })
            }
        },
        mounted() {
            this.getuser()
            this.getorder()
        }
    }
</script>

<style scoped>

</style>
