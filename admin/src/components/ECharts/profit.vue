<template>
    <div>
        <div :id="id" :style="{width: width, height: height}"></div>
    </div>
</template>

<script>
    import echarts from 'echarts'

    export default {
        name: "profit",
        props: {
            id: {
                type: String,
                default: 'myChart'
            },
            width: {
                type: String,
                default: '100%'
            },
            height: {
                type: String,
                default: '100%'
            }
        },
        data() {
            return {
                chart: null
            }
        },
        mounted() {
            this.initChart()
        },
        methods: {
            initChart() {
                this.chart = echarts.init(document.getElementById(this.id))

                this.chart.setOption({
                    title: {
                        text: '周利润表'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    legend: {
                        data: ['利润', '支出', '收入']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    yAxis: [
                        {
                            type: 'category',
                            axisTick: {
                                show: false
                            },
                            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                        }
                    ],
                    series: [
                        {
                            name: '利润',
                            color:"#F57171",
                            type: 'bar',
                            label: {
                                show: true,
                                position: 'inside'
                            },
                            data: [200, 170, 240, 244, 200, 220, 210]
                        },
                        {
                            name: '收入',
                            type: 'bar',
                            stack: '总量',
                            color:"#4BA3FF",
                            label: {
                                show: true
                            },
                            data: [320, 302, 341, 374, 390, 450, 420]
                        },
                        {
                            name: '支出',
                            type: 'bar',
                            color:'#F4D884',
                            stack: '总量',
                            label: {
                                show: true,
                                position: 'left'
                            },
                            data: [-120, -132, -101, -134, -190, -230, -210]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>

</style>
