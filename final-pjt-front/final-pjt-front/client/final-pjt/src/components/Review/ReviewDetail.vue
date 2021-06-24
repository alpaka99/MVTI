<template>
  <b-container style="max-width: 800px;">
    <div class="container text-left">
      <div class="background-box">
        <b-form class="review-detail" @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-1"
            label="리뷰 제목"
            label-for="input-1"
            
          >
            <b-form-input
              class="review-label"
              style="min-height: 3rem;"
              id="input-1"
              v-model="tossData.reviewData.title"
              type="text"
              required
              :readonly="readonly_flag"
              :placeholder="this.currentReview.title"
            ></b-form-input>
          </b-form-group>

          <b-form-group 
            id="input-group-2" 
            label="리뷰 내용" 
            label-for="input-2"
            class="review-label"
            >
            <b-form-textarea
                id="input-2"
                v-model="tossData.reviewData.content"
                required
                :readonly="readonly_flag"
                :placeholder="this.currentReview.content"
                rows="3"
                max-rows="6"
            ></b-form-textarea>
          </b-form-group>

          <b-form-group 
          id="input-group-3"
          label="영화" 
          label-for="input-3"
          class="review-label">

            <b-form-select
              id="input-3"
              style="min-height: 3rem;"
              v-model="tossData.reviewData.movie"
              :options="this.movieTitles"
              required
              :disabled="readonly_flag"
              :placeholder="this.currentReview.movie"
            >
            <option disabled value="">영화를 선택하세요</option>
            </b-form-select>
          </b-form-group>

          <b-form-group 
            id="input-group-4" 
            label="평점" 
            label-for="input-4"
            class="detail-label">
            <b-form-rating id="rating-inline" inline v-model="tossData.reviewData.rating"
            variant='danger' stars="10" show-value show-value-max :readonly="readonly_flag"></b-form-rating>
          </b-form-group>
          
          <div v-if="readonly_flag" style="margin-top: 3rem;">
            <b-button variant="outline-danger" class='text-white review-detail-botton' type="reset" @click="onFix">Fix</b-button>
          </div>
          <div v-else style="margin-top: 3rem;">
            <b-button class='text-white review-detail-botton' type="submit" variant="danger">Update</b-button>
          </div>
      
        </b-form>
        <hr class="mid-line">
        <CommentForm :reviewId="this.currentReview.id"/>
        <CommentList :reviewId="this.currentReview.id"/>
      </div>
    </div>
  </b-container>
</template>

<script>
import CommentList from '@/components/Comment/CommentList.vue'
import CommentForm from '@/components/Comment/CommentForm.vue'
export default {
  name: 'ReviewDetail',
  components: {
    CommentList,
    CommentForm
  },
  data: function() {
    return {
      currentReview: this.$store.state.reviewList[this.$route.params.id],
      tossData: {
      reviewData: {
        title: this.$store.state.reviewList[this.$route.params.id].title,
        content: this.$store.state.reviewList[this.$route.params.id].content,
        movie: this.$store.state.reviewList[this.$route.params.id].movie,
        rating: this.$store.state.reviewList[this.$route.params.id].rating,
      },
        reviewId: this.$store.state.reviewList[this.$route.params.id].id,
        reviewRouteId: this.$route.params.id
      },
      movieTitles: this.$store.state.movieTitleList,
      show: true,
      readonly_flag: true,
    }
  },
  methods: {
    deleteReview(){
      this.$store.dispatch('deleteReview',this.currentReview.id)
    },
    onSubmit(event) {
        event.preventDefault()
        // alert(JSON.stringify(this.form))
        this.$store.dispatch('updateReview',this.tossData)
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.reviewData.title = ''
        this.reviewData.content = ''
        this.reviewData.rating = ''
        this.reviewData.content = ''
        // Trick to reset/clear native browser form validation state
        this.$nextTick(() => {
          this.show = true
        })
      },
       onFix(event) {
        event.preventDefault()
        // Reset our form values
        // Trick to reset/clear native browser form validation state
        this.readonly_flag = !this.readonly_flag
        this.$nextTick(() => {
          this.show = true
        })
        // console.log(this.readonly_flag)
      }
  }
}

</script>

<style>
.review-detail {
  color: white;
  font-size: 1.8rem;
  font-weight: 700;
}
.review-label{
  margin: 0.5rem 0 2rem 0;
}
.background-box {
  background-color: rgba(80, 80, 80, .2);
  padding: 2rem;
}
.mid-line {
  margin: 5rem 0 0 0;
  width: 100%;
  border: 0;
  color: rgb(255, 255, 255);
}
.review-detail-botton {
  width: 100%;
}
</style>