import axios from 'axios'
// import { Message } from 'element-ui'
// import router from "../router"

axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// axios.defaults.headers['Content-Type'] = 'application/json'
// axios.defaults.headers['Authorization'] = 'JWT '+localStorage.getItem('token')


// 请求之前加上token字段
axios.interceptors.request.use(config => {
  // 格式化userinfo
  config.headers['Content-Type'] = 'application/json'
  if(localStorage.getItem('userInfo')!==null){
    config.headers.Authorization  = JSON.parse(localStorage.getItem('userInfo')).token || ''
  }
  return config
}, error => {
  return Promise.reject(error)
})


axios.interceptors.response.use(response => {
  return response
}, error => {
  console.log(error)
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
