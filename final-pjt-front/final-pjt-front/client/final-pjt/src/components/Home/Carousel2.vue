<template>
<div>
    <carousel :autoplay="true" :navigationEnabled="true" class='bg-dark'>
      <slide v-for="(movie,idx) in $store.state.carouselList[0]"
      :key='idx'  >
      <!-- <p>{{movie.title}}</p> -->
        <img :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path" alt="" v-b-modal="'modal1-'+idx">
    <b-modal :id="'modal1-'+idx"  :title="$store.state.carouselList[0][idx].title" >
      <p p class="my-4" v-if="$store.state.carouselList[0][idx].overview">{{$store.state.carouselList[0][idx].overview}}</p>
          <p p class="my-4" v-else>줄거리가 존재하지 않습니다!</p>

          <p p class="my-4">평점 </p>

          <b-form-rating readonly id="rating-inline" inline v-model="$store.state.carouselList[0][idx].vote_average" 
          variant='danger' stars="10" show-value show-value-max></b-form-rating>
    </b-modal>
      </slide>
    </carousel>  
</div>
</template>

<script>
import { Carousel, Slide} from 'vue-carousel'
// import Carousel from './Carousel.vue'
export default {
  components : {
    Carousel,
    Slide
  }
}
</script>

<style scoped>
#mdal {
  background-color:rgb(70, 70, 70);
}
</style>