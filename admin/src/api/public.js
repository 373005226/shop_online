import axios from 'axios'
import { Message } from 'element-ui'
import router from "../router"

axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// axios.defaults.headers['Content-Type'] = 'application/json'
// axios.defaults.headers['Authorization'] = 'JWT '+localStorage.getItem('token')


// 请求之前加上token字段
axios.interceptors.request.use(config => {
    config.headers['Content-Type'] = 'application/json'
    config.headers.authorization  = localStorage.getItem('admintoken') || ''
    return config
}, error => {
    console.log(error) // for debug
    return Promise.reject(error)
})


axios.interceptors.response.use(response => {
    return response
}, error => {
    console.log(error)
    if (error.response) { // 响应错误码处理
        switch (error.response.status) {
            // 401错误是未登录
            case 401:
                Message.error({message:'您未登录',duration:5000})
                setTimeout(router.push({
                    path:'/login',
                    querry:{redirect:router.currentRoute.fullPath}//从哪个页面跳转
                }),5000)
                break
            // 403错误是toekn过期
            case 403:
                Message.error({message:'登陆状态过期',duration:5000})
                setTimeout(router.push({
                    path:'/login',
                    querry:{redirect:router.currentRoute.fullPath}//从哪个页面跳转
                }),5000)
                break
            case 500:
                Message.error({message:'服务器错误',duration:5000})
                break
        }
    }
    return Promise.reject(error)
})

export default {
    /**
     * 封装get方法
     * @param url
     * @param data
     * @returns {Promise}
     */
    fetchGet(url, data = {}) {
        return new Promise((resolve, reject) => {
            axios.get(url, data).then(res => {
                resolve(res.data)
            }).catch(error => {
                reject(error)
            })
        })
    },
    /**
     * 封装post请求
     * @param url
     * @param data
     * @returns {Promise}
     */
    fetchPost(url, data = {}) {
        return new Promise((resolve, reject) => {
            axios.post(url, data).then(res => {
                resolve(res.data)
            }).catch(error => {
                reject(error)
            })
        })
    },
    /**
     * 封装delete请求
     * @param url
     * @param data
     * @returns {Promise}
     */
    fetchDelete(url, data = {}) {
        return new Promise((resolve, reject) => {
            axios.delete(url, data).then(res => {
                resolve(res.data)
            }).catch(error => {
                reject(error)
            })
        })
    },
    /**
     * 封装put请求
     * @param url
     * @param params
     * @param data 携带参数
     * @returns {Promise}
     */
    fetchPut(url, params, data = {}) {
        return new Promise((resolve, reject) => {
            axios.put(url, params, data).then(res => {
                resolve(res.data)
            }).catch(error => {
                reject(error)
            })
        })
    },
    /**
     * 封装导出Excal文件请求
     * @param url
     * @param data
     * @returns {Promise}
     * */
    exportExcel(url, data = {}) {
        return new Promise((resolve, reject) => {
            axios({
                method:'post',
                url:url,
                data:data,
                responseType: 'blob'
            }).then(response => {
                resolve(response.data)
                let blob = new Blob([response.data], {type: "application/vnd.ms-excel"});
                let fileName = "订单列表_"+Date.parse(new Date())+".xls" ;
                if (window.navigator.msSaveOrOpenBlob) {
                    navigator.msSaveBlob(blob, fileName);
                } else {
                    var link = document.createElement('a');
                    link.href = window.URL.createObjectURL(blob);
                    link.download = fileName;
                    link.click();
                    window.URL.revokeObjectURL(link.href);
                }
            },error => {
                reject(error)
            })
        })
    }
}



