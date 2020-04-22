<template>
  <v-container>
    <v-tabs v-model="tab">
      <v-tab>Текущие заказы</v-tab>
      <v-tab>Выполненные заказы</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab" class="overflow-y-auto">
      <v-tab-item>
        <orders :orders="orders" />
      </v-tab-item>
      <v-tab-item>
        <orders :orders="pastorders" />
      </v-tab-item>
    </v-tabs-items>
    <v-btn to="/personal/fastorder" nuxt text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">Быстрый заказ</v-btn>
  </v-container>
</template>

<script>
  const mockup = [{
      id: 1,

      place: "ул Розовая 5",
      cart: {
        sum: 145,
        items: [{
          id: 2,
          description: "Two",
          count: 7
        }]
      },
      date: "1.01",
      status: "В доставке"
    },
    {
      id: 1,
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
    },
  ]

  const mockup2 = [{
      id: 1,

      place: "ул Розовая 25",
      cart: {
        sum: 45,
        items: [{
          id: 2,
          description: "Two",
          count: 3
        }]
      },
      date: "6.01",
      status: "В доставке"
    },
    {
      id: 1,
      place: "ул Розовая 1",
      cart: {
        sum: 147,
        items: [{
          id: 1,
          description: "One",
          count: 2
        }]
      },
      date: "9.05",
      status: "В обработке"
    },
  ]

  import Orders from "~/components/Orders.vue"

  export default {
    head: {
      title: 'Мои заказы'
    },
    components: {
      Orders
    },
    layout: 'personal',
    data: () => ({
      tab: null,
      orders: mockup,
      pastorders: mockup2,
    }),
  }

</script>
