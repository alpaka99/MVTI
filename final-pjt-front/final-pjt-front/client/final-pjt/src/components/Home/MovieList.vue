<template>
<div>
  <b-container class='mt-5'>
  <VueSlickCarousel :arrows="true" v-bind="settings">
    <div v-for="(movie, idx) in this.movieList" :key='idx'>
      <div class="carousel-item">
       <img class="carousel-img " :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
       <div class="carousel-text">
         <p>{{movie.title}}</p>
       </div>
      </div>
    </div>
  </VueSlickCarousel>
  <hr class='my-hr'>
  </b-container>
  <b-container fluid>
    <h1 class="Movie_List_Title">All Movies</h1>
    <h2 class='Movie-list-sub-title' style="letter-spacing: -3px;">지금 확인할 수 있는 영화</h2>
      <div class="inline" v-for="(movie, idx) in this.movieList" :key='idx' v-b-modal="'modal-'+idx">
        <div class="list_item mt-5 mb-1 imgWraper replacement">
         <img class="list_img"  :src= "'https://image.tmdb.org/t/p/w500/' + movie.poster_path" :alt= "movie.title">
         <video class="video-overlay" autoplay loop muted src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" type="video/mp4"></video>

         <b-modal :id="'modal-'+idx"  :title="$store.state.movieList[idx].title" >
          <p p class="my-4" v-if="$store.state.movieList[idx].overview">{{$store.state.movieList[idx].overview}}</p>
          <p p class="my-4" v-else>줄거리가 존재하지 않습니다!</p>

          <p p class="my-4">평점: </p>

          <b-form-rating readonly id="rating-inline" inline v-model="$store.state.movieList[idx].vote_average" 
          variant='danger' stars="10" show-value show-value-max></b-form-rating>
          <template #modal-footer="{ok}">

            <!-- Emulate built in modal footer ok and cancel button actions -->
            <b-button size="lg" variant="dark" class="text-light" @click="ok()">
              OK
            </b-button>
     
            </template>
        </b-modal>
        </div>
        <!-- <div style="text-align: center; width: 200px;" class='mx-2 px-3'>
          <p class="list_text singLine">{{movie.title}}</p>
          
        </div> -->
      </div>  
  </b-container>

  
</div>
</template>

<script>
// import {mapActions} from 'vuex'
// import {mapState} from 'vuex'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
// optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
export default {
  name: 'MovieList',
  components: {
    VueSlickCarousel
  },
  data: function() {
    return {
      // movieList: JSON.parse(sessionStorage.getItem('movieList'))
      movieList: this.$store.state.movieList,
      bigger: "width=100 height=100",
      settings: {
          "dots": false,
          "focusOnSelect": true,
          "infinite": true,
          "autoplay": true,
          "autoplaySpeed": 4000,
          "speed": 500,
          "slidesToShow": 4,
          "slidesToScroll": 4,
          "initialSlide": 0,
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
  
  },
  methods: {
    showDetail: function(movie){
      console.log(movie)
      this.$store.dispatch('getMovieDetail')
    }
  },
  computed: {
    getMovieList: function () {
      return sessionStorage.getItem('movieList')
    }
  },
  created() {
     this.$store.dispatch('getMovieList')
  }
}

</script>

<style>
  @import "https://unpkg.com/vue-slick-carousel";
  .singLine {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    /* color: #2b90d9; */
  }
  .multiLine {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp:2;
    -webkit-box-orient: vertical;
    /* color: #2b90d9; */

  }
  .list_item {
    display: inline-block;
    width: 200px;
    height: 300px;
    /* margin: 2px; */
    overflow: hidden;
    color: #2b90d9;
    margin: 0 2rem 0 2rem;
  }
  .list_item:hover{            /* 마우스 호버시 */
   transform:scale(1.3);            /* 이미지 확대 */
   transition: transform .7s; 	/*  시간 설정  */
   color: #2b90d9;
   
  }
  .list_img {
    display: inline-block;
    overflow: hidden;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
    color: #2b90d9;
  }
  .Movie_List_Title {
    margin: 3rem 0 0 0;
    color: rgb(180, 2, 12);
    font-family: 'Roboto';
    font-weight: 700;
    font-size: 100px;
    
  }
  .list_text {
    font-size: 16px;
    margin: 0;
    padding: 0;
    color: rgb(255, 255, 255);
  }
  .inline {
    display: inline-block;
  }
  .card-style{
    display: inline-block;
  }
  .expand:hover{
    background-color: black;
  }
  .carousel-item {
    display: inline-block;
    position: relative;
    width: 400px;
    height: 600px;
    overflow: hidden;
    background-color: rgba(0, 0, 0, 0);
  }
  .carousel-img {
    display: inline-block;
    overflow: hidden;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .carousel-text {
    display: none;
    color: whitesmoke;
    position: absolute;
    margin: auto;
    margin-right: 1rem;
    bottom: 15px;
    left: 35px;
    font-size: 1.5rem;
    
  }
  .carousel-item:hover .carousel-text{
    display: block;
  }
  .carousel-item:hover .carousel-img{
   opacity:0.5;
  }
  .my-hr {
    margin: 5rem 0 0 0;
    width: 100%;
    color: rgb(70, 70, 70);
  }
  .Movie-list-sub-title {
    color : whitesmoke;
  }
  .navbar-dark .navbar-nav .nav-link {
    color: rgba(255,255,255);
  }
  .bd-navbar .navbar-nav .nav-link.active {
    color: rgba(255,255,255);
    font-weight: 900;
}


</style>