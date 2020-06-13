import http from './public'

export const getVisit=(params)=>{
    return http.fetchGet('PCVisit/',params)
}
