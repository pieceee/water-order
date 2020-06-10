<template>
  <v-container ma-0 pa-0 fill-height fluid>
    <v-skeleton-loader></v-skeleton-loader>
    <client-only>
      <yandex-map style="width: 100%; height: 100%;" :controls="controls" :settings="settings" :coords="coords"
        :zoom="16" @click="onClick" @map-was-initialized="initHandler">
        <ymap-marker :coords="coords" marker-id="1" hint-content="Точка заказа" />
      </yandex-map>
    </client-only>

    <v-card justify="center" max-width="700px" flat style="position: absolute; bottom: 40px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">

      <v-card-text>
        {{place}}
        <!--<v-text-field v-model="comment" placeholder="Комментарий к месту"></v-text-field>-->
        <v-row>
            <v-col cols="6">
         <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="date"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
      
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="date"
            label="Дата доставки"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        
        <v-date-picker v-model="date" no-title scrollable min="2020-06-09" max="2020-06-16">
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
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text to="/confirm" nuxt>
          Далее
        </v-btn>
      </v-card-actions>
    </v-card>
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
    layout: 'empty',
    data: () => ({
      date: "",
      menu: false,
      controls: ["geolocationControl", "zoomControl"],
      settings: {
        apiKey: '2211e631-8c8c-4174-afcf-ae413fe0ce70',
        lang: 'ru_RU',
        coordorder: 'latlong',
        version: '2.1'
      },
      coords: [
        51.656496, 39.2061
      ],
      place: '',
      comment: '',
      mapObject: null,

    }),
    methods: {
      onClick(e) {
        this.coords = e.get('coords');
      },
      initHandler(obj) {
        this.mapObject = obj
        const vm = this
        vm.coords = [51.656495, 39.206099]
        const mySearchControl = new ymaps.control.SearchControl({
          options: {
            noPlacemark: true,
            provider: 'yandex#map',
            boundedBy: [
              [51.31, 38.288],
              [51.9, 40.2]
            ]
          }
        })
        mySearchControl.events.add('resultselect', function (e) {
          var index = e.get('index');
          mySearchControl.getResult(index).then(function (res) {
            console.log(res.geometry.getCoordinates())
            vm.coords = res.geometry.getCoordinates()
          });
        })
        this.mapObject.controls.add(mySearchControl)
      }
    },
    watch: {
      coords: function (newCoords) {
        ymaps.geocode(newCoords).then((res) => {
          const geoObject = res.geoObjects.get(0)
          this.place = (geoObject.getThoroughfare() || geoObject.getLocalities()) + " " + (geoObject
            .getPremiseNumber() || "")
          this.$store.commit('setMapData', {
            coords: this.coords,
            name: this.place
          })
        })
      },
      date: function (newDate) {
        this.$store.commit('setDate', this.date)
      }

    }
  };

</script>
