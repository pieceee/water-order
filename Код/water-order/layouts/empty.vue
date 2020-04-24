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

        <v-list-item @click="snackbar = true">
          <v-list-item-title>Войти</v-list-item-title>
        </v-list-item>

        

        <v-list-item v-for="(item, i) in items" :key="i" :to="item.link" nuxt link>
          <v-list-item-title>{{item.text}}</v-list-item-title>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-content>
      <nuxt />
    </v-content>
    <v-snackbar v-model="snackbar" top>
      <v-btn to="/personal/fastorder" nuxt text >
        Клиент
      </v-btn>
      <v-btn to="/manage/orders" nuxt text >
        Менеджер
      </v-btn>
      <v-btn color="pink" text @click="snackbar = false" icon>
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
  const links = [{
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
        snackbar: false,
        items: links
      }
    }
  }

</script>
