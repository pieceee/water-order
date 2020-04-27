<template>
  <v-container>
    <v-card flat>

      <v-card-actions>
        Контакты
        <v-spacer />
        <v-btn small text>Изменить</v-btn>
      </v-card-actions>
      <v-card-text class="text--primary">

        Rjynfrn.<br>
        89999989
      </v-card-text>
      <v-divider />
      <v-card-actions>
        Адреса
        <v-spacer />
        <v-btn small text>Добавить</v-btn>
      </v-card-actions>
      <v-list>
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-content>
            <v-list-item-title>{{item}}</v-list-item-title>


          </v-list-item-content>
          <v-btn small text class="pa-0">Удалить</v-btn>
        </v-list-item>
        <v-divider />
      </v-list>
    </v-card>
    <v-btn to="/personal/fastorder" nuxt text color="primary" style="position: absolute; bottom: 24px; left: 50%;
        margin-right: -50%;
        transform: translate(-50%);">Быстрый заказ</v-btn>
  </v-container>
</template>

<script>
  export default {
    head: {
      title: 'Мои данные'
    },
    layout: 'personal',
    data: () => ({
      items: ["kk", "kkkkkkkbsfbgsgs555588"]
    }),
  }

</script>
