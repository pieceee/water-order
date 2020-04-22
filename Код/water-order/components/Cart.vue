<template>
  <v-container id='cart'>
    <v-list style="max-height: 9rem" class="overflow-y-auto">

      <v-list-item v-for="item in $store.state.cart.cartitems" :key="item.id">
        <v-list-item-content style="max-width: 80%;">
          <v-list-item-title>{{item.description}} x{{item.count}}</v-list-item-title>
        </v-list-item-content>
        <v-list-item-icon>
          <v-icon @click="$store.commit('deleteElementFromCart', item)" color="primary">mdi-minus</v-icon>
        </v-list-item-icon>
      </v-list-item>

    </v-list>
    <p>Всего: {{$store.state.cart.sum}}Р</p>
  </v-container>
</template>