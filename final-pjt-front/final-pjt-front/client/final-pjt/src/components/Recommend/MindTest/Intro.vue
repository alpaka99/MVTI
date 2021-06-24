<template>
  <b-container style="max-width: 960px;">
    <div class="intro-box">
        <h2 class="intro-title">당신의 <span>MVTI </span>는?</h2>
        <p class="intro-sub-title">당신에게 어울리는 영화를 찾아보세요</p>
        
        <b-button class="btn-muted btn-lg text-light" variant="outline-danger" @click='startTest' style=" margin: 1rem 0 0 0;">Start</b-button>
      </div>
  </b-container>

</template>


<script>

export default {
  name: 'Intro',
  methods: {
    startTest: function() {
      this.$store.dispatch('startTest')
    }
  }
}
</script>
<style>
span {
  color: rgb(180, 2, 12);
}
.intro-box {
  padding: 9rem 0 9rem 0;
}
.intro-title {
  /* margin: 9rem 0 0 0; */
  color: whitesmoke;
  font-family: Noto Sans KR, serif;
  font-size: 3.5rem;
  font-weight: 500;
}
.intro-sub-title {
  color: whitesmoke;
  font-family: Noto Sans KR, serif;
  font-size: 1rem;
  font-weight: 300;
}

</style>