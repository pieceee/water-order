import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = () => new Vuex.Store({

  state: {
    mapdata: {
      coords: [],
      name: ""
    },
    cart: {
      sum: 0,
      cartitems: []
    },
    date: "",
    personaldata: {
      phone: "",
      name: ""
    },
    manager: {
      selecteduser: {
        id: "",
        phone: "",
        name: ""
      },
      orders: {
        carts: [{
          sum: 0,
          cartitems: []
        }]
      }
    }
  },
  getters: {
    getElementById: state => id => {
      return state.cart.cartitems.find(el => el.id === id)
    },
    getToken: state => {      
      return sessionStorage.getItem('key')
    }
  },
  mutations: {
    setToken(state, obj) {
      sessionStorage.setItem('key', obj.token)
      sessionStorage.setItem('role', obj.role)
    },
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
      state.cart.sum -= (element.count * element.price)
      state.cart.cartitems.splice(state.cart.cartitems.indexOf(element), 1)
    },
    addElementCount(state, element) {
      state.cart.sum += element.price
      element.count++
    },
    setPersonalData(state, data) {
      state.personaldata.name = data.name
      if (data.phone) {
        state.personaldata.phone = data.phone
      }
    },
    setMapData(state, data) {
      state.mapdata = data
    },
    setDate(state, time) {
      state.date = time
    },
    logout(state, data) {
      state.mapdata = data
    },
    signin(state, data) {
      state.mapdata = data
    },
  }
})

export default store
