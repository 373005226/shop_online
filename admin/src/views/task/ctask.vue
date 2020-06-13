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
                    prop="picker"
                    label="订单拣货人"
                    width="200">
            </el-table-column>
            <el-table-column
                    prop="picker_time"
                    label="订单拣货时间"
            >
            </el-table-column>
            <el-table-column
                    prop="inspecter"
                    label="订单二次检验人员"
            >
            </el-table-column>
            <el-table-column
                    prop="inspecter_time"
                    label="订单二次检验时间"
            >
            </el-table-column>
            <el-table-column
                    prop="status"
                    label="订单状态"
                    :formatter="formatorder"
                    width="200">
            </el-table-column>
            <el-table-column
                    label="订单分类"
                    width="150"
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
                    label="提取人"
                    width="200"
            >
            </el-table-column>
            <el-table-column
                    prop="singer_mobile"
                    label="提取人手机号"
                    width="200"
            >
            </el-table-column>
            <el-table-column
                    prop="gettime"
                    label="提取时间"
                    width="200"
            >
            </el-table-column>
            <el-table-column
                    prop="inspecter"
                    label="二次拣货人"
                    width="200"
            >
            </el-table-column>

            <el-table-column label="确认订单">
                <template slot-scope="scope">
                    <template v-if="scope.row.takegoods_status==='online'">
                        <el-button
                                size="mini"
                                @click="handleEdit(scope.$index, scope.row)">查看订单商品
                        </el-button>
                        <template v-if="scope.row.pay_status==='Delivery'">
                            <el-button
                                    size="mini"
                                    @click="sureorder(scope.$index, scope.row)">确认商品提取
                            </el-button>
                        </template>
                    </template>

                    <template v-else>
                        <template v-if="scope.row.takegoods_status==='self_mention'">
                            <el-button
                                    size="mini"
                                    @click="handleEdit(scope.$index, scope.row)">查看订单商品
                            </el-button>
                            <el-button
                                    size="mini"
                                    @click="handorder(scope.$index, scope.row)">自提
                            </el-button>
                        </template>
                    </template>

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

            <template v-if="orderdetail.takegoods_status==='online'">
                <el-input
                        type="textarea"
                        :rows="2"
                        placeholder="请输入订单备注:例有刺、商品较重、商品易碎等"
                        v-model="orderdetail.remarks" disabled>
                </el-input>
            </template>

            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="sure">确定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="收货地址" :visible.sync="dialogFormVisible" width="30%">
            <el-form label-position="right" label-width="80px" :model="formLabelAlign">
                <el-form-item label="订单号">
                    <el-input v-model="formLabelAlign.order_sn" disabled></el-input>
                </el-form-item>
                <el-form-item label="提货人">
                    <el-input v-model="formLabelAlign.name" disabled></el-input>
                </el-form-item>
                <el-form-item label="手机号">
                    <el-input v-model="formLabelAlign.phone" disabled></el-input>
                </el-form-item>
                <el-form-item label="提货时间">
                    <el-input v-model="formLabelAlign.gettime" disabled></el-input>
                </el-form-item>
                <el-form-item label="提取码">
                    <el-input v-model="formLabelAlign.number" style="width: 74%"></el-input>
                    <el-button type="primary" @click="sendcode(formLabelAlign.phone)">发送提取码</el-button>
                </el-form-item>
            </el-form>
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="goodscancel">取消</el-button>
                <el-button type="primary" @click="goodssure">确认</el-button>
            </div>
        </el-dialog>

        <el-dialog title="确认订单提取" :visible.sync="dialoggetorder" width="30%">
            本订单由<span style="color: #56a9ff">{{delivery}}</span>提取
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="ordersurebutton">确认</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, getOrderdetail, sendnumber, changeOrder} from "../../api/order";

    export default {
        name: 'ctask',
        data() {
            return {
                tableData: [],
                ordergoods: [],
                orderdetail: [],
                dialogFormVisible: false,
                dialogTableVisible: false,
                dialoggetorder: false,
                formLabelAlign: {},
                delivery: ''
            }
        },
        methods: {
            getNowFormatDate() {
                var date = new Date();
                var seperator1 = "-"; //设置成自己想要的日期格式 年/月/日
                var seperator2 = ":"; //设置成自己想要的时间格式 时:分:秒
                var month = date.getMonth() + 1; //月
                var strDate = date.getDate(); //日
                var House = date.getHours()
                var Minutes = date.getMinutes()
                if (month >= 1 && month <= 9) {
                    month = "0" + month;
                }
                if (strDate >= 0 && strDate <= 9) {
                    strDate = "0" + strDate;
                }
                if (House > 0 && House <= 9) {
                    House = "0" + House
                }
                if (Minutes > 0 && Minutes <= 9) {
                    Minutes = "0" + Minutes
                }
                var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate +
                    " " + House + seperator2 + Minutes +
                    seperator2 + date.getSeconds();
                return currentdate;
            },
            sureorder(index, row) {
                console.log(index, row)
                this.delivery = row.deliveryman
                getOrderdetail(row.id).then(res => {
                    console.log(res)
                    this.orderdetail = res
                })
                this.dialoggetorder = true
            },
            ordersurebutton() {
                console.log(this.orderdetail)
                changeOrder(this.orderdetail.id, {
                    pay_status: 'Deliverying',
                    singer_mobile: this.orderdetail.singer_mobile,
                    user: this.orderdetail.user,
                    delivery_time:this.getNowFormatDate()
                }).then(res => {
                    console.log(res)
                    this.tableData = []
                    this.getorder()
                })
                this.dialoggetorder = false
            },
            sendcode(phone) {
                sendnumber({
                    mobile: phone
                }).then(res => {
                    console.log(res)
                })
            },
            cancel() {
                this.dialogTableVisible = false
            },
            sure() {
                this.dialogTableVisible = false
            },
            goodscancel() {
                this.dialogFormVisible = false
            },
            goodssure(){
                console.log(this.orderdetail)
                changeOrder(this.orderdetail.id, {
                    pay_status: 'trade_evaluate',
                    singer_mobile: this.orderdetail.singer_mobile,
                    user: this.orderdetail.user,
                    success_time:this.getNowFormatDate()
                }).then(res => {
                    console.log(res)
                    this.tableData = []
                    this.getorder()
                })

                this.$message({
                    showClose: true,
                    message: '商品提取成功',
                    type: 'success'
                })
                this.dialogFormVisible = false
            },
            handleEdit(index, row) {
                console.log(index, row.id)
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
            handorder(index, row) {
                console.log(index, row)
                this.formLabelAlign.order_sn = row.order_sn
                this.formLabelAlign.name = row.signer_name
                this.formLabelAlign.phone = row.singer_mobile
                this.formLabelAlign.gettime = row.gettime

                getOrderdetail(row.id).then(res => {
                    console.log(res)
                    this.orderdetail = res
                    // this.ordergoods = []
                    // for (let i of res.goods) {
                    //     console.log(i)
                    //     this.ordergoods.push(i)
                    // }
                    // console.log(this.ordergoods)
                })
                this.dialogFormVisible = true
            },
            formatorder(row) {
                if (row.pay_status === "checkout" && row.takegoods_status === "online") {
                    return '等待订单分配'
                }
                if (row.pay_status === "Delivery" && row.takegoods_status === "online") {
                    return '订单分配完毕，等待送货小哥提取'
                }
                if (row.pay_status === "checkout" && row.takegoods_status === "self_mention") {
                    return '等待用户提取'
                }
            },
            getpaymethods(info) {
                if (info === 'online') {
                    return '线上支付'
                } else {
                    return '线下自提'
                }
            },
            getorder() {
                getallorder().then(res => {
                    console.log(res)
                    for (let i of res) {
                        if (i.pay_status === "checkout" || i.pay_status === 'Delivery') {
                            this.tableData.push(i)
                        }
                    }
                    console.log(this.tableData)
                    // this.tableData = res
                })
            }
        },
        mounted() {
            this.getorder()
        }
    }
</script>

<style scoped>

</style>
