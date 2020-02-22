import http from './public'

// 手机发送验证码功能
export const sendcode =(params)=>{
  return http.fetchPost('codes/',params)
}

// 注册功能
export const userregister =(params)=>{
  return http.fetchPost('user/',params)
}

//登录功能
export const userlogin =(params)=>{
  return http.fetchPost('login/',params)
}

//添加收货地址功能
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

//用户收藏商品功能
export const adduserfavs =(params)=>{
  return http.sendPost('userfavs/', params)
}

//查询用户收藏的所有商品
export const getallfav =(params)=>{
  return http.getinformation('userfavs/',params)
}

//删除用户收藏的商品
export const deletefav =(params)=>{
  return http.fetchDelete('userfavs/'+params)
}
