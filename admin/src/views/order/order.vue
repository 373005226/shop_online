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
                    label="订单号">
            </el-table-column>
            <el-table-column
                    prop="signer_name"
                    width="150"
                    label="收货人">
            </el-table-column>
            <el-table-column
                    prop="pay_status"
                    :formatter="formatorder"
                    label="订单状态"
                    width="150"
            >
            </el-table-column>
            <el-table-column
                    prop="picker"
                    label="拣货员"
                    width="150"
            >
            </el-table-column>

            <el-table-column
                    prop="distributor"
                    :formatter="formatdistributor"
                    label="订单分配员">
            </el-table-column>

            <el-table-column
                    prop="inspecter"
                    label="二次检验员">
            </el-table-column>
            <el-table-column
                    prop="deliveryman"
                    :formatter="formatoperator"
                    label="送货员">
            </el-table-column>
            <el-table-column
                    prop="order_mount"
                    width="120"
                    label="金额">
            </el-table-column>
            <el-table-column
                    prop="pay_time"
                    label="下单时间"
                    sortable
                    :filter-method="filterHandler"
            >
            </el-table-column>
            <el-table-column
                    label="订单分类"
                    :filters="[{ text: '线上支付', value: 'online' }, { text: 'self_mention', value: '线下自提' }]"
            >
                <template slot-scope="scope">
                    <el-tag
                            :type="scope.row.takegoods_status === 'online' ? 'primary' : 'success'"
                            disable-transitions>{{getpaymethods(scope.row.takegoods_status)}}
                    </el-tag>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">查看订单商品
                    </el-button>
                    <el-button
                            size="mini"
                            @click="handledetail(scope.$index, scope.row)">查看订单信息
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
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="sure">确定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="订单信息" :visible.sync="dialogTabledetailonline">
            <div class="block">
                <el-timeline>
                    <el-timeline-item :timestamp="online.pay_time" placement="top">
                        <el-card>
                            <h4>支付时间</h4>
                            <p>用户<span class="name">{{online.signer_name}}</span><span
                                   class="time">于{{online.pay_time}}</span>支付完成</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="online.picker_time" placement="top" v-if="online.picker!==''&&online.picker!==null">
                        <el-card>
                            <h4>商品拣货时间</h4>
                            <p>商品拣货员于<span class="name">{{online.picker}}</span> 于 <span class="time">{{online.picker_time}}</span>拣货</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="online.inspecter_time" placement="top" v-if="online.inspecter!==''&&online.inspecter!==null">
                        <el-card>
                            <h4>商品二次检验时间</h4>
                            <p>商品检验员<span class="name">{{online.inspecter}}</span>于<span class="time">{{online.inspecter_time}}</span>检验完毕</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="online.inspecter_time" placement="top" v-if="online.pay_status==='Delivery'">
                        <el-card>
                            <h4>送货员提取时间</h4>
                            <p>订单分配员<span class="name">{{online.distributor}}</span>于<span class="time">{{online.distributor_time}}</span>分配好送货员</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="online.inspecter_time" placement="top" v-if="online.pay_status==='Deliverying'&&online.deliveryman!==null">
                        <el-card>
                            <h4>送货员提取时间</h4>
                            <p>送货员<span class="name">{{online.deliveryman}}</span>于<span class="time">{{online.delivery_time}}</span>提取订单商品</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="online.success_time" placement="top" v-if="online.success_time!==''&&online.success_time!==null">
                        <el-card>
                            <h4>送货员送达时间</h4>
                            <p>送货员<span class="name">{{online.deliveryman}}</span>于<span class="time">{{online.success_time}}</span>送达商品，交易结束</p>
                        </el-card>
                    </el-timeline-item>
                </el-timeline>
            </div>
        </el-dialog>

        <el-dialog title="订单信息" :visible.sync="dialogTabledetailself_method">
            <div class="block">
                <el-timeline>
                    <el-timeline-item :timestamp="self_method.pay_time" placement="top">
                        <el-card>
                            <h4>支付时间</h4>
                            <p>用户<span class="name">{{self_method.signer_name}}</span><span
                                    class="time">于{{self_method.pay_time}}</span>支付完成</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="self_method.picker_time" placement="top" v-if="self_method.picker!==null&&self_method.picker!==''">
                        <el-card>
                            <h4>商品拣货时间</h4>
                            <p>商品拣货员于<span class="name">{{self_method.picker}}</span> 于 <span class="time">{{self_method.picker_time}}</span>拣货</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="self_method.inspecter_time" placement="top" v-if="self_method.inspecter!==null&&self_method.inspecter!==''">
                        <el-card>
                            <h4>商品二次检验时间</h4>
                            <p>商品检验员<span class="name">{{self_method.inspecter}}</span>于<span class="time">{{self_method.inspecter_time}}</span>检验完毕</p>
                        </el-card>
                    </el-timeline-item>
                    <el-timeline-item :timestamp="self_method.inspecter_time" placement="top" v-if="self_method.success_time!==''">
                        <el-card>
                            <h4>用户自提商品完成时间</h4>
                            <p>用户<span class="name">{{self_method.signer_name}}</span>于<span class="time">{{self_method.success_time}}</span>已经自提订单商品，交易结束</p>
                        </el-card>
                    </el-timeline-item>
                </el-timeline>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, getOrderdetail} from '../../api/order'

    export default {
        name: 'maintable',
        data() {
            return {
                tableData: [],
                ordergoods: [],
                dialogTableVisible: false,
                dialogTabledetailonline: false,
                dialogTabledetailself_method:false,
                online: [],
                self_method: []
            }
        },
        methods: {
            cancel() {
                this.dialogTableVisible = false
            },
            sure() {
                this.dialogTableVisible = false
            },
            formatorder(row) {
                if (row.pay_status === "Picking_complete") {
                    return '等待二次检验'
                }
                if (row.pay_status === 'paying') {
                    return '订单正在等待支付'
                }
                if (row.pay_status === "Delivery") {
                    return '订单商品等待送货员提取'
                }
                if (row.pay_status === 'Deliverying') {
                    return '订单商品送货中'
                }
                if (row.pay_status === "checkout") {
                    return '商品正在进行二次检验'
                }
                if (row.pay_status === "checkout" && row.takegoods_status === "online") {
                    return '商品二次检验完，等待送货人员取货'
                }
                if (row.pay_status === "trade_evaluate" || row.pay_status === "TRADE_SUCCESS") {
                    return '交易结束'
                }
            },
            formatdistributor(row) {
                if (row.distributor === null) {
                    return '无'
                } else {
                    return row.distributor
                }
            },
            formatoperator(row) {
                if (row.deliveryman === null) {
                    return '无'
                } else {
                    return row.deliveryman
                }
            },
            handleEdit(index, row) {
                console.log(index, row.id)
                getOrderdetail(row.id).then(res => {
                    console.log(res)
                    // this.orderdetail = res
                    this.ordergoods = []
                    for (let i of res.goods) {
                        console.log(i)
                        this.ordergoods.push(i)
                    }
                    console.log(this.ordergoods)
                })
                this.dialogTableVisible = true
            },
            handledetail(index, row) {
                console.log(index, row)
                if (row.takegoods_status === 'online') {
                    this.dialogTabledetailonline = true
                    this.online = row
                    // this.online.push(row)
                }else {
                    this.dialogTabledetailself_method =true
                    this.self_method = row
                }
                console.log(this.self_method)
            },
            filterTag(value, row) {
                return row.tag === value
            },
            filterHandler(value, row, column) {
                const property = column['property']
                return row[property] === value
            },
            getorder() {
                getallorder().then(res => {
                    console.log(res)
                    for (let i of res) {
                        this.tableData.push(i)
                    }
                    // this.tableData = res
                })
            },
            getpaymethods(info) {
                if (info === 'online') {
                    return '线上支付'
                } else {
                    return '线下自提'
                }
            },
            gettime(time) {
                return time
            }
        },
        mounted() {
            this.getorder()
        }
    }
</script>

<style scoped>
    .name {
        padding-left: 10px;
        color: #56a9ff;
    }

    .time {
        padding-left: 10px;
        padding-right: 10px;
        color: #F56C6C
    }
</style>
