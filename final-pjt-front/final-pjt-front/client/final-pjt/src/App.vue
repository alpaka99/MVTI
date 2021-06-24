<template>

  <div id="app" >
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark" style="padding: 1rem">
        <b-navbar-brand href="#">
          <img src="@/assets/mvti_icon2.png" alt="icon" width="40px" style="margin: 0 0 0 0.5rem;">
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <div v-if='isLoggedIn' class='justify-items-flex-start'>
            <b-navbar-nav class="nav-text">
              <b-nav-item  @click="moveTo('Home')"><b>H</b>ome</b-nav-item>
              <b-nav-item @click="moveTo('Community')"><b>C</b>ommunity</b-nav-item>
              <b-nav-item @click="moveTo('Recommend')"><b>R</b>ecommend</b-nav-item>
              <b-nav-item @click="moveTo('Logout')"><b>L</b>ogout</b-nav-item>
            </b-navbar-nav>
          </div>
          <div v-else>
              <b-navbar-nav  class="nav-text">
                <b-nav-item @click="moveTo('Home')"><b>H</b>ome</b-nav-item>
                <b-nav-item @click="moveTo('Login')"><b>L</b>ogin</b-nav-item>
                <b-nav-item @click="moveTo('Signup')"><b>S</b>ignup</b-nav-item>
              </b-navbar-nav>
          </div>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <!-- <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form> -->
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template #button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <div>
      <img alt="Vue logo" src="@/assets/mvti_logo3.png" width="400" class="mt-5">
    </div>
    <div class="main-router">
      <router-view/>
    </div>
    <div class="footer">
        <Footer />
      </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
html {
  overflow-y: auto !important;
}
html, body {
  margin: 0px !important;
  padding: 0px !important;
  /* height: 100%; */
  margin-bottom: 0;
  min-height:100vh;
}
.title{
  color: whitesmoke;
  font-family: Noto Sans KR, serif;
  font-size: 3.5rem;
  font-weight: 500;
}
.footer{
  margin-top: 3rem ;
}
.main-router {
  flex: 1;
}
.nav-text {
  font-size: 1.4rem;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(30, 30, 30);
  min-height:100vh;
  display: flex;
  flex-direction: column;
}

#nav {
  padding: 30px;
  background-color:thistle;
}

#nav a {
  font-weight: bold;
  color: #e68a34;
}

.navbar.navbar-dark.bg-dark{
  background-color: rgb(180, 2, 12)!important;
}

/* #nav a.router-link-exact-active {
  color: #42b983;
} */
</style>

<script>
import {mapGetters,mapActions} from 'vuex'
import Footer from '@/views/Footer.vue'
// import Header from '@/components/Home/Header.vue'
export default {
  name: 'App',
  components: {
    Footer,
  },
  computed: {
    ...mapGetters([
      'isLoggedIn'
    ])
  },
  methods: {
    ...mapActions([
      'logout'
    ]),
    moveTo(page){
      this.$router.push({name: page})
    }
  },
  created() {
    //  this.$store.dispatch('getMovieList')
    //  this.$store.dispatch('getReviewList')
     this.$store.dispatch('setTest')
     this.$store.dispatch('doItAgain')
  }  
}
</script>