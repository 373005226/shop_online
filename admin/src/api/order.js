//获取所有的订单
import http from "./public";

//获取所有订单
export const getallorder = (params)=>{
    return http.fetchGet('allorder/',params)
}

//获取订单详情
export const getOrderdetail =(params)=>{
    return http.fetchGet('allorder/'+params+'/')
}

//更改订单状态
export const changeOrder =(params,data)=>{
    return http.fetchPut('allorder/'+params+'/',data)
}

//发送提取码
export const sendnumber =(params)=>{
    return http.fetchPost('sendextractnumber/',params)
}
