import http from './public'

export const catelogy =(params)=>{
  return http.fetchGet('catelogy/',params)
}

export const goods =(params)=>{
  return http.fetchGet('goods/',params)
}
