<template>
  <v-container>
    <v-card flat>

      <v-card-actions>
        Контакты
        <v-spacer />
        <v-btn @click="dialog = true" text>Изменить</v-btn>
      </v-card-actions>
      <v-card-text class="text--primary">

        {{personal.name}} <br>
        {{personal.phone}}
      </v-card-text>
      <v-divider />
      <v-card-actions>
        Адреса
        <v-spacer />
        <v-btn @click="map = true" small text>Добавить</v-btn>
      </v-card-actions>
      <v-list>
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-content>
            <v-list-item-title>{{item.name}}</v-list-item-title>


          </v-list-item-content>
          <v-btn small text class="pa-0">Удалить</v-btn>
        </v-list-item>
        <v-divider />
      </v-list>
    </v-card>
    <v-btn to="/personal/fastorder" nuxt text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">Быстрый заказ</v-btn>


    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Изменить контакты</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Как к вам обращаться*" required v-model="name"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Изменение телефона недоступно" disabled required></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*обязательные поля</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog = false">Закрыть</v-btn>
          <v-btn color="blue darken-1" text @click="changePersonal()">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="map" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dark color="primary">
          <v-btn icon dark @click="map = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Выберите адрес</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark text @click="dialog = false">Добавить</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <client-only>

        </client-only>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  import {
    yandexMap,
    ymapMarker
  } from 'vue-yandex-maps'

  export default {
    components: {
      yandexMap,
      ymapMarker
    },
    head: {
      title: 'Мои данные'
    },
    layout: 'personal',
    data: () => ({
      dialog: false,
      map: false,
      items: [{
        pos: [],
        name: "kk"
      }, {
        pos: [],
        name: "kkkkkkkbsfbgsgs555588"
      }],
      name: ""
    }),
    methods: {
      changePersonal() {
        this.$store.commit('setPersonalData', {
          name: this.name
        })
        this.dialog = false
      }
    },
    computed: {
      personal() {
        return this.$store.state.personaldata
      }
    },
  }

</script>
