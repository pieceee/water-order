<template>
    <v-container>
        <v-card flat>
            <v-card-title>
                Корзина
            </v-card-title>
            <v-card-text></v-card-text>
        </v-card>
        <v-card flat>
            <v-card-title>
                Данные
            </v-card-title>
            <v-card-text>
                <v-form>
                    <v-text-field></v-text-field>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>    
</template>

<script>
export default {
    layout: 'empty',
    data: () => ({

    }),
}
</script>