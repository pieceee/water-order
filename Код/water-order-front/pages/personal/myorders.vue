<template>
  <v-container>
    <v-tabs v-model="tab">
      <v-tab>Текущие заказы</v-tab>
      <v-tab>Выполненные заказы</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab" class="overflow-y-auto">
      <v-tab-item>
        <orders :orders="orders" :ismanager="false" />
      </v-tab-item>
      <v-tab-item>
        <orders :orders="pastorders" :ismanager="false" />
      </v-tab-item>
    </v-tabs-items>

    <v-btn to="/personal/fastorder" nuxt text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">Быстрый заказ</v-btn>
  </v-container>
</template>

<script>
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
      orders: [],
      pastorders: [],
    }),
    created: function () {

      const response = await fetch('/api/orders/', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer' + this.$store.getters.getToken
        },
        body: JSON.stringify({
          status: "registered",
          client_id: ""
        })
      })
      this.orders = response.json()

      const res = await fetch('/api/orders/', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer' + this.$store.getters.getToken
        },
        body: JSON.stringify({
          status: "past",
          client_id: ""
        })
      })
      this.pastorders = res.json()
    }
  }

</script>
