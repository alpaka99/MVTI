<template>
  <div>
    <!-- <ReviewForm /> -->
    <ReviewList3 />
    </div>
</template>

<script>
// import ReviewForm from '@/components/Community/ReviewForm.vue'
import ReviewList3 from '@/components/Review/ReviewList3.vue'
export default {
  name: 'Community',
  components: {
    // ReviewForm,
    ReviewList3
  }
}
</script>

<style scoped>
.title {
  color: #ceaa8a;
}
</style>