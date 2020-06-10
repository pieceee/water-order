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

        <v-list-item @click="login = true">
          <v-list-item-title>Войти</v-list-item-title>
        </v-list-item>



        <v-list-item v-for="(item, i) in items" :key="i" :to="item.link" nuxt link>
          <v-list-item-title>{{item.text}}</v-list-item-title>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

    <v-dialog v-model="login" max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Войти</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Телефон" required v-model="tel"></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-btn color="blue darken-1" text @click="sendcode()" v-if="requestcode">Направить код</v-btn>
                <v-text-field label="Проверочный код" required v-else v-model="code"></v-text-field>
              </v-col>

            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="doLogin" :disabled="requestcode">Войти</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-content>
      <nuxt />
    </v-content>

    <v-snackbar v-model="snackbar" top>
      Ошибка входа
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
        items: links,
        login: false,
        requestcode: true,
        tel: "",
        code: ""
      }
    },
    methods: {
      sendcode() {
        fetch('/api/auth', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            phone: this.tel
          })
        }).then(
          successResponse => {
            if (successResponse.status != 200) {
              this.requestcode = false
            } else {
              this.snackbar = true
            }
          },
          failResponse => {
            this.snackbar = true
          }
        )
      },
      doLogin() {
        fetch('/api/confirm', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            phone: this.tel,
            code: this.code
          })
        }).then(
          successResponse => {
            if (successResponse.status != 200) {
              this.snackbar = true
            } else {
              this.$store.commit("setToken", successResponse.json().access_token)
              try {
                yaCounter62256409.reachGoal('SIGNIN')
              } catch (error) {
                console.error("Unable to laod Yandex Metrika")
              }
              if (successResponse.json().role === "manager") {
                this.$nuxt.$router.replace({
                  path: '/manage/orders'
                })
              } else {
                this.$nuxt.$router.replace({
                  path: '/personal/fastorder'
                })
              }
            }
          },
          failResponse => {
            this.snackbar = true
          }
        )

      }
    },
  }

</script>
