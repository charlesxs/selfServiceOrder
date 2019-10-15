import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routers from './router'
import store from './store'

// iView infrastructure
import iView from 'iview'
import 'iview/dist/styles/iview.css'

const router = new VueRouter({
  routes: Routers
})


Vue.use(iView)
Vue.use(VueRouter)
// Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
