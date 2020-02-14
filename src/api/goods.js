import http from './public'

//获取分类数据
export const catelogy =(params)=>{
  return http.fetchGet('catelogy/',params)
}

//获取商品数据
export const goods =(params)=>{
  return http.fetchGet('goods/',params)
}

//获取商品详情数据
export const detail =(params)=>{
  return http.fetchGet('goods/'+params)
}

// 获取当前类别的所有数据
export const catelogygoods=(params,page)=>{
  return http.fetchGet('goods/?category_type='+params+'&page='+page)
}