<template>
  <v-container id='orders'>
    <v-list expand>
      <v-divider />
      <div v-for="(order, i) in orders" :key="i">
        <v-list-group flat>
          <template v-slot:activator>
            <v-list-item three-line @click="yaCounter62256409.reachGoal('SELECT_ODER')">
              <v-list-item-content>
                <v-list-item-title class="display-1">{{order.cart.sum}}Р</v-list-item-title>
                <v-list-item-title class="subtitle-1">{{order.place}}</v-list-item-title>
                <v-list-item-subtitle class="caption">Доставка {{order.date}} | {{order.status}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
          <v-list-item>
            <v-list-item-content class="d-inline">
              <v-btn @click="yaCounter62256409.reachGoal('CANCEL_ORDER')" text>Action 1</v-btn>
              <v-btn text>Action 2</v-btn>

              <v-chip-group max="0">
                <v-chip v-for="item in order.cart.items" :key="item.id">
                  {{ item.description }} x {{item.count}}
                </v-chip>
              </v-chip-group>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
        <v-divider />
      </div>
    </v-list>
  </v-container>
</template>

<script>
  export default {
    props: ['orders']
    // methods: {
    //   deleteItem: function (cntxt) {
    //       this.cart.sum -= (cntxt.count*cntxt.price)
    //       this.cart.cartitems.splice(this.cart.cartitems.indexOf(cntxt), 1)
    //   }
    // }
  }

</script>
