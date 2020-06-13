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
                            :key="item.name"
                            :label="item.name"
                            :value="item.name">
                    </el-option>
                </el-select>
            </div>
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="sure">确认</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, getOrderdetail,changeOrder} from "../../api/order";
    import {getalluser} from "../../api/user"

    export default {
        name: 'distributer',
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
                    console.log(res)
                    for (let i of res) {
                        if(i.name ===this.value){
                            console.log(i)
                            this.deliveryphone = i.mobile
                            //把送货人，送货人手机号，订单状态一并修改状态
                            if (this.orderdetail.takegoods_status === 'online') {
                                changeOrder(this.orderdetail.id, {
                                    pay_status: 'Delivery',
                                    singer_mobile: this.orderdetail.singer_mobile,
                                    user: this.orderdetail.user,
                                    distributor: this.$store.getters.getname,
                                    distributor_time:this.getNowFormatDate(),
                                    deliveryman: this.value,
                                    deliveryman_phone:this.deliveryphone
                                }).then(res => {
                                    console.log(res)
                                    this.tableData = []
                                    this.getorder()
                                }).catch(error=>{
                                    console.log(error)
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
                    message: '订单分配操作成功',
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
                    console.log(res)
                    for (let i of res) {
                        if (i.pay_status === 'checkout' && i.takegoods_status === 'online') {
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
