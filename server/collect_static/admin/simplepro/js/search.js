Vue.component('search', {
    props: ['data'],
    data() {
        var models = [];

        this.data.forEach(item => {
            if (!item.models) {
                models.push(item);
            } else {
                item.models.forEach(node => models.push(node));
            }

        });

        return {
            show: false,
            input: '',
            models: models
        }
    },
    watch:{
        show:function () {
            this.input = '';
        }
    },
    methods: {
        querySearchAsync: function (queryString, cb) {

            var rs = this.models.filter(item => item.name.toLowerCase().indexOf(queryString.toLowerCase()) != -1);
            var values = [];
            rs.forEach(item => {
                values.push({
                    value: item.name,
                    item: item
                })
            });
            cb(values);
        },
        handleSelect: function (item) {
            app.openTab(item.item);
        }
    },
    created() {
        document.addEventListener('click', __ => this.show = false)
    },
    template: '<template><el-autocomplete @select="handleSelect" :fetch-suggestions="querySearchAsync" style="display: inline-block;width: 150px" @click.native.stop="show=true" size="small" v-if="show" prefix-icon="el-icon-search" placeholder="请输入内容" v-model="input"> <template slot-scope="{ item }">\n' +
        '    <i :class="item.item.icon"></i>\n' +
        '    <span>{{ item.value }}</span>\n' +
        '  </template></el-autocomplete><el-button v-else icon="el-icon-search" @click.stop="show=true" circle></el-button></template>'
});