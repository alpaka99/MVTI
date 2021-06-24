# Client Progress

## 2021-05-20 (Day1)

### Today I did...

- 전체적인 프로젝트 진행 방향 및 프로젝트 기간에 대한 정립
- 프로젝트 컨셉 설정 완료

- vuex와 router를 이용하여 구현하기로 결정
- views에 영화 목록 조회, 리뷰작성, 영화 추천, 로그인, 회원가입 .vue파일 생성

- 각각의 views의 파일에 맞는 component .vue 파일들 생성 및 디렉토리에 나눠서 저장
- 영화목록 조회, 로그인, 회원가입 구현 -> 아직 django 서버와 테스트를 해보지는 못함



### Tomorrow I will...

- 리뷰작성, 댓글 작성 기능 완성
- 시간이 된다면 영화 추천 기능도 구현 도전
- 전체적인 스타일링을 어떻게 할 것인지 bootstrap-vue document를 살펴보기
- 기분좋고 열정적으로 프로젝트 진행하기! 🙂👍



## 2021-05-21 (Day2)

### Today I did...

- 리뷰작성 완성 ( 동적 라우팅 )
- 댓글 작성 완성
- 어제 완성했다고 생각했던 기능들의 action과 mutation들을 다듬음
- 영화 추천 알고리즘에 제작에 대한 힌트 얻음



### Next Day I will...

- Vue.js로 만든 front-end와 Django로 만든 back-end 연결
- Day2까지 만들어 놓은 기능들이 정상적으로 동작하는지 test
- 시간이 남으면 영화 추천 기능도 작성
- 오늘보다 조금 더 많은 일을 할 수 있도록 노력하기! 👏



## 2021-05-22(Day3)

### Today I did...

- Front-end(Vue.js)와 Back-end(django)를 잇는 작업 시작
- 회원가입, 로그인 기능 구현
- django 코드를 수정(settings의 installed apps랑 accounts.model)해서 CORS랑 create_review가 동작하도록 만듬 -> 4시간은 걸린듯...ㅠㅠ
- movieList가 vue.js 내부에만 저장되서 reviewForm에서 새로고침하면 selected bar에서 리뷰를 진행할 영화 목록이 사라지는것을 localStorage에 저장하고 불러오면서 새로고침을 해도 정상적으로 출력되도록 수정



### Next Day I will...

- reviewList를 불러올때도 movieList와 마찬가지로 새로고침하면 사라지는 현상 수정
- comment 기능 구현
- maybe 평점 구현...?
- maybe 영화 추천기능 구현..?
- 



## 2021-05-23(Day4)

### Today I did...

- reviewList를 불러와도 movieList가 사라지는 현상 수정 완료(sessionStorage저장 + JSON strigify & parse)
- comment list받는거는 구현은 했는데 전체 comment가 아니라 해당하는 review에 대한 comment만 받아오는걸로 수정 필요
- 영화 추천 기능 구현에 대한 힌트 얻음(show(), hide()로 구현..?)



### Next Day I will...

- 해당 게시글에 대한 comment 전체 리스트를 반환하는 로직 back-end 에게 말해놓기
- comment create, delete, update 추가 구현
- movieList 디자인 부분: 하나를 선택해서 클릭하면 component를 show하면서 보여주는건 어떨까?(watcha처럼)
- 이제 프로젝트 제출해야하는 주가 됐으니까 더 열심히 하자! :) 



## 2021-05-24(Day5)

### Today I did...

- vuex-persistedstate 라이브러리를 이용하여 새로고침하면 vuex 로컬 데이터가 날아가거나, 리뷰를 작성한것이 새로고침 한번 안하면 반영 안되는 부분을 수정 완료
- movie의 data들 잘 불러와지는것 확인
- review create, delete가 잘 동작하는것 확인
- comment get, create, delete가 잘 동작하는것 확인
- recommand 기능 큰 틀 구현 완료 -> MVTI 심리검사는 구현 완료 



### Next Day I will

- review update, comment update 구현
- 영화에 대한 평점 넣는것 구현
- user profile 구현
- 디자인적인 측면들 이제 진짜 해야함
- 오늘 하루 뭔가 너무 많이 헤맸다.. MVTI 구현 훨씬 빨리 할 수 있을 줄 알았는데 아쉽다...
- 오늘 생각보다 진도가 안나간 만큼 내일 더 진도를 끝내보자...!



## 2021-05-25(Day6)

### Today I did...

- recommend 기능 구현 backend에서 추천영화 가져오기까지 완료
- MovieList에 carousel넣음
- MovieList card로 배열하는것은 소영님께서 해주심(큰 감사)
- navigator들 수정
- review를 collapse를 이용하여 구현
- logout 컴포넌트를 따로 제작



## Next Day I will...

- 스타일링 마무리(recommend, ReviewForm, MovieDetail)
  - bootstrap icon들 넣기
- 영화추천을 한 장르 말고 여러 장르 받아오기 -> 해서 각 장르마다 carousel 1개씩?

- 잘 하면 내일 끝내고 동영상 제작해서 제출 가능할지도...? :)