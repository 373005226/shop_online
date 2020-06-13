<template>
    <div id="userinfo">
        <el-row>
            <el-col :span="6">
                <el-form ref="form" :model="form" label-width="100px">
                    <el-form-item label="管理员权限">
                        <el-input v-model="status" disabled></el-input>
                    </el-form-item>
                    <el-form-item label="名字">
                        <el-input v-model="name" disabled></el-input>
                        <!--                        <el-select v-model="form.region" placeholder="请选择活动区域">-->
                        <!--                            <el-option label="区域一" value="shanghai"></el-option>-->
                        <!--                            <el-option label="区域二" value="beijing"></el-option>-->
                        <!--                        </el-select>-->
                    </el-form-item>
                    <!--                    <el-form-item label="手机号" width="80%">-->
                    <!--                        <el-input v-model="form.phone" disabled></el-input>-->
                    <!--                        -->
                    <!--                    </el-form-item>-->

                    <el-form-item label="手机号">
                        <el-input v-model="phonenumber" style="width: 76%" disabled></el-input>
                        <el-button type="primary" @click="dialogTableVisible = true">修改手机号</el-button>
                    </el-form-item>

                    <el-form-item label="用户头像" style="width: 50%">
                        <el-upload
                                class="avatar-uploader"
                                action="https://jsonplaceholder.typicode.com/posts/"
                                :show-file-list="false"
                                :on-success="handleAvatarSuccess"
                                :before-upload="beforeAvatarUpload">
                            <img v-if="imageUrl" :src="imageUrl" class="avatar">
                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                        </el-upload>
                    </el-form-item>

                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">立即创建</el-button>
                        <el-button>取消</el-button>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>

        <el-dialog title="修改手机号" :visible.sync="dialogTableVisible" width="25%">
            <el-form label-position="right" label-width="80px">
                <el-form-item label="手机号">
                    <el-input v-model="phone"></el-input>
                </el-form-item>
                <el-form-item label="提取码">
                    <el-input v-model="number" style="width: 78%"></el-input>
                    <el-button type="primary" @click="sendcode">发送验证码</el-button>
                </el-form-item>
            </el-form>
            <div style="text-align: center;padding-top: 20px">
                <el-button type="danger" @click="cancel">取消</el-button>
                <el-button type="primary" @click="sure">确认</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {sendcode, putuserinfo} from '../../api/user'

    export default {
        name: "userinfo",
        data() {
            return {
                form: {},
                phone: '',
                number: '',
                imageUrl: '',
                dialogTableVisible: false
            }
        },
        methods: {
            sendcode() {
                sendcode({mobile: this.phone}).then(res => {
                    console.log(res)
                })
            },
            getrole() {
                if (this.$store.getters.getrole === 'boss') {
                    return '超级管理员'
                }
                if (this.$store.getters.getrole === 'order_distributor') {
                    return '订单分配员'
                }
                if (this.$store.getters.getrole === 'shop_inspector') {
                    return '超市自提商品管理员'
                }
                if (this.$store.getters.getrole === 'manager') {
                    return '后台管理员'
                }
            },
            onSubmit() {
                console.log('submit!');
            },
            cancel() {
                this.dialogTableVisible = false
            },
            sure() {
                putuserinfo({mobile: this.phone}, {
                    headers: {
                        Authorization: localStorage.getItem('admintoken')
                    }
                }).then(res => {
                    console.log(res)
                })
                this.$message({
                    showClose: true,
                    message: '修改信息成功',
                    type: 'success'
                })
                this.$store.commit('changemobile', this.phone)
                this.dialogTableVisible = false
            },
            handleAvatarSuccess(res, file) {
                this.imageUrl = URL.createObjectURL(file.raw);
            },
            beforeAvatarUpload(file) {
                const isJPG = file.type === 'image/jpeg';
                const isLt2M = file.size / 1024 / 1024 < 2;

                if (!isJPG) {
                    this.$message.error('上传头像图片只能是 JPG 格式!');
                }
                if (!isLt2M) {
                    this.$message.error('上传头像图片大小不能超过 2MB!');
                }
                return isJPG && isLt2M;
            }
        },
        computed: {
            status() {
                return this.getrole(this.$store.getters.getrole)
            },
            name() {
                return this.$store.getters.getname
            },
            phonenumber() {
                return this.$store.getters.getmobile
            }
        },
        created() {
            // this.form.status = this.getrole(this.$store.getters.getrole)
            // this.form.name = this.$store.getters.getname
            // this.form.phone = this.$store.getters.getmobile
        }
    }
</script>

<style scoped lang="scss">
    .avatar-uploader {
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;

        &:hover {
            border-color: #409EFF;
        }
    }

    .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        line-height: 178px;
        text-align: center;
    }

    .avatar {
        width: 178px;
        height: 178px;
        display: block;
    }
</style>
