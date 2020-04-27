<template>
  <v-container>

    <orders-list :orders="mockup" />

    <v-btn text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">Выгрузить</v-btn>

  </v-container>
</template>

<script>
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
    },
    {
      id: 3,

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
      id: 4,
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
  import OrdersList from "~/components/OrdersList.vue"

  export default {
    head: {
      title: 'Заказы'
    },
    components: {
      OrdersList
    },
    layout: 'manage',
    data: () => ({mockup: mockup})
  }

</script>
