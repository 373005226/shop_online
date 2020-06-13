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
                    prop="odd"
                    label="订单号">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="收货人">
            </el-table-column>
            <el-table-column
                    prop="status"
                    label="订单状态"
                    width="130">
            </el-table-column>
            <el-table-column
                    prop="amount"
                    label="金额">
            </el-table-column>
            <el-table-column
                    prop="date"
                    label="下单时间"
                    sortable
                    :filters="[{text: '2018-01-01', value: '2018-01-01'}, {text: '2018-01-02', value: '2018-01-02'}, {text: '2018-01-03', value: '2018-01-03'}, {text: '2018-01-04', value: '2018-01-04'}, {text: '2018-01-05', value: '2018-01-05'}]"
                    :filter-method="filterHandler"
            >
            </el-table-column>
            <el-table-column label="原因内容" prop="content" align="left" header-align="center"
            ></el-table-column>
            <el-table-column
                    prop="tag"
                    label="订单分类"
                    width="150"
                    :filters="[{ text: '线上购买', value: '线上购买' }, { text: '线下自提', value: '线下自提' }]"
                    :filter-method="filterTag"
                    filter-placement="bottom-end">
                <template slot-scope="scope">
                    <el-tag
                            :type="scope.row.tag === '线上购买' ? 'primary' : 'success'"
                            disable-transitions>{{scope.row.tag}}
                    </el-tag>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button
                            type="danger"
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">查看详情
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
        <div style="margin: 0 auto">
        </div>
    </div>
</template>

<script>
    export default {
        name: 'order_question',
        data() {
            return {
                tableData: []
            }
        },
        methods: {
            handleEdit(index, row) {
                console.log(index, row)
                this.$message({
                    showClose: true,
                    message: index, row,
                    type: 'success'
                })
            },
            handleDelete(index, row) {
                console.log(index, row)
                this.$message({
                    showClose: true,
                    message: index, row,
                    type: 'success'
                })
            },
            filterTag(value, row) {
                return row.tag === value
            },
            filterHandler(value, row, column) {
                const property = column['property']
                return row[property] === value
            }
        }
    }
</script>

<style scoped>

</style>
