<template>
   <b-container style="max-width: 800px;">
     <div class="row justify-content-center text-left">
      <div class="col-12">
        <div class="background-box">
          <b-form class="review-detail" @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group 
              id="input-group-1"
              label="리뷰 제목"
              label-for="input-1"
              stye="font-size: 3rem;"
            >
              <b-form-input
                class="review-label"
                id="input-1"
                v-model="reviewData.title"
                type="text"
                placeholder="Enter title"
                required
                style="min-height: 3rem;"
              ></b-form-input>
            </b-form-group>

            <b-form-group 
              id="input-group-2" 
              label="리뷰 내용" 
              label-for="input-2">

              <b-form-textarea
                class="review-label"
                id="input-2"
                style="min-height: 10rem;"
                v-model="reviewData.content"
                placeholder="Enter content"
                required
              ></b-form-textarea>
            </b-form-group>

            <b-form-group 
              id="input-group-3" 
              label="영화" 
              label-for="input-3">

              <b-form-select
                class="review-label"
                id="input-3"
                v-model="reviewData.movie"
                :options="this.movieTitles"
                required
              ></b-form-select>
            </b-form-group>


            <b-form-group 
            id="input-group-4" 
            label="평점" 
            label-for="input-4"
            class="review-label">

              <b-form-rating id="rating-inline" inline v-model="reviewData.rating"
              variant='danger' stars="10" show-value show-value-max></b-form-rating>
            </b-form-group>
            
            <div class="new-review-buttons">
              <b-button class='btn-danger btn-outline-danger text-light new-review-button' type="submit" variant="">Submit</b-button>
              <b-button class='text-white new-review-button' type="reset" variant="">Reset</b-button>
            </div>
          </b-form>
        </div>
      </div>
     </div>
  </b-container>
</template>

<script>
export default {
  name: 'ReviewForm2',
  data() {
      return {
        reviewData: {
        title: '',
        rating: '',
        movie: '',
        content: '',
      },
      movieTitles: this.$store.state.movieTitleList,
      show: true,
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        // alert(JSON.stringify(this.form))
        this.$store.dispatch('createReview',this.reviewData)
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.reviewData.title = ''
        this.reviewData.content = ''
        this.reviewData.rating = ''
        this.reviewData.content = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    },
}
</script>

<style scoped>

.label{
  color: #ceaa8a;
}
.new-review-buttons {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.new-review-button{
  width: 49%;
}
</style>