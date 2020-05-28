// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import Select from 'element-ui'
import Option from 'element-ui'
import Button from 'element-ui'
import Menu from 'element-ui'
import Message from 'element-ui'
import store from './store'
import Vuex from 'vuex'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
Vue.use(Select)
Vue.use(Option)
Vue.use(Button)
Vue.use(store)
Vue.use(Menu)
Vue.use(Vuex)
Vue.use(Message)

import axios from 'axios'
Vue.prototype.axios = axios
axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';


Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
