<template>
  <div>
    <p class="mt-4" style="color:rgb(255, 255, 255); font-size:1.3rem;">댓글 달기</p>
    <div class="comment-form-box">
      <input class="comment_input mx-0" type="text" id="commentContent" v-model="comment.content" placeholder="내용">
      <button @click="createComment(comment) " class="btn btn-danger mx-2">작성</button>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'CommentForm',
  data : function() {
    return {
      comment: {
        reviewId: this.reviewId,
        // title: '',
        content: '',
      }
    }
  },
 props : {
    reviewId: {
      type: String
    }
 },
  methods: {
    ...mapActions([
      'createComment'
    ])
  }
}
</script>

<style>
.comment_input {
  background-color: white;
  min-height:2.2rem;
  width: 89%;
  flex: 1;
}
.comment-form-box {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>