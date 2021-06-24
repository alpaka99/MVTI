// modal로 만들거임
<template>
  <b-container style="color: rgb(220,220,220)">
   <div class='detail-info'>
     <!-- <h2>MovieDetail</h2> -->
      <div class='detail-info-content'>
        <img :src="this.image" :alt="this.currentMovie.title" width="300px" height="450px">
        <div class="detail-right">
          <p class="detail-title">{{this.currentMovie.title}}</p>
          <p>줄거리</p>
          <p class="datail-overview">{{this.currentMovie.overview}}</p>
        </div>
      </div>
   </div>
   </b-container> 
</template>

<script>
// import router from '../router'

export default {
  name: 'MovieDetail',
  data: function(){
    return {
      currentMovie: this.$store.state.movieList[this.$route.params.id],
      image: this.img_path
    }
  },
  created() {
    this.image = 'https://image.tmdb.org/t/p/w500' + this.currentMovie.poster_path
  }
}
</script>

<style>
  .detail-info {
    margin: 0 auto;
    padding-top: 40px;
    padding-bottom: 40px;
  }
  .detail-info-content {
    display: flex;
    align-items: flex-start;
    flex-wrap: nowrap;
  }
  .detail-right {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    align-content: center;
    width: 700px;
    box-sizing: border-box;
    padding-left: 40px;
  }
  .detail-title {
    display: inline-block;
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 10px;
    width: 286px;
    font-size: 2.4em;
    font-weight: 700;
    text-align: left;
  }
  .datail-overview {
    display: inline-block;
    margin: 10px;
    text-align: left;
    /* width: 286px;
    font-size: 2.4em;
    font-weight: 700; */
  }
</style>