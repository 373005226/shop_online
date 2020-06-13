import axios from 'axios'

axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// axios.defaults.baseURL = 'http://39.106.12.6:8000/'

axios.defaults.headers['Content-Type'] = 'application/json'
// axios.defaults.headers['Authorization'] = 'JWT '+localStorage.getItem('token')

export default {
  fetchGet(url, params = {}, config = {}) {
    return new Promise((resolve, reject) => {
      axios.get(url, params, config).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  fetchPost(url, data = {}, config = {}) {
    return new Promise((resolve, reject) => {
      axios.post(url, data, config).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  fetchDelete(url, data = {}, config = {}) {
    return new Promise((resolve, reject) => {
      axios.delete(url, data, config).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  fetchPut(url ,params, data = {}, config = {}) {
    return new Promise((resolve, reject) => {
      axios.put(url , params , data, config).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  }
}



