<template>
    <v-container>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>{{clientdata.name}}</v-list-item-title>
            <v-list-item-subtitle>{{clientdata.tel}}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-btn text color="primary">Изменить</v-btn>
          </v-list-item-action>
        </v-list-item>

        <v-divider />

        <orders-list :orders="orders" />
    </v-container>
</template>

<script>
const m = {name: "Anton", tel: "8877"}
const mockup = [{
      id: 1,
      place: "ул Розовая 15",
      cart: {
        sum: 145,
        items: [{
          id: 2,
          description: "Twofgfggdgs",
          count: 7
        }]
      },
      date: "1.01",
      status: "Выполнен"
    },
    {
      id: 2,
      place: "ул Розовая 15",
      cart: {
        sum: 1457,
        items: [{
          id: 1,
          description: "One",
          count: 3
        }]
      },
      date: "5.05",
      status: "В обработке"
    },]

import OrdersList from "~/components/OrdersList.vue"

export default {
    head: {
      title: 'Клиент'
    },
    components: {
        OrdersList
    },
    layout: 'manage',
    data: () => ({
      clientdata: null,
      orders: null
    }),
    watch: {
      
    },
    created() {
        this.clientdata = m
        this.orders = mockup
    }
  }
</script>