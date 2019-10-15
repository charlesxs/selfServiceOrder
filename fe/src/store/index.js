//

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    order: {},
    orderPay: false,
  },
  mutations: {
    pushOrder (state, order) {
      state.order = order
    },
    orderPay (state, orderPay) {
      state.orderPay = orderPay
    }
  }
})
