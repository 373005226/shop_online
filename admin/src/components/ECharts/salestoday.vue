<template>
    <div>
        <div :id="id" :style="{width: width, height: height}" class="table"></div>
    </div>
</template>

<script>
    import echarts from 'echarts'

    export default {
        name: 'salestoday',
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
                        text: '今日销量饼图',
                        // subtext: '纯属虚构',
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b} : {c} ({d}%)'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
                    },
                    backgroundColor: '#FFFFFF',
                    series: [
                        {
                            name: '访问来源',
                            type: 'pie',
                            radius: '55%',
                            center: ['50%', '60%'],
                            data: [
                                {value: 335, name: '直接访问'},
                                {value: 310, name: '邮件营销'},
                                {value: 234, name: '联盟广告'},
                                {value: 135, name: '视频广告'},
                                {value: 1548, name: '搜索引擎'}
                            ],
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ],

                })
            }
        }
    }
</script>

<style scoped>
    .table{
        box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
    }
</style>
