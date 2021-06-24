<template>
  <div class="home">
    <!-- <h2>Home</h2> -->
    <div>
      <!-- <Carousel2/> -->
    </div>
    <div>
      <MovieList />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import Carousel2 from '@/components/Home/Carousel2.vue'
import MovieList from '@/components/Home/MovieList.vue'

export default {
  name: 'Home',
  components: {
    // Carousel2,
    MovieList,
  }
}
</script>
