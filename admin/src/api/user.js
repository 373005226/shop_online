import http from './public'

//登录功能
export const userlogin =(params)=>{
    return http.fetchPost('login/',params)
}

//获取所有的用户
export const getalluser = (params)=>{
    return http.fetchGet('alluser/',params)
}

//发送短信
export const sendcode =(params)=>{
    return http.fetchPost('codes/',params)
}

//修改个人信息接口
export const putuserinfo =(params,data)=>{
    return http.fetchPut('user/111/',params,data)
}
