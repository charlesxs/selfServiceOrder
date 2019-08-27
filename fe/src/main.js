import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routers from './router'

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
  render: h => h(App),
}).$mount('#app')
