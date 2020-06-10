<template>
  <v-container id='cart'>
    
    <v-list style="max-height: 9rem; max-width: 90vw" class="overflow-y-auto overflow-x-auto">

      <v-list-item v-for="item in $store.state.cart.cartitems" :key="item.id">
        <v-list-item-content>
          <v-list-item-title>{{item.description}} x{{item.count}}</v-list-item-title>
        </v-list-item-content>
        <v-list-item-icon>
          <v-icon @click="$store.commit('addElementCount', item)" color="primary">mdi-plus</v-icon>
          <v-icon @click="$store.commit('deleteElementFromCart', item)" >mdi-delete</v-icon>
        </v-list-item-icon>
      </v-list-item>

    </v-list>
    <p>Всего: {{$store.state.cart.sum}}Р</p>
        
  </v-container>
</template>