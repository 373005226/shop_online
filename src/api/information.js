import http from './public'

export const addvisitor =(params)=>{
  return http.fetchPost('PCVisit/',params)
}

