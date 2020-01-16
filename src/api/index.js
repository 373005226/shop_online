import http from './public'

export const banner =(params)=>{
  return http.fetchGet('banner/',params)
}
