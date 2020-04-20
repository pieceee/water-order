<template>
  <v-container>
    <v-card flat>
      <v-carousel hide-delimiters v-model="show">
      <v-carousel-item
        v-for="item in items"
        :key="item.id"
        :src="item.src"
      ></v-carousel-item>
      </v-carousel>
      <div class="text-center">
      <v-btn class="ma-2"  x-large outlined tile color="primary">В корзину</v-btn>
      <p class="display-1">{{showitems.price}}Р</p>
      </div>
    </v-card>
    <v-card flat>
      <v-card-title>Почему мы?</v-card-title>
      <v-card-text>
        Классный текст, который скоро здесь будет. 
        У нас там это, водичка, вот
      </v-card-text>
    </v-card>
    <div style="z-index: 500; position: sticky; bottom: 24px; display: table;
  margin: 0 auto; background: #fff; ">
      <v-btn  outlined tile color="primary" @click="sheet = !sheet">Корзина</v-btn><v-btn to="/map" nuxt  outlined tile color="primary" >Оформить</v-btn>
    </div>
    <v-bottom-sheet v-model="sheet" scrollable>
      <v-sheet height="400px">
        <v-btn
          block
          text
          @click="sheet = !sheet"
        ><v-icon>mdi-chevron-down</v-icon></v-btn>
        
        <v-list width="70%" style="display: table; margin: 0 auto;">

          <v-list-item >            
            <v-list-item-content  style="max-width: 80%;">              
              <v-list-item-title >1</v-list-item-title>              
            </v-list-item-content>            
              <v-list-item-icon >
                <v-icon color="primary">mdi-minus</v-icon>
              </v-list-item-icon>
          </v-list-item>
          
        </v-list>
      </v-sheet>
    </v-bottom-sheet>
  
  </v-container>
      
    
  
</template>

<script>
const mockup = [
  {
    id: 1,
    src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
    price: 169,
    description: "First"
  },
  {
    id: 2,
    src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
    price: 178,
    description: "Second"
  },
  {
    id: 3,
    src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
    price: 187,
    description: "Third"
  },
  {
    id: 4,
    src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
    price: 196,
    description: "444"
  },
]

export default {
  layout: 'empty',
  components: {
    
  },
  data () {
      return {
        sheet: false,
        cart: {
          cartitems: []
        },
        items: mockup,
        show: 0,  
        showitems: {}
      }
    },
  watch: {
    show: function(index) {
       this.showitems = {...this.items[index]} 
    }
  },
  created: function() {
    this.showitems = {...this.items[0]} 
  }
}
</script>
