export default{
    login(state,information){
        state.adminusername = information.adminusername
        state.admintoken = information.admintoken
        localStorage.setItem('adminusername',state.adminusername)
        localStorage.setItem('admintoken',state.admintoken)
    },
    logout(state){
        localStorage.removeItem('adminusername')
        localStorage.removeItem('adminmobile')
        localStorage.removeItem('admintoken')
        localStorage.removeItem('adminrole')
        localStorage.removeItem('adminavatar')
        localStorage.removeItem('adminname')
        state.adminusername = null
        state.adminmobile = null
        state.admintoken = null
        state.adminrole=null
        state.adminavatar=null
        state.adminname= null
    },
    Userinfo(state,information){
        state.adminrole = information.adminrole
        state.adminavatar = information.adminavatar
        state.adminmobile = information.adminmobile
        state.adminname = information.adminname
        localStorage.setItem('adminrole',state.adminrole)
        localStorage.setItem('adminavatar',state.adminavatar)
        localStorage.setItem('adminmobile',state.adminmobile)
        localStorage.setItem('adminname',state.adminname)
    },
    changemobile(state,information){
        state.adminmobile = information
        localStorage.setItem('adminmobile',state.adminmobile)
    },
    changename(state,information){
        state.adminname = information
    }
}
