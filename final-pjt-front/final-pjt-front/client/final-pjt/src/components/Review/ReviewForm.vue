<template>
  <div class='d-flex flex-column container'>
    <h2>ReviewForm</h2>
    <div class='row'>
      <div class='col'>
        <label for="reviewTitle">ReviewTitle: </label>
        <input type="text" v-model="reviewData.title" placeholder="제목">
      </div>
    </div>
    <div class='row'>
      <div class='col'>
        <!-- <label for="select">Movie List: </label> -->
        <select v-model="reviewData.movie" id='select'>
          <option disabled value="">리뷰할 영화를 골라주세요</option>
          <option 
          v-for="(movie, idx) in movieList"
          :key="idx"
          :value="movie.id">{{movie.title}}</option>
        </select>
      </div>
    </div>
     <div>
    <label for="rating-inline">평점:{{this.reviewData.rating}}</label>
    <b-form-rating id="rating-inline" inline v-model="reviewData.rating"></b-form-rating>
  </div>
    <div>
      <label for="reviewContent">ReviewContent: </label>
      <!-- <input type="text" v-model="reviewContent"> -->
      <textarea name="" id="reviewContent" cols="30" rows="10" v-model="reviewData.content" placeholder="내용"></textarea>
    </div>
    <button @click="createReview(reviewData)">리뷰 작성</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'ReviewForm',
  data: function() {
    return {
      movieList: this.$store.state.movieList,
      reviewData: {
        title: '',
        rating: '',
        movie: '',
        content: '',
      },
    }
  },
  methods: {
    ...mapActions([
      'createReview'
    ])
  },
  created() {
    this.$store.dispatch('getMovieList')
  }
 
}
</script>

<style>

</style>