<template>
  <div>
    <b-carousel
      id="carousel-1"
      class='carousel-class d-flex'
      v-model="slide"
      :interval="6000"
      fade
      controls
      indicators
      background="#ababab"
      img-width="100"
      img-height="100"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
    
      <b-carousel-slide v-for="(movie,idx) in $store.state.carouselList[0]"
      :key='idx'>
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="50"
            height="50"
            :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>

    </b-carousel>

    <p class="mt-4">
      <!-- Slide #: {{ slide }}<br> -->
      {{this.$store.state.carouselList[0][slide].title}}
      <!-- Sliding: {{ sliding }} -->
    </p>
  </div>
</template>

<script>
  export default {
    name: 'Carousel',
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      }
    }
  }
</script>

<style scoped>
  #carousel-class {
   height:1rem!important;
   width:1rem!important;
 }
</style>