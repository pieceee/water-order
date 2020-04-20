<template> 
    <v-container id='info-page'>    
        <v-card flat>
            <v-card-title>
                <h1>{{title}}</h1>
            </v-card-title>
            <v-card-text>
                <main>        
                    {{content}}
                </main>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    props: ['title', 'content']
}
</script>