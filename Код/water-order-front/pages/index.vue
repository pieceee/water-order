<template>
  <v-container>
    <v-card flat>
      <v-carousel hide-delimiters v-model="show">
        <v-carousel-item v-for="item in items" :key="item.id" :src="item.src"></v-carousel-item>
      </v-carousel>
      <div class="text-center">
        <p>{{showitems.description}}</p>
        <v-btn class="ma-2" @click="addelement" x-large outlined tile color="primary">В корзину</v-btn>
        <p class="display-1">{{showitems.price}}Р</p>
      </div>
    </v-card>
    <v-card flat>
      <v-card-title>Почему мы?</v-card-title>
      <v-card-text>
        Компания «VitaWater» разработала и выпустила воду, обогащенную витаминами.
        Вода«Watermin» - это четыре ярких вкуса, обогащенных витаминами. В составе каждой бутылки содержится от 20 до
        100% от рекомендованной суточной нормы витаминов группы B, C, D, E, а также калий, магний, йод, цинк. При
        разработке линейки воды «Watermin» учитывались все потребности организма человека на протяжении дня - это
        умственные нагрузки, физические, поддержание жизненного тонуса, хорошего самочувствия и быстрого восстановления
        сил.
      </v-card-text>
    </v-card>
    <div  v-if="$store.state.cart.sum" style="z-index: 500; position: sticky; bottom: 24px; display: table;
  margin: 0 auto; background: #fff; ">
      <v-btn outlined tile color="primary" @click="sheet = !sheet">Корзина</v-btn>
      <v-btn to="/map" nuxt outlined tile color="primary">Оформить</v-btn>
    </div>
    <v-bottom-sheet v-model="sheet" scrollable>
      <v-sheet height="400px">
        <v-btn block text @click="sheet = !sheet">
          <v-icon>mdi-chevron-down</v-icon>
        </v-btn>
        <v-card flat width="80%" style="display: table; margin: 0 auto;">
          <cart />
        </v-card>
      </v-sheet>
    </v-bottom-sheet>

  </v-container>



</template>

<script>
  const mockup = [{
      id: 1,
      src: '/def.png',
      price: 169.00,
      description: "Vitamin Defence Water (ВИТАМИНИЗИРОВАННАЯ ВОДА «ЗАЩИТА»)"
    },
    {
      id: 2,
      src: '/eve.png',
      price: 178.00,
      description: "Vitamin Every Day Water (ВИТАМИНИЗИРОВАННАЯ ВОДА «КАЖДЫЙ ДЕНЬ»)"
    },
    {
      id: 3,
      src: '/pow.png',
      price: 187,
      description: "Vitamin Power Water (ВИТАМИНИЗИРОВАННАЯ ВОДА «СИЛА»)"
    },
    {
      id: 4,
      src: '/det.png',
      price: 196,
      description: "Vitamin Detox Water (ВИТАМИНИЗИРОВАННАЯ ВОДА «ДЕТОКС»)"
    },
  ]

  import Cart from "~/components/Cart.vue"

  export default {
    layout: 'empty',
    components: {
      Cart
    },
    data() {
      return {
        sheet: false,
        items: mockup,
        show: 0,
        showitems: {}
      }
    },
    methods: {
      addelement() {
        try {
          yaCounter62256409.reachGoal('ADD_TO_CART')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }
        
        const element = {
          ...this.items[this.show]
        }
        element['count'] = 1
        this.$store.commit('addElement', element)
      }
    },
    watch: {
      show: function (index) {
        this.showitems = {
          ...this.items[index]
        }
      }
    },
    created: function () {
      this.showitems = {
        ...this.items[0]
      }
    }
  }

</script>
