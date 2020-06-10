<template>
  <v-app>

    <v-app-bar app flat>
      <v-app-bar-nav-icon @click="drawer = true" />

    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app temporary width="512">
      <v-list>
        <v-list-item>
          <v-list-item-action @click="drawer = !drawer">
            <v-icon light>
              mdi-close
            </v-icon>
          </v-list-item-action>
        </v-list-item>

        <v-list-item>          
          <v-list-item-title>{{name}}</v-list-item-title>
          <v-list-item-title>Выйти</v-list-item-title>
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
  const links = [{
      link: "/personal/fastorder",
      text: "Быстрый заказ"
    },
    {
      link: "/personal/myorders",
      text: "Мои заказы"
    },
    {
      link: "/personal/mydata",
      text: "Мои данные"
    },
    {
      link: "/",
      text: "Главная"
    },
  ]

  export default {
    data() {
      return {
        drawer: false,
        items: links,        
      }
    },
    computed: {      
      name() {
        return this.$store.state.personaldata.name
      }
    },
  }

</script>
