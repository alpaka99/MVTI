<template>
  <b-container style="max-width: 960px;">
    <!-- <p>test start</p> -->
    <div id="TestDiv" class="test-box">
      <div class="question-gage-container" style="transform: translate(0px, 0px); opacity: 1; visibility: inherit;">
        <div class="question-gage">
          <span class="question-gage-bar" :style="'width:'+this.$store.state.progressPercentage+'%;'"></span>
        </div>
      </div>
      <div class="test-header-box">
        <h2 class="test-header text-center fw-bold">{{$store.state.answerList[$store.state.question_num].question}}</h2>
      </div>
      <div class="test-body-box container">
        <b-row>
          <b-col class="test-body-col-1">
            <b-button block variant="outline-danger" @click='nextQuestion(1)'>
              
              <p class="test-question">{{$store.state.answerList[$store.state.question_num].option1}}</p>
              
            </b-button>
          </b-col>
          <b-col class="test-body-col-2">
            <b-button block variant="outline-danger" @click='nextQuestion(2)'>
              <p class="test-question">{{$store.state.answerList[$store.state.question_num].option2}}</p>
            </b-button>
          </b-col>
        </b-row>
      </div>
      <div @click='doItAgain' class="test-retry text-white">처음으로 돌아가기</div>
      
      
    </div>

  </b-container>
</template>

<script>
export default {
  name: 'Test',
  data: function(){
    return {
      progressBar: this.$store.state.progressPercentage
    }
  },
  methods: {
    doItAgain() {
      this.$store.dispatch('doItAgain')
    },
    nextQuestion(selected) {
      this.$store.dispatch('nextQuestion', selected)
    }
  },
  created() {
    this.$store.dispatch('setTest')
  },
}
</script>

<style>
#TestDiv {
  font-family: Noto Sans KR, serif;
  padding: 3rem 0 3rem 0;
}
.test-box {
  border-radius: 2em;
  margin: 0 5rem 0 5rem;
  /* 안먹힘 ㅠ */
}
.test-header-box {
  /* background-color: rgba( 50, 50, 50, 0.5 ); */
  display:block;
  padding-bottom: 1rem;
  padding-top: 1rem;
  border-radius: calc(.5rem - 1px) calc(.5rem - 1px) 0 0;
}
.test-header {
  display:block;
  text-align: center;
  color: white;
  font-family: Noto Sans KR;
  font-weight: 200;
  
  margin: 0; 
}
.test-body-box {
  display: block;

}
.test-body-col-1{
  padding:0;
  margin: 1rem;
  color:rgb(194, 194, 194);
}
.test-body-col-2{
  padding:0;
  margin: 1rem;
  color:rgb(194, 194, 194);
}
.test-question {
  margin-top: 3rem;
  margin-bottom: 3rem;
  font-size: 1.5rem;
  font-weight: 400;
}
.test-retry {
  margin: 2rem 0 0 0;
  padding: 0.8rem;
  font-family: Noto Sans KR, serif;
  font-weight: 300;
  font-size: 1.2rem;
  border-radius: 0 0 calc(.5rem - 1px) calc(.5rem - 1px);
}
.question-gage-container {
  visibility: hidden;
  opacity: 0;
  position: relative;
  margin: auto;
  margin-top: 1rem;
  margin-bottom: 2rem;
  width: 90%;
}
.question-gage {
    height: 2px;
    /* width: 190px; */
    background-color: #444444;
    overflow: hidden;
}
.question-gage-bar {
  position: relative;
  display: block;
  height: 2px;
  width: 0%;
  background-color: rgba(151, 12, 21, 0.459)
}
</style>