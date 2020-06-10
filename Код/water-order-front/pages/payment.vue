<template>
    <info-page :title="pagecontent.title" :content="pagecontent.content" />
</template>

<script>
import InfoPage from '~/components/InfoPage.vue'

const mockup = {
    title: "Оплата",
    content: "Мы принимает оплату только наличным платежом, и у нас всегда найдется сдача с любой суммы для вас. В дальнейшем планируется сделать оплату онлайн, чтобы сделать сервис более удобным."
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