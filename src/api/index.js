import http from './public'

// 手机发送验证码
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

//添加收货地址
export const useraddress = (params,config)=>{
  return http.fetchPost('address/',params,config)
}

//查看收货地址
export const getuseraddress =(params,config)=>{
  return http.fetchGet('address/',params,config)
}

//删除收货地址
export const deleteaddress =(params,config)=>{
  return http.fetchDelete('address/'+params,config)
}

//修改收货地址
export const changeaddress=(params,data,config)=>{
  return http.fetchPut('address/'+params+'/',data,config)
}

//用户收藏商品
export const adduserfavs =(params,config)=>{
  return http.fetchPost('userfavs/', params,config)
}

//查询用户收藏的所有商品
export const getallfav =(params,config)=>{
  return http.fetchGet('userfavs/',params,config)
}

//删除用户收藏的商品
export const deletefav =(params,config)=>{
  return http.fetchDelete('userfavs/'+params+'/' ,config)
}

//获取购物车信息
export const getcart =(params,config)=>{
  return http.fetchGet('shopcarts/',params,config)
}

//修改购物车的信息
export const putcart=(params,data,config)=>{
  return http.fetchPut('shopcarts/'+params+'/',data,config)
}
