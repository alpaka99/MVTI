<template>
  <div id="Recommend">
    <b-container>
      <!-- <h2>로고 들어갈 자리</h2> -->
      
      <MindTest/>
      
    </b-container>
      <!-- <div>     
      <ShowRecommend />
      </div> -->

  </div>
</template>

<script>
import MindTest from '@/components/Recommend/MindTest/MindTest.vue'
// import ShowRecommend from '@/components/Recommend/ShowRecommend.vue'

// import {mapGetters} from 'vuex'

export default {
  name: 'Recommend',
  components: {
    MindTest,
    // ShowRecommend
  },
  // computed: {
  //   ...mapGetters ([
  //     'isTested'
  //   ])
  // }
}
</script>

<style>
#Recommend{
font-family: Noto Sans KR, serif;
/* min-height:100vh; */
}
</style>