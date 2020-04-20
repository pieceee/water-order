<template>
    <info-page :title="pagecontent.title" :content="pagecontent.content" />
</template>

<script>
import InfoPage from '~/components/InfoPage.vue'

const mockup = {
    title: "Оплата",
    content: "..."
}

export default {
    layout: 'empty',
    components: {
        InfoPage
    },
    data () {
      return {
        pagecontent: mockup
      }
    },
}
</script>