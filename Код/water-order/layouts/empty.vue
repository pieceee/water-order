<template>
    <!-- <v-app-bar
        app
        flat
        fixed

    >
    <v-spacer />
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"  class="hidden-md-and-up" />
      <v-toolbar-items class="hidden-sm-and-down">
            <v-btn text>Link One</v-btn>
            <v-btn text>Link Two</v-btn>
            <v-btn text>Link Three</v-btn>
        </v-toolbar-items>
      
    </v-app-bar> -->

    <v-app>
    
    <v-app-bar          
        app
        flat
    >
      <v-app-bar-nav-icon @click="drawer = true"  />
      
    </v-app-bar>

    
    <v-navigation-drawer
      v-model="drawer"      
      app
      temporary
      width="512"
    >        
      <v-list>
        <v-list-item>
          <v-list-item-action @click="drawer = !drawer">
            <v-icon light>
              mdi-close
            </v-icon>
          </v-list-item-action>
        </v-list-item>

        <v-list-item v-for="(item, i) in items" :key="i" :to="item.link" nuxt link>
          <v-list-item-title>{{item.text}}</v-list-item-title>
        </v-list-item>
        
      </v-list>
    </v-navigation-drawer>
    <v-content>      
        <nuxt />
    </v-content>
    
  </v-app>
</template>

<script>
const links = [
  {
    link: "/",
    text: "Главная"
  },
  {
    link: "/about",
    text: "О компании"
  },
  {
    link: "/payment",
    text: "Оплата"
  },
  {
    link: "/delivery",
    text: "Доставка"
  },
]

export default {
    data() {
        return {
            drawer: false,
            items: links
        }
    }
}
</script>