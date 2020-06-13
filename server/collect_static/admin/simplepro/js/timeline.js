Vue.component('timeline', {
    props: ['show'],
    data: function () {
        return {}
    },
    created: function () {

    },
    mounted: function () {
    },
    template: '#timeline'
});

Vue.component('timeline-btn', {
    data: function () {
        return {
            show: false
        }
    },
    methods: {
        click: function () {
            this.show = !this.show;
        }
    },
    template: '<el-button icon="el-icon-tickets" @click="click" circle><timeline :show="show"></timeline></el-button>'
});