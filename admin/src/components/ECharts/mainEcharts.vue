<template>
    <div>
        <div :id="id" :style="{width: width, height: height}"></div>
    </div>
</template>

<script>
    import echarts from 'echarts'
    import {getVisit} from '../../api/data'
    export default {
        name: 'mainEcharts',
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
                date: '',
                weekDay: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
                visit: {
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
            this.getallVisit()
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

            //获取PC端的周流量
            getallVisit(){
                getVisit().then(res => {
                    for (let i of res) {
                        if(this.isSameWeek(i.add_time,new Date())){
                            switch (this.formatDate(i.add_time.substr(0, 10))) {
                                case '星期一':
                                    this.visit.Monday += i.count
                                    break
                                case '星期二':
                                    this.visit.Tuesday +=i.count
                                    break
                                case '星期三':
                                    this.visit.Wednesday +=i.count
                                    break
                                case '星期四':
                                    this.visit.Thursday +=i.count
                                    break
                                case '星期五':
                                    this.visit.Friday +=i.count
                                    break
                                case '星期六':
                                    this.visit.Saturday +=i.count
                                    break
                                case '星期日':
                                    this.visit.Sunday +=i.count
                                    break
                            }
                        }
                    }
                    this.initChart()
                })
            },


            //图表显示方法
            initChart() {
                this.chart = echarts.init(document.getElementById(this.id))

                this.chart.setOption({
                    title: {
                        text: '周流量表'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['PC端', '移动端']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: 'PC端',
                            type: 'line',
                            stack: '总量',
                            color: '#409EFF',
                            data: [this.visit.Monday, this.visit.Tuesday, this.visit.Wednesday, this.visit.Thursday, this.visit.Friday, this.visit.Saturday, this.visit.Sunday]
                        },
                        {
                            name: '移动端',
                            type: 'line',
                            stack: '总量',
                            color: '#F56C6C',
                            data: [10, 10, 10, 10, 10, 10, 10]
                        }
                    ]
                })
            }
        }
    }
</script>

<style scoped>

</style>
