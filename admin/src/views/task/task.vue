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
                    label="订单拣货人"
                    prop="picker"
                    width="180">
            </el-table-column>
            <el-table-column
                    label="订单状态"
                    prop="picker_time"
                    width="180">
            </el-table-column>
            <el-table-column
                    label="订单状态"
                    prop="pay_status"
                    :formatter="formatorder"
                    width="180">
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
                    label="用户提货时间"
                    width="200"
            >
            </el-table-column>
            <el-table-column
                    prop="picker"
                    label="订单商品拣货人"
                    width="200"
            >
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">点击验货
                    </el-button>
                    <el-button
                            size="mini"
                            type="danger"
                            @click="handledoubt(scope.$index, scope.row)">订单配送错误
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

            <template v-if="orderdetail.takegoods_status==='online'">
                <el-input
                        type="textarea"
                        :rows="2"
                        placeholder="请输入订单备注:例有刺、商品较重、商品易碎等"
                        v-model="textarea">
                </el-input>
            </template>




            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">订单商品配送错误</el-button>
                <el-button type="primary" @click="sure">确认订单验货完毕</el-button>
            </div>
        </el-dialog>

        <el-dialog title="填写问题表单" :visible.sync="doubtVisible" width="30%">
            <el-form ref="form" label-width="80px">
                <el-form-item label="错误原因">
                    <el-input type="textarea" v-model="formInline.doubtform"></el-input>
                </el-form-item>
            </el-form>
            <div style="text-align: center;padding-top: 20px">
                <el-button type="primary" @click="sure">提交</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {getallorder, getOrderdetail, changeOrder} from "../../api/order";

    export default {
        name: 'task',
        data() {
            return {
                tableData: [],
                ordergoods: [],
                orderdetail: [],
                textarea: '',
                dialogTableVisible: false,
                doubtVisible: false,
                formInline: {
                    doubtform: '',
                }
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
                if (row.pay_status === "Picking_complete") {
                    return '等待二次检验'
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
                this.dialogTableVisible = false
            },
            sure() {
                console.log(this.orderdetail)
                if (this.orderdetail.takegoods_status === 'online') {
                    changeOrder(this.orderdetail.id, {
                        pay_status: 'checkout',
                        singer_mobile: this.orderdetail.singer_mobile,
                        user: this.orderdetail.user,
                        inspecter: this.$store.getters.getname,
                        inspecter_time:this.getNowFormatDate(),
                        remarks:this.textarea
                    }).then(res => {
                        console.log(res)
                        this.tableData = []
                        this.getorder()
                    })
                } else {
                    changeOrder(this.orderdetail.id, {
                        pay_status: 'checkout',
                        singer_mobile: this.orderdetail.singer_mobile,
                        user: this.orderdetail.user,
                        inspecter: this.$store.getters.getname,
                        inspecter_time:this.getNowFormatDate()
                    }).then(res => {
                        console.log(res)
                        this.tableData = []
                        this.getorder()
                    })
                }

                this.$message({
                    showClose: true,
                    message: '订单检验成功',
                    type: 'success'
                })
                this.dialogTableVisible = false
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

            handledoubt(index, row) {
                console.log(index, row.id)
                // getOrderdetail(row.id).then(res => {
                //     console.log(res)
                //     this.orderdetail = res
                //     this.ordergoods = []
                //     for (let i of res.goods) {
                //         console.log(i)
                //         this.ordergoods.push(i)
                //     }
                //     console.log(this.ordergoods)
                // })
                this.doubtVisible = true
            },
            filterTag(value, row) {
                return row.tag === value
            },
            getorder() {
                getallorder().then(res => {
                    console.log(res)
                    for (let i of res) {
                        if (i.pay_status === "Picking_complete") {
                            this.tableData.push(i)
                        }
                    }
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
