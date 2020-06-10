<template>
  <v-container id="orderslist">
    <v-tabs v-model="tab">
      <v-tab v-for="(p,i) in status" :key="i">{{p}}</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" class="overflow-y-auto">
      <v-tab-item v-for="(p,i) in placesorders" :key="i">
        <orders :orders="p" :ismanager="ismanager" />
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
  import Orders from "~/components/Orders.vue"

  export default {
    components: {
      Orders
    },
    props: ['orders', 'ismanager'],
    data: () => ({
      tab: 0,
      selected: 0,
      status: ["Текущие", "В доставке", "Выполненные"],
      placesorders: [
        [],
        [],
        []
      ],
    }),
    watch: {
      tab: function (n) {
        this.selected = 0
      }
    },
    created: function () {
      const vm = this
      this.orders.forEach(element => {
        switch (element.status) {
          case "В обработке":
            vm.placesorders[0].push(element)
            break;
          case "В доставке":
            vm.placesorders[1].push(element)
            break;
          case "Выполнен":
            vm.placesorders[2].push(element)
            break;
        }
      });
    }
  }

</script>
