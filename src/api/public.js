import axios from 'axios'
axios.defaults.timeout = 5000
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
axios.defaults.headers['Content-Type'] = 'application/json'
// axios.defaults.headers['Authorization'] = 'JWT '+localStorage.getItem('token')

const instance = axios.create({
  timeout : 1000,
  headers:{
    Authorization : 'JWT '+localStorage.getItem('token')
  }
})

export default {
  fetchGet (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.get(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  fetchPost (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.post(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  fetchDelete (url, params = {}) {
    return new Promise((resolve, reject) => {
      instance.delete(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  sendPost (url, params = {}) {
    return new Promise((resolve, reject) => {
      instance.post(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },
  getinformation (url, params = {}) {
    return new Promise((resolve, reject) => {
      instance.get(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },

}



