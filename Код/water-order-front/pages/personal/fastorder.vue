<template>
  <v-container>

    <v-tabs v-model="tab">
      <v-tab v-for="(p,i) in places" :key="i">{{p}}</v-tab>
      <v-btn large text to="/personal/mydata">Добавить</v-btn>
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
                <v-btn @click="dialog=true" text>Изменить</v-btn>
                <v-dialog v-model="dialog" max-width="600px">
                  <v-card>
                    <v-card-title>
                      <span class="headline">Выбор списка</span>
                    </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-row>
                          <p v-for="(item, k) in cart.items" :key="k">{{item.description}} x {{item.count}}</p>
                        </v-row>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn text @click="dialog = false">Закрыть</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
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
      selected: -1,
      places: [],
      placesorders: [],
      dialog: false
    }),
    watch: {
      tab: function (n) {
        this.selected = -1
      },
      selected: function () {
        try {
          yaCounter62256409.reachGoal('SELECTCART')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }

      }
    },
    created: function () {
      const vm = this


      const response = await fetch('/api/client/', {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer' + this.$store.getters.getToken
        },
        body: JSON.stringify({
          status: "",
          client_id: ""
        })
      })
      await res.json().forEach(element => {
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
