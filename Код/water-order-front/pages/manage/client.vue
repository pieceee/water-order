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

    <orders-list :orders="orders" :ismanager="true" />
  </v-container>
</template>

<script>
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
    created() {
      const res = await fetch('/api/orders/', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer' + this.$store.getters.getToken
        },
        body: JSON.stringify({
          status: "",
          client_id: this.$store.state.selecteduser.id
        })
      })

      this.orders = res.json()
      this.clientdata = this.$store.state.selecteduser
      this.orders = res.json()
    }
  }

</script>
