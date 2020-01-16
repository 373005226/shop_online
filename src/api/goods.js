import http from './public'

export const catelogy =(params)=>{
  return http.fetchGet('catelogy/',params)
}
