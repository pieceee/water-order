import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = () => new Vuex.Store({

  state: {
    cart: {
      sum: 0,
      cartitems: []
    }
  },
  getters: {
    getElementById: state => id => {
      return state.cart.cartitems.find(el => el.id === id)
    }
  },
  mutations: {
    addElement(state, element) {
      const item = state.cart.cartitems.find(el => el.id === element.id)
      if (item) {
        item.count++
      } else {
        state.cart.cartitems.push(element)
      }
      state.cart.sum += element.price
    },
    deleteElementFromCart(state, element) {
        state.cart.sum -= (element.count*element.price)
        state.cart.cartitems.splice(state.cart.cartitems.indexOf(element), 1)
    }
  }
})

export default store
