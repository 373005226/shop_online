<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="12">
                <line-echarts id="lineEcharts" height="450px" ref="echarts"></line-echarts>
            </el-col>

            <el-col :span="12">
                    <salestoday id="salestoday" height="450px" ref="echarts"></salestoday>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="24">
                <profit id="profit" height="580px" ref="echarts"></profit>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import LineEcharts from '../../components/ECharts/lineEcharts'
    import salestoday from "../../components/ECharts/salestoday"
    import profit from "../../components/ECharts/profit"
    export default {
        name: "sales_today",
        components: {
            LineEcharts,
            salestoday,
            profit
        }
    }
</script>

<style scoped lang="scss">

</style>
