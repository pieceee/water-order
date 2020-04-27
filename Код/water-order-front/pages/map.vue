<template>
<v-container ma-0 pa-0 fill-height fluid> 
    <v-skeleton-loader></v-skeleton-loader>
    <client-only>
    <yandex-map     
        style="width: 100%; height: 100%;"
        :controls="controls"
        :settings="settings"
        :coords="coords"
        :zoom="16" 
        @click="onClick"
        @map-was-initialized="initHandler"
    >
        <ymap-marker 
        :coords="coords" 
        marker-id="1" 
        hint-content="Точка заказа" 
        />
    </yandex-map>
    </client-only>
     
    <v-card
        justify="center"
            max-width="700px"
        flat      
        style="position: absolute; bottom: 40px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);"
    >
    
        <v-card-text>
            {{place}}
            <v-text-field
            v-model="comment"
            placeholder="Комментарий к месту"
          ></v-text-field>
        </v-card-text>
        
        <v-card-actions>
          <v-spacer></v-spacer>  
            <v-btn
                text
                to="/confirm" nuxt
            >
                Далее
            </v-btn>
        </v-card-actions>
    </v-card>
</v-container>
</template>

<script>
import { yandexMap, ymapMarker } from 'vue-yandex-maps'

export default {    
    components: { yandexMap, ymapMarker },
    layout: 'empty',
    data: () => ({
        controls: ["geolocationControl", "zoomControl"],
        settings:{
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
        mapObject: null
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
                    boundedBy: [[51.31,38.288],[51.9,40.2]]
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
        coords: function(newCoords) {
            ymaps.geocode(newCoords).then((res)=>{ 
                const geoObject = res.geoObjects.get(0)            
                this.place = (geoObject.getThoroughfare() || geoObject.getLocalities())  + " " + (geoObject.getPremiseNumber() || "")
            })
        }

    }
    };
</script>