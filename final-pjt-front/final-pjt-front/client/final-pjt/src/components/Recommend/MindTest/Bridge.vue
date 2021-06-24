<template>
  <b-container style="max-width: 960px;">
    <div class="bridge-box">
        <p class="bridge-title">당신의 MVTI는...?</p>
        <b-button class="btn-muted btn-lg text-light" variant="outline-danger" @click="getRecommend" style=" margin: 1rem 0 0 0;">확인하기</b-button>
      </div>
  </b-container>

</template>

<script>
export default {
  name: 'Bridge',
  methods: {
    getRecommend() {
      this.$store.dispatch('decideMVTI')
      this.$store.dispatch('getMVTIRecommend',this.$store.state.genreList)
    }
  }
}
</script>

<style>
.bridge-box {
  border-radius: calc(.5rem - 1px);
  margin: 0 5rem 0 5rem;
  padding: 7.5rem 0 8rem;
  
  /* background-color: rgba( 100, 100, 100, 0.5 ); */
  color: whitesmoke;
}
.bridge-title {
  font-size: 3.5rem;
  font-weight: 500;
}
.bridge-sub-title {
  font-size: 1.5rem;
  font-weight: 300;
}
</style>