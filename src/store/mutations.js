export default{
    login(state,information){
        state.mobile = information.mobile
        state.token = information.token
    }
}