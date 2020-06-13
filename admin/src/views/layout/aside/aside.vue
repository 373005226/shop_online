<template>
    <div>
        <el-aside id="asideNav">
            <div class="logo-name">
                <p v-if="$store.getters.logoShow">XU</p>
                <p v-else>多购商城后台管理系统</p>
            </div>
            <el-menu class="el-menu-vertical" background-color="#03152A" :collapse="false" router
                     :unique-opened="true" :collapse-transition="true" active-text-color="#ffffff"
                     @select="selectmenu"
                     text-color="rgba(255,255,255,.7)">
                <template v-for="(item,index) in nav">
                    <el-menu-item v-if="item.alone==true&&item.meta.roles.includes($store.getters.getrole)" :index="item.path" :key="index">
                        <i :class="item.iconCls"></i>
                        <span slot="title">{{item.name}}</span>
                    </el-menu-item>

                    <el-submenu v-if="item.alone!=true&&item.children.length>1&&item.meta.roles.includes($store.getters.getrole)" :index="index.toString()" :key="index">
                        <template>
                            <template slot="title" :index="item.path">
                                <i :class="item.iconCls"></i>
                                <span slot="title">{{item.name}}</span>
                            </template>
                            <template v-for="(its,idx) in item.children">
                                <el-menu-item :index="its.path" :key="idx">{{its.name}}</el-menu-item>
                            </template>
                        </template>
                    </el-submenu>

                    <el-menu-item v-if="item.alone!=true&&item.children.length==1&&item.meta.roles.includes($store.getters.getrole)" :index="item.children[0].path" :key="index">
                        <i :class="item.iconCls"></i>
                        <span slot="title">{{item.name}}</span>
                    </el-menu-item>
                </template>
            </el-menu>
        </el-aside>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                isCollapse: true,
                nav: [],
                roles:["order_distributor","shop_inspector","manager","boss"]
            };
        },
        created() {
            console.log(this.$route)
            // console.log(this.$router.options.routes)
            for (let i of this.$router.options.routes) {
                // console.log(i)
                if (!i.hidden) {
                    this.nav.push(i)
                }
            }
            console.log(this.nav)
            console.log(this.roles.includes(this.$store.getters.getrole))
        },
        methods: {
            selectmenu(key) {
                console.log(key)
            }
        }
    }
</script>
<style lang="scss" scoped>
    $top: top;
    $bottom: bottom;
    $left: left;
    $right: right;
    %w100 {
        width: 100%;
    }

    %h100 {
        height: 100%;
    }

    %cursor {
        cursor: pointer;
    }

    @mixin set-value($side, $value) {
        @each $prop in $leftright {
            #{$side}-#{$prop}: $value;
        }
    }

    #asideNav {
        width: auto !important;
        display: flex;
        flex-direction: column;
        border-right: solid 1px #e6e6e6;

        .logo-name {
            background-color: #03152A !important;
            @extend %w100;
            font-weight: 300;
            z-index: 999;

            p {
                height: 50px;
                line-height: 50px;
                text-align: center;
                font-size: 16px;
                color: #5e6d82;
            }
        }

        .el-menu-vertical:not(.el-menu--collapse) {
            width: 200px;
            @extend %h100;
            overflow-y: scroll;
            overflow-x: hidden;
        }

        .el-menu {
            flex: 1;
            overflow: inherit;
            border-right: none;

            &::-webkit-scrollbar {
                display: none;
            }

            .fa {
                vertical-align: middle;
                margin-right: 5px;
                width: 24px;
                text-align: center;
                font-size: 18px;
            }

            .el-menu-item {
                background-color: #020f1d !important;
                border-bottom: 1px solid #020f1d;

                &:hover {
                    color: #ffffff !important;
                    background-color: #375573 !important;
                }
            }

            .el-menu-item.is-active {
                background-color: #56a9ff !important
            }

            .is-opened > .el-submenu__title > .el-icon-arrow-down {
                color: #ffffff;
                font-weight: 500;
                font-size: 18px;
            }
        }
    }
</style>
