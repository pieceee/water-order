<template>
  <v-container>
    <v-text-field v-model="findfield" placeholder="Номер телефона" />
    <v-list>
      <v-list-item-group color="secondary">
        <v-list-item v-for="(result,i) in searchresult" :key="i" two-line to="/manage/client" nuxt>
          <v-list-item-content>
            <v-list-item-title>{{result.name}}</v-list-item-title>
            <v-list-item-subtitle>{{result.tel}}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-icon>mdi-chevron-right</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-container>
</template>

<script>
  const mockup = [{
    tel: "8999",
    name: "Ak"
  }, {
    tel: "899988",
    name: "Aks"
  }]

  export default {
    head: {
      title: 'Клиенты'
    },
    layout: 'manage',
    data: () => ({
      findfield: '',
      searchresult: mockup
    }),
    watch: {
      findfield: function () {

      }
    }
  }

</script>
