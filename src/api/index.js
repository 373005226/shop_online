import http from './public'

// 获取首页轮播图
export const banner =(params)=>{
  return http.fetchGet('banner/',params)
}


// 手机发送验证码功能
export const sendcode=(params)=>{
  return http.fetchPost('codes/',params)
}