<template>
  <b-container id="ShowRecommend" style="max-width: 1200px;">
    <div>
      <h3 class='titles'>{{$store.state.recommendPhrase[0]}}</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie,idx) in $store.state.recommendMovieList[0]" :key='idx'>
          <div class="r-carousel-item">
            <img class="r-carousel-img " :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
            <div class="recommend-text">
              <p>{{movie.title}}</p>
            </div>
          </div>
        </div>
      </VueSlickCarousel>    
    </div>
    <div>
      <h3 class='titles'>{{$store.state.recommendPhrase[1]}}</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie,idx) in $store.state.recommendMovieList[1]" :key='idx'>
          <div class="r-carousel-item">
            <img class="r-carousel-img " :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
            <div class="recommend-text">
                <p>{{movie.title}}</p>
              </div>
          </div>
        </div>
      </VueSlickCarousel>    
    </div>
        <div>
      <h3 class='titles'>{{$store.state.recommendPhrase[2]}}</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie,idx) in $store.state.recommendMovieList[2]" :key='idx'>
          <div class="r-carousel-item">
            <img class="r-carousel-img " :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
            <div class="recommend-text">
                <p>{{movie.title}}</p>
              </div>
          </div>
        </div>
      </VueSlickCarousel>    
    </div>
        <div>
      <h3 class='titles'>{{$store.state.recommendPhrase[3]}}</h3>
      <VueSlickCarousel :arrows="true" v-bind="settings">
        <div v-for="(movie,idx) in $store.state.recommendMovieList[3]" :key='idx'>
          <div class="r-carousel-item">
            <img class="r-carousel-img " :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
            <div class="recommend-text">
                <p>{{movie.title}}</p>
              </div>
          </div>
        </div>
      </VueSlickCarousel>    
    </div>
  </b-container>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
  // optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'ShowRecommend',
  components : {

    VueSlickCarousel
  },
  data: function() {
    return {
      settings: {
             "dots": false,
             "focusOnSelect": true,
             "infinite": true,
             "autoplay": true,
             "autoplaySpeed": 4000,
             "speed": 500,
             "slidesToShow": 3,
             "slidesToScroll": 1,
             "initialSlide": 0,
            //  "centerPadding": "0px",
             "responsive": [
               {
                 "breakpoint": 1024,
                 "settings": {
                   "slidesToShow": 2,
                   "slidesToScroll": 2,
                   "infinite": true,
                   
                 }
               },
               {
                 "breakpoint": 600,
                 "settings": {
                   "slidesToShow": 1,
                   "slidesToScroll": 1,
                   "initialSlide": 2
                 }
               }
             ]
           }

    }
  }
}
</script>

<style>
#ShowRecommend{
  color: whitesmoke;
}
.titles {
  margin: 4rem 0 2rem 0;
}
.r-carousel-item {
  display: inline-block;
  position: relative;
  width: 300px;
  height: 420px;
  overflow: hidden;
  background-color: rgba(0, 0, 0, 0);
}
.r-carousel-img {
  display: inline-block;
  overflow: hidden;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.recommend-text{
  display: none;
  color: whitesmoke;
  position: absolute;
  margin: auto;
  bottom: 20px;
  left: 35px;
  font-size: 1.5rem;
}
.r-carousel-item:hover .recommend-text{
  display: block;
}
.r-carousel-item:hover .r-carousel-img{
  opacity:0.5;
}

</style>