<template>
    <div>
        <p class="title"><i class="el-icon-tickets"></i>最新10条等待处理订单</p>
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
                    label="订单分类"
                    width="150"
                    :filters="[{ text: '线上支付', value: 'online' }, { text: 'self_mention', value: '线下自提' }]"
            >
                <template slot-scope="scope">
                    <el-tag
                            :type="scope.row.takegoods_status === 'online' ? 'primary' : 'success'"
                            disable-transitions>{{getpaymethods(scope.row.takegoods_status)}}
                    </el-tag>
                </template>
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
                            @click="handleEdit(scope.$index, scope.row)">分配配送员
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-dialog title="订单列表" :visible.sync="dialogTableVisible">
            <el-table :data="ordergoods">
                <el-table-column label="商品" align="center" width="200">
                    <template slot-scope="scope">
                        {{scope.row.goods.name}}
                    </template>
                </el-table-column>
                <el-table-column label="头像" align="center" width="200" height="200">
                    <template slot-scope="scope">
                        <img :src="scope.row.goods.images[0].image"
                             alt="" width="100px" height="100px" style="border-radius: 50%;">
                    </template>
                </el-table-column>
                <el-table-column property="goods_num" label="商品数量" width="200"></el-table-column>
                <el-table-column label="规格">
                    <template slot-scope="scope">
                        {{scope.row.goods.specification[0].specification_text}}
                    </template>
                </el-table-column>
            </el-table>

            <div style="text-align: right;padding-top: 30px">
                <span style="padding-right: 10px">请选择配送人员</span>
                <el-select v-model="value" clearable placeholder="请选择">
                    <el-option
                            v-for="item in options"
                            :key="item.id"
                            :label="item.name"
                            :value="item.id">
                    </el-option>
                </el-select>
            </div>
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="sure()">确认订单验货完毕</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, getOrderdetail, changeOrder} from "../../api/order";
    import {getalluser} from "../../api/user"

    export default {
        name: 'order_mainIndex',
        data() {
            return {
                tableData: [],
                ordergoods: [],
                orderdetail: [],
                deliveryphone: '',
                options: [{
                    value: '27',
                    label: '配送人员LY'
                },
                    {
                        value: '28',
                        label: '配送人员LY1'
                    }],
                value: '',
                dialogTableVisible: false,
            }
        },
        methods: {
            formatorder(row) {
                if (row.pay_status === "checkout") {
                    return '二次检验完毕，等待分配送货员'
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
                    for (let i of res) {
                        if (i.id === this.value) {
                            console.log(i)
                            this.deliveryphone = i.mobile
                            console.log(this.deliveryphone)
                        }
                    }
                    //把送货人，送货人手机号，订单状态一并修改状态
                    if (this.orderdetail.takegoods_status === 'online') {
                        changeOrder(this.orderdetail.id, {
                            pay_status: 'Delivery',
                            singer_mobile: this.orderdetail.singer_mobile,
                            user: this.orderdetail.user,
                            distributor: this.$store.getters.getname,
                            inspecter: this.$store.getters.adminname,
                            operator: this.value,
                            operator_phone: this.deliveryphone,
                        }).then(res => {
                            console.log(res)
                            this.tableData = []
                            this.getorder()
                        })
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
                getOrderdetail(row.id).then(res => {
                    console.log(res)
                    this.orderdetail = res
                    this.ordergoods = []
                    for (let i of res.goods) {
                        console.log(i)
                        this.ordergoods.push(i)
                    }
                    console.log(this.ordergoods)
                })
                this.dialogTableVisible = true
            },
            filterTag(value, row) {
                return row.tag === value
            },
            getorder() {
                getallorder().then(res => {
                    for (let i of res) {
                        if (i.pay_status === 'checkout' && i.takegoods_status === 'online') {
                            this.tableData.push(i)
                        }
                    }
                })
            },
            getuser() {
                getalluser().then(res => {
                    this.options = []
                    for (let i of res) {
                        // console.log(i)
                        if (i.role === "delivery") {
                            this.options.push(i)
                        }
                    }
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
