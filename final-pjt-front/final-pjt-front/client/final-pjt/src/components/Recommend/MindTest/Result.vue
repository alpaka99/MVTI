<template>
  <b-container style="max-width: 960px;">
    <div class="result_box">
      <p class='m-0' style="font-weight: 500; font-size: 3.5rem;">당신의 MVTI는 <span>{{$store.state.MVTI}}</span> 입니다!</p>
      <!-- <p>{{$store.state.genreList}}</p> -->
      <b-button class="btn-muted btn-lg text-light" variant="outline-danger" @click="doItAgain" style=" margin: 1rem 0 0 0;">다시하기</b-button>
      
    </div>
    <hr class="my-hr">
    <div class="">
      <h3 class="recommend-movie">{{$store.state.MVTI}}에게 추천하는 영화</h3>
      <div>     
      <ShowRecommend />
      </div>
    </div>
  </b-container>
</template>

<script>
import ShowRecommend from '@/components/Recommend/ShowRecommend.vue'
export default {
  name: 'Result',
  components: {
    ShowRecommend
  },
  methods: {
    doItAgain() {
      this.$store.dispatch('doItAgain')
    },
  },
  created() {
    // this.$store.dispatch('decideMVTI')
  }
}
</script>

<style scoped>
.result_box {
  color:whitesmoke;
  padding: 7.5rem 0 8rem 0;
  font-size: 3rem;

}
.again {
  font-size: 1rem;  
}
/* .Again:hover {
  background-color: rgba(120, 20, 120, 0.5);
} */
span {
  font:italic;
  color: rgb(180, 2, 12);
}
.my-hr {
    margin: 5rem 0 0 0;
    width: 100%;
    color: rgb(70, 70, 70);
  }
.recommend-movie {
  margin: 7rem 0 1rem 0;
  color:whitesmoke;
  font-size: 2.5rem;
}
</style>