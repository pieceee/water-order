<template>
  <v-container>

    <orders-list :orders="mockup" :ismanager="true" />

    <v-btn text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);" @click="download">Выгрузить EXCEL</v-btn>

  </v-container>
</template>

<script>  
  import OrdersList from "~/components/OrdersList.vue"

  export default {
    created: function() {
      fetch('/api/orders/', {
          method: 'GET',
          headers: {
            'Authorization': 'Bearer' + this.$store.getters.getToken
          }
        }).then(
          successResponse => {
            if (successResponse.status != 200) {
              alert("Error")
            } else {
              this.mockup = successResponse.json()
            }
          },
          failResponse => {
            alert("Error")
          }
        )
    },
    head: {
      title: 'Заказы'
    },
    components: {
      OrdersList
    },
    layout: 'manage',
    data: () => ({
      mockup: {}
    }),
    methods: {
      download() {
        fetch('/api/report/', {
          method: 'GET',
          headers: {
            'Authorization': 'Bearer' + this.$store.getters.getToken
          }
        }).then(
          successResponse => {
            if (successResponse.status != 200) {
              alert("Error")
            } else {
              successResponse.blob()
            }
          },
          failResponse => {
            alert("Error")
          }
        )

      }
    },
  }

</script>
