import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import lodash from 'lodash'
import createPersistedState from 'vuex-persistedstate'


// axios.defaults.baseUrl = process.env.VUE_APP_API_URL
//==> 뭐지 이거 왜 적용 안됨??? 버그 터졌네
axios.interceptors.request.use(config => {
  const accessToken = localStorage.getItem('access_token')
  config.headers.common['Authorization'] = accessToken ? `Bearer ${accessToken}` : ''
  return config
})
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // movie data 관련
    // movieList: ['영화1', '영화2', '영화3', '영화4'],
    // movieList: sessionStorage.getItem('movieList'),
    movieList: [],
    movieTitleList: [],
    movie: '',
    carouselList: [],

    //review data 관련
    // reviewList: ['리뷰1', '리뷰2', '리뷰3'],
    // reviewList: sessionStorage.getItem('reviewList'),
    reviewList : [],

    // comment data 관련
    commentList: [],

    // recommend 관련
    test_state: 0,
    question_num: 0,
    answerList: [],
    currentQuestion: '',
    currentAnswers: '',
    userGenre : {
      R : 0,
      A : 0,
      H : 0, 
      S : 0,
      D : 0,
      C : 0,
      F : 0,
      W : 0
    },
    genreList: [],
    MVTI: '',
    recommendMovieList: [],
    mvtiPhrase: {
      '10749': '달콤한 로맨스 영화들', // R
      '28': '화끈한 액션 영화들', // A
      '27' : '으스스한 공포 영화들', // H
      '878' : '흥미로운 SF 영화들', // S
      '80' : '치밀한 범죄 영화들', // D
      '10752' : '웅장한 전쟁 영화들',  //W
      '35' : '빵 터지는 코미디 영화들', // C
      '14' : '상상속의 판타지 영화들' //F
    },

    recommendPhrase: [],
    progressPercentage: 0,
    // 로그인 관련
    accessToken: localStorage.getItem('access_token') || ''
  },
  getters: {
    isLoggedIn({accessToken}) {
      return accessToken ? true : false
    },
    // 심리테스트를 했으면 true 아니면 false를 반환
    isTested({test_result}){
      return test_result ? true : false
    }
  },
  mutations: {
    // MovieList 관련 함수들
    SET_MOVIELIST(state, movieList){
      state.movieList = movieList
      let tmp = Object.assign([],movieList.map(x=>({'value':x.id,'text':x.title})))
      console.log(tmp)
      state.movieTitleList = tmp
      // sessionStorage.setItem('movieList', JSON.stringify(movieList))
      // console.log(JSON.parse(localStorage.getItem('movieList')))
    },
    SET_CAROUSEL(state, movieList){
      state.carouselList = []
      state.carouselList.push(lodash.sampleSize(movieList, 5))
      // console.log(state.carouselList)
    },
    // Review 관련 함수들
    SET_REVIEWLIST(state, reviewList){
      state.reviewList = reviewList
      // sessionStorage.setItem('reviewList', JSON.stringify(reviewList))
    }, 
    CREATE_REVIEW(state, review){
      state.reviewList.unshift(review)
    },
    DELETE_REVIEW(state,review_pk){
      state.reviewList.forEach(function(value, index){
        if (value.id === review_pk) {
          state.reviewList.pop(index)
        }
      })
    },
    UPDATE_REVIEW(state,reviewData){
      state.reviewList = state.reviewList.map(review => {
        if (review.id === reviewData.id) {
          return reviewData
        }
        return review
      })
    },
    // comment 관련 함수들
    SET_COMMENTLIST(state,commentList){
      // state.commentList = commentList
      state.commentList = commentList
      // localStorage.setItem('commentList',commentList)
    },
    CREATE_COMMENT(state, comment){
      state.commentList.push(comment)
    },
    DELETE_COMMENT(state, comment){
      console.log('DELETE_COMMENT')
      state.commentList.forEach(function(value, index){
        if (value.id === comment) {
          state.commentList.pop(index)
        }
      })
    },
    // recommend 관련 함수들
    SET_TEST(state){
      state.question_num = 1
      state.userGenre = {
        R : 0,
        A : 0,
        H : 0, 
        S : 0,
        D : 0,
        C : 0,
        F : 0,
        W : 0
      },

      state.genreList =  []
  
      state.answerList = {
        '1' : {
          question: '오늘의 기분은 어떤 온도인가요?',
          option1 : '차갑다',
          option2: '뜨겁다',
          1 : ['H'],
          2 : ['R', 'A', 'W', 'C']
        },
        '2' : {
          question:  '당신의 선호 방향은',
          option1 : '프론트(Front)',
          option2 : '백(Back)',
          1 : ['R', 'F', 'C', 'S'],
          2 : ['H', 'D', 'W']
        },
        '3' : {
          question:  '당신은......?',
          option1 : '찍먹파',
          option2 : '부먹파',
          1 : ['D', 'S'],
          2 : ['H', 'R']
        },
        '4' : {
          question:  '좋은 꿈을 꿨을 때',
          option1 : '꿈은 꿈일 뿐이다',
          option2 : '아싸! 복권 사러가자',
          1 : ['D', 'W', 'H'],
          2 : ['R', 'F', 'A', 'S']
        },
        '5' : {
          question: 'CPU는',
          option1 : '암드(AMD)',
          option2 : '인텔(Intel)',
          1 : ['A', 'H', 'C', 'W'],
          2 : ['S', 'D', 'F']
        },
        '6' : {
          question:  '복권이 하나 당첨된다면',
          option1 : '로또(한방에 목돈)',
          option2 : '연금복권(다달이 일정금액)',
          1 : ['A', 'F', 'C'],
          2 : ['R', 'D']
        },
        '7' : {
          question:  '핸드폰은 역시.....!',
          option1 : '갤럭시',
          option2 : '아이폰',
          1 : ['F', 'D', 'H'],
          2 : ['S', 'W', 'A']
        },
        '8' : {
          question: '반려동물은 역시',
          option1 : '고양이',
          option2 : '강아지',
          1 : ['C', 'A', 'D', 'W'],
          2 : ['S', 'H', 'F', 'R']
        },
        '9' : {
          question: '나의 이상형에 더 가까운 쪽은',
          option1 : '따뜻하고 포근한 강아지상',
          option2 : '차갑고 도도한 고양이상',
          1 : ['S', 'A', 'F', 'R'],
          2 : ['C', 'H', 'W', 'D']
        },
        '10' : {
          question: '둘 중 하나를 꼭 먹어야 한다면......',
          option1 : '탄산 없는 탄산음료 ',
          option2 : '녹아서 액체가 된 아이스크림',
          1 : ['R', 'H', 'W', 'A'],
          2 : ['S', 'C', 'D', 'F']
        },
        '11' : {
          question: '노래방에 가면',
          option1 : '잔잔한 발라드',
          option2 : '속 시원한 락',
          1 : ['R', 'C', 'F'],
          2 : ['S', 'W', 'A', 'C']
        },
      }
      state.genreList = [],
      state.MVTI = '',
      state.recommendMovieList = [[],[],[],[]],
      state.recommendPhrase = [],
      state.progressPercentage = 0
    },
    START_TEST(state){
      state.test_state = 1
      // state.currentQuestion = state.answerList[state.question_num]
      // state.currentAnswers = state.answerList[state.question_num]

    },
    DO_IT_AGAIN(state){
      state.test_state = 0
      state.question_num = 1
    },
    INCREASE_MVTI(state, selected){
      // console.log(selected)
      selected.forEach(function(value){
          state.userGenre[value] ++
      })
    },
    DECIDE_MVTI(state){
      let mvti = ''
      // console.log(mvti)
      if (state.userGenre['R'] > state.userGenre['A']){
        mvti += 'R'
        state.genreList.push([10749, state.userGenre['R']])
      }
      else {
        mvti += 'A'
        state.genreList.push([28, state.userGenre['A']])
      }
      if (state.userGenre['H'] > state.userGenre['S']){
        mvti += 'H'
        state.genreList.push([27, state.userGenre['H']])
      }
      else {
        mvti += 'S'
        state.genreList.push([878,state.userGenre['S']])
      }
      if (state.userGenre['D'] > state.userGenre['C']){
        mvti += 'D'
        state.genreList.push([80,state.userGenre['D']])
      }
      else {
        mvti += 'C'
        state.genreList.push([35,state.userGenre['C']])
      }
      if (state.userGenre['F'] > state.userGenre['W']){
        mvti += 'F'
        state.genreList.push([14,state.userGenre['F']])
      }
      else {
        mvti += 'W'
        state.genreList.push([10752,state.userGenre['W']])
      }
      state.MVTI = mvti
    },
    NEXT_QUESTION(state) {
      state.question_num = state.question_num + 1
      // state.currentQuestion = state.questionList[state.question_num]
      // state.currentAnswers = state.answerList[state.question_num]
    },
    PROGRESS_UPDATE(state){
      state.progressPercentage = (state.question_num / 11)*100
      console.log(state.progressPercentage)
    },
    BRIDGE(state){
      state.test_state = 2
    },
    SHOW_RESULT(state,genreList){
      console.log(genreList)
      state.test_state = 3
      state.movieList.forEach(function(movie){
      JSON.parse(movie.genre_ids).forEach(function(value){
        genreList.forEach(function(genre,idx){
          state.recommendPhrase.push(state.mvtiPhrase[genre])
          if (value == genre){
            state.recommendMovieList[idx].push(movie)
          }
        })
      })
    })
    console.log(state.recommendMovieList)
    },
    // 로그인 관련 함수들
    UPDATE_TOKEN(state, accessToken){
      state.accessToken = accessToken
    },
    DELETE_TOKEN(state){
      state.accessToken = ''
    },
  },
  actions: {
    /* ############## movie관련 actions ##################*/
    getMovieList({commit}){
      console.log('getMovieList')
      axios.get('http://127.0.0.1:8000/movies/')
      .then(res => {
        commit('SET_MOVIELIST',res.data)
        commit('SET_CAROUSEL',res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    /* ############## review 관련 actions ##################*/
    getReviewList({commit}){
      console.log('getReviewList')
      axios.get('http://127.0.0.1:8000/community/')
      .then(res => {
        commit('SET_REVIEWLIST',res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    createReview ({commit}, reviewData){
      console.log(reviewData)
      console.log('createReview')
      // console.log(reviewData)
      axios.post('http://127.0.0.1:8000/community/',reviewData)
      .then((res) => {
        console.log('Review Created!')
        commit('CREATE_REVIEW', res.data)
        // db에 넣어주고 commentList를 다시 받아오자!
        console.log(res.data)
      })
      .then(() => {
        router.push({name: 'Community'})
      })
      .catch(err => {
        console.log('Review Creation Error!')
        console.log(err)
        alert('모든 내용을 채워주세요')
      })
    },
    updateReview({commit}, tossData){
      const reviewData = tossData.reviewData
      axios.put(`http://127.0.0.1:8000/community/${tossData.reviewId}/`, reviewData)
      .then(res => {
        commit('UPDATE_REVIEW',res.data)
      })
      .then(() => {
        router.push('/community')
      })
      .catch(err => {
        console.log(err)
      })
    },
    seeInfo({commit},data){
      console.log(data)
      commit
    },
    deleteReview({commit},reviewData){
      // console.log('delete review')
      // console.log(reviewData)
      axios.delete(`http://127.0.0.1:8000/community/${reviewData.reviewId}/`)
      .then(res => {
        console.log('delete success')
        console.log(res)
        commit('DELETE_REVIEW',reviewData)
      })
      .then(() =>{
        router.push({name: 'Community'})
      })
      .catch(err => {
        console.log(err)
      })
    },
    /* ############## comment 관련 actions ##################*/
    getCommentList({commit}, reviewId){
      console.log(reviewId)
      axios.get(`http://127.0.0.1:8000/community/${reviewId}/comments/`)
      .then(res => {
        console.log('getCommentList')
        commit('SET_COMMENTLIST',res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    createComment({commit}, commentData){
      console.log('createComment')
      console.log(commentData)
      const reviewId = commentData.reviewId
      // console.log(reviewId)
      axios.post(`http://127.0.0.1:8000/community/${reviewId}/comments/`,commentData)
      .then(res => {
        console.log(res)
        commit('CREATE_COMMENT',res.data)
        window.location.reload() 
      })
      .catch(err => {
        console.log(err)
        alert('댓글 내용을 채워주세요')
      })
    },
    deleteComment({commit},commentData){
      console.log('deleteComment')
      const comment_pk=commentData.comment_pk
      axios.delete(`http://127.0.0.1:8000/community/comments/${comment_pk}/`)
      .then(res => {
        console.log('delete Success!')
        console.log(res)
        commit('DELETE_COMMENT', comment_pk)
        window.location.reload() 
      })
      .catch(err => {
        console.log('delete failed')
        console.log(err)
      })
    },
    updateComment({commit}, commentData){
      console.log(commentData)
      axios.put('comment/',commentData)
      .then(res => {
        console.log(res)
        commit
      })
      .catch(err => {
        console.log(err)
      })
    },
    /* ############## recommend 관련 actions ##################*/
    setTest({commit}){
      commit('SET_TEST')
    },
    startTest({commit}){
      commit('START_TEST')
    },
    doItAgain({commit}){
      commit('DO_IT_AGAIN')
    },
    nextQuestion({commit}, selected){
      commit('INCREASE_MVTI', this.state.answerList[this.state.question_num][selected])
   
      if (this.state.question_num < 11){
        commit('NEXT_QUESTION')
        commit('PROGRESS_UPDATE')
      }
      else{
        console.log('exceeded length')
        commit('BRIDGE')
        }
      },
    decideMVTI({commit}){
      commit('DECIDE_MVTI')
    },
    getMVTIRecommend({commit},genreList){
      // console.log(genreList)
      let genreData = {
        'g0' : genreList[0],
        'g1' : genreList[1],
        'g2' : genreList[2],
        'g3' : genreList[3]
      }
      // console.log(genreData)
      // commit
      axios.post('http://127.0.0.1:8000/movies/recommend/',genreData)
      .then(res => {
        // console.log(res.data['성공'])
        commit('SHOW_RESULT',res.data['장르'])
      })
      .catch(err => {
        console.log(err)
      })
    },
    /* ############## account 관련 actions ##################*/
    login(context, credentials){
      console.log('login')
      console.log(credentials)
      axios.post('http://127.0.0.1:8000/token/',credentials)
      .then(res => {
        console.log('login success')
        // console.log(res)
        localStorage.setItem('access_token',res.data.access)
        context.commit('UPDATE_TOKEN',res.data.access)
      })
      .then(() => {
        router.push({name: 'Home'})
      })
      .catch(err => {
        console.log('login error!')
        console.log(err)
        // alert('아이디와 비밀번호를 확인해주세요')
      })
    },
    logout({commit}){
      console.log('logout')
      commit('DELETE_TOKEN')
      // localStorage.removeItem('access_token')
      router.push({name: 'Home'})

    },
    signup({commit}, credentials){
      axios.post('http://127.0.0.1:8000/accounts/signup/',credentials)
      .then(res => {
        console.log(res)
        // 회원 가입 후 자동으로 로그인해줌
        console.log('signup completed!')
        commit
        // commit.dispatch('login',credentials)
      })
      .then(() => {
        router.push({name: 'Login'})
      })
      .catch(err => {
        console.log('error during signup')
        console.log(err)
      })
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})
