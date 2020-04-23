<template>
  <v-container>

    <v-tabs v-model="tab">
      <v-tab v-for="(p,i) in places" :key="i">{{p}}</v-tab>
      <v-btn large text>Добавить</v-btn>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="(carts, i) in placesorders" :key="i">
        <v-list style="max-height: 10rem" class="overflow-y-auto">
          <v-list-item-group color="secondary" v-model="selected">
            <v-list-item v-for="(cart, j) in carts" :key="j">
              <v-list-item-content>
                <p v-for="(item, k) in cart.items" :key="k">{{item.description}} x {{item.count}}</p>
              </v-list-item-content>

              <v-list-item-action>
                <v-list-item-title class="display-1">{{cart.sum}}Р</v-list-item-title>
                <v-btn text>Изменить</v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-tab-item>
    </v-tabs-items>

    <order-brief :brief="{}" :firstorder="false" />    

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
      status: "В доставке"
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

  import OrderBrief from "~/components/OrderBrief.vue"

  export default {
    head: {
      title: 'Мои заказы'
    },
    components: {
      OrderBrief
    },
    layout: 'personal',
    data: () => ({
      tab: 0,
      selected: 0,
      places: [],
      placesorders: [],
    }),
    watch: {
      tab: function (n) {
        this.selected = 0
      }
    },
    created: function () {
      const vm = this
      mockup.forEach(element => {
        const n = vm.places.indexOf(element.place)
        if (n === -1) {
          vm.places.push(element.place)
          vm.placesorders.push(Array(element.cart))
        } else {
          vm.placesorders[n].push(element.cart)
        }
      });
    }
  }

</script>
