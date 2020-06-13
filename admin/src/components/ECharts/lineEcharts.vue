<template>
    <div>
        <div :id="id" :style="{width: width, height: height}"></div>
    </div>
</template>

<script>
    import echarts from 'echarts'
    import {getallorder} from '@/api/order'

    export default {
        name: 'lineEcharts',
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
                chart: null,
                weekDay: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
                pc_ordernum: {
                    Monday: 0,
                    Tuesday: 0,
                    Wednesday: 0,
                    Thursday: 0,
                    Friday: 0,
                    Saturday: 0,
                    Sunday: 0
                }
            }
        },
        mounted() {
            this.getorderinfo()
        },
        methods: {
            //将日期转换为星期的方法
            formatDate(date) {
                var array = new Array()
                array = date.split('-')
                var ndate = new Date(array[0], parseInt(array[1] - 1), array[2])
                var weekArray = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
                return weekArray[ndate.getDay()]
            },

            //判断日期是否为这个星期
            isSameWeek(timeStampA, timeStampB) {
                let A = new Date(timeStampA).setHours(0, 0, 0, 0);
                let B = new Date(timeStampB).setHours(0, 0, 0, 0);
                var oneDayTime = 1000 * 60 * 60 * 24;
                var old_count = parseInt(A / oneDayTime);
                var now_other = parseInt(B / oneDayTime);
                return parseInt((old_count + 4) / 7) === parseInt((now_other + 4) / 7);
            },

            //先是判断是不是这个星期的订单，然后再累计相加
            getorderinfo() {
                getallorder().then(res => {
                    console.log(res)
                    for (let i of res) {
                        if (i.pay_status === "trade_evaluate" || i.pay_status === "TRADE_SUCCESS") {
                            if (this.isSameWeek(i.add_time,new Date())) {
                                switch (this.formatDate(i.add_time.substr(0, 10))) {
                                    case '星期一':
                                        this.pc_ordernum.Monday += i.order_mount
                                        break
                                    case '星期二':
                                        this.pc_ordernum.Tuesday += i.order_mount
                                        break
                                    case '星期三':
                                        this.pc_ordernum.Wednesday += i.order_mount
                                        break
                                    case '星期四':
                                        this.pc_ordernum.Thursday += i.order_mount
                                        break
                                    case '星期五':
                                        this.pc_ordernum.Friday += i.order_mount
                                        break
                                    case '星期六':
                                        this.pc_ordernum.Saturday += i.order_mount
                                        break
                                    case '星期日':
                                        this.pc_ordernum.Sunday += i.order_mount
                                        break
                                }
                            }
                        }
                    }
                    console.log(this.pc_ordernum)
                    this.initChart()
                })
            }
            ,
            initChart() {
                this.chart = echarts.init(document.getElementById(this.id))

                this.chart.setOption({
                    title: {
                        text: '周销量图'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985'
                            }
                        }
                    },
                    legend: {
                        data: ['PC端', '移动端']
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value'
                        }
                    ],
                    series: [
                        {
                            name: 'PC端',
                            type: 'line',
                            stack: '总量',
                            color: '#409EFF',
                            areaStyle: {},
                            data: [this.pc_ordernum.Monday, this.pc_ordernum.Tuesday, this.pc_ordernum.Wednesday, this.pc_ordernum.Thursday, this.pc_ordernum.Friday, this.pc_ordernum.Saturday, this.pc_ordernum.Sunday]
                        },
                        {
                            name: '移动端',
                            type: 'line',
                            stack: '总量',
                            color: '#F56C6C',
                            areaStyle: {},
                            data: [220, 182, 191, 234, 290, 330, 310]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>

</style>
