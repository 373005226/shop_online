import http from './public'

// 获取首页轮播图
export const banner =(params)=>{
  return http.fetchGet('banner/',params)
}

// 手机发送验证码功能
export const sendcode =(params)=>{
  return http.fetchPost('codes/',params)
}

// 注册功能
export const userregister =(params)=>{
  return http.fetchPost('user/',params)
}

//收货地址功能
export const useraddress = (params)=>{
  return http.sendPost('address/',params)
}

//查看收货地址
export const getuseraddress =(params)=>{
  return http.getinformation('address/',params)
}

//删除收货地址
export const deleteaddress =(params)=>{
  return http.fetchDelete('address/'+params)
}
