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
export const useraddress = (params,config)=>{
  return http.fetchPost('address/',params,config)
}

//查看收货地址
export const getuseraddress =(params,config)=>{
  return http.fetchGet('address/',params,config)
}

//删除收货地址
export const deleteaddress =(params)=>{
  return http.fetchDelete('address/'+params)
}

//用户收藏商品功能
export const adduserfavs =(params,config)=>{
  return http.fetchPost('userfavs/', params,config)
}

//查询用户收藏的所有商品
export const getallfav =(params,config)=>{
  return http.fetchGet('userfavs/',params,config)
}

//删除用户收藏的商品
export const deletefav =(params)=>{
  return http.fetchDelete('userfavs/'+params+'/')
}
