<template>
  <div>
    <button @click="createReview">새 리뷰 작성</button>
    <b-table v-b-modal.modal-1 hover :items="$store.state.reviewList" :fields="fields" caption-top>
      <template v-slot:table-caption>실제 영화를 관람한 사람들이 작성한 리뷰입니다.</template>
    </b-table>

    <b-modal id="modal-1" title="영화 리뷰">
    <p class="my-4">Hello from modal!</p>
  </b-modal>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        fields: [
          { key: 'title', label: '제목' },
          { key: 'rating', label: '평점' },
          { key: 'user', label: '작성자' },
          ],
      }
    },
    mounted: function() {
    this.$store.dispatch('getReviewList')
  },
    methods: {
    createReview: function() {
      this.$router.push({name: 'reviewForm'})
      },
    }
  }
</script>