<template>
  <info-page :title="pagecontent.title" :content="pagecontent.content" />
</template>

<script>
  import InfoPage from '~/components/InfoPage.vue'

  const mockup = {
    title: "Доставка",
    content: "Доставка осуществляется в день. который вы выбрали." +
      " За 30 минут до приезда мы предупредим вас, что уже рядом." +
      " В случае непредвиденных обстоятельств дата доставки может меняться. Доставка осуществляется только в пределах города Воронеж."

  }

  export default {
    layout: 'empty',
    components: {
      InfoPage
    },
    data() {
      return {
        pagecontent: mockup
      }
    },
  }

</script>
