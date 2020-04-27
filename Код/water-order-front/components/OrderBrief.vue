<template>
  <v-container id='order-brief'>
    <v-form>
      <p v-if="brief.place">{{brief.place}}</p>
      <p>Завтра, 10:00 - 18:00</p>
      <v-text-field label="Комментари к заказу"></v-text-field>
      <template v-if="firstorder">
        <v-text-field label="Ваше имя"></v-text-field>
        <v-text-field label="Номер телефона"></v-text-field>
        <v-row>
        <v-col cols="4">
        
        <v-text-field append-outer-icon="mdi-send" @click:append-outer="sendcode"
          label="Код подтверждения"></v-text-field>
          </v-col>
      </v-row>
      </template>
      <p>Сособ оплаты: <br>Наличными при получении</p>
      <v-btn text block @click="order">Заказать</v-btn>
    </v-form>
  </v-container>
</template>

<script>
  export default {
    props: ['brief', 'firstorder'],
    data: () => ({
      datetime: '',
      comment: '',
    }),
    methods: {
      sendcode: () => {
        yaCounter62256409.reachGoal('AUTH_PHONE')
      },
      order: () => {
        yaCounter62256409.reachGoal('ORDER_SUCCES')
      }
    },
    created() {}
  }

</script>
