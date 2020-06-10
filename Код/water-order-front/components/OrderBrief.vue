<template>
  <v-container id='order-brief'>
    <v-form>
      <p v-if="brief.place">{{brief.place}}</p>
      <v-row>
        <v-col cols="6">
          <v-menu ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="date"
            transition="scale-transition" offset-y min-width="290px">

            <template v-slot:activator="{ on, attrs }">
              <v-text-field v-model="date" label="Дата доставки" readonly v-bind="attrs" v-on="on"></v-text-field>
            </template>

            <v-date-picker v-model="date" no-title scrollable min="2020-06-10" max="2020-06-17">
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="menu = false">Отмена</v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(date)">OK</v-btn>
            </v-date-picker>

          </v-menu>
        </v-col>
        <v-col cols="6">
          Время: 10:00-18:00
        </v-col>
      </v-row>
      <p>{{place}}</p>
      <v-text-field label="Комментарий к заказу"></v-text-field>
      <template v-if="firstorder">
        <v-text-field label="Ваше имя"></v-text-field>
        <v-text-field label="Номер телефона"></v-text-field>
        <v-row v-if="firstorder">
          <v-col cols="6">
            <v-btn color="blue darken-1" text @click="sendSms()" v-if="requestcode">Направить код</v-btn>
            <v-text-field v-else append-outer-icon="mdi-send" @click:append-outer="sendcode" label="Код подтверждения">
            </v-text-field>
            <v-snackbar v-model="snackbar" top>
              <p>Код верный</p>
              <v-btn color="pink" text @click="snackbar = false" icon>
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-snackbar>
          </v-col>
        </v-row>
      </template>
      <p>Способ оплаты: <br>Наличными при получении</p>
      <v-btn text block @click="order">Заказать</v-btn>
    </v-form>

    <v-dialog v-model="infodialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="closedialog">
            <v-icon>mdi-close</v-icon>
          </v-btn>

        </v-toolbar>
        <v-container fluid>
          <p>{{message}}</p>
        </v-container>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  export default {
    props: ['brief', 'firstorder'],
    data: () => ({
      date: '',
      comment: '',
      requestcode: true,
      snackbar: false,
      menu: false,
      infodialog: false,
      message: "",
      sucsess: false
    }),
    methods: {
      sendSms() {
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
      sendcode() {
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
          yaCounter62256409.reachGoal('AUTH_PHONE')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }         
            }
          },
          failResponse => {
            this.snackbar = true
          }
        )  
        
      },
      order() {
        fetch('/api/neworder/', {
          method: 'POST',
          headers: {
            'Authorization': 'Bearer' + this.$store.getters.getToken
          },
          body: JSON.stringify({
            cart: this.$store.state.cart.cartitems,
            address: this.$store.state.mapdata,
            comment: this.comment
          })
        }).then(
          successResponse => {
            this.infodialog = true
            if (successResponse.status != 200) {
              alert("Error")
            } else {
              this.message = "Заказ успешен"
        this.sucsess = true
        try {
          yaCounter62256409.reachGoal('ORDER_SUCCES')
        } catch (error) {
          console.error("Unable to laod Yandex Metrika")
        }
            }
          },
          failResponse => {
            this.message = "Ошибка выполнения заказа, проверьте правильность введеных данных"
          }
        )
        
        
        
      },
      closedialog() {
        if (this.firstorder & this.sucsess) {
          this.$nuxt.$router.replace({ path: '/personal/fastorder'})
        }
        else {
          this.infodialog = false
        }
      }
    },
    computed: {
      place() {
        return this.$store.state.mapdata.name
      }
    },
    created: function () {
      this.date = this.$store.state.date
    }
  }

</script>
