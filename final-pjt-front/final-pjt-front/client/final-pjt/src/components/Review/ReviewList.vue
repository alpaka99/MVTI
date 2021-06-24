<template>
  <div>
    <h2>ReviewList</h2>
    <button @click="createReview">새 리뷰 작성</button>
      <!-- 와...동적 라우팅은 신이다...  -->
    <!-- <ul>
      <li v-for="(review,idx) in this.reviewList"
      :key="idx"> 
      <div>
      <router-link :to="`reviewDetail/${idx}`"> 
      {{review.title}}
      <b-form-rating v-model="review.rating" readonly></b-form-rating>
      <p class="mt-1">Value: {{ review.rating }}</p>
      </router-link>
      </div>
      </li>
    </ul> -->
     <div>
    <b-table striped hover :items="reviewList"></b-table>
  </div>
    </div>
</template>

<script>
// import {mapGetters} from 'vuex'

export default {
  name: 'ReviewList',
  data: function (){
    return {
      reviewList: this.$store.state.reviewList
    }
  },
  // created () {
  //     this.$store.dispatch('getReviewList')
  // },
  // beforeMount: function () {
  //     this.$store.dispatch('getReviewList')
  // },
  mounted: function() {
    this.$store.dispatch('getReviewList')
  },
   
  methods: {
    createReview: function() {
      this.$router.push({name: 'reviewForm'})
    }
  }
}
</script>

<style>

</style>