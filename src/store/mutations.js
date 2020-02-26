export default{
    logintoken(state,information){
      // state.mobile = information.mobile
      state.token = information.token
      // localStorage.setItem('mobile',information.mobile)
      localStorage.setItem('token',information.token)
    },
    loginusername(state,information){
      state.mobile = information
      localStorage.setItem('mobile',information)
    }
}
