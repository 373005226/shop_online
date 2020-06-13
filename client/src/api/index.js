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

//个人信息接口
export const userInfo =(params)=>{
  return http.fetchGet('userinfo/',params)
}

//修改个人信息接口
export const putuserinfo =(params,data)=>{
  return http.fetchPut('userinfo/111/',params,data)
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

//添加购物车商品
export const addcart=(params,config)=>{
  return http.fetchPost('shopcarts/',params,config)
}

//获取购物车商品信息
export const getcart =(params,config)=>{
  return http.fetchGet('shopcarts/',params,config)
}

//修改购物车的商品
export const putcart=(params,data,config)=>{
  return http.fetchPut('shopcarts/'+params+'/',data,config)
}

//删除购物车商品
export const deletecart =(params,config)=>{
  return http.fetchDelete('shopcarts/'+params,config)
}

//获取所有的订单信息
export const getorder = (params,config)=>{
  return http.fetchGet('orders/',params,config)
}

//获取订单的详情
export const getorderdetail =(params,config)=>{
  return http.fetchGet('orders/'+params+'/',config)
}

//把购物车商品推送到订单中
export const postorder=(params,config)=>{
  return http.fetchPost('orders/',params,config)
}

//把积分的商品加到个人积分商品上
export const postintegralgoods=(params,config)=>{
  return http.fetchPost('IntegralgoodsCart/',params,config)
}

//获取用户的积分商品
export const getintegralgoods=(config)=>{
  return http.fetchGet('IntegralgoodsCart/',config)
}

//评论商品
export const postcommon=(params,config)=>{
  return http.fetchPost('common/',params,config)
}

//修改订单状态
export const putorder=(params,data,config)=>{
  return http.fetchPut('orders/'+params+'/',data,config)
}
