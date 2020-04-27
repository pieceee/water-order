<template>
    <v-container>
        <v-card flat>
            <v-card-title>
                Корзина
            </v-card-title>
            <v-card-text>
                <cart />
            </v-card-text>
        </v-card>
        <v-card flat>
            <v-card-title>
                Данные
            </v-card-title>
            <order-brief :brief="{}" :firstorder="true" />
        </v-card>
    </v-container>    
</template>

<script>
import Cart from "~/components/Cart.vue"
import OrderBrief from "~/components/OrderBrief.vue"

export default {
    layout: 'empty',
    components: {
      Cart,
        OrderBrief
    },
    data: () => ({

    }),
}
</script>