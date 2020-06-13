import Vue from 'vue'
import Vuex from 'vuex'
import action from "./action";
import mutations from "./mutations";

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    iscollapse:false,
    adminusername:localStorage.getItem('adminusername'),
    admintoken:localStorage.getItem('admintoken'),
    adminmobile:localStorage.getItem('adminmobile'),
    adminrole:localStorage.getItem('adminrole'),
    adminavatar:localStorage.getItem('adminavatar'),
    adminname:localStorage.getItem('adminname')
  },
  mutations,
  action,
  getters: {
    getusername(state){
      return state.adminusername
    },
    gettoken(state){
      return state.admintoken
    },
    getmobile(state){
      return state.adminmobile
    },
    getrole(state){
      return state.adminrole
    },
    getavatar(state){
      return state.adminavatar
    },
    getname(state){
      return state.adminname
    }
  },
  modules: {

  },
})

export default store
