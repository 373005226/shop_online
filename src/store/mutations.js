export default{
    logintoken(state,information){
      state.token = information.token
      localStorage.setItem('token',information.token)
    },
    loginusername(state,information){
      state.mobile = information
      localStorage.setItem('mobile',information)
    },
    setsearchgoodslist(state,information){
      state.searchlist = information
    }
}
