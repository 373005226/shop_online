/**
 封装echarts在vue中使用
 **/

Vue.component('echarts', {
    props: ['option', 'style'],
    data: function () {
        return {}
    },
    mounted: function () {
        this.$nextTick(function () {
            var el = this.$el;
            var chart = echarts.init(el, 'macarons');
            chart.setOption(this.option);
            this.chart = chart;

        });
    },
    watch: {
        option: function (newValue, oldValue) {
            //option发生改变，就重新渲染
            this.chart.setOption(newValue);
        }
    },
    template: '<div :style="style">{{option}}</div>'
})