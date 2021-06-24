<template>
  <div style="margin-top:5rem;">
    <div v-if="$store.state.commentList" class="row">
    <ul>
      <li v-for="(comment,idx) in $store.state.commentList"
      :key="idx">
        <div class="comment-list-box">
          <span class="comment-content" >{{comment.content}}</span>
          <button class="btn btn-outline-warning">댓글 수정</button>
          <button class="btn btn-outline-danger" @click='deleteComment(comment.id)'>댓글 삭제</button>
        </div>
      </li>
    </ul>
    </div>
    <div v-else>
      <p>아직 댓글이 없습니다!</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'CommentList',
  data: function (){
    return {
      commentList: [],
      commentData: {
        review_pk: this.reviewId,
        comment_pk: ''
      }
    }
  },
  methods: {
    deleteComment(comment_pk) {
      this.commentData.comment_pk = comment_pk
      this.$store.dispatch('deleteComment',this.commentData)
    }
  },
  props : {
    reviewId: {
      type: String
    }
  },
  created () {
      this.$store.dispatch('getCommentList',this.reviewId)
  },

  // mounted () {
  //   this.$store.dispatch('getReviewList')
  // },
}
</script>

<style>
.comment-content{
  color: whitesmoke;
  margin: 0 1rem 0 0;
  font-size: 1.2rem;
  flex:1;
}
.comment-list-box{
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>