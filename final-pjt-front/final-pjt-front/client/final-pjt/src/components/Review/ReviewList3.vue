<template>
  <div class="mt-5">
    <div class='d-flex flex-column'>
      <div class='row'>
        <div class='col'>
        <button class="btn btn-muted btn-outline-danger btn-lg  mb-2" @click="createReview">Write Review</button>
        </div>
      </div>
      <div class='row justify-content-center'>
        <div role="tablist" class='col-5'>
          <b-card no-body class="mb-1 tmp0" 
            v-for="(review,idx) in $store.state.reviewList"
            :key="idx">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button block href="#" v-b-toggle="'accordion-'+idx" variant="danger" class="d-flex justify-content-between align-items-center  tmp1">
                {{review.title}}
                <b-badge variant="dark">평점: ⭐{{review.rating}}
                </b-badge>
              </b-button>
            </b-card-header>
            <b-collapse :id="'accordion-'+idx"  accordion="my-accordion" role="tabpanel" >
              <b-card-body class="text-left">
                <b-card-text >영화 제목: {{$store.state.movieTitleList[review.movie].text}}</b-card-text>
                <b-card-text>{{ review.content }}</b-card-text>
                <router-link :to="`reviewDetail/${idx}`"> 
                <b-card-text>자세히 보기</b-card-text>
                </router-link>
              </b-card-body>
            </b-collapse>
          </b-card>  
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewList3',
  methods: {
    createReview: function() {
      this.$router.push({name: 'ReviewForm2'})
      },
    },
}
</script>

<style>
.tmp0 {
  color: white;
  background-color: rgb(121, 16, 16);
}
.tmp1 {
  color: black;
  background-color: rgb(248, 69, 69);
}
/* .btn {
  outline-color: #ceaa8a;

} */
</style>