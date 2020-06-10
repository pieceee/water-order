<template>
  <v-container id='orders'>
    <v-list expand>
      <v-divider />
      <div v-for="(order, i) in orders" :key="i">
        <v-list-group flat>
          <template v-slot:activator>
            <v-list-item three-line @click="selectorder">
              <v-list-item-content>
                <v-list-item-title class="display-1">{{order.cart.sum}}Р</v-list-item-title>
                <v-list-item-title class="subtitle-1">{{order.place}}</v-list-item-title>
                <v-list-item-subtitle class="caption">Доставка {{order.date}} | {{order.status}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </template>
          <v-list-item>
            <v-list-item-content class="d-inline">
              <v-btn @click="cancelorder(order)" text>Отменить заказ</v-btn>
              <v-btn text v-if="ismanager">В доставку</v-btn>
              <v-btn text v-if="ismanager">Выполнен</v-btn>
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
    props: ['orders', 'ismanager'],
    methods: {
      selectorder: function () {
        try {
          yaCounter62256409.reachGoal('SELECT_ORDER')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }
      },
      cancelorder: function (order) {
        try {
          yaCounter62256409.reachGoal('CANCEL_ORDER')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }
      }
    }
  }

</script>
