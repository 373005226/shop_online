<template>
    <div class='basic'>
        <el-row>
            <el-col :span='24'>
                <el-card>
                    <div slot="header">
                        商品评论列表
                    </div>
                    <div class="table-wrapper">
                        <el-table
                                v-loading="loading"
                                element-loading-text="加载数据中"
                                :data='tableData'
                                border
                                :row-class-name="addRowClass">
                            <el-table-column label="商品" prop="goodname" align="center" width="80"></el-table-column>
                            <el-table-column label="商品图片" align="center" width="120" height="120">
                                <template>
                                    <img src="https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2471723103,4261647594&fm=26&gp=0.jpg"
                                         alt="商品图" width="80" height="80" style="border-radius: 50%;">
                                </template>
                            </el-table-column>
                            <el-table-column label="用户名" prop="username" align="center" width="80"></el-table-column>
                            <el-table-column label="头像" align="center" width="120" height="120">
                                <template>
                                    <img src="https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/3421077522/O1CN01l8gaEP25R7nRyMp7g_!!0-item_pic.jpg_250x250.jpg_.webp"
                                         alt="用户头像" width="80" height="80" style="border-radius: 50%;">
                                </template>
                            </el-table-column>
                            <el-table-column label="评分" prop="score" align="center" width="180">
                                <el-rate v-model="value" disabled></el-rate>
                            </el-table-column>
                            <el-table-column label="评价类型" align="center" width="80">
                                <template slot-scope="scope">{{scope.row.rateType | rateTypeToText}}</template>
                            </el-table-column>
                            <el-table-column label="内容" prop="content" align="left" header-align="center"
                            ></el-table-column>
                            <el-table-column label="交易完成时间" prop="deliveryTime" align="center"
                                             width="180"></el-table-column>
                            <el-table-column label="评价时间" align="center" width="160" prop="comment_time">
                            </el-table-column>
                        </el-table>
                        <el-pagination
                                style="margin-top: 16px; text-align:right;"
                                layout="total, sizes, prev, pager, next, jumper"
                                :page-sizes="[5, 10, 15, 20]"
                                :total="total"
                                @size-change="handleSizeChange"
                                @current-change="handleCurrentChange">
                        </el-pagination>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<script>

    const POSITIVE = 0;
    const NEGATIVE = 1;
    export default {
        name: 'comment',
        created() {
        },
        data() {
            return {
                tableData: [
                    {
                        goodname:'水果',
                        username: 'GZX',
                        deliveryTime: '2020-04-02',
                        comment_time: '2020-04-02',
                        content: '111',
                        address: '111'
                    }
                ],
                loading: false,
                pagesize: 10,
                currentpage: 1,
                total: 1,
                value: 5
            }
        },
        methods: {
            show(scope) {
                console.log(scope);
            },
            handleSizeChange(value) {
                this.pagesize = value;
                this.getTableData();
            },
            handleCurrentChange(value) {
                this.currentpage = value;
                this.getTableData();
            },
            addRowClass({row}) {
                if (row.rateType === NEGATIVE) {
                    return 'warning-row';
                }
            }
        },
        filters: {
            rateTypeToText(rateType) {
                return rateType === POSITIVE ? '满意' : '不满意';
            },
            formatDate() {

            }
        },
        components: {}
    };
</script>
<style lang='scss'>
    .basic {
        .el-table {
            .warning-row {
                background-color: oldlace;
            }
        }

        .recommend-tag {
            display: inline-block;
            margin: 4px 0;
            margin-right: 4px;

            &:last-child {
                margin-right: 0;
            }
        }
    }
</style>
