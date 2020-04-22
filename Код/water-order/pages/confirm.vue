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
            <v-card-text>
                <v-form>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>    
</template>

<script>
import Cart from "~/components/Cart.vue"

export default {
    layout: 'empty',
    components: {
      Cart
    },
    data: () => ({

    }),
}
</script>